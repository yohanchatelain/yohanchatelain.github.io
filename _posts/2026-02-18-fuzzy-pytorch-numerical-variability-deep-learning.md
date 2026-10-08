---
title: 'Fuzzy PyTorch: evaluating numerical variability in deep learning'
date: 2026-02-18
description: Fuzzy PyTorch integrates PRISM stochastic arithmetic into PyTorch to evaluate numerical variability
  in deep learning models.
permalink: /2026/02/18/fuzzy-pytorch-numerical-variability-deep-learning.html
last_modified_at: '2026-10-08'
layout: post
paper:
  title: 'Fuzzy PyTorch: Rapid Numerical Variability Evaluation for Deep Learning Models'
  url: https://openreview.net/forum?id=0ogq232VGP
  identifier: OpenReview:0ogq232VGP
  journal: Transactions on Machine Learning Research
  authors:
  - Inés Gonzalez-Pepe
  - Hiba Akhaddar
  - Tristan Glatard
  - Yohan Chatelain
---

Fuzzy PyTorch evaluates arithmetic variability in deep-learning models by combining instrumented PyTorch with the Verificarlo compiler and PRISM probabilistic rounding. The paper appeared in *Transactions on Machine Learning Research* in January 2026; this post retains its original announcement date of February 18.

## Research question

How can repeated stochastic-arithmetic executions be made practical for deep-learning workloads while preserving access to the numerical outputs that need to be analyzed? Model predictions can differ through arithmetic even when weights and inputs are fixed. Experiments therefore need to separate arithmetic variability from initialization, data order, and other application randomness.

## Method

PRISM, which I created, supplies probabilistic rounding operations through the Verificarlo instrumentation interface. The study evaluates stochastic rounding and up-down rounding and compares their execution costs with other numerical-analysis tools. The [reproducibility repository](https://github.com/big-data-lab-team/fuzzy-pytorch/tree/4670875252272ca3d7ef8fd12e5f7a039053bba7) includes harmonic-series experiments, NAS Parallel Benchmarks, and deep-learning workloads involving MNIST, FastSurfer, and WavLM.

A scalar output distribution can be summarized by its sample mean and standard deviation. Those summaries should be supplemented with the relevant task endpoint: prediction scores, spatial segmentation measurements, or another quantity used by the scientific analysis. Treating a constant discrete prediction as proof of constant numerical outputs can conceal variation before the decision boundary.

## Findings

The [published paper](https://openreview.net/pdf?id=0ogq232VGP) reports runtime reductions of 5–60 times relative to Verrou across its evaluated configurations. It evaluates models spanning 1–341 million parameters. These results describe the paper's workloads and comparison settings; reproducing the timings requires the matching builds, datasets, and hardware.

| Resource | Purpose |
|---|---|
| Instrumented PyTorch and PRISM | Repeated arithmetic realizations |
| Benchmark scripts and notebooks | Timing and task-specific analysis |
| Unperturbed execution | Baseline for the selected workload |

## Limitations and interpretation

Arithmetic dispersion characterizes the selected model and instrumented scope. It does not establish uncertainty about the data-generating process, and a small dispersion does not exclude systematic numerical error. Backend probabilities also matter: distance-weighted stochastic rounding and equal-probability up-down rounding can have different bias properties. The [rounding guide](/guides/monte-carlo-arithmetic-stochastic-rounding/) derives an illustrative case without relying on a neural-network benchmark.

The reviewed repository targets Linux and requires a compiled instrumented environment. GPU coverage, external libraries, and additional packages need to be checked for the build actually used. Changing or replacing the instrumented PyTorch library can invalidate the intended arithmetic experiment.

## Reproducibility resources

- [Software overview, scope, and installation links](/software/fuzzy-pytorch/).
- [Versioned container recipes](https://github.com/big-data-lab-team/fuzzy-pytorch/tree/4670875252272ca3d7ef8fd12e5f7a039053bba7/containers).
- [Benchmark code and notebooks](https://github.com/big-data-lab-team/fuzzy-pytorch/tree/4670875252272ca3d7ef8fd12e5f7a039053bba7/experiments).
- [Paper, author list, and citation on OpenReview](https://openreview.net/forum?id=0ogq232VGP).

**Authors:** Inés Gonzalez-Pepe, Hiba Akhaddar, Tristan Glatard, and Yohan Chatelain. The authorship of the paper is separate from the authorship of this explanatory post.
