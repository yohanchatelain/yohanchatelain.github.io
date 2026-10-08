"""Audit production HTML, structured data, preserved URLs, and internal links.

Uses only the Python standard library. Run after a production Jekyll build.
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://yohanchatelain.github.io"
PERSON = ORIGIN + "/#person"
NEW_PATHS = [
    "/software/verificarlo/", "/software/fuzzy-pytorch/", "/software/pytracer/",
    "/guides/numerical-instability-python/",
    "/guides/monte-carlo-arithmetic-stochastic-rounding/",
    "/guides/numerical-variability-neuroimaging/",
]
PAPER_PATHS = [
    "/2024/10/01/New-paper-accepted.html",
    "/2026/02/18/fuzzy-pytorch-numerical-variability-deep-learning.html",
    "/2026/07/27/parkinsons-mri-scientific-reports-acceptance.html",
]
NAV_PATHS = ["/", "/about/", "/projects", "/research", "/cv", "/contact/"]
# A separately published GitHub Pages project shares this hostname but not this build.
EXTERNAL_PROJECT_PATHS = {"/floacon-firebase/"}


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.description = ""
        self.modified = None
        self.canonicals = []
        self.links = []
        self.ids = set()
        self.data = []
        self.times = {}
        self.nav = []
        self.math_scripts = []
        self.equations = 0
        self.text = []
        self._title = False
        self._hidden = 0
        self._json = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = {name: value or "" for name, value in attrs}
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "title":
            self._title = True
        if tag == "meta" and attrs.get("name") == "description":
            self.description = attrs.get("content", "")
        if tag == "meta" and attrs.get("name") == "dcterms.modified":
            self.modified = attrs.get("content")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href", ""))
        if tag in {"a", "link", "img", "script"}:
            target = attrs.get("href") or attrs.get("src")
            if target:
                self.links.append(target)
        if tag == "a" and "page-link" in attrs.get("class", "").split():
            self.nav.append(attrs["href"])
        if tag == "time":
            self.times[attrs.get("itemprop")] = attrs.get("datetime")
        if tag == "script":
            if "MathJax.js" in attrs.get("src", ""):
                self.math_scripts.append(attrs["src"])
            if attrs.get("type", "").startswith("math/tex"):
                self.equations += 1
            if attrs.get("type") == "application/ld+json":
                self._json = []
        if tag in {"script", "style"}:
            self._hidden += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._title = False
        if tag == "script" and self._json is not None:
            self.data.append(json.loads("".join(self._json)))
            self._json = None
        if tag in {"script", "style"}:
            self._hidden = max(0, self._hidden - 1)

    def handle_data(self, value):
        if self._title:
            self.title += value
        if self._json is not None:
            self._json.append(value)
        if not self._hidden:
            self.text.append(value)
            self.equations += value.count(r"\[") + value.count(r"\(")


def resolve_path(site, path):
    """GitHub Pages resolves extensionless permalinks to their .html files."""
    path = unquote(path).lstrip("/")
    candidate = site / path
    if not candidate.resolve().is_relative_to(site.resolve()):
        return None
    if candidate.is_file():
        return candidate
    if (candidate / "index.html").is_file():
        return candidate / "index.html"
    if not candidate.suffix and candidate.with_suffix(".html").is_file():
        return candidate.with_suffix(".html")
    return None


def entities(data):
    for item in data:
        if "@graph" in item:
            yield from item["@graph"]
        else:
            yield item


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    site = args.site.resolve()
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    documents = {}
    for file in sorted(site.rglob("*.html")):
        try:
            documents[file] = Document(file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            errors.append(f"{file.relative_to(site)}: invalid HTML/JSON-LD: {error}")

    content = {file: doc for file, doc in documents.items() if file.name != "404.html"}
    expected = set()
    for file, doc in content.items():
        label = str(file.relative_to(site))
        check(bool(doc.title.strip()), f"{label}: empty title")
        check(bool(doc.description.strip()), f"{label}: empty description")
        check(len(doc.canonicals) == 1, f"{label}: expected one canonical")
        if len(doc.canonicals) != 1:
            continue
        canonical = doc.canonicals[0]
        parsed = urlsplit(canonical)
        check(canonical.startswith(ORIGIN + "/") and not parsed.query and not parsed.fragment,
              f"{label}: incorrect absolute canonical {canonical}")
        check(resolve_path(site, parsed.path) == file, f"{label}: canonical points elsewhere")
        check(canonical not in expected, f"{label}: duplicate canonical")
        expected.add(canonical)
        if file.name not in {"resume-EN.html", "resume-FR.html"}:
            check(doc.nav == NAV_PATHS, f"{label}: primary navigation changed: {doc.nav}")
        check(len(doc.math_scripts) <= 1, f"{label}: duplicate equation renderer")
        if doc.equations:
            check(len(doc.math_scripts) == 1, f"{label}: equation source without renderer")
        for entity in entities(doc.data):
            check(entity.get("@context") == "https://schema.org" or "@graph" in entity,
                  f"{label}: missing schema.org context")
            if entity.get("@type") == "BlogPosting":
                check(entity.get("author", {}).get("name") == "Yohan Chatelain",
                      f"{label}: article authorship does not identify the site author")
                if "dateModified" in doc.times:
                    check(entity.get("dateModified") == doc.times["dateModified"],
                          f"{label}: displayed modification date disagrees with JSON-LD")

    # Include the error page in link checks, but not in canonical sitemap coverage.
    link_count = 0
    for file, doc in documents.items():
        base = doc.canonicals[0] if doc.canonicals else ORIGIN + "/404.html"
        for target in doc.links:
            parsed = urlsplit(urljoin(base, target))
            if parsed.netloc != urlsplit(ORIGIN).netloc or parsed.scheme not in {"http", "https"}:
                continue
            if parsed.path in EXTERNAL_PROJECT_PATHS:
                continue
            link_count += 1
            destination = resolve_path(site, parsed.path)
            check(destination is not None, f"{file.relative_to(site)}: broken link {target}")
            if destination in documents and parsed.fragment:
                check(unquote(parsed.fragment) in documents[destination].ids,
                      f"{file.relative_to(site)}: missing anchor {target}")

    baseline = json.loads((ROOT / "docs/baseline-urls.json").read_text(encoding="utf-8"))
    for page in baseline["pages"]:
        destination = resolve_path(site, urlsplit(page["url"]).path)
        check(destination in content, f"Previously public URL disappeared: {page['url']}")
        if destination in content:
            check(content[destination].canonicals == [page["url"]],
                  f"Previously public URL has changed canonical: {page['url']}")
            if page.get("datePublished"):
                dates = [e.get("datePublished") for e in entities(content[destination].data)
                         if e.get("@type") == "BlogPosting"]
                # Date-only front matter is serialized at midnight in the pinned `timezone: UTC`.
                check(dates == [f"{page['datePublished']}T00:00:00+00:00"],
                      f"Publication date changed: {page['url']}")

    for path in NEW_PATHS + PAPER_PATHS:
        destination = resolve_path(site, path)
        check(destination in content, f"Required page missing: {path}")
        if destination not in content:
            continue
        doc = content[destination]
        check(len(" ".join(doc.text).split()) >= 400, f"Substantive static content missing: {path}")
        if path.startswith("/software/"):
            software = [e for e in entities(doc.data) if e.get("@type") == "SoftwareSourceCode"]
            check(len(software) == 1, f"Software metadata missing: {path}")
            if software:
                check(software[0].get("contributor", {}).get("@id") == PERSON,
                      f"Software contributor identifier changed: {path}")
                check(bool(software[0].get("codeRepository")), f"Missing code repository: {path}")
        if path in PAPER_PATHS:
            types = [e.get("@type") for e in entities(doc.data)]
            check("BlogPosting" in types and "ScholarlyArticle" in types,
                  f"Paper and announcement metadata must remain separate: {path}")
            paper = next((e for e in entities(doc.data) if e.get("@type") == "ScholarlyArticle"), {})
            check(len(paper.get("author", [])) >= 4, f"Incomplete paper authors: {path}")
            check(bool(paper.get("identifier")), f"Missing paper identifier: {path}")

    for path in ["/", "/about/", "/cv"]:
        doc = content.get(resolve_path(site, path))
        if doc:
            people = [e.get("mainEntity", {}) for e in entities(doc.data)
                      if e.get("mainEntity", {}).get("@type") == "Person"]
            check(len(people) == 1 and people[0].get("@id") == PERSON,
                  f"Existing Person identifier not preserved: {path}")
    cv = content.get(resolve_path(site, "/cv"))
    if cv:
        text = " ".join(cv.text)
        check("Scientific Associate" in text and "CAMH" in text and "Expérience" in text,
              "The CV must retain build-time English and French content")
    home = content.get(resolve_path(site, "/"))
    if home:
        check(home.title == "Numerical Reliability and Scientific Computing | Yohan Chatelain",
              "Homepage rendered title differs from the agreed title")

    sitemap = ET.parse(site / "sitemap.xml").getroot()
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = [u.findtext("s:loc", namespaces=namespace) for u in sitemap]
    check(set(sitemap_urls) == expected and len(sitemap_urls) == len(expected),
          f"Sitemap coverage differs from public HTML: {set(sitemap_urls) ^ expected}")
    for entry in sitemap:
        url = entry.findtext("s:loc", namespaces=namespace)
        modified = entry.findtext("s:lastmod", namespaces=namespace)
        check(bool(modified), f"Sitemap content date missing: {url}")
        doc = content.get(resolve_path(site, urlsplit(url).path))
        if doc:
            metadata_date = doc.modified or next(
                (e["dateModified"] for e in entities(doc.data) if e.get("dateModified")), None
            )
            check(metadata_date == modified, f"Sitemap date differs from metadata: {url}")
        if doc and "dateModified" in doc.times:
            check(modified == doc.times["dateModified"], f"Sitemap date differs from article: {url}")
    robots = (site / "robots.txt").read_text(encoding="utf-8")
    check("User-agent: *\nAllow: /" in robots and f"Sitemap: {ORIGIN}/sitemap.xml" in robots,
          "Search crawler permission or sitemap declaration missing")
    llms = (site / "llms.txt").read_text(encoding="utf-8")
    check(all(ORIGIN + p in llms for p in NEW_PATHS + PAPER_PATHS), "Discovery document lacks new destinations")
    for utility in ["Gemfile", "Gemfile.lock", "vendor", "docs", "scripts", "README.md",
                    "requirements-validation.txt", ".github"]:
        check(not (site / utility).exists(), f"Repository utility copied into public build: {utility}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(content)} public HTML pages, {len(baseline['pages'])} preserved URLs, "
          f"{len(sitemap_urls)} sitemap entries, {link_count} internal links; metadata and static content valid.")


if __name__ == "__main__":
    main()
