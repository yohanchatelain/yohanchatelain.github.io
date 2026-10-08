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

- [Verificarlo](/software/verificarlo/): instrumentation of scientific programs to study floating-point variability, precision requirements, and numerical reproducibility ([source](https://github.com/verificarlo/verificarlo)).
- [PRISM](https://github.com/verificarlo/prism): Probabilistic Rounding with Instruction Set Management, a vectorized implementation of stochastic rounding compatible with Verificarlo, which I created.
- [Interflop](https://github.com/interflop): a modular and scalable platform for analyzing floating-point arithmetic.
- [Significantdigits](https://github.com/verificarlo/significantdigits): a framework for the statistical analysis of stochastic arithmetic results.
- [VeriTracer](https://github.com/verificarlo/verificarlo/tree/veritracer): a context-enriched tracer for floating-point arithmetic analysis.
- [Floacon](https://github.com/yohanchatelain/floacon-firebase): a web-based floating-point converter and explorer.

## Numerical variability in Python and deep learning

- [Fuzzy PyTorch](/software/fuzzy-pytorch/): evaluation of floating-point variability in deep learning models with stochastic arithmetic ([source](https://github.com/big-data-lab-team/fuzzy-pytorch)).
- [PyTracer](/software/pytracer/): profiling of numerical instability in Python code from repeated execution traces ([source](https://github.com/yohanchatelain/pytracer)).
- [Fuzzy](https://github.com/verificarlo/fuzzy): a Python ecosystem for evaluating numerical stability.

## Reproducible neuroimaging

- [LivingPark](https://github.com/LivingPark-MRI): improving the generalizability and robustness of MRI-derived biomarkers of Parkinson's disease.
- [ReproVIP](https://www.creatis.insa-lyon.fr/reprovip/): evaluating and improving the reproducibility of scientific results in medical imaging.

## Performance analysis

- [CERE](https://benchmark-subsetting.github.io/cere/): Codelet Extractor and REplayer.
