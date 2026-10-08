# Source and claim record

Reviewed on 2026-10-08. The implementation is based on `origin/main` commit `b8b2f4ad53112ffc83ca22c361bdaa36e5fb260b`, not the older local `master`. The original 24 public URLs, titles, and announcement dates are recorded in [baseline-urls.json](baseline-urls.json).

## Software and contributions

| Page | Versioned primary documentation | Supported claims |
|---|---|---|
| Verificarlo | [README](https://github.com/verificarlo/verificarlo/blob/783a8bd41c63a5a87fd1f3426df24e8543d90dec/README.md), [backends](https://github.com/verificarlo/verificarlo/blob/783a8bd41c63a5a87fd1f3426df24e8543d90dec/doc/02-Backends.md) | LLVM instrumentation, configurable MCA/PRISM/VPREC arithmetic, C/C++/Fortran wrappers, container installation and documented amd64/aarch64 support |
| Fuzzy PyTorch | [README](https://github.com/big-data-lab-team/fuzzy-pytorch/blob/4670875252272ca3d7ef8fd12e5f7a039053bba7/README.md), [containers](https://github.com/big-data-lab-team/fuzzy-pytorch/tree/4670875252272ca3d7ef8fd12e5f7a039053bba7/containers) | Linux compiled instrumented PyTorch, Verificarlo/PRISM, SR and UD configurations, preserving instrumented dependencies, provided MNIST/FastSurfer/WavLM workloads |
| PyTracer | [README](https://github.com/yohanchatelain/pytracer/blob/c37d5b4c6f42de1412b240cccfb81e9ab74de5ba/README.md), [package requirements](https://github.com/yohanchatelain/pytracer/blob/c37d5b4c6f42de1412b240cccfb81e9ab74de5ba/pyproject.toml) | Current PyTracer 2 rewrite, Python ≥3.12, wrapping/NumPy/monitoring/native-shim coverage, elementwise versus summary metrics; observation distinguished from the perturbation engine |

Contribution statements derive from the current CV and the linked publication record: Verificarlo/VeriTracer/VPREC doctoral work, development of PyTracer, creation of PRISM, and contributions to Fuzzy PyTorch. Yohan Chatelain confirmed that he created PRISM; this attribution is reflected in both CV languages. The Fuzzy PyTorch `SoftwareSourceCode` identifies his contribution to that project; PRISM's creation and the paper's full authorship are recorded separately. Metadata does not invent release versions, licenses, installations, popularity, or performance guarantees.

The software pages' downloadable minimal experiments establish the arithmetic concepts used in diagnosis. They are explicitly described as pedagogical standard-library experiments. They are not executions or performance validations of compiled Verificarlo or Fuzzy PyTorch installations; upstream installation and workload instructions remain the authority for those environments.

## Quantitative and publication claims

| Claim in public content | Primary source and location | Scope retained in the text |
|---|---|---|
| Fuzzy PyTorch runtime reductions of 5–60× relative to Verrou; evaluated model sizes 1–341 million parameters | [TMLR paper](https://openreview.net/pdf?id=0ogq232VGP), abstract; [publication record](https://openreview.net/forum?id=0ogq232VGP) | Evaluated configurations and workloads; not a general speedup guarantee |
| TMLR publication in January 2026; four paper authors | TMLR paper first-page publication header and author line | Month only; no invented publication day in schema. Original February 18 post date preserved |
| FreeSurfer 7.3.1; variation approaching one third of population variability in several regions; thirteen literature studies; approximately 5% cross-sectional and 10% longitudinal average significance-flip probabilities | [Scientific Reports article](https://www.nature.com/articles/s41598-026-64679-2), abstract and publication record | Selected regional measures, literature cases, and numerical model; no universal MRI error rates |
| MRI acceptance July 27 and online publication August 13, 2026; five full paper authors | Same publisher record, dates and author list | Acceptance announcement retained; publisher identifies available text as an unedited early-access manuscript |
| IEEE TC volume 74(1), pp. 200–209, January 2025; eight paper authors and DOI | [DOI record](https://doi.org/10.1109/TC.2024.3475586), [Crossref API record](https://api.crossref.org/works/10.1109/TC.2024.3475586) | October 2024 acceptance announcement retained; issue month not converted to an invented publication day |
| TC reference distributions, common image geometry, masking/normalization/smoothing, voxelwise comparisons, Bonferroni correction, random-seed and GNU libmath perturbations | [Accessible manuscript v2](https://arxiv.org/html/2307.01373v2), Methods and results-stability experiments | Explicitly grounded in the accessible preprint; journal version is linked for final-analysis reproduction. One-ulp changes to rounded libmath outputs are not described as ideal SR |

The Fuzzy PyTorch and MRI numerical claims above are confined to the published abstracts. The pages do not infer unavailable dataset sizes, hardware configurations, exact confidence intervals, or a formula for the paper's NPVR from those abstracts. The neuroimaging guide defines its own illustrative standard-deviation ratio explicitly and does not equate it with the paper's NPVR implementation.

## Mathematical exposition

| Topic | Primary reference |
|---|---|
| Forward error, relative conditioning, backward stability | Higham, [Accuracy and Stability of Numerical Algorithms, second edition](https://doi.org/10.1137/1.9780898718027), 2002 |
| Significant-bit estimation and statistical assumptions | Sohier and colleagues, [Confidence Intervals for Stochastic Arithmetic](https://doi.org/10.1145/3432184), 2021 |
| Ideal stochastic rounding and probabilistic backward-error analysis | Connolly, Higham, Mary, [Stochastic Rounding and Its Probabilistic Backward Error Analysis](https://doi.org/10.1137/20M1334796), 2021 |
| Finite random-bit SR bias | El Arar, Fasi, Filip, Mikaitis, [Probabilistic Error Analysis of Limited-Precision Stochastic Rounding](https://doi.org/10.1137/24M1681458), 2025 |
| Original PyTracer contribution and authorship | Chatelain, Yong, Kiar, Glatard, [PyTracer: Automatically profiling numerical instabilities in Python](https://arxiv.org/abs/2112.11508), 2021 preprint |

The cancellation condition number, fixed-grid binomial expectations, and additive variance/covariance identities are derived in the guides. Empirical sample summaries are kept separate from those analytical statements. The synthetic neuroimaging example is deliberately near a significance threshold and contains no patient data; its crossing fractions are not false-positive rates or estimates of the published study's results.

## Executed examples and figures

| Example | Recorded outputs | Figure |
|---|---|---|
| Cancellation against an 80-digit Decimal reference to the exact binary64 input | [JSON](../assets/examples/results/numerical-instability.json) | [SVG](../assets/images/guides/numerical-instability.svg) |
| Exact-rational fixed-grid summation: nearest, distance-weighted SR, equal endpoint probabilities | [JSON](../assets/examples/results/stochastic-rounding.json) | [SVG](../assets/images/guides/stochastic-rounding.svg) |
| Fixed synthetic cohort with independent Gaussian numerical errors | [JSON](../assets/examples/results/neuroimaging-variability.json) | [SVG](../assets/images/guides/neuroimaging-variability.svg) |

Executed with Python 3.12.3 on Linux x86_64, Matplotlib 3.11.2, NumPy 2.5.3. Seeds, repetitions, model inputs, and plotting commands are recorded in the scripts and guides. `scripts/check_examples.py` compares regenerated JSON with recorded numbers and regenerates all three SVGs. No execution time is presented as an upstream software benchmark.

## Discovery controls

Crawler behavior follows [OpenAI's official bot documentation](https://developers.openai.com/api/docs/bots). Public crawling and OAI-SearchBot are allowed; GPTBot retains the existing permissive policy through the wildcard rule. Search and training are separate controls. `llms.txt` is retained as a descriptive directory; [Google's documentation](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) does not treat it as a ranking mechanism or prerequisite.
