---
title: Best Paper Award (ACM REP 24)
date: 2024-06-21
---

I am thrilled to announce that the paper titled **"[The Impact of Hardware Variability on Applications Packaged with Docker and Guix: a Case Study in Neuroimaging](https://dl.acm.org/doi/pdf/10.1145/3641525.3663626)"** has been awarded the Best Paper Award at [ACM REP 24](https://acm-rep.github.io/2024/).


## Description
The reproducibility of neuroimaging analyses across computational environments has gained significant attention over the last few years. While software containerization solutions such as Docker and Singularity have been deployed to mask the effects of software-induced variability, variations in hardware architectures still impact neuroimaging results in an unclear way.

This study examines the effect of hardware variability on linear registration results produced by the FSL FLIRT application, a widely-used software component in neuroimaging data analyses. Utilizing the Grid'5000 infrastructure, the authors investigated the effect of nine different CPU models using two software packaging systems (Docker and Guix), and compared the resulting hardware variability to numerical variability measured with random rounding.

Results indicate that hardware, software, and numerical variability lead to perturbations of similar magnitudes — albeit uncorrelated — suggesting that these three types of variability act as independent sources of numerical noise with similar magnitude. Therefore, random rounding emerges as a practical solution to measure the effect of numerical noise induced by hardware variability in this application. The effect of hardware perturbations on linear registration remains moderate, with average translation errors of 0.1 mm (maximum: 0.5 mm) and average rotation errors of 0.02 degrees (maximum: 0.2 degrees). Such variations might impact downstream analyses when linear registration is used as an initialization step for other operations.


## Authors
- Gaël Vila
- Emmanuel Medernach
- Inés Gonzalez
- Axel Bonnet
- Yohan Chatelain
- Michaël Sdika
- Tristan Glatard
- Sorina Camarasu-Pop
