from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from .organizer import organize_path, preview_plan, DEFAULT_RULES
from .config import load_rules_from_path

app = typer.Typer(help="File Organizer CLI")
console = Console()
logger = logging.getLogger("file_organizer")


@app.command()
def preview(
    src: Path = typer.Argument(..., exists=True, file_okay=False, help="Source directory"),
    rules: Optional[Path] = typer.Option(None, "--rules", "-r", help="JSON or YAML rules file"),
):
    """Preview planned moves."""
    rule_map = load_rules_from_path(rules) if rules else DEFAULT_RULES
    plan = preview_plan(src, rule_map)
    if not plan:
        console.print("No files matched rules.")
        raise typer.Exit(0)
    table = Table("Source", "Destination")
    for op in plan:
        table.add_row(op["src"], op["dest"])
    console.print(table)


@app.command()
def organize(
    src: Path = typer.Argument(..., exists=True, file_okay=False, help="Source directory"),
    rules: Optional[Path] = typer.Option(None, "--rules", "-r", help="JSON or YAML rules file"),
    dry_run: bool = typer.Option(True, "--dry-run/--no-dry-run", help="Dry-run by default"),
    conflict: str = typer.Option("suffix", "--conflict", help="Conflict strategy: suffix|overwrite|skip"),
    dedupe: bool = typer.Option(False, "--dedupe/--no-dedupe", help="Skip duplicates by hash"),
):
    """Organize files."""
    rule_map = load_rules_from_path(rules) if rules else DEFAULT_RULES
    moved = organize_path(src, rule_map, dry_run=dry_run, conflict_strategy=conflict, dedupe=dedupe)
    console.print(f"[green]Done.[/green] Files moved: {moved}")