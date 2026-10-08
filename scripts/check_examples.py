"""Execute the scientific examples; compare recorded numbers and regenerate SVGs."""

import json
import math
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = [
    ("numerical_instability.py", "numerical-instability"),
    ("stochastic_rounding.py", "stochastic-rounding"),
    ("neuroimaging_variability.py", "neuroimaging-variability"),
]


def compare(actual, expected, location="result"):
    if isinstance(expected, dict):
        assert actual.keys() == expected.keys(), location
        for key in expected:
            compare(actual[key], expected[key], f"{location}.{key}")
    elif isinstance(expected, list):
        assert len(actual) == len(expected), location
        for index, (left, right) in enumerate(zip(actual, expected)):
            compare(left, right, f"{location}[{index}]")
    elif isinstance(expected, float):
        # Allow last-bit libm variation across platforms; preserve the reported precision.
        assert math.isclose(actual, expected, rel_tol=1e-10, abs_tol=1e-18), (location, actual, expected)
    else:
        assert actual == expected, (location, actual, expected)


def pinned_matplotlib():
    requirements = (ROOT / "requirements-validation.txt").read_text()
    return re.search(r"^matplotlib==(\S+)$", requirements, re.MULTILINE).group(1)


def main():
    # The committed SVGs are byte-reproducible under the pinned Matplotlib; other versions may render differently.
    exact = version("matplotlib") == pinned_matplotlib()
    with tempfile.TemporaryDirectory() as temporary:
        destination = Path(temporary)
        for script, label in EXAMPLES:
            output, figure = destination / f"{label}.json", destination / f"{label}.svg"
            subprocess.run([sys.executable, str(ROOT / "assets/examples" / script),
                            "--output", str(output), "--plot", str(figure)],
                           check=True, stdout=subprocess.DEVNULL)
            expected = json.loads((ROOT / f"assets/examples/results/{label}.json").read_text())
            compare(json.loads(output.read_text()), expected)
            generated = ET.parse(figure).getroot()
            assert generated.tag.endswith("svg") and len(generated) > 0
            recorded = (ROOT / f"assets/images/guides/{label}.svg").read_text()
            equal = figure.read_text() == recorded
            assert equal or not exact, f"{label}.svg does not match {script}; regenerate it with --plot"
            print(f"PASS: {script}: reported numbers verified; SVG regenerated "
                  f"({'identical' if equal else 'valid, unpinned Matplotlib renders differently'})", flush=True)


if __name__ == "__main__":
    main()
