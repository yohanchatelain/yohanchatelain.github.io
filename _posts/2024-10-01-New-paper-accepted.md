---
title: New paper (IEEE TC 2024)
date: 2024-10-01
---

I am thrilled to announce that the paper titled "**[A numerical variability approach to results stability
tests and its application to neuroimaging](https://arxiv.org/pdf/2307.01373.pdf)**" has been accepted for publication in [IEEE Transactions on Computers (TC)](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=12) journal.

## Description

Ensuring the long-term reproducibility of data analyses requires results
stability tests to verify that analysis results remain within acceptable
variation bounds despite inevitable software updates and hardware evolutions.
This paper introduces a numerical variability approach for results stability
tests, which determines acceptable variation bounds using random rounding of
floating-point calculations. 

By applying the resulting stability test to
fMRIPrep, a widely-used neuroimaging tool, we show that the test is sensitive
enough to detect subtle updates in image processing methods while remaining
specific enough to accept numerical variations within a reference version of the
application. This result contributes to enhancing the reliability and
reproducibility of data analyses by providing a robust and flexible method for
stability testing.

## Authors
- Yohan Chatelain
- Loic Tetrel
- Christopher J. Markiewicz
- Mathias Goncalvez
- Gregory Kiar
- Oscar Esteban
- Pierre Bellec
- Tristan Glatard