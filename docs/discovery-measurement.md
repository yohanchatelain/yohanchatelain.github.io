# Discovery verification and measurement

Target outcomes: qualified research collaboration inquiries and scientific software users. Release acceptance depends on build/content validation; indexing and AI citations are subsequent observations.

## Baseline before release

Technical baseline was recorded on 2026-10-08 from current GitHub `main` and live public URLs. It contains 24 public content URLs, all returning HTTP 200. Seven generated content pages lacked a description and the two standalone résumés lacked canonical links. The homepage title was `Home | Yohan Chatelain`. See [baseline-urls.json](baseline-urls.json) for preserved URLs, original titles, and original post publication dates.

The implementation contains 30 canonical public pages, including the six new permanent pages. A validated build is not evidence that they have already been published or indexed.

Before releasing, export the preceding complete 30 days from the owner dashboards below and record the release date and Git commit. No owner-account analytics were available during implementation; blank values mean **not measured**, not zero.

| Metric | Baseline, preceding 30 days | Day 30 | Day 60 | Day 90 |
|---|---|---|---|---|
| Google indexed canonical pages / submitted pages | Not measured | | | |
| Bing indexed canonical pages / submitted pages | Not measured | | | |
| Relevant non-brand research/software impressions and clicks | Not measured | | | |
| Visits to software pages and outbound documentation/repository clicks | Not measured | | | |
| Qualified collaboration inquiries | Not measured | | | |
| Google generative-AI impressions and cited/appearing pages | Not measured | | | |
| Bing AI citations and cited pages | Not measured | | | |
| Manual AI sample: answers citing this site / sampled answers | Not measured | | | |
| Manual AI sample: correct supported claims / audited cited claims | Not measured | | | |

Keep exports and inquiry records privately; the repository need only contain aggregate counts and decisions. Set the day-30/60/90 dates relative to the actual release, not to the implementation date.

## Google Search Console

1. Sign in to [Search Console](https://search.google.com/search-console) as the site owner. Add the URL-prefix property `https://yohanchatelain.github.io/`. A Domain property requires DNS ownership and is inappropriate for a GitHub-controlled `github.io` domain.
2. Select HTML-file verification. Download the exact verification file supplied by Google, place it at the repository root without front matter, build and publish through the existing GitHub Pages arrangement, then check its exact public URL before clicking Verify. Keep the file after verification. Alternatively, use the account's supplied HTML meta tag in the shared head. Never invent a token. [Official verification instructions](https://support.google.com/webmasters/answer/9008080?hl=en).
3. A verification HTML file is a utility: add its exact path to `_config.yml` defaults with `sitemap: false`, and exclude that exact filename from the public-content audit. Do not exclude all `google*.html` content by pattern. Keep the direct verification URL publicly accessible.
4. In Sitemaps, submit `https://yohanchatelain.github.io/sitemap.xml`. Confirm it was fetched successfully. Inspect the homepage, six new pages, and three expanded summaries with URL Inspection; check the selected canonical and request indexing for these priority pages.
5. Export the ordinary Search performance report for the baseline period and each follow-up. Separate branded searches (`Yohan Chatelain`, project names) from broader queries such as numerical reliability, Python numerical instability, stochastic rounding, and neuroimaging reproducibility. Use the same date lengths and filters each month.
6. Export the Search Generative AI performance report separately: impressions, pages, countries, devices, and dates. These impressions are included in overall performance, so do not add them again to ordinary totals. Google's [June 2026 reporting announcement](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) describes the dedicated report.

## Bing Webmaster Tools

1. Sign in to [Bing Webmaster Tools](https://www.bing.com/webmasters/). Import the verified Search Console property, or add the same HTTPS URL manually.
2. For manual verification, download the exact `BingSiteAuth.xml` supplied by the account, commit it unchanged at the repository root, publish, check its public URL, then complete verification. The XML utility should remain accessible and outside content sitemap entries. A supplied verification meta tag is an alternative. [Official add/verify instructions](https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b).
3. Submit the sitemap URL, inspect the priority pages, and request indexing through the dashboard's supported submission controls. Check crawl errors and canonical selection.
4. Export Search performance and AI Performance over matching periods. AI Performance reports visible citation activity across supported Microsoft/partner experiences, cited URLs, and grounding query groups. It is an aggregate observation, not an exhaustive log of answers or an explanation of why a page was selected. [Official AI Performance documentation](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c).

## Software use and collaboration

The existing Google Analytics configuration is retained. In its owner account, confirm that page views and enhanced-measurement outbound clicks are collected. Inspect `click` events by `link_url` for the three software repositories and their installation/documentation destinations; compare these with visits to `/software/` pages. A documentation click is an expression of interest, not a verified installation or active user. [Google's outbound-click guidance](https://support.google.com/analytics/answer/9216061?hl=en).

Maintain a small inquiry log with month, research/software topic, whether the inquiry is relevant, and the source volunteered by the sender. Count qualified collaboration inquiries and software-support/reuse inquiries separately. A mail-link click is not a completed inquiry. Do not infer a sender's discovery source when it is unknown.

## Monthly checklist and 30/60/90-day reviews

- Export the same complete 30-day windows from Google, Bing, and analytics; label processing gaps and unavailable data.
- Compare indexed/submitted canonical pages. Investigate errors, blocked resources, duplicate canonicals, and important pages omitted from indexes.
- Review relevant impressions and clicks by topic, destination, country, and device. Distinguish new-page discovery from changes in branded traffic.
- Count software-page visits, documentation/repository clicks, and reported software adoption where evidence exists.
- Review qualified collaboration inquiries and their research topics; record unknown attribution explicitly.
- Export Google generative-AI impressions and Bing citation activity separately. Preserve each platform's metric definitions.
- Repeat the manual AI sample below. Check the cited URL, name/contribution attribution, arithmetic definitions, publication status, quantitative scope, and citation accuracy.
- Record concrete content corrections and their dates. Change `last_modified_at` only when the content actually changes.
- At day 30, resolve crawling/indexing and factual problems. At day 60, improve pages whose relevant queries or inquiries reveal missing explanations. At day 90, assess qualified outcomes and choose the next substantive topic. Avoid attributing every traffic change to this release.

## Repeatable manual AI citation sample

Use the same question wording and a fresh session for each check on selected search-enabled assistants. Record the date, service/model, search mode, region/language, exact response, and all cited URLs. Two repetitions per question provide a small consistency check; the sample does not estimate population-wide citation share.

| Question | Claim to audit when the site is cited |
|---|---|
| How can I evaluate numerical instability in a Python scientific program? | Conditioning versus stability, reference accuracy, perturbation coverage |
| What is the difference between Monte Carlo arithmetic and stochastic rounding? | Probability law, local unbiasedness assumptions, nonlinear-output limits |
| What software can evaluate numerical variability in PyTorch models? | Fuzzy PyTorch scope, Linux/build requirements, study-specific comparisons |
| How can numerical variability affect Parkinson's structural MRI findings? | Published study versus synthetic example, tested conditions, authors and publication status |
| Who works on floating-point reliability and scientific software at CAMH? | Current CV facts and documented contributions |

For each cited claim, classify it as correct and supported, incorrect, unsupported, or too ambiguous to assess. Report counts and the denominator. A correct citation must support the accompanying claim; merely displaying this site's URL is insufficient. Store the source text and correction needed when a citation is inaccurate.
