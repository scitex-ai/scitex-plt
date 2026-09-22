"""E2E: compose a figure and save it with data sidecars (PS-212).

The full story — ``subplots()`` builds a real figure, ``ax.plot``
draws onto it, and ``save()`` persists the PNG next to its CSV sidecar
in a tmp dir. Real rendering (Agg), real filesystem, no network.
Gated on ``RUN_E2E=1`` (skipped by default).
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = [
    pytest.mark.e2e,
    pytest.mark.skipif(
        os.environ.get("RUN_E2E") != "1",
        reason="e2e: set RUN_E2E=1 to run end-to-end workflows",
    ),
]

_PROBE = (
    "import matplotlib\n"
    "matplotlib.use('Agg')\n"
    "import os, sys\n"
    "import scitex_plt as plt\n"
    "out = os.path.join(sys.argv[1], 'figure.png')\n"
    "fig, ax = plt.subplots()\n"
    "ax.plot([1, 2, 3], [1, 4, 9])\n"
    "plt.save(fig, out)\n"
    "print(os.path.isfile(out))\n"
    "print(os.path.getsize(out) > 0)\n"
)


def test_compose_and_save_figure_with_sidecars(tmp_path: Path) -> None:
    # Arrange
    probe = tmp_path / "probe_e2e.py"
    probe.write_text(_PROBE)
    argv = [sys.executable, str(probe), str(tmp_path)]

    # Act
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=120)

    # Assert
    assert (completed.returncode, completed.stdout.split()) == (0, ["True", "True"])
