---
title: New preprint (arXiv 2026)
date: 2026-10-02
---

I am thrilled to announce the preprint **"[Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision Emulation Study of a Small GPT-2](https://arxiv.org/abs/2610.01889)"** is available on arXiv.

## Description
This work asks whether low-precision transformer inference should use stochastic rounding (SR) or round-to-nearest (RN), and shows that the answer depends on where in the network the rounding happens. We extend the PRISM vectorized rounding library to arbitrary virtual precision with a variable-precision stochastic rounding algorithm, then derive a probabilistic forward-error bound for linear projections and a second-order decomposition of the cross-entropy loss change at the output softmax. On DistilGPT-2 at 6 significand bits, SR in the MLP keeps perplexity at 1.15x the full-precision reference versus 2.21x for RN, while the ordering reverses at the language-model head; assigning SR to the MLP and RN to the head brings perplexity within 1.10x of the reference. Code is available at [big-data-lab-team/fuzzy-llm](https://github.com/big-data-lab-team/fuzzy-llm).

## Authors
- Yohan Chatelain
- Pablo de Oliveira Castro
