---
layout: post
title: "Significant digits viewer"
date: 2024-03-12
categories: significant digits
---


This post demonstrates how to visualize numerical instability in floating-point computations by simulating instability in Chebyshev polynomials using [Monte Carlo Arithmetic](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=3b55cfb2325bc081f113612204733c2a3bd650fe) with [Verificarlo](https://github.com/verificarlo/verificarlo) and displaying the results as an animated GIF.

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Visualizing Numerical Instability in Chebyshev Polynomials

![Animation](/assets/images/tchebychev.gif)


## Example: Chebyshev Polynomial Instability

Chebyshev polynomials are commonly used in numerical analysis and approximation theory, but they can exhibit severe numerical instability due to their ill-conditioned nature, particularly when computed near certain points, such as zeros close to the boundary of the domain. This phenomenon was studied in the polynomial $$ T_{20}(z) = \cos (20\,\cos^{-1}(z)) $$, where the zeros of the polynomial are located at $$ \cos((2k + 1)\pi/40) $$ for $$ k = 0, 1, \dots, 19 $$. In this example from the MCA paper, we focus on the ill-conditioning that arises from computing the polynomial using single-precision floating-point arithmetic. As shown in the figure, small changes in the input lead to large variations in the computed values, especially near \( z = 1 \).

This example highlights how catastrophic cancellation, a common issue in floating-point arithmetic, can affect the accuracy of numerical computations. The results suggest that, while single-precision arithmetic provides accurate results for some values, it becomes unreliable near ill-conditioned points.

### Simulating Instability with Verificarlo

[Verificarlo](https://github.com/verificarlo/verificarlo) can be used to simulate this kind of numerical instability by introducing random perturbations to the floating-point operations. By enabling [Monte Carlo Arithmetic]([Parker, 1999](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=3b55cfb2325bc081f113612204733c2a3bd650fe)) (MCA), Verificarlo randomly perturbs floating-point calculations to mimic the real-world inaccuracies that can arise due to hardware precision limits.

### Visualizing the Instability with Significantdigit-Viewer

After simulating the instability, a critical observation can be made by visualizing how precision deteriorates over time. This loss of significant digits is a direct result of floating-point instability, where small rounding errors progressively accumulate and amplify, especially in ill-conditioned areas of computation. 

When dealing with floating-point numbers, the mantissa (or significand) represents the precision of the number. During computations, numerical instability can introduce noise into the less significant bits of the mantissa, which compromises the accuracy of the result. 

In the visualization, we use color to distinguish between accurate and inaccurate bits in the mantissa. **Correct bits** that remain stable and represent the precise portion of the computation are shown in **blue**, while **noisy bits**, which are affected by rounding errors or floating-point imprecision, are displayed in **red**. 

As the computation progresses, you’ll observe that the **blue section** of the mantissa (the correct bits) shrinks, while the **red section** (the noisy bits) grows. This visual representation provides a clear view of how the floating-point instability corrupts the computation by gradually introducing more noise into the significant digits, reducing the overall precision and reliability of the result.

By visualizing the numerical output as an animated GIF, you can clearly see where the loss of precision begins and how it spreads throughout the computation. The animation highlights how the number of significant digits ([Sohier et al. 2021](https://dl.acm.org/doi/10.1145/3432184)) computed with the Python package [significantdigits](https://pypi.org/project/significantdigits/), decreases as we approach 1.

