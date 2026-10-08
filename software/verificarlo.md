---
layout: page
title: "Verificarlo: floating-point instrumentation and numerical reliability"
permalink: /software/verificarlo/
description: "Verificarlo instruments scientific programs to study floating-point variability, precision requirements, and numerical reproducibility."
last_modified_at: 2026-10-08
math: true
software:
  name: Verificarlo
  repository: https://github.com/verificarlo/verificarlo
  languages: [C, C++, Fortran, Python]
---

Verificarlo instruments floating-point computations during compilation and delegates their execution to configurable arithmetic backends. It supports experiments on rounding sensitivity, reduced precision, and the numerical reproducibility of scientific programs. I contribute to its numerical-analysis and instrumentation tools; my doctoral work included Verificarlo, VeriTracer, and VPREC.

## Scientific problem and instrumentation model

A floating-point program computes an approximation to a real-arithmetic expression. Changing an instruction sequence, compiler optimization, library implementation, or parallel reduction order can change that approximation. Bitwise disagreement alone does not establish whether the difference matters for a scientific conclusion.

Verificarlo uses LLVM instrumentation to replace selected arithmetic operations with calls to a backend. The backend determines which operations are perturbed and how they are evaluated. The [documented backends](https://github.com/verificarlo/verificarlo/blob/783a8bd41c63a5a87fd1f3426df24e8543d90dec/doc/02-Backends.md) include Monte Carlo arithmetic, PRISM probabilistic rounding, and variable-precision arithmetic. These modes answer different experimental questions: a distribution under virtual precision, sensitivity to a rounding rule, or the consequences of reducing a representation's precision.

Write a perturbed result as $$Y_r=F(x;\omega_r)$$, where the input $$x$$ and program configuration are fixed and $$\omega_r$$ identifies the arithmetic realization. Repeated executions estimate the distribution induced by that configuration. Its dispersion describes sensitivity to the selected model; it is not an exhaustive enumeration of hardware behavior or a proof of forward accuracy.

## Supported workflow

Compile the code to be investigated, select a backend, execute independent repetitions, and retain outputs at scientifically relevant boundaries. Keep input data, application-level random seeds, and thread settings fixed while changing arithmetic seeds. Record the compiler revision, backend options, and instrumented scope.

The [versioned upstream README](https://github.com/verificarlo/verificarlo/blob/783a8bd41c63a5a87fd1f3426df24e8543d90dec/README.md) documents C, C++, and Fortran compiler wrappers and container-based installation. Its installation documentation covers amd64 and aarch64. Rebuilding an application with Verificarlo does not automatically instrument opaque external libraries: their inclusion must be checked separately.

## Minimal numerical experiment

Before applying instrumentation to a production pipeline, establish a reference calculation. The [fixed-grid rounding example](/assets/examples/stochastic_rounding.py) compares deterministic nearest rounding, distance-weighted stochastic rounding, and equal endpoint probabilities using exact rational intermediate values:

```sh
python3 stochastic_rounding.py
```

Download the script, then run this command with Python 3.12 or later. It requires only the standard library. The exact sum is 10; the script checks its stochastic sample mean against the analytical expectation. This is a pedagogical arithmetic model, not a Verificarlo backend implementation. The [rounding guide](/guides/monte-carlo-arithmetic-stochastic-rounding/) gives the derivation and generated figure.

For an instrumented application, follow the [upstream usage and tutorial](https://github.com/verificarlo/verificarlo/blob/783a8bd41c63a5a87fd1f3426df24e8543d90dec/README.md#usage). Compare its unperturbed output and repeated backend outputs against a reference or scientific acceptance criterion. An unchanged output can also indicate incomplete instrumentation, so confirm backend coverage before interpreting it.

## Limitations and interpretation

Small dispersion can coexist with systematic error. Overflow, underflow, discontinuous branching, and an ill-conditioned input problem also require separate investigation. Backend settings and library coverage belong in a report of the experiment, because they determine what the observed distribution represents.

For Python call-level attribution, see [PyTracer](/software/pytracer/). For stochastic arithmetic within deep-learning workloads, see [Fuzzy PyTorch](/software/fuzzy-pytorch/). The [neuroimaging guide](/guides/numerical-variability-neuroimaging/) explains how numerical variability can be propagated to an inferential endpoint.

## Documentation and citation

- [Repository and installation](https://github.com/verificarlo/verificarlo)
- [Backend documentation at the reviewed revision](https://github.com/verificarlo/verificarlo/blob/783a8bd41c63a5a87fd1f3426df24e8543d90dec/doc/02-Backends.md)
- [Upstream citation instructions](https://github.com/verificarlo/verificarlo#how-to-cite-verificarlo)
- [My software contributions and research experience](/cv)

The repository links above identify the reviewed source revision. Consult the current release documentation before installing a different version.
