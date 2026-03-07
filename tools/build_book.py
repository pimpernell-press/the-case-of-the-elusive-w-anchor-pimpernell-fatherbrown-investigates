import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add repo root to path for anchor import
from __future__ import annotations

import argparse
import re
import shlex
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
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


def require_tool(exe: str) -> None:
    if shutil.which(exe) is None:
        raise RuntimeError(f"Required tool not found on PATH: {exe}")


def run(cmd: list[str], cwd: Path) -> None:
    print(f"RUN (cwd={cwd}):", shlex.join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)  # drop punctuation
    s = re.sub(r"[\s_-]+", "-", s)  # collapse whitespace/underscores
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


def compute_base_title(src: Path, meta: Path | None) -> str:
    if meta:
        title = read_title_from_meta(meta)
        if title:
            return title
    return src.stem


def compute_display_title(base_title: str, label: str | None) -> str:
    label = (label or "").strip()
    return f"{base_title}  {label}" if label else base_title


def compute_out_stem_with_label_and_date(
    *,
    src: Path,
    meta: Path | None,
    out_stem_arg: str | None,
    label: str | None,
    date_stamp: bool,
) -> str:
    base_title = compute_base_title(src=src, meta=meta)
    base_stem = slugify(out_stem_arg) if out_stem_arg else slugify(base_title)
    label_stem = slugify(label) if (label and label.strip()) else ""
    parts = [p for p in [base_stem, label_stem] if p]
    if date_stamp:
        parts.append(date.today().isoformat())
    return "__".join(parts) if parts else "book"


def parse_args(argv: list[str]) -> tuple[Path | None, Targets, Path | None, Path | None, str | None, str | None, bool]:
    ap = argparse.ArgumentParser(description="Reproducible Self-Pub Kit builder (sequential)")
    ap.add_argument("--project-root", type=Path, default=None)
    ap.add_argument("--src", type=Path, default=None, help="Default: publication/manuscript.md")
    ap.add_argument("--meta", type=Path, default=None, help="Pandoc --metadata-file (also used for title naming)")
    ap.add_argument("--out-stem", type=str, default=None, help="Override output filename stem")

    ap.add_argument("--label", type=str, default=None, help="Append to title + output stem (e.g. 'Draft Manuscript')")
    ap.add_argument("--date-stamp", action="store_true", help="Append YYYY-MM-DD to output stem")

    ap.add_argument("--all", action="store_true")
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--epub", action="store_true")
    ap.add_argument("--docx", action="store_true")

    args = ap.parse_args(argv)

    any_flag = args.all or args.pdf or args.epub or args.docx
    if not any_flag or args.all:
        targets = Targets(pdf=True, epub=True, docx=True)
    else:
        targets = Targets(pdf=args.pdf, epub=args.epub, docx=args.docx)

    return args.project_root, targets, args.src, args.meta, args.out_stem, args.label, args.date_stamp


def resolve_under_root(root: Path, p: Path | None) -> Path | None:
    if p is None:
        return None
    return (root / p).resolve() if not p.is_absolute() else p.resolve()


def print_config(pp, src: Path, meta: Path | None, out_stem: str, display_title: str) -> None:
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
        f"display_title = {display_title}",
    ]
    print("\n".join(lines))


def validate_skeleton(pp) -> None:
    must_exist_dir(pp.inputs, "inputs")
    ensure_dir(pp.outputs)
    must_exist_dir(pp.publication, "publication")
    print("OK: path sanity checks passed.")


def manuscript_source(pp, src_arg: Path | None) -> Path:
    return src_arg if src_arg is not None else pp.manuscript_md


def pandoc_base_cmd(src: Path, out: Path, meta: Path | None, display_title: str | None) -> list[str]:
    cmd = ["pandoc", str(src), "-o", str(out)]
    if meta is not None:
        must_exist_file(meta, "metadata")
        cmd.extend(["--metadata-file", str(meta)])
    if display_title:
        cmd.extend(["--metadata", f"title={display_title}"])
    return cmd


def build_pdf(pp, src: Path, out_stem: str, meta: Path | None, display_title: str) -> None:
    out_dir = pp.outputs / "pdf"
    ensure_dir(out_dir)
    must_exist_file(src, "manuscript markdown")

    out = out_dir / f"{out_stem}.pdf"
    cmd = pandoc_base_cmd(src=src, out=out, meta=meta, display_title=display_title)
    cmd.extend(["--pdf-engine=xelatex"])
    run(cmd, cwd=pp.root)
    print(f"Built PDF: {out}")


def build_epub(pp, src: Path, out_stem: str, meta: Path | None, display_title: str) -> None:
    out_dir = pp.outputs / "epub"
    ensure_dir(out_dir)
    must_exist_file(src, "manuscript markdown")

    out = out_dir / f"{out_stem}.epub"
    cmd = pandoc_base_cmd(src=src, out=out, meta=meta, display_title=display_title)
    run(cmd, cwd=pp.root)
    print(f"Built EPUB: {out}")


def build_docx(pp, src: Path, out_stem: str, meta: Path | None, display_title: str) -> None:
    out_dir = pp.outputs / "docx"
    ensure_dir(out_dir)
    must_exist_file(src, "manuscript markdown")

    out = out_dir / f"{out_stem}.docx"
    cmd = pandoc_base_cmd(src=src, out=out, meta=meta, display_title=display_title)
    run(cmd, cwd=pp.root)
    print(f"Built DOCX: {out}")


def main(argv: list[str]) -> int:
    project_root, targets, src_arg, meta_arg, out_stem_arg, label, date_stamp = parse_args(argv)
    pp = project_paths(project_root)

    require_tool("pandoc")
    if targets.pdf:
        require_tool("xelatex")

    src = manuscript_source(pp, src_arg)
    src = resolve_under_root(pp.root, src)
    assert src is not None

    meta_arg = resolve_under_root(pp.root, meta_arg)

    base_title = compute_base_title(src=src, meta=meta_arg)
    display_title = compute_display_title(base_title=base_title, label=label)

    out_stem = compute_out_stem_with_label_and_date(
        src=src, meta=meta_arg, out_stem_arg=out_stem_arg, label=label, date_stamp=date_stamp
    )

    print_config(pp, src=src, meta=meta_arg, out_stem=out_stem, display_title=display_title)
    validate_skeleton(pp)

    if targets.pdf:
        build_pdf(pp, src, out_stem, meta_arg, display_title)
    if targets.epub:
        build_epub(pp, src, out_stem, meta_arg, display_title)
    if targets.docx:
        build_docx(pp, src, out_stem, meta_arg, display_title)

    print("OK: build finished (sequential).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

