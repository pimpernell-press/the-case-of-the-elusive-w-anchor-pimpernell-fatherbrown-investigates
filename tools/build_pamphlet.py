from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from paths import project_paths


@dataclass(frozen=True)
class Targets:
    pdf: bool
    epub: bool
    docx: bool


def must_exist_dir(p: Path, label: str) -> None:
    if not p.exists() or not p.is_dir():
        raise FileNotFoundError(f"Expected {label} directory to exist: {p}")


def must_exist_file(p: Path, label: str) -> None:
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(f"Expected {label} file to exist: {p}")


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def run(cmd: list[str], cwd: Path) -> None:
    print("RUN:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)


def parse_args(argv: list[str]) -> tuple[Path | None, Targets]:
    ap = argparse.ArgumentParser(description="Pamphlet builder (sequential)")
    ap.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Override PROJECT_ROOT (defaults to auto-detected repo root).",
    )

    ap.add_argument("--all", action="store_true", help="Build PDF + EPUB + DOCX (sequential).")
    ap.add_argument("--pdf", action="store_true", help="Build PDF.")
    ap.add_argument("--epub", action="store_true", help="Build EPUB.")
    ap.add_argument("--docx", action="store_true", help="Build DOCX.")

    args = ap.parse_args(argv)

    any_flag = args.all or args.pdf or args.epub or args.docx
    if not any_flag or args.all:
        targets = Targets(pdf=True, epub=True, docx=True)
    else:
        targets = Targets(pdf=args.pdf, epub=args.epub, docx=args.docx)

    return args.project_root, targets


def print_config(pp, src: Path, out_root: Path) -> None:
    lines = [
        "Build config (pamphlet)",
        f"PROJECT_ROOT = {pp.root}",
        f"publication = {pp.publication}",
        f"src = {src}",
        f"out_root = {out_root}",
    ]
    print("\n".join(lines))


def validate_skeleton(pp) -> None:
    must_exist_dir(pp.inputs, "inputs")
    must_exist_dir(pp.outputs, "outputs")
    must_exist_dir(pp.publication, "publication")
    print("OK: path sanity checks passed.")


def pamphlet_source(pp) -> Path:
    # Canonical pamphlet markdown:
    return pp.publication / "pamphlet_issue_1.md"


def build_pdf(pp, src: Path, out_root: Path) -> None:
    out_dir = out_root / "pdf"
    ensure_dir(out_dir)

    must_exist_file(src, "pamphlet markdown")

    out = out_dir / "pamphlet_issue_1.pdf"
    run(
        [
            "pandoc",
            str(src),
            "-o",
            str(out),
            "--pdf-engine=xelatex",
            "-V",
            "papersize=a5",
            "-V",
            "fontsize=11pt",
            "-V",
            "geometry:margin=18mm",
        ],
        cwd=pp.root,
    )
    print(f"Built PDF: {out}")


def build_epub(pp, src: Path, out_root: Path) -> None:
    out_dir = out_root / "epub"
    ensure_dir(out_dir)

    must_exist_file(src, "pamphlet markdown")

    out = out_dir / "pamphlet_issue_1.epub"
    run(
        [
            "pandoc",
            str(src),
            "-o",
            str(out),
            "--toc",
            "--toc-depth=2",
        ],
        cwd=pp.root,
    )
    print(f"Built EPUB: {out}")


def build_docx(pp, src: Path, out_root: Path) -> None:
    out_dir = out_root / "docx"
    ensure_dir(out_dir)

    must_exist_file(src, "pamphlet markdown")

    out = out_dir / "pamphlet_issue_1.docx"
    run(
        [
            "pandoc",
            str(src),
            "-o",
            str(out),
        ],
        cwd=pp.root,
    )
    print(f"Built DOCX: {out}")


def main(argv: list[str]) -> int:
    project_root, targets = parse_args(argv)
    pp = project_paths(project_root)

    src = pamphlet_source(pp)
    out_root = pp.outputs / "pamphlet"

    print_config(pp, src, out_root)
    validate_skeleton(pp)

    if targets.pdf:
        build_pdf(pp, src, out_root)
    if targets.epub:
        build_epub(pp, src, out_root)
    if targets.docx:
        build_docx(pp, src, out_root)

    print("OK: pamphlet build finished (sequential).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
