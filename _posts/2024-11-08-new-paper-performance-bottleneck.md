---
title: New paper accepted (GigaScience 2025)
date: 2024-11-08
---

I am thrilled to announce that the paper titled **"[An analysis of performance bottlenecks in MRI preprocessing](https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giae098/8063371?login=true)"** has been accepted at [GigaScience 25](https://academic.oup.com/gigascience).


## Description
Magnetic resonance imaging (MRI) preprocessing is a critical step for neuroimaging analysis. However, the computational cost of MRI preprocessing pipelines is a major bottleneck for large cohort studies and some clinical applications. While high-performance computing and, more recently, deep learning have been adopted to accelerate the computations, these techniques require costly hardware and are not accessible to all researchers. Therefore, it is important to understand the performance bottlenecks of MRI preprocessing pipelines to improve their performance. 

Using the Intel VTune profiler, we characterized the bottlenecks of several commonly used MRI preprocessing pipelines from the Advanced Normalization Tools (ANTs), FMRIB Software Library, and FreeSurfer toolboxes. 

We found few functions contributed to most of the CPU time and that linear interpolation was the largest contributor. Data access was also a substantial bottleneck. We identified a bug in the Insight Segmentation and Registration Toolkit library that impacts the performance of the ANTs pipeline in single precision and a potential issue with the OpenMP scaling in FreeSurfer recon-all. Our results provide a reference for future efforts to optimize MRI preprocessing pipelines.

## Authors
- Mathieu Dugré
- Yohan Chatelain
- Tristan Glatard