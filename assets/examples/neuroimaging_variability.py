"""Synthetic fixed-cohort experiment; no patient data or MRI pipeline is used."""
import argparse
import json
import math
import random
import statistics
from pathlib import Path


def cohort(rng, n, mean):
    values = [rng.gauss(0, 1) for _ in range(n)]
    center, scale = statistics.mean(values), statistics.stdev(values)
    return [(x - center) / scale + mean for x in values]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plot", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    seed, n, repetitions = 20261008, 40, 500
    rng = random.Random(seed)
    control, case = cohort(rng, n, 0), cohort(rng, n, -0.44)
    # One test for the baseline and every realization: the known population variance.
    # Holding the reference fixed attributes every crossing to the added errors alone.
    se = math.sqrt(2 / n)
    baseline_p = math.erfc(abs(-0.44 / se) / math.sqrt(2))
    results, pvalues = [], []
    for ratio in (0.0, 0.1, 0.3, 0.6):
        repeated = [[value + rng.gauss(0, ratio) for _ in range(repetitions)]
                    for value in control + case]
        ps = []
        for k in range(repetitions):
            difference = statistics.mean(row[k] for row in repeated[n:]) - statistics.mean(row[k] for row in repeated[:n])
            ps.append(math.erfc(abs(difference / se) / math.sqrt(2)))
        within_sd = math.sqrt(statistics.mean(statistics.variance(row) for row in repeated))
        flips = sum((p < 0.05) != (baseline_p < 0.05) for p in ps) / repetitions
        results.append({"numerical_to_population_sd_ratio": ratio,
                        "estimated_numerical_sd": within_sd, "decision_crossing_fraction": flips})
        pvalues.append(ps)
        assert abs(within_sd - ratio) < 0.03
    assert results[0]["decision_crossing_fraction"] == 0
    result = {"model": "synthetic independent Gaussian errors; known population SD = 1",
              "seed": seed, "subjects_per_group": n, "repetitions": repetitions,
              "constructed_group_difference": -0.44, "baseline_p": baseline_p,
              "test": "two-sided normal reference with known population variance, fixed across realizations; threshold 0.05",
              "scenarios": results}
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
    if args.plot:
        import matplotlib.pyplot as plt
        plt.rcParams.update({"svg.hashsalt": "neuroimaging-variability", "font.size": 11})
        fig, axes = plt.subplots(1, 2, figsize=(8, 4.2), layout="constrained")
        axes[0].hist(pvalues[2], bins=30, color="#2676a5")
        axes[0].axvline(0.05, color="#b34733", linestyle="--")
        axes[0].set(xlabel="Normal-reference p-value", ylabel="Repetitions", title="Fixed cohort, SD ratio = 0.3")
        axes[1].plot([r["numerical_to_population_sd_ratio"] for r in results],
                     [r["decision_crossing_fraction"] for r in results], marker="o")
        axes[1].set(xlabel="Numerical / population SD", ylabel="Decision-crossing fraction",
                    ylim=(0, 1), title="Constructed near-threshold contrast")
        fig.savefig(args.plot, metadata={"Date": None})


if __name__ == "__main__":
    main()
