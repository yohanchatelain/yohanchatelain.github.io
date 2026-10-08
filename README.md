# Yohan Chatelain's research website

Jekyll and Minima website at <https://yohanchatelain.github.io>. GitHub Pages' existing publishing arrangement is retained. The `validate-site` workflow builds and checks pull requests; it does not publish them.

## Build and review

Use Ruby 3.3 and Python 3.12. The locked gems include the GitHub Pages dependency set and `jekyll-sitemap`.

```sh
bundle install
JEKYLL_ENV=production bundle exec jekyll build --trace
python3 scripts/audit_site.py
```

The HTML audit checks titles, descriptions, absolute canonical URLs, JSON-LD, the six navigation links, internal links and anchors, sitemap coverage, preserved URLs and original post dates, static scientific content, and the English/French CV. The separately hosted FloaCon project shares the site's hostname and is documented as an external project rather than a file in this build.

To execute the examples, regenerate their figures, and check Chromium rendering:

```sh
python3 -m pip install -r requirements-validation.txt
python3 -m playwright install --with-deps chromium
python3 scripts/check_examples.py
python3 scripts/check_browser.py --screenshots /tmp/site-screenshots
```

Browser checks use a temporary local server and cover desktop/mobile layouts, light/dark themes, mathematical rendering, figures, navigation, and the CV with and without JavaScript. MathJax is loaded once from the shared head on `math: true` pages. Its CDN must be reachable for the rendering check; equation source and explanatory text remain in the static HTML.

## Content maintenance

- Preserve established permalinks and publication dates. Update `last_modified_at` when the page's content or descriptive metadata actually changes, not on every build.
- Set a unique `description` on every public page. Use `nav_title` for the six main navigation pages; subpages are linked from the indexes.
- Software front matter identifies the repository and supported implementation languages. Its schema records Yohan as a contributor. It does not claim sole software authorship.
- Paper-summary front matter records the full paper author list and verified identifier. Keep the post's `BlogPosting` authorship and dates separate from `ScholarlyArticle` metadata. Omit an exact paper publication date when only a month is verified.
- Keep About and the existing Person metadata consistent with the CV. The permanent Person identifier is `https://yohanchatelain.github.io/#person`.
- New discovery destinations belong in the homepage/index links and `llms.txt`. The sitemap is generated from public HTML; error and repository utility files are excluded.
- Run the scientific examples before changing reported numbers or figures. The Python calculations use the standard library; plotting and browser packages are pinned separately.

See [source and claim records](docs/content-sources.md), the [validation record](docs/validation.md), and the [verification and measurement checklist](docs/discovery-measurement.md).
