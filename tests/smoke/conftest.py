"""Smoke-test isolation: every subprocess gets a fake home.

`scitex-logging` writes a runtime log under ``$SCITEX_DIR`` — it must land
in a tmp dir, never the developer's real ``~/.scitex``. This package mints
no keys and reads no dotenv-managed secrets, so there is no key variable
to blank here (contrast scitex-genai's gateway key).

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
