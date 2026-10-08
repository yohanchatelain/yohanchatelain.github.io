---
layout: post
title: "Invited lecture at ATPESC 2026: Verificarlo"
date: 2026-07-30
categories: [talks]
tags: [verificarlo, floating-point, mixed-precision, hpc, atpesc]
description: "Lecture and hands-on tutorial on debugging and optimizing floating-point calculations with Verificarlo at ATPESC 2026."
permalink: "/talks/2026/07/30/atpesc-2026-verificarlo-lecture.html"
last_modified_at: "2026-10-08"
---

I gave an invited lecture and hands-on tutorial, **"Verificarlo: Debugging and optimising floating-point calculations"**, at the [Argonne Training Program on Extreme-Scale Computing (ATPESC 2026)](https://extremecomputingtraining.anl.gov/2026-agenda), in the *Track 4b: Mixed Precision Computing* session (Thursday, July 30, 2026, Q Center, St. Charles, IL).

📊 **[Slides](https://docs.google.com/presentation/d/1CudyPJLy3CAvQ2MOzgMWqPbONmUNGX9gLfYSqt1096M/edit?usp=sharing)** — the tutorial part runs in Google Colab.

## Content

The talk covers how numerical variability arises in scientific software, and what the Verificarlo toolchain gives you to measure and act on it:

*   **Why floating point bites**: Ariane 5, the Vancouver Stock Exchange index, the Pentium FDIV bug — rounding, overflow, and cancellation as engineering risks, amplified by long-lived codes and hardware/software updates.
*   **Measuring error without a ground truth**: Monte Carlo Arithmetic and stochastic rounding turn "do I trust this result?" into an observable number of significant digits (illustrated on an ill-conditioned 2×2 Cramer system, and on Muller's sequence, which converges to the *wrong* limit at every finite precision).
*   **[Verificarlo](https://github.com/verificarlo/verificarlo)**: a clang/flang-based compiler that replaces floating-point operations with generic calls, so several numerical models can be selected at runtime from a single compilation.
*   **VPREC**: dynamic reduced-precision emulation (3–15× overhead), and its use to find mixed-precision configurations — cutting time, memory footprint, and MPI communication volume on the YALES2 combustion solver.
*   **[Fuzzy](https://github.com/verificarlo/fuzzy) and [PRISM](https://github.com/big-data-lab-team/fuzzy-pytorch)**: stochastic arithmetic for Python, libm, and PyTorch. PRISM's vectorized stochastic rounding is ~50× faster than the state of the art, making SR tractable on CPU for models like FastSurfer and WavLM.
*   **Localizing instabilities**: VeriTracer and PyTracer, and case studies where the instability was traced to max-pooling index selection (FastSurfer) or to a significant numerical change introduced in fMRIPrep LTS 20.2.5.

## Takeaways

Numerical error is measurable, more precision is not a silver bullet, and the same instrumentation answers three different questions: *is it right?* (stochastic rounding), *how little precision do I need?* (VPREC), and *where does it break?* (VeriTracer, PyTracer).
