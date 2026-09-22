"""Smoke: the installed entry point answers ``--help`` (PS-211).

Subprocess-driven (the ``scitex-plt`` console script resolves to
``figrecipe._cli:main``) so this proves the installed entry point
resolves — an in-process import would not. Hermetic: no network, no
credentials, no writes outside tmp dirs.
"""

from __future__ import annotations

import shutil
import subprocess
import sys

import pytest

pytestmark = pytest.mark.smoke


def test_console_script_answers_help_flag() -> None:
    # Arrange
    binary = shutil.which("scitex-plt") or f"{sys.prefix}/bin/scitex-plt"
    argv = [binary, "--help"]

    # Act
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=30)

    # Assert
    assert (completed.returncode, "Usage:" in completed.stdout) == (0, True)
