import pytest
from pathlib import Path
from file_organizer.organizer import preview_plan, organize_path, DEFAULT_RULES


def test_preview(tmp_path: Path):
    files = ["a.jpg", "b.png", "doc.pdf"]
    for f in files:
        (tmp_path / f).write_text("test")
    plan = preview_plan(tmp_path, DEFAULT_RULES)
    assert len(plan) == len(files)


def test_organize(tmp_path: Path):
    files = ["a.jpg", "b.png"]
    for f in files:
        (tmp_path / f).write_text("test")
    organize_path(tmp_path, DEFAULT_RULES, dry_run=False)
    assert (tmp_path / "Images" / "a.jpg").exists()