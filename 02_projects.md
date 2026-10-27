---
title: Projects
permalink: /projects
layout: page
nav_title: "Projects"
description: "PRISM, created by Yohan Chatelain, and his work on Verificarlo, PyTracer, Fuzzy PyTorch, and reproducible neuroimaging software."
last_modified_at: "2026-10-08"
---

My software work connects floating-point analysis and instrumentation with the reproducibility of scientific software, AI, and neuroimaging pipelines. Selected results are summarized in posts on [numerical variability in deep learning](/2026/02/18/fuzzy-pytorch-numerical-variability-deep-learning.html), [Parkinson's structural MRI](/2026/07/27/parkinsons-mri-scientific-reports-acceptance.html), and [results stability tests](/2024/10/01/New-paper-accepted.html); the full list of publications is on the [Research](/research) page. Technical guides cover [Python numerical stability](/guides/numerical-instability-python/), [Monte Carlo arithmetic and stochastic rounding](/guides/monte-carlo-arithmetic-stochastic-rounding/), and [numerical variability in neuroimaging](/guides/numerical-variability-neuroimaging/).

Verificarlo, Fuzzy PyTorch, and PyTracer have dedicated pages describing my contributions, the arithmetic model, documented workflows, examples, and limitations.

## Floating-point analysis and stochastic arithmetic

- [Verificarlo](/software/verificarlo/): instrumentation of scientific programs to study floating-point variability, precision requirements, and numerical reproducibility ([source](https://github.com/verificarlo/verificarlo)). \\
  <cite-o-meter github="verificarlo/verificarlo" docker="verificarlo/verificarlo" doi="10.1109/arith.2016.31" layout="badge" lazy="true"></cite-o-meter>
- [PRISM](https://github.com/verificarlo/prism): Probabilistic Rounding with Instruction Set Management, a vectorized implementation of stochastic rounding compatible with Verificarlo, which I created. \\
  <cite-o-meter github="verificarlo/prism" layout="badge" lazy="true"></cite-o-meter>
- [Interflop](https://github.com/interflop): a modular and scalable platform for analyzing floating-point arithmetic. \\
  <cite-o-meter github="interflop" layout="badge" lazy="true"></cite-o-meter>
- [Significantdigits](https://github.com/verificarlo/significantdigits): a framework for the statistical analysis of stochastic arithmetic results. \\
  <cite-o-meter github="verificarlo/significantdigits" pypi="significantdigits" doi="10.1145/3432184" layout="badge" lazy="true"></cite-o-meter>
- [VeriTracer](https://github.com/verificarlo/verificarlo/tree/veritracer): a context-enriched tracer for floating-point arithmetic analysis. \\
  <cite-o-meter doi="10.1109/arith.2018.8464687" layout="badge" lazy="true"></cite-o-meter>
- [Floacon](https://github.com/yohanchatelain/floacon-firebase): a web-based floating-point converter and explorer. \\
  <cite-o-meter github="yohanchatelain/floacon-firebase" layout="badge" lazy="true"></cite-o-meter>

## Numerical variability in Python and deep learning

- [Fuzzy PyTorch](/software/fuzzy-pytorch/): evaluation of floating-point variability in deep learning models with stochastic arithmetic ([source](https://github.com/big-data-lab-team/fuzzy-pytorch)). \\
  <cite-o-meter github="big-data-lab-team/fuzzy-pytorch" arxiv="2605.25991" layout="badge" lazy="true"></cite-o-meter>
- [PyTracer](/software/pytracer/): profiling of numerical instability in Python code from repeated execution traces ([source](https://github.com/yohanchatelain/pytracer)). \\
  <cite-o-meter github="yohanchatelain/pytracer" pypi="pytracer" doi="10.1109/tc.2022.3224377" arxiv="2112.11508" layout="badge" lazy="true"></cite-o-meter>
- [Fuzzy](https://github.com/verificarlo/fuzzy): a Python ecosystem for evaluating numerical stability. \\
  <cite-o-meter github="verificarlo/fuzzy" docker="verificarlo/fuzzy" layout="badge" lazy="true"></cite-o-meter>

## Reproducible neuroimaging

- [LivingPark](https://github.com/LivingPark-MRI): improving the generalizability and robustness of MRI-derived biomarkers of Parkinson's disease. \\
  <cite-o-meter github="LivingPark-MRI" pypi="livingpark-utils" layout="badge" lazy="true"></cite-o-meter>
- [ReproVIP](https://www.creatis.insa-lyon.fr/reprovip/): evaluating and improving the reproducibility of scientific results in medical imaging.

## Performance analysis

- [CERE](https://benchmark-subsetting.github.io/cere/): Codelet Extractor and REplayer. \\
  <cite-o-meter github="benchmark-subsetting/cere" doi="10.1145/2700312" layout="badge" lazy="true"></cite-o-meter>

## Scholarly metrics and web tools

- [Citeometer](https://github.com/yohanchatelain/citeometer): an embeddable, zero-dependency web component for live citation, download, and readership metrics across OpenAlex, Semantic Scholar, Crossref, Europe PMC, NASA ADS, bioRxiv, PLOS, and Zenodo ([post](/projects/web/tools/2026/10/27/citeometer-scholarly-metrics-widget.html), [live demo](https://yohanchatelain.github.io/citeometer/), [npm](https://www.npmjs.com/package/citeometer)). \\
  <cite-o-meter github="yohanchatelain/citeometer" npm="citeometer" layout="badge" lazy="true"></cite-o-meter>
