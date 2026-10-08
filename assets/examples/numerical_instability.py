"""Compare two evaluations of sqrt(x*x + 1) - x against Decimal arithmetic."""
import argparse
import json
import math
from decimal import Decimal, localcontext
from pathlib import Path


def evaluate(x):
    naive = math.hypot(x, 1.0) - x
    stable = 1.0 / (math.hypot(x, 1.0) + x)
    with localcontext() as context:
        context.prec = 80
        dx = Decimal.from_float(x)
        reference = (dx * dx + 1).sqrt() - dx
        errors = [float(abs(Decimal.from_float(y) - reference) / reference)
                  for y in (naive, stable)]
    return {"x": x, "naive": naive, "stable": stable,
            "naive_relative_error": errors[0], "stable_relative_error": errors[1],
            "relative_condition_number": x / math.hypot(x, 1.0)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plot", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = [evaluate(10.0 ** (i / 2)) for i in range(25)]
    assert all(row["stable_relative_error"] < 1e-14 for row in rows)
    assert evaluate(1e8)["naive"] == 0.0
    result = {"reference_decimal_digits": 80, "arithmetic": "Python binary64",
              "examples": [evaluate(x) for x in (1.0, 1e4, 1e8, 1e12)], "curve": rows}
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
    if args.plot:
        import matplotlib.pyplot as plt
        plt.rcParams.update({"svg.hashsalt": "numerical-instability", "font.size": 11})
        fig, ax = plt.subplots(figsize=(7, 4.2), layout="constrained")
        for key, label in [("naive", "Direct subtraction"), ("stable", "Rationalized expression")]:
            ax.loglog([r["x"] for r in rows],
                      [max(r[key + "_relative_error"], 1e-18) for r in rows],
                      marker="o", markersize=3, label=label)
        ax.set(xlabel="Input x", ylabel="Relative forward error",
               title="Cancellation in a well-conditioned function")
        ax.grid(True, which="both", alpha=0.25)
        ax.legend()
        fig.savefig(args.plot, metadata={"Date": None})


if __name__ == "__main__":
    main()
