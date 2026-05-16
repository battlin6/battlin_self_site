from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


BODY_PATTERN = re.compile(r"<body[^>]*>(.*?)</body>", re.IGNORECASE | re.DOTALL)
TITLE_PATTERN = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
TAG_PATTERN = re.compile(r"<[^>]+>")
NUMBER_PATTERN = re.compile(r"\d+")


def numeric_sort_key(file_path: Path) -> tuple[int, str]:
    match = NUMBER_PATTERN.search(file_path.stem)
    if not match:
        return (10**9, file_path.name.lower())
    return (int(match.group()), file_path.name.lower())


def extract_title(content: str, fallback: str) -> str:
    match = TITLE_PATTERN.search(content)
    if not match:
        return fallback
    raw_title = TAG_PATTERN.sub("", match.group(1))
    title = html.unescape(raw_title).strip()
    return title or fallback


def extract_body(content: str) -> str:
    match = BODY_PATTERN.search(content)
    if match:
        return match.group(1).strip()
    return content.strip()


def build_output_html(document_title: str, sections: list[tuple[str, str, str]]) -> str:
    lines: list[str] = []
    lines.append("<!DOCTYPE html>")
    lines.append('<html lang="zh-CN">')
    lines.append("<head>")
    lines.append('  <meta charset="UTF-8">')
    lines.append('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    lines.append(f"  <title>{html.escape(document_title)}</title>")
    lines.append("  <style>")
    lines.append("    body { font-family: sans-serif; max-width: 1100px; margin: 0 auto; padding: 20px; line-height: 1.6; }")
    lines.append("    nav { position: sticky; top: 0; background: #fff; border-bottom: 1px solid #ddd; padding: 10px 0; }")
    lines.append("    nav ul { list-style: none; display: flex; gap: 10px; overflow-x: auto; padding: 0; margin: 0; }")
    lines.append("    nav a { text-decoration: none; color: #0d47a1; white-space: nowrap; }")
    lines.append("    section { margin: 22px 0 38px; }")
    lines.append("  </style>")
    lines.append("</head>")
    lines.append("<body>")
    lines.append(f"  <h1>{html.escape(document_title)}</h1>")
    lines.append("  <nav><ul>")
    for section_id, section_label, _ in sections:
        lines.append(f'    <li><a href="#{html.escape(section_id)}">{html.escape(section_label)}</a></li>')
    lines.append("  </ul></nav>")
    for section_id, section_label, section_body in sections:
        lines.append(f'  <section id="{html.escape(section_id)}">')
        lines.append(f"    <h2>{html.escape(section_label)}</h2>")
        lines.append(section_body)
        lines.append("  </section>")
    lines.append("</body>")
    lines.append("</html>")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Merge paginated HTML files into one valid HTML document."
    )
    parser.add_argument(
        "-i",
        "--input-dir",
        type=Path,
        default=script_dir / "readin",
        help="Directory containing source HTML pages.",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        type=Path,
        default=script_dir / "after_merge.html",
        help="Path for merged HTML output.",
    )
    parser.add_argument(
        "-t",
        "--title",
        default="Combined HTML Archive",
        help="Document title for merged output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = args.input_dir.resolve()
    output_file = args.output_file.resolve()

    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    source_files = sorted(
        [path for path in input_dir.iterdir() if path.is_file() and path.suffix.lower() == ".html"],
        key=numeric_sort_key,
    )

    if not source_files:
        raise FileNotFoundError(f"No HTML files found in: {input_dir}")

    sections: list[tuple[str, str, str]] = []
    for page_number, file_path in enumerate(source_files, start=1):
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        page_title = extract_title(content, file_path.name)
        section_id = f"page-{page_number}"
        section_label = f"{file_path.name} | {page_title}"
        section_body = extract_body(content)
        sections.append((section_id, section_label, section_body))

    output_html = build_output_html(args.title, sections)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(output_html, encoding="utf-8")
    print(f"Merged {len(source_files)} files -> {output_file}")


if __name__ == "__main__":
    main()
