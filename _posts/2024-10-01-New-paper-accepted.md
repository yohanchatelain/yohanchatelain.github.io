---
title: Numerical variability for results stability tests in neuroimaging
date: 2024-10-01
description: A study of numerical variability as a reference distribution for detecting changes in fMRIPrep results,
  published in IEEE Transactions on Computers.
permalink: /2024/10/01/New-paper-accepted.html
last_modified_at: '2026-10-08'
layout: post
paper:
  title: A numerical variability approach to results stability tests and its application to neuroimaging
  url: https://doi.org/10.1109/TC.2024.3475586
  identifier: 10.1109/TC.2024.3475586
  journal: IEEE Transactions on Computers
  authors:
  - Yohan Chatelain
  - Loïc Tetrel
  - Christopher J. Markiewicz
  - Mathias Goncalves
  - Gregory Kiar
  - Oscar Esteban
  - Pierre Bellec
  - Tristan Glatard
---

This work uses a numerical reference distribution to test whether a candidate scientific pipeline result remains compatible with a reference implementation. The original post announced acceptance in October 2024. The journal article appears in *IEEE Transactions on Computers*, volume 74, issue 1, pages 200–209, January 2025, with DOI [10.1109/TC.2024.3475586](https://doi.org/10.1109/TC.2024.3475586).

## Research question

How should a software test distinguish an expected numerical difference from a change in image-processing behavior? Requiring exact equality can reject harmless changes in arithmetic; a fixed tolerance can also be poorly calibrated to the data and operation being tested.

## Method

The [open manuscript](https://arxiv.org/abs/2307.01373) samples perturbed executions of a reference pipeline and compares an unperturbed candidate result with the resulting distribution. Its structural fMRIPrep application preprocesses outputs onto a common image grid, applies masking, normalization, and smoothing, then evaluates voxelwise standardized discrepancies. Multiple comparisons are controlled with Bonferroni correction.

The manuscript investigates both application random-seed variation and approximate random rounding of GNU libmath outputs. The latter adds or removes one unit in the last place from an already rounded function result. This is an approximation to an arithmetic perturbation, not exact probabilistic rounding of an exact real result.

## Findings

The experiments examine reference-consistency checks and changes to image-processing methods. They show that a numerically calibrated comparison can detect subtle method changes while accommodating variation in a reference pipeline. The study also finds that usable smoothing and significance settings depend on the data. Its reported calibration should not be transferred unchanged to another pipeline or image resolution.

## Limitations and statistical interpretation

For an individual location, a standardized discrepancy uses a reference mean and standard deviation. A small dispersion makes a fixed absolute change relatively large. The significance calculation depends on the model for the reference distribution and the preprocessing applied to the compared images.

The normal-reference model, finite reference sample, and spatial preprocessing constrain interpretation. A nominal threshold does not establish sensitivity to every scientifically important change. Failed alignment or incompatible image geometry must be resolved before applying an intensity comparison.

A passing test establishes compatibility with the selected reference distribution and criterion. It does not prove anatomical accuracy or equivalence of every downstream analysis. This distinction is particularly important when the reference implementation has systematic error.

## Reproducibility resources

- [Open manuscript, version 2](https://arxiv.org/abs/2307.01373v2).
- [Journal article and citation](https://doi.org/10.1109/TC.2024.3475586).
- [Fuzzy arithmetic tooling](https://github.com/verificarlo/fuzzy).
- [Statistical analysis with significantdigits](https://github.com/verificarlo/significantdigits).
- [Verificarlo overview](/software/verificarlo/) and [neuroimaging variance guide](/guides/numerical-variability-neuroimaging/).

**Authors:** Yohan Chatelain, Loïc Tetrel, Christopher J. Markiewicz, Mathias Goncalves, Gregory Kiar, Oscar Esteban, Pierre Bellec, and Tristan Glatard. The statistical description above is grounded in the accessible preprint; consult the journal version when reproducing its final published analysis.
