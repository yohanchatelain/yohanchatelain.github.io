---
layout: page
title: "PyTracer: profiling numerical instability in Python"
permalink: /software/pytracer/
description: "PyTracer records repeated Python execution traces to locate numerical variability, significant-digit loss, and control-flow divergence."
last_modified_at: 2026-10-08
math: true
software:
  name: PyTracer
  repository: https://github.com/yohanchatelain/pytracer
  languages: [Python, C]
---

PyTracer records and compares repeated executions of Python scientific workloads to locate functions associated with numerical variability. I developed PyTracer and coauthored its original study with Nigel Yong, Gregory Kiar, and Tristan Glatard. The [current repository](https://github.com/yohanchatelain/pytracer) documents PyTracer 2, a rewrite for modern Python; the original paper describes the earlier system.

## From output disagreement to attribution

An end-to-end output distribution shows that a result varies, but does not identify the functions that amplify the variation. PyTracer captures function inputs and outputs and aligns corresponding events across executions. This supports inspection of variability at intermediate program boundaries.

For a scalar output with nonzero mean, the descriptive quantity

$$
b_{\mathrm{proxy}}=-\log_2\left(\frac{s_y}{|\bar y|}\right)
$$

expresses relative dispersion in bits. It is a scale-based proxy, not a guarantee that this many output bits equal the exact answer. Near-zero means, non-Gaussian distributions, and systematic bias need separate treatment. The [significantdigits methodology](https://doi.org/10.1145/3432184) defines probability-based estimators with explicit statistical assumptions.

The reviewed PyTracer 2 documentation distinguishes elementwise estimates from summaries computed from array means. A stable average can conceal unstable elements. Inspect the report's metric type and coverage ledger before assigning a scientific interpretation to an apparent precision loss.

## Instrumentation and perturbation are separate

PyTracer observes Python calls and supported numerical operations. A perturbation engine, such as instrumented scientific libraries or fuzzy libmath, supplies changed arithmetic realizations. Repeating an otherwise deterministic, unperturbed program may produce identical traces; that is not evidence that the program is insensitive to rounding changes.

The [reviewed README](https://github.com/yohanchatelain/pytracer/blob/c37d5b4c6f42de1412b240cccfb81e9ab74de5ba/README.md) describes function wrapping, NumPy ufunc interception, tracing arrays, Python runtime monitoring, and an optional native BLAS shim. These mechanisms have different coverage and overhead. Native extensions and operators outside the selected instrumentation still require inspection.

## Minimal numerical experiment

Download the [cancellation example](/assets/examples/numerical_instability.py) and run it:

```sh
python3 numerical_instability.py
```

It evaluates two algebraically equivalent expressions against an 80-digit Decimal reference. At an input of $$10^8$$, direct subtraction produces zero while the rationalized expression gives approximately $$5\times10^{-9}$$. The [Python numerical-instability guide](/guides/numerical-instability-python/) derives the condition number and explains why this is an algorithmic cancellation problem.

To trace a workload, install the documented PyTracer revision in an isolated Python environment, select the intended targets and perturbation engine, and follow the repository's tracing and report commands. The reviewed version requires Python 3.12 or later. Its generated report distinguishes observed calls from captured calls and can be inspected before introducing automated acceptance thresholds.

## Limits of inference

A function may receive already unstable inputs. Compare input and output variability before concluding that it caused the loss. Divergent branches also complicate call alignment: a missing match is not interchangeable with an arithmetic error. Significant-digit estimates describe the chosen perturbation distribution and sample size; they do not replace an accuracy reference or a domain-specific acceptance criterion.

## Documentation and publications

- [Installation, CLI, examples, and coverage at the reviewed revision](https://github.com/yohanchatelain/pytracer/blob/c37d5b4c6f42de1412b240cccfb81e9ab74de5ba/README.md)
- [PyTracer: Automatically profiling numerical instabilities in Python, preprint](https://arxiv.org/abs/2112.11508)
- [Confidence intervals for stochastic arithmetic](https://doi.org/10.1145/3432184)
- [Verificarlo instrumentation](/software/verificarlo/) and [my research publications](/research)
