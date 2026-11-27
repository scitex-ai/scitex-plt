"""Regression test: importing tests/conftest.py must not touch site-packages."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

CONFTEST = Path(__file__).resolve().parents[1] / "conftest.py"

_CHILD_CODE = """\
import os
import runpy
import site

# Arrange
os.environ["COVERAGE_PROCESS_START"] = "sentinel-start"
os.environ["COVERAGE_FILE"] = "sentinel-file"
dirs = []
for d in (site.getsitepackages() + [site.getusersitepackages()]):
    dirs.append(d)
before = {d: sorted(os.listdir(d)) if os.path.isdir(d) else None for d in dirs}

# Act
runpy.run_path(%r, run_name="conftest_under_test")

# Assert
after = {d: sorted(os.listdir(d)) if os.path.isdir(d) else None for d in dirs}
assert before == after, "conftest modified site-packages"
assert os.environ.get("COVERAGE_PROCESS_START") == "sentinel-start"
assert os.environ.get("COVERAGE_FILE") == "sentinel-file"
""" % str(CONFTEST)


def test_conftest_leaves_site_packages_untouched():
    # Arrange
    cmd = [sys.executable, "-c", _CHILD_CODE]
    # Act
    proc = subprocess.run(cmd, capture_output=True, text=True)
    # Assert
    assert proc.returncode == 0, proc.stderr
