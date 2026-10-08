---
title: 'Numerical variability in Parkinson’s structural MRI: Scientific Reports study'
date: 2026-07-27
description: A study of FreeSurfer numerical variability, the Numerical-Population Variability Ratio, and statistical
  conclusions in Parkinson’s MRI research.
permalink: /2026/07/27/parkinsons-mri-scientific-reports-acceptance.html
last_modified_at: '2026-10-08'
layout: post
paper:
  title: The practical impact of numerical variability on structural MRI measures of Parkinson’s disease
  url: https://doi.org/10.1038/s41598-026-64679-2
  identifier: 10.1038/s41598-026-64679-2
  published_on: '2026-08-13'
  journal: Scientific Reports
  authors:
  - Yohan Chatelain
  - Andrzej Sokołowski
  - Madeleine Sharp
  - Jean-Baptiste Poline
  - Tristan Glatard
---

This study evaluates how numerical variability in structural MRI processing can affect group comparisons and clinical associations in Parkinson's disease research. The original post announced acceptance on July 27, 2026. The [Scientific Reports article](https://doi.org/10.1038/s41598-026-64679-2) was published online on August 13, 2026. At this revision, the publisher identifies the available text as an unedited early-access manuscript.

## Research question

Are the numerical differences produced by a processing pipeline small relative to the differences being interpreted statistically? An image can appear similar across executions while a regional measurement or inferential result changes. The relevant comparison therefore involves both numerical dispersion and the scale of the population measurements.

## Method

The study instruments FreeSurfer 7.3.1 to simulate numerical differences across computational environments, then measures variability in structural MRI analyses of Parkinson's disease patients and controls. Its Numerical-Population Variability Ratio (NPVR) workflow estimates the numerical contribution in a study and propagates that contribution to statistics and associated p-values. Definitions and implementation details are provided by the paper and [study repository](https://github.com/yohanchatelain/livingpark-numerical-variability).

Repeated processing holds the scientific input fixed while changing a numerical realization. Between-subject variability answers a different question. Ratios should state whether their numerator and denominator are variances or standard deviations; these have different numerical values and interpretations.

## Findings

The published abstract reports numerical variation approaching one third of population variability in multiple cortical and subcortical regions. Applying the workflow to thirteen previously published studies produced average significance-flip probabilities of approximately 5% for cross-sectional analyses and 10% for longitudinal analyses. These are results of the study's selected measures, literature cases, and perturbation model, not universal rates for MRI analysis.

| Analysis level | Quantity to inspect |
|---|---|
| Pipeline output | Regional morphometric measurements across realizations |
| Group comparison | Effect estimates and their numerical distributions |
| Longitudinal analysis | Change scores and numerical covariance across time points |

## Limitations and interpretation

A significance crossing is not, by itself, a demonstration that a biological claim is false. It indicates that a chosen numerical realization can affect a thresholded statistical decision. Its interpretation depends on the effect estimate, uncertainty model, threshold, and analysis design.

Correlated errors across regions or time points require attention when propagating variability. Scanner noise, motion, and population sampling are additional sources of uncertainty. Numerical instrumentation does not substitute for evaluating those sources, nor does the observed variability exhaust all possible computational environments.

The [neuroimaging guide](/guides/numerical-variability-neuroimaging/) develops an additive model and an intentionally near-threshold synthetic contrast. That example illustrates a mechanism; its simulated crossing fraction is separate from the published study's measured results.

## Reproducibility resources

- [Published article and DOI](https://doi.org/10.1038/s41598-026-64679-2).
- [Original January 2026 bioRxiv announcement](/2026/01/09/parkinsons-mri-numerical-variability.html).
- [Processing, analysis code, and reproducibility artifacts](https://github.com/yohanchatelain/livingpark-numerical-variability).
- [Numerical variability and neuroimaging reproducibility](/guides/numerical-variability-neuroimaging/).

**Authors:** Yohan Chatelain, Andrzej Sokołowski, Madeleine Sharp, Jean-Baptiste Poline, and Tristan Glatard.
