# tools/paths.py — Programmatic path resolver for build scripts.
# Import this in scripts: from tools.paths import project_paths
#
# This is NOT anchor.py. anchor.py is the session-start verification tool.
# This module resolves paths dynamically at runtime for any script that needs them.
# See anchor.py at repo root for the canonical path registry.

from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add repo root to path for anchor import

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectPaths:
    root: Path
    manuscript_md: Path
    manuscript_docx: Path
    assets: Path
    inputs: Path
    inputs_canonical: Path
    outputs: Path
    publication: Path
    tools: Path
    publish: Path
    templates: Path


def find_project_root(start: Path | None = None) -> Path:
    """
    Resolve repo root by walking up until we find a marker file/dir.

    Does not depend on the current working directory.

    Priority:
    1) Explicit override via env var PROJECT_ROOT (if set)
    2) Unique marker file(s)
    3) Expected repo layout (directories)
    4) Git metadata (.git file/dir) + expected layout guard
    """
    env_root = os.environ.get("PROJECT_ROOT")
    if env_root:
        p = Path(env_root).expanduser().resolve()
        if not p.exists():
            raise RuntimeError(f"PROJECT_ROOT is set but does not exist: {p}")
        return p

    here = (start or Path(__file__)).resolve()
    if here.is_file():
        here = here.parent

    unique_markers: tuple[str, ...] = ("PRINT_AND_BUILD_NOTES.md",)
    common_markers: tuple[str, ...] = ("pyproject.toml", "README.md", ".git")
    expected_dirs: tuple[str, ...] = ("publication", "tools", "publish", "outputs")

    def has_any_marker(p: Path, markers: tuple[str, ...]) -> bool:
        return any((p / m).exists() for m in markers)

    def has_expected_layout(p: Path) -> bool:
        return all((p / d).is_dir() for d in expected_dirs)

    for p in (here, *here.parents):
        # Strongest signal: unique marker file
        if has_any_marker(p, unique_markers):
            return p

        # Next: layout match (good for zip copies)
        if has_expected_layout(p):
            return p

        # Last: git marker, but guard with layout to avoid false positives
        if has_any_marker(p, (".git",)) and has_expected_layout(p):
            return p

        # Optional: allow other common markers if layout matches
        if has_any_marker(p, common_markers) and has_expected_layout(p):
            return p

    raise RuntimeError(
        "Could not find PROJECT_ROOT starting from "
        f"{here}. Expected either {', '.join(unique_markers)} "
        f"or directories {', '.join(expected_dirs)}"
    )


def project_paths(project_root: Path | None = None) -> ProjectPaths:
    root = (project_root or find_project_root()).resolve()
    return ProjectPaths(
        root=root,
        manuscript_md=root / "publication" / "manuscript.md",
        manuscript_docx=root / "outputs" / "docx" / "book.docx",
        assets=root / "assets",
        inputs=root / "inputs",
        inputs_canonical=root / "inputs" / "canonical",
        outputs=root / "outputs",
        publication=root / "publication",
        tools=root / "tools",
        publish=root / "publish",
        templates=root / "templates",
    )
