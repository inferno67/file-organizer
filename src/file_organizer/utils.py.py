from __future__ import annotations

from pathlib import Path


def load_rules_from_json(path: Path) -> dict:
    return __import__("json").load(path.open("r"))