---
title: New paper (TMLR 2026)
date: 2026-02-18
---

I am thrilled to announce the paper **"[Fuzzy PyTorch: Rapid Numerical Variability Evaluation for Deep Learning Models](https://openreview.net/pdf?id=0ogq232VGP)"** has been published in *Transactions on Machine Learning Research (2026)*.

## Description
This paper introduces Fuzzy PyTorch, a framework for assessing how floating-point arithmetic uncertainties affect deep learning model behavior. It integrates stochastic arithmetic into PyTorch via PRISM (Probabilistic Rounding with Instruction Set Management), a novel library interfacing with the Verificarlo compiler. The approach supports both traditional stochastic rounding and a newly developed up-down rounding mode, achieving runtime reductions of 5× to 60× versus Verrou while scaling to models with up to 341 million parameters.

## Code and Data
The code is open source and available on GitHub: [big-data-lab-team/fuzzy-pytorch](https://github.com/big-data-lab-team/fuzzy-pytorch). The repository includes the PRISM library, the modified Verificarlo compiler, a Dockerfile to build Fuzzy PyTorch, and the scripts used to run the experiments.

## Authors
- Inés Gonzalez Pepe
- Hiba Akhaddar
- Tristan Glatard
- Yohan Chatelain
