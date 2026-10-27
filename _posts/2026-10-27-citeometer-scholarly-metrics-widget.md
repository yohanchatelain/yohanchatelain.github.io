---
layout: post
title: "Citeometer: Live Citation, Readership, and Download Badges for Academic Sites"
date: 2026-10-27
categories: [projects, web, tools]
tags: [bibliometrics, web-component, openalex, academic, open-science]
description: "Citeometer is a zero-dependency web component and CLI for displaying live scholarly citations, NASA ADS reads, and preprint downloads on static academic websites."
permalink: "/projects/web/tools/2026/10/27/citeometer-scholarly-metrics-widget.html"
last_modified_at: "2026-10-27"
---

I built **[Citeometer](https://github.com/yohanchatelain/citeometer)**, a lightweight, zero-dependency Web Component (`<cite-o-meter>`) to display live scholarly publication metrics—citations, recent readership, PDF downloads, and software/dataset usage—on static academic websites and GitHub Pages.

<cite-o-meter
  title="Longitudinal brain structure changes in Parkinson's disease: a replication study"
  doi="10.1371/journal.pone.0295069"
  ads="2024PLoSO..1995069S"
  layout="card">
</cite-o-meter>

## What Citeometer Does

Academic publications are indexed across multiple open infrastructures, each capturing a different dimension of reach:

- **Citation counts and annual trends** from **OpenAlex**, **Semantic Scholar** (including influential citations), **Crossref**, **Europe PMC**, **OpenCitations**, and **DataCite**—automatically merging preprint and published journal versions so citations are not split across identifiers.
- **Article readership and usage** from **PLOS COUNTER** (views and PDF downloads), **NASA ADS** (90-day rolling reads), and **bioRxiv / medRxiv** (abstract views and PDF downloads).
- **Software and dataset reach** from **Zenodo** (record views and downloads) and **GitHub** (stars and release asset downloads).

For sources that do not permit direct cross-origin browser requests (such as NASA ADS and bioRxiv usage tables), Citeometer includes a zero-dependency Node CLI (`npx citeometer`) that can run in a daily GitHub Action to maintain a static JSON snapshot alongside live browser queries.

## Quickstart

Load the bundle from npm via jsDelivr in your site `<head>`:

```html
<script src="https://cdn.jsdelivr.net/npm/citeometer@1.1.1/dist/citeometer.min.js" defer></script>
```

Then drop `<cite-o-meter>` under any publication entry (`badge`, `compact`, or `card` layout):

```html
<cite-o-meter
  doi="10.1109/tc.2024.3475586"
  arxiv="2307.01373"
  layout="badge">
</cite-o-meter>
```

## Links

- **Live playground and embed generator:** [yohanchatelain.github.io/citeometer](https://yohanchatelain.github.io/citeometer/)
- **npm package:** [npmjs.com/package/citeometer](https://www.npmjs.com/package/citeometer)
- **Source code:** [github.com/yohanchatelain/citeometer](https://github.com/yohanchatelain/citeometer)
- **Live on this site:** [Research publications](/research)
