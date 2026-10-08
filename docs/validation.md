# Implementation validation

Validated on 2026-10-08 on branch `seo-ai-discovery`, based on current `origin/main` commit `b8b2f4ad53112ffc83ca22c361bdaa36e5fb260b`.

## Build environment

Ruby 3.3.9 was provisioned from the official Ruby builder's Ubuntu 24.04 toolcache. Bundler 2.5.22 resolved the existing GitHub Pages dependencies into `Gemfile.lock`: GitHub Pages 232, Jekyll 3.10.0, Minima 2.5.1, jekyll-seo-tag 2.8.0, and jekyll-sitemap 1.4.0. The production build completed successfully. The new pull-request workflow uses Ruby 3.3 via `ruby/setup-ruby` and retains the existing publishing arrangement.

Python 3.12.3 executed the examples and audits on Linux x86_64. Figure generation used Matplotlib 3.11.2 and NumPy 2.5.3. Browser validation used Playwright 1.63.0 with Chromium 153.

## Acceptance checks

| Check | Result |
|---|---|
| Production Jekyll build | Pass |
| Public HTML titles, descriptions, absolute self-canonicals | All 30 pages pass |
| JSON-LD parsing and metadata separation | Pass: existing Person identifier; software contributor metadata; separate BlogPosting and ScholarlyArticle on three summaries |
| Historical URLs and publication dates | All 24 original URLs resolve in the build; original post dates match the recorded baseline |
| Internal links and anchors | Pass; separate FloaCon project checked live, HTTP 200 |
| Sitemap | Exactly 30 canonical content URLs; no error/utility entries; content modification dates retained across rebuilds |
| Navigation | Exactly six existing primary pages with concise labels |
| Static scientific content and bilingual CV | Pass with JavaScript disabled in desktop and mobile browsers |
| Scientific examples | All three execute; reported JSON matches and SVG figures regenerate identically in the recorded environment |
| Mathematical rendering | Once per marked page; no rendering errors; original equation source retained in static HTML |
| Desktop/mobile and both themes | Pass: navigation, equations, code blocks, tables, figures, page width |
| Interactive CV | Pass: English/French selection, section menu, print control, loaded résumé content |
| Source traceability | Quantitative paper claims and publication records linked in content-sources.md; simulations clearly separate from measured research results |

The browser script checks the five main content/index/CV pages, the revised significant-digits article, six new pages, and three expanded summaries. It performs 90 page checks: 30 without JavaScript and 60 across mobile/desktop and light/dark combinations. Representative homepage, guide, and CV screenshots were inspected. Wide tables and display equations scroll within the reading column on phones; the dark theme has explicit table and code colors. The production HTML audit also passes with the UTC timezone used by CI; historical calendar dates are preserved without assigning an invented publication time.

The missing Chebyshev GIF in the original significant-digits post was replaced with a mathematical explanation and links to the executed guides. Its permalink and original date remain unchanged; significant-bit agreement is distinguished from reference accuracy.

## Re-run

```sh
JEKYLL_ENV=production bundle exec jekyll build --trace
python3 scripts/audit_site.py
python3 scripts/check_examples.py
python3 scripts/check_browser.py --screenshots /tmp/site-screenshots
```

The build, audit, examples, and browser checks are included in `.github/workflows/validate-site.yml`. Scientific scripts use only the standard library unless figure generation is requested. The pinned validation requirements supply plotting and browser dependencies.

The repository changes and validated build are local review artifacts. No deployment or owner-account verification/submission was performed. Search indexing, analytics baselines, and AI citations require the owner actions and follow-up observations in [discovery-measurement.md](discovery-measurement.md); they are not release prerequisites.
