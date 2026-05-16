from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import quote


DATA_TITLE_PATTERN = re.compile(r'data-title="(.*?)"', re.IGNORECASE | re.DOTALL)
DESCRIPTION_PATTERN = re.compile(r'<meta\s+name="description"\s+content="(.*?)"', re.IGNORECASE | re.DOTALL)
TITLE_PATTERN = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
DATETIME_PATTERN = re.compile(r'datetime="([^"]+)"', re.IGNORECASE)
TAG_PATTERN = re.compile(r"<[^>]+>")


@dataclass
class TopicPage:
    folder_name: str
    href: str
    title: str
    description: str
    first_post_time: str
    mtime: float


def clean_text(value: str) -> str:
    text = TAG_PATTERN.sub("", value)
    return html.unescape(text).replace("\n", " ").strip()


def first_match(pattern: re.Pattern[str], content: str) -> str:
    match = pattern.search(content)
    if not match:
        return ""
    return clean_text(match.group(1))


def encode_href(path: Path) -> str:
    return "/".join(quote(part) for part in path.parts)


def parse_topic_page(root_dir: Path, topic_dir: Path) -> TopicPage | None:
    index_file = topic_dir / "index.html"
    if not index_file.exists():
        return None

    content = index_file.read_text(encoding="utf-8", errors="ignore")
    data_title = first_match(DATA_TITLE_PATTERN, content)
    html_title = first_match(TITLE_PATTERN, content)
    html_title = html_title.split("|")[0].strip() if html_title else ""
    title = data_title or html_title or topic_dir.name

    description = first_match(DESCRIPTION_PATTERN, content)
    if not description:
        description = "No summary available."
    description = re.sub(r"\s+", " ", description).strip()
    if len(description) > 180:
        description = description[:177] + "..."

    first_post_time = first_match(DATETIME_PATTERN, content)

    href = encode_href(Path(root_dir.name) / topic_dir.name / "index.html")
    return TopicPage(
        folder_name=topic_dir.name,
        href=href,
        title=title,
        description=description,
        first_post_time=first_post_time,
        mtime=index_file.stat().st_mtime,
    )


def sort_topics(topics: list[TopicPage], sort_by: str) -> list[TopicPage]:
    if sort_by == "mtime":
        return sorted(topics, key=lambda item: item.mtime, reverse=True)
    if sort_by == "date":
        def date_key(item: TopicPage) -> datetime:
            value = item.first_post_time.replace(" UTC", "")
            try:
                return datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
            except ValueError:
                return datetime.min

        return sorted(topics, key=date_key, reverse=True)
    return sorted(topics, key=lambda item: item.folder_name.casefold())


