"""Check readable HTML and interactive behavior with Playwright Chromium.

Starts a local static server with GitHub Pages' extensionless URL handling.
Requires requirements-validation.txt and `playwright install chromium`.
"""

import argparse
import functools
import json
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlsplit

from playwright.sync_api import sync_playwright

from audit_site import Document, NEW_PATHS, PAPER_PATHS, ROOT, resolve_path


class PagesHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        destination = resolve_path(Path(self.directory), urlsplit(path).path)
        return str(destination) if destination else super().translate_path(path)

    def log_message(self, *args):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", type=Path, default=ROOT / "_site")
    parser.add_argument("--screenshots", type=Path)
    args = parser.parse_args()
    handler = functools.partial(PagesHandler, directory=str(args.site.resolve()))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    origin = f"http://127.0.0.1:{server.server_port}"
    routes = ["/", "/about/", "/projects", "/research", "/cv",
              "/significant/digits/2024/03/12/significantdigits-viewwer.html"] + NEW_PATHS + PAPER_PATHS
    checks = 0
    try:
        with TemporaryDirectory() as temporary, sync_playwright() as playwright:
            screenshots = args.screenshots or Path(temporary)
            screenshots.mkdir(parents=True, exist_ok=True)
            browser = playwright.chromium.launch()
            browser_version = browser.version
            # Crawlers and no-script browsers must receive the complete article and both CVs.
            for viewport in [{"width": 390, "height": 844}, {"width": 1440, "height": 1000}]:
                context = browser.new_context(java_script_enabled=False, viewport=viewport)
                page = context.new_page()
                for route in routes:
                    response = page.goto(origin + route)
                    assert response.status == 200, route
                    text = page.locator("main").inner_text()
                    assert len(text.split()) > 50, f"Static content missing: {route}"
                    if route in NEW_PATHS + PAPER_PATHS:
                        assert len(text.split()) > 350, route
                    if route == "/cv":
                        assert "Scientific Associate" in text and "Expérience" in text
                        assert page.locator(".resume-static").count() == 2
                    if route.startswith("/guides/"):
                        assert Document(response.text()).equations > 0
                        assert page.locator("pre code").count() > 0
                    checks += 1
                context.close()
            print(f"PASS: static content and CV in both viewport sizes ({checks} checks)", flush=True)

            for viewport_name, viewport in [
                ("mobile", {"width": 390, "height": 844}),
                ("desktop", {"width": 1440, "height": 1000}),
            ]:
                for theme in ["light", "dark"]:
                    context = browser.new_context(viewport=viewport)
                    context.add_init_script(
                        "localStorage.setItem('theme','dark-theme');" if theme == "dark"
                        else "localStorage.removeItem('theme');"
                    )
                    page = context.new_page()
                    errors = []
                    page.on("pageerror", lambda error: errors.append(str(error)))
                    # Analytics are independent of rendering and need not make requests in validation.
                    page.route("**/google-analytics.com/**", lambda route: route.abort())
                    page.route("**/googletagmanager.com/**", lambda route: route.abort())
                    for route in routes:
                        errors.clear()
                        response = page.goto(origin + route, wait_until="load")
                        assert response.status == 200, route
                        assert page.locator("body").evaluate(
                            "(el) => el.classList.contains('dark-theme')"
                        ) == (theme == "dark"), f"Theme did not persist: {route}"
                        assert page.locator(".site-nav .page-link").count() == 6
                        if viewport_name == "mobile":
                            page.locator('label[for="nav-trigger"]').click()
                            assert page.locator('.site-nav a[href="/about/"]').is_visible()
                            page.locator('label[for="nav-trigger"]').click()
                        if Document(response.text()).equations:
                            page.wait_for_function(
                                "window.MathJax && MathJax.Hub && MathJax.Hub.queue.pending === 0 "
                                "&& document.querySelector('.MathJax')", timeout=45000
                            )
                            assert page.locator(".MathJax_Error").count() == 0, route
                            assert page.locator("script[src*='MathJax.js']").count() == 1
                        for image in page.locator('main img[src^="/assets/images/guides/"]').all():
                            assert image.evaluate("(el) => el.complete && el.naturalWidth > 0"), route
                            assert image.get_attribute("alt"), route
                        if route == "/cv":
                            page.wait_for_function(
                                "document.querySelector('#resume-document').shadowRoot.querySelector('.cv')"
                            )
                            assert not page.locator("#resume-download").is_disabled()
                            page.locator('[data-resume-language="fr"]').click()
                            page.wait_for_function(
                                "document.querySelector('#resume-document').lang === 'fr-CA' && "
                                "!document.querySelector('#resume-download').disabled"
                            )
                            assert "Expérience" in page.locator("#resume-document").evaluate(
                                "(el) => el.shadowRoot.querySelector('.cv').innerText"
                            )
                            assert page.locator("#resume-jump option").count() > 2
                            jump_target = page.locator("#resume-jump option").nth(2).get_attribute("value")
                            page.locator("#resume-jump").select_option(jump_target)
                            page.evaluate("window.print = () => { window.__printCalled = true; }")
                            page.locator("#resume-download").click()
                            page.wait_for_function("window.__printCalled === true")
                            page.locator('[data-resume-language="en"]').click()
                            page.wait_for_function(
                                "document.querySelector('#resume-document').lang === 'en-CA' && "
                                "!document.querySelector('#resume-download').disabled"
                            )
                        dimensions = page.evaluate(
                            "({viewport: innerWidth, width: document.documentElement.scrollWidth})"
                        )
                        assert dimensions["width"] <= dimensions["viewport"] + 1, (
                            f"Horizontal page overflow: {route}, {viewport_name}, {dimensions}"
                        )
                        assert not errors, f"Browser script errors: {route}: {errors}"
                        if route in ["/", "/cv", "/guides/numerical-instability-python/"]:
                            label = "home" if route == "/" else route.strip("/").replace("/", "-")
                            page.screenshot(path=str(screenshots / f"{label}-{viewport_name}-{theme}.png"),
                                            full_page=True)
                        checks += 1
                    page.goto(origin + "/")
                    page.locator("#theme-switcher").click()
                    assert page.locator("body").evaluate(
                        "(el) => el.classList.contains('dark-theme')"
                    ) == (theme != "dark")
                    context.close()
                    print(f"PASS: {viewport_name}, {theme}; navigation, equations, figures, CV, layout", flush=True)
            browser.close()
        print(json.dumps({"browser": "Chromium", "version": browser_version,
                          "page_checks": checks, "result": "PASS"}))
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
