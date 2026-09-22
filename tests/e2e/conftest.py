"""E2E isolation: fake home only, plus the RUN_E2E execution gate.

Per PS-212, end-to-end workflows run only with ``RUN_E2E=1`` (skipped by
default) so a plain ``pytest`` stays fast. Isolation mirrors
``tests/smoke/conftest.py``: ``$SCITEX_DIR`` points at a tmp dir.

No monkeypatch (PA-306): explicit save/restore with try/finally.
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def _isolated_scitex_home(tmp_path: Path) -> Iterator[None]:
    previous = os.environ.get("SCITEX_DIR")
    os.environ["SCITEX_DIR"] = str(tmp_path / "scitex-home")
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop("SCITEX_DIR", None)
        else:
            os.environ["SCITEX_DIR"] = previous