def render_index(topics: list[TopicPage], page_title: str) -> str:
    cards = []
    for topic in topics:
        time_line = topic.first_post_time or "unknown time"
        cards.append(
            "\n".join(
                [
                    f'<li class="topic-card" data-search="{html.escape((topic.folder_name + " " + topic.title + " " + topic.description).lower())}">',
                    f'  <a class="topic-link" href="{html.escape(topic.href)}">',
                    f'    <h2>{html.escape(topic.title)}</h2>',
                    f'    <p class="topic-desc">{html.escape(topic.description)}</p>',
                    f'    <p class="topic-meta">Folder: {html.escape(topic.folder_name)} | First post: {html.escape(time_line)}</p>',
                    "  </a>",
                    "</li>",
                ]
            )
        )

    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{
      --bg: #f4efe6;
      --ink: #1d2a3a;
      --paper: #fffdf8;
      --line: #d8cfc2;
      --accent: #0f5c7a;
      --accent-soft: #c7e4ee;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Georgia, "Times New Roman", serif; color: var(--ink); background: radial-gradient(circle at 20% 20%, #f8f4ec, #efe6d8 55%, #e6dccd); }}
    main {{ max-width: 980px; margin: 24px auto 48px; padding: 0 16px; }}
    .hero {{ background: linear-gradient(135deg, var(--paper), #f9f3e7); border: 1px solid var(--line); border-radius: 16px; padding: 20px; box-shadow: 0 14px 30px rgba(43, 33, 18, 0.08); }}
    h1 {{ margin: 0 0 10px; font-size: clamp(1.6rem, 2.2vw, 2.3rem); letter-spacing: 0.02em; }}
    .sub {{ margin: 0; color: #42556b; }}
    .search-wrap {{ margin-top: 16px; }}
    input[type="search"] {{ width: 100%; padding: 12px 14px; border: 1px solid var(--line); border-radius: 10px; font-size: 1rem; background: #fff; }}
    ul {{ list-style: none; padding: 0; margin: 18px 0 0; display: grid; gap: 14px; }}
    .topic-card {{ border: 1px solid var(--line); border-radius: 14px; background: #fffefb; overflow: hidden; transition: transform 120ms ease, box-shadow 120ms ease; }}
    .topic-card:hover {{ transform: translateY(-2px); box-shadow: 0 8px 20px rgba(30, 45, 70, 0.12); }}
    .topic-link {{ display: block; color: inherit; text-decoration: none; padding: 16px; }}
    .topic-link h2 {{ margin: 0 0 8px; font-size: 1.1rem; color: var(--accent); }}
    .topic-desc {{ margin: 0 0 8px; line-height: 1.45; }}
    .topic-meta {{ margin: 0; font-size: 0.9rem; color: #5a6475; }}
    .empty {{ display: none; margin-top: 16px; color: #5a6475; }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <h1>{title}</h1>
      <p class="sub">Archived topic index with summaries.</p>
      <div class="search-wrap">
        <input id="search" type="search" placeholder="Search by title, folder, or text..." aria-label="Search topics">
      </div>
      <ul id="topic-list">
        {cards}
      </ul>
      <p id="empty" class="empty">No matching topics.</p>
    </section>
  </main>
  <script>
    const searchInput = document.getElementById('search');
    const cards = Array.from(document.querySelectorAll('.topic-card'));
    const empty = document.getElementById('empty');

    function applyFilter() {{
      const key = searchInput.value.trim().toLowerCase();
      let visible = 0;
      cards.forEach((card) => {{
        const haystack = card.dataset.search || '';
        const show = !key || haystack.includes(key);
        card.style.display = show ? '' : 'none';
        if (show) visible += 1;
      }});
      empty.style.display = visible ? 'none' : 'block';
    }}

    searchInput.addEventListener('input', applyFilter);
  </script>
</body>
</html>
""".format(title=html.escape(page_title), cards="\n".join(cards))


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    parser = argparse.ArgumentParser(description="Generate root index page for archived topics.")
    parser.add_argument(
        "-r",
        "--root-dir",
        type=Path,
        default=project_root / "html_list",
        help="Root directory containing topic folders.",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        type=Path,
        default=project_root / "index.html",
        help="Output HTML file path.",
    )
    parser.add_argument(
        "-s",
        "--sort-by",
        choices=["name", "mtime", "date"],
        default="name",
        help="Sort topics by folder name, modified time, or first post date.",
    )
    parser.add_argument(
        "--title",
        default="Page Links",
        help="Page title shown on the generated index.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root_dir = args.root_dir.resolve()
    output_file = args.output_file.resolve()

    if not root_dir.exists() or not root_dir.is_dir():
        raise FileNotFoundError(f"Root directory not found: {root_dir}")

    topics: list[TopicPage] = []
    for entry in root_dir.iterdir():
        if entry.is_dir():
            parsed = parse_topic_page(root_dir, entry)
            if parsed:
                topics.append(parsed)

    ordered_topics = sort_topics(topics, args.sort_by)
    html_content = render_index(ordered_topics, args.title)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(html_content, encoding="utf-8")
    print(f"Generated {output_file} with {len(ordered_topics)} topics.")


if __name__ == "__main__":
    main()
