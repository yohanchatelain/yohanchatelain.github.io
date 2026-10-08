---
layout: post
title: "Evaluating numerical instability in Python"
permalink: /guides/numerical-instability-python/
description: "Distinguish conditioning, algorithmic stability, and arithmetic variability with a Python cancellation experiment and a high-precision reference."
date: 2026-10-08
last_modified_at: 2026-10-08
author: Yohan Chatelain
math: true
---

Numerical diagnosis requires separating sensitivity of the mathematical problem from errors introduced by its implementation. This guide derives a cancellation example, evaluates it against a high-precision reference, and explains how repeated arithmetic experiments complement that comparison.

## Conditioning, stability, and forward error

Let $$f(x)$$ be an exact mathematical quantity and $$\widehat f(x)$$ its computed approximation. Relative forward error is

$$
E_f(x)=\frac{|\widehat f(x)-f(x)|}{|f(x)|},\qquad f(x)\ne0.
$$

For a differentiable scalar function with $$x\ne0$$ and $$f(x)\ne0$$, and a small input perturbation $$\delta x$$, the relative condition number is

$$
\kappa_f(x)=\left|\frac{x f'(x)}{f(x)}\right|,
\qquad
\frac{|\delta f|}{|f(x)|}\approx\kappa_f(x)\frac{|\delta x|}{|x|}.
$$

Conditioning is a property of the problem at the chosen input. Backward stability is a property of an algorithm: its output can be interpreted as the exact result for a nearby input, with a suitably small backward error. Even a backward-stable algorithm can have a large forward error when the problem is ill-conditioned. Conversely, an unstable evaluation can lose accuracy on a well-conditioned problem.

These definitions follow the classical distinction in [Higham, *Accuracy and Stability of Numerical Algorithms*](https://doi.org/10.1137/1.9780898718027). A reference calculation tests forward accuracy at specific inputs; it does not establish a general stability theorem.

## A well-conditioned function with an unstable evaluation

Consider, for $$x>0$$,

$$
f(x)=\sqrt{x^2+1}-x
    =\frac{1}{\sqrt{x^2+1}+x}.
$$

Differentiation gives $$f'(x)=-f(x)/\sqrt{x^2+1}$$ and therefore

$$
\kappa_f(x)=\frac{x}{\sqrt{x^2+1}}<1.
$$

The exact function is well-conditioned under relative perturbations of positive $$x$$. For large $$x$$, however, the direct expression subtracts nearly equal quantities. A rounding error in the square root can be comparable to the entire difference, which is asymptotically $$1/(2x)$$. Rationalization avoids that subtraction.

The experiment uses `math.hypot(x, 1.0)` to evaluate the square root without unnecessarily overflowing `x*x`. This improves the intermediate calculation but cannot prevent cancellation in the subsequent subtraction.

## Reproduce the experiment

Download [numerical_instability.py](/assets/examples/numerical_instability.py). The calculation uses only Python's standard library:

```sh
python3 numerical_instability.py
```

The script compares both expressions with an 80-digit Decimal evaluation over 25 inputs from 1 to $$10^{12}$$. The Decimal reference starts from the exact binary64 input through `Decimal.from_float`, so the comparison concerns evaluation error at that input, rather than disagreement about how a decimal input was represented.

| Input | Direct subtraction | Rationalized expression | Relative error of direct subtraction |
|---|---:|---:|---:|
| $$10^4$$ | approximately $$5.0000000556\times10^{-5}$$ | approximately $$4.9999999875\times10^{-5}$$ | approximately $$1.36\times10^{-8}$$ |
| $$10^8$$ | 0 | approximately $$5\times10^{-9}$$ | 1 |
| $$10^{12}$$ | 0 | approximately $$5\times10^{-13}$$ | 1 |

These values come from the [recorded run](/assets/examples/results/numerical-instability.json). Last-bit differences in mathematical libraries can affect the table on another platform. The example checks that the rationalized expression remains below a relative error of $$10^{-14}$$ over the tested range.

![Relative forward error of direct subtraction and the rationalized expression, compared with an 80-digit reference.](/assets/images/guides/numerical-instability.svg)

*Figure: executed example results. The mathematical condition number stays below one while the direct evaluation loses accuracy. Plotted errors have a display floor of $$10^{-18}$$.*

To regenerate the figure, install Matplotlib 3.11.2 and run:

```sh
python3 numerical_instability.py --plot numerical-instability.svg
```

The recorded environment was Python 3.12.3 on Linux x86_64; plotting used Matplotlib 3.11.2 and NumPy 2.5.3. Both numerical formulas and the reference calculation are independent of NumPy.

## What repeated experiments add

For arithmetic realizations $$Y_1,\ldots,Y_R$$ with fixed scientific inputs, estimate the sample mean and variance:

$$
\bar Y=R^{-1}\sum_rY_r,\qquad
s^2=(R-1)^{-1}\sum_r(Y_r-\bar Y)^2.
$$

The variance characterizes sensitivity to the chosen perturbation model. It cannot detect an identical systematic bias in every realization: repeated zero outputs in the cancellation example could have zero sample variance and a relative forward error of one. Compare a distribution with a reference or an application-level criterion whenever one is available.

[PyTracer](/software/pytracer/) helps localize variability across Python call boundaries; [Verificarlo](/software/verificarlo/) and other perturbation engines change selected arithmetic operations. Verify coverage, vary arithmetic seeds independently, and report the instrumented scope. A stable mean of an array does not establish that every element is stable.

## Interpretation and references

Avoid treating a rounding experiment as measurement uncertainty or as a complete hardware model. Validate behavior near zero, underflow, overflow, and branch boundaries separately. The positive-input derivation above is specific to this function and does not extend automatically to another algorithm.

- Higham (2002), [*Accuracy and Stability of Numerical Algorithms*, second edition](https://doi.org/10.1137/1.9780898718027).
- Chatelain, Yong, Kiar, and Glatard, [*PyTracer: Automatically profiling numerical instabilities in Python*](https://arxiv.org/abs/2112.11508).
- Sohier and colleagues, [*Confidence intervals for stochastic arithmetic*](https://doi.org/10.1145/3432184).
- [Monte Carlo arithmetic and stochastic rounding](/guides/monte-carlo-arithmetic-stochastic-rounding/).
