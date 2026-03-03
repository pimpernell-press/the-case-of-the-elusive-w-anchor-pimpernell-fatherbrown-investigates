from __future__ import annotations

import argparse
import re
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


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)   # drop punctuation
    s = re.sub(r"[\s_-]+", "-", s)   # collapse whitespace/underscores
    s = s.strip("-")
    return s or "book"


def read_title_from_meta(meta_path: Path) -> str | None:
    """
    Minimal parser for a metadata file that contains a line like:
      title: My Great Book
    Works for simple YAML-ish or plain markdown containing that line.
    """
    must_exist_file(meta_path, "metadata")

    for line in meta_path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^\s*title\s*:\s*(.+?)\s*$", line, flags=re.IGNORECASE)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def compute_out_stem(src: Path, meta: Path | None, out_stem: str | None) -> str:
    if out_stem:
        return slugify(out_stem)

    if meta:
        title = read_title_from_meta(meta)
        if title:
            return slugify(title)

    return slugify(src.stem)


def parse_args(argv: list[str]) -> tuple[Path | None, Targets, Path | None, Path | None, str | None]:
    ap = argparse.ArgumentParser(description="Reproducible Self-Pub Kit builder (sequential)")
    ap.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Override PROJECT_ROOT (defaults to auto-detected repo root).",
    )

    ap.add_argument(
        "--src",
        type=Path,
        default=None,
        help="Path to manuscript markdown (default: publication/manuscript.md).",
    )
    ap.add_argument(
        "--meta",
        type=Path,
        default=None,
        help="Optional metadata file with e.g. a 'title: ...' line (used for output naming).",
    )
    ap.add_argument(
        "--out-stem",
        type=str,
        default=None,
        help="Optional override for output filename stem (e.g. 'my-book-v2').",
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

    return args.project_root, targets, args.src, args.meta, args.out_stem


def print_config(pp, src: Path, meta: Path | None, out_stem: str) -> None:
    lines = [
        "Build config",
        f"PROJECT_ROOT = {pp.root}",
        f"inputs_canonical = {pp.inputs_canonical}",
        f"manuscript_md = {pp.manuscript_md}",
        f"manuscript_docx = {pp.manuscript_docx}",
        f"assets = {pp.assets}",
        f"outputs = {pp.outputs}",
        f"publication = {pp.publication}",
        f"src = {src}",
        f"meta = {meta}" if meta else "meta = (none)",
        f"out_stem = {out_stem}",
    ]
    print("\n".join(lines))


def validate_skeleton(pp) -> None:
    must_exist_dir(pp.inputs, "inputs")
    must_exist_dir(pp.outputs, "outputs")
    must_exist_dir(pp.publication, "publication")
    print("OK: path sanity checks passed.")


def manuscript_source(pp, src_arg: Path | None) -> Path:
    # Default location. Override with --src.
    return src_arg if src_arg is not None else (pp.publication / "manuscript.md")


def build_pdf(pp, src: Path, out_stem: str) -> None:
    out_dir = pp.outputs / "pdf"
    ensure_dir(out_dir)

    must_exist_file(src, "manuscript markdown")

    out = out_dir / f"{out_stem}.pdf"
    run(["pandoc", str(src), "-o", str(out), "--pdf-engine=xelatex"], cwd=pp.root)
    print(f"Built PDF: {out}")


def build_epub(pp, src: Path, out_stem: str) -> None:
    out_dir = pp.outputs / "epub"
    ensure_dir(out_dir)

    must_exist_file(src, "manuscript markdown")

    out = out_dir / f"{out_stem}.epub"
    run(["pandoc", str(src), "-o", str(out)], cwd=pp.root)
    print(f"Built EPUB: {out}")


def build_docx(pp, src: Path, out_stem: str) -> None:
    out_dir = pp.outputs / "docx"
    ensure_dir(out_dir)

    must_exist_file(src, "manuscript markdown")

    out = out_dir / f"{out_stem}.docx"
    run(["pandoc", str(src), "-o", str(out)], cwd=pp.root)
    print(f"Built DOCX: {out}")


def main(argv: list[str]) -> int:
    project_root, targets, src_arg, meta_arg, out_stem_arg = parse_args(argv)
    pp = project_paths(project_root)

    src = manuscript_source(pp, src_arg)
    out_stem = compute_out_stem(src=src, meta=meta_arg, out_stem=out_stem_arg)

    print_config(pp, src=src, meta=meta_arg, out_stem=out_stem)
    validate_skeleton(pp)

    if targets.pdf:
        build_pdf(pp, src, out_stem)
    if targets.epub:
        build_epub(pp, src, out_stem)
    if targets.docx:
        build_docx(pp, src, out_stem)

    print("OK: build finished (sequential).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
