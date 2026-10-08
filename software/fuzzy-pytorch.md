---
layout: page
title: "Fuzzy PyTorch: numerical variability in deep learning"
permalink: /software/fuzzy-pytorch/
description: "Fuzzy PyTorch combines Verificarlo and PRISM to evaluate floating-point variability in deep learning models with stochastic arithmetic."
last_modified_at: 2026-10-08
math: true
software:
  name: Fuzzy PyTorch
  repository: https://github.com/big-data-lab-team/fuzzy-pytorch
  languages: [Python, C++, C]
---

Fuzzy PyTorch combines an instrumented PyTorch build with Verificarlo and the PRISM backend to evaluate floating-point variability in deep-learning computations. I created the [PRISM library](https://github.com/verificarlo/prism), contributed to Fuzzy PyTorch, and coauthored the [TMLR paper](/2026/02/18/fuzzy-pytorch-numerical-variability-deep-learning.html) with Inés Gonzalez Pepe, Hiba Akhaddar, and Tristan Glatard.

## Which uncertainty is being evaluated?

For a fixed model $$f_\theta$$ and input $$x$$, write an instrumented inference result as $$Y_r=f_\theta(x;\omega_r)$$. Here $$\omega_r$$ changes arithmetic realizations; it does not denote a new set of learned weights. Hold the checkpoint, preprocessing, dropout configuration, and application-level random seeds fixed when isolating arithmetic sensitivity.

The [versioned documentation](https://github.com/big-data-lab-team/fuzzy-pytorch/blob/4670875252272ca3d7ef8fd12e5f7a039053bba7/README.md) describes stochastic rounding (SR) and up-down rounding (UD) configurations. Distance-weighted SR and equal-probability UD do not have the same error distribution. The [rounding guide](/guides/monte-carlo-arithmetic-stochastic-rounding/) derives a small example of this distinction; implementation-specific coverage and rounding behavior must still be checked in PRISM.

## Execution and analysis workflow

The reviewed repository targets Linux and provides build recipes for instrumented containers. Select the arithmetic mode, build the documented PyTorch environment, and run an existing inference or training script inside it. Additional packages must preserve the instrumented PyTorch and BLAS/LAPACK builds; the upstream instructions discuss installation with dependencies disabled for this purpose.

Capture predictions before taking an argmax or threshold. A discrete classification can remain constant while the underlying scores vary. For segmentation, examine both spatial disagreement and the downstream regional measurements. For training, distinguish arithmetic perturbations from changes in initialization, minibatch order, and nondeterministic kernels.

For repeated scalar predictions, estimate

$$
\bar y=\frac{1}{R}\sum_{r=1}^{R}y_r,\qquad
s_y^2=\frac{1}{R-1}\sum_{r=1}^{R}(y_r-\bar y)^2.
$$

The standard deviation $$s_y$$ characterizes individual realizations. The standard error $$s_y/\sqrt R$$ characterizes the estimated mean under independent sampling. Reporting the latter as numerical variability would understate the dispersion of a single execution.

## Minimal analysis example

Download and run the [rounding experiment](/assets/examples/stochastic_rounding.py):

```sh
python3 stochastic_rounding.py
```

This standard-library example isolates rounding probabilities from a neural network's other components. It uses exact rational arithmetic between fixed-grid rounding steps, so its expected mean and variance can be derived independently of the implementation. It is an introductory diagnostic, not an instrumented PyTorch benchmark.

For actual models, use the [pinned container recipes](https://github.com/big-data-lab-team/fuzzy-pytorch/tree/4670875252272ca3d7ef8fd12e5f7a039053bba7/containers) and [experimental workloads](https://github.com/big-data-lab-team/fuzzy-pytorch/tree/4670875252272ca3d7ef8fd12e5f7a039053bba7/experiments). Those workloads include MNIST, FastSurfer, and WavLM. Reproducing their timings requires the corresponding build, inputs, and execution environment.

## Findings and limits

The TMLR paper reports runtime reductions of 5–60 times relative to Verrou across its evaluated configurations and models spanning 1–341 million parameters. These are comparisons for the paper's tested workloads, not a speedup guarantee for another architecture. See the [research summary](/2026/02/18/fuzzy-pytorch-numerical-variability-deep-learning.html) for the study's method and interpretation.

The instrumented scope determines which sources of arithmetic variability are observable. A CPU-oriented build does not establish instrumentation of every GPU operation. Model accuracy, arithmetic dispersion, and uncertainty about the data-generating process are different quantities and should be evaluated separately.

## Resources

- [Source repository](https://github.com/big-data-lab-team/fuzzy-pytorch)
- [Reviewed README and Linux prerequisites](https://github.com/big-data-lab-team/fuzzy-pytorch/blob/4670875252272ca3d7ef8fd12e5f7a039053bba7/README.md)
- [Published TMLR paper and citation](https://openreview.net/forum?id=0ogq232VGP)
- [Significant-digits analysis](https://github.com/verificarlo/significantdigits)
- [My documented contributions](/cv)
