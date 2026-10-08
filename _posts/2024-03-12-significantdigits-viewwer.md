---
layout: post
title: "Visualizing numerical instability with significant digits"
date: 2024-03-12
categories: significant digits
description: "Visualize significant bits in a Chebyshev polynomial computation using Monte Carlo arithmetic, Verificarlo, and significantdigits."
permalink: "/significant/digits/2024/03/12/significantdigits-viewwer.html"
last_modified_at: "2026-10-08"
math: true
---

This post introduces a significant-bit view of repeated arithmetic executions. The accompanying [significantdigits package](https://github.com/verificarlo/significantdigits) implements statistical estimators for stochastic arithmetic. Such estimates describe agreement within a chosen experiment; an external accuracy reference is needed to distinguish stable errors from correct results.

## Chebyshev polynomials: conditioning and evaluation

For an integer degree $$n$$ and $$-1<z<1$$, the Chebyshev polynomial of the first kind is

$$
T_n(z)=\cos(n\arccos z).
$$

For $$n=20$$, its roots are $$\cos((2k+1)\pi/40)$$ for $$k=0,\ldots,19$$. Wherever the output is nonzero, its relative condition number with respect to the input is

$$
\kappa(z)=\left|\frac{zT'_n(z)}{T_n(z)}\right|.
$$

Relative conditioning becomes problematic near a root because the denominator approaches zero. Near a zero output, absolute error is often more interpretable than relative error. At the endpoint $$z=1$$, the limiting derivative is $$n^2$$; this sensitivity is finite for a fixed degree and is a different issue from relative conditioning at a root.

The evaluation method also matters. A recurrence, an expanded power-basis polynomial, and the trigonometric expression can accumulate different arithmetic errors. Sensitivity of the mathematical problem does not by itself diagnose instability of a particular evaluation algorithm. The [Python numerical-instability guide](/guides/numerical-instability-python/) supplies an executed example in which a well-conditioned function loses accuracy through cancellation.

## What a significant-bit visualization means

Repeated executions under a specified stochastic arithmetic model produce an empirical output distribution. The [methodology of Sohier and colleagues](https://doi.org/10.1145/3432184) defines significant-bit estimators and confidence bounds under stated statistical assumptions. A visualization can color positions associated with low estimated variability, but it should not label those bits as correct without an appropriate reference.

Sample size, perturbation law, virtual precision, and output normalization affect the estimate. A mean close to zero can make a relative estimator uninformative. A multimodal distribution or divergent execution path also requires more than a single precision score. In particular, a deterministic but wrong result can have zero empirical variance.

## Reproduce a numerical diagnosis

[Verificarlo](/software/verificarlo/) supplies compiler instrumentation and arithmetic backends for repeated numerical experiments. [PyTracer](/software/pytracer/) helps compare intermediate Python calls. The [Monte Carlo arithmetic and stochastic-rounding guide](/guides/monte-carlo-arithmetic-stochastic-rounding/) distinguishes their perturbation models and includes an executed experiment with downloadable results and a static figure.

Record the instrumented operations and libraries, arithmetic seeds, precision, number of repetitions, and the accuracy or task criterion used to interpret the outputs. These records make the numerical evidence reviewable even when an interactive visualization is unavailable.
