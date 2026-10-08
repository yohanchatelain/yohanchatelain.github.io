"""Exact-rational fixed-grid experiment: nearest, SR, and equal-probability rounding."""
import argparse
import json
import math
import random
import statistics
from fractions import Fraction
from pathlib import Path


def trial(mode, rng, steps=400):
    spacing, increment = Fraction(1, 8), Fraction(1, 40)
    value = Fraction(0)
    for _ in range(steps):
        units = (value + increment) / spacing
        lower = units.numerator // units.denominator
        fraction = units - lower
        if mode == "nearest":
            rounded = round(units)
        elif fraction == 0:
            rounded = lower
        elif mode == "sr":
            # Exact Bernoulli probability: no floating-point probability approximation.
            rounded = lower + (rng.randrange(fraction.denominator) < fraction.numerator)
        else:
            rounded = lower + rng.randrange(2)
        value = rounded * spacing
    return float(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plot", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    runs, steps, seed = 1000, 400, 7
    samples = {mode: [trial(mode, random.Random(seed + i), steps) for i in range(runs)]
               for mode in ("nearest", "sr", "equal")}
    summaries = {mode: {"mean": statistics.mean(values), "sample_sd": statistics.stdev(values)}
                 for mode, values in samples.items()}
    # SR's exact endpoint probability is 1/5, giving final mean 10 and variance 1.
    assert abs(summaries["sr"]["mean"] - 10.0) < 6.0 / math.sqrt(runs)
    assert samples["nearest"] == [0.0] * runs
    assert abs(summaries["equal"]["mean"] - 25.0) < 6.0 * 1.25 / math.sqrt(runs)
    result = {"seed_sequence": "7 through 1006", "runs": runs, "steps": steps,
              "spacing": "1/8", "increment": "1/40", "exact_sum": 10,
              "sr_theoretical_mean": 10, "sr_theoretical_sd": 1,
              "equal_theoretical_mean": 25, "equal_theoretical_sd": 1.25,
              "summaries": summaries}
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
    if args.plot:
        import matplotlib.pyplot as plt
        plt.rcParams.update({"svg.hashsalt": "stochastic-rounding", "font.size": 11})
        fig, ax = plt.subplots(figsize=(7, 4.2), layout="constrained")
        for mode, label in [("sr", "Distance-weighted SR"), ("equal", "Equal endpoint probabilities")]:
            ax.hist(samples[mode], bins=25, alpha=0.65, label=label)
        ax.axvline(10, color="black", linestyle="--", label="Exact sum = 10")
        ax.axvline(0, color="gray", linestyle=":", label="Nearest result = 0")
        ax.set(xlabel="Final sum on the fixed grid", ylabel="Repetitions",
               title="Rounding probabilities change bias and dispersion")
        ax.legend(fontsize=9)
        fig.savefig(args.plot, metadata={"Date": None})


if __name__ == "__main__":
    main()
