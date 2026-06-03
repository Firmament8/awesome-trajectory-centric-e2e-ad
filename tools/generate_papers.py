import csv
import re
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / "bibliography" / "references.bib"
PAPERS_PATH = ROOT / "papers" / "papers.tsv"
README_LIST_PATH = ROOT / "papers" / "paper_list.md"


CATEGORIES = [
    (
        "Surveys and Positioning",
        [
            "survey",
            "overview",
            "milestones",
            "frontiers",
            "review",
            "comprehensive",
        ],
    ),
    (
        "VLM, VLA, Language, and Reasoning",
        [
            "vision-language",
            "vision language",
            "vision-language-action",
            "language-action",
            "vla",
            "language",
            "llm",
            "gpt",
            "reason",
            "drivegpt",
            "drivelm",
            "vqa",
            "cognitive",
            "simlingo",
        ],
    ),
    (
        "World Models, Rollout, and Generative Simulation",
        [
            "world model",
            "world models",
            "rollout",
            "autoregressive",
            "generative",
            "jepa",
            "dream",
            "drivedreamer",
            "drivinggpt",
            "epona",
            "latent",
        ],
    ),
    (
        "Planning-Oriented Evaluation and Benchmarks",
        [
            "navsim",
            "nuplan",
            "argoverse",
            "benchmark",
            "dataset",
            "waymo",
            "womd",
            "bdd100k",
            "dair",
            "waymax",
            "scenario",
            "simulation",
            "simulator",
            "drivearena",
            "maplm",
            "lampilot",
            "omnidrive",
        ],
    ),
    (
        "BEV, Occupancy, and Perception",
        [
            "bev",
            "bird",
            "occupancy",
            "occ",
            "3d object",
            "perception",
            "fusion",
            "lidar",
            "camera",
            "segmentation",
            "tracking",
            "voxel",
            "grid",
        ],
    ),
    (
        "Trajectory Prediction and End-to-End Planning",
        [
            "trajectory",
            "planning",
            "planner",
            "motion",
            "forecast",
            "end-to-end",
            "control",
            "diffusion",
            "distill",
            "hydra",
            "goalflow",
            "resad",
        ],
    ),
    (
        "Background: Intelligent Transportation and Autonomous Driving",
        [
            "traffic",
            "transportation",
            "mixed-autonomy",
            "vehicle",
            "intelligent vehicles",
        ],
    ),
]


def strip_latex(value: str) -> str:
    value = value.replace("{\\ss}", "ss")
    value = value.replace("{\\'\\i}", "i")
    value = value.replace("\\'e", "e")
    value = value.replace("{\\\"e}", "e")
    value = value.replace('\\"o', "o")
    value = value.replace("{\\\"o}", "o")
    value = value.replace("{\\u g}", "g")
    value = value.replace("\\u g", "g")
    value = re.sub(r"\\[a-zA-Z]+", "", value)
    value = value.replace("{", "").replace("}", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def split_entries(text: str) -> list[dict[str, str]]:
    starts = [m.start() for m in re.finditer(r"@\w+\s*\{", text)]
    entries = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(text)
        raw = text[start:end].strip()
        header = re.match(r"@(?P<type>\w+)\s*\{\s*(?P<key>[^,]+),", raw)
        if not header:
            continue
        fields = {"entry_type": header.group("type"), "key": header.group("key").strip()}
        body = raw[header.end() :]
        for field_match in re.finditer(r"(?m)^\s*([A-Za-z][A-Za-z0-9_-]*)\s*=", body):
            name = field_match.group(1).lower()
            value_start = body.find("{", field_match.end())
            if value_start == -1:
                continue
            depth = 0
            value_end = None
            for pos in range(value_start, len(body)):
                char = body[pos]
                if char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                    if depth == 0:
                        value_end = pos
                        break
            if value_end is None:
                continue
            fields[name] = strip_latex(body[value_start + 1 : value_end])
        entries.append(fields)
    return entries


def arxiv_from_note(note: str) -> str:
    match = re.search(r"arXiv\s*:\s*([0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?)", note, flags=re.I)
    return match.group(1) if match else ""


def paper_link(entry: dict[str, str]) -> tuple[str, str]:
    doi = entry.get("doi", "").strip()
    if doi:
        return f"https://doi.org/{doi}", "doi"
    arxiv = arxiv_from_note(entry.get("note", ""))
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv}", "arxiv"
    url = entry.get("url", "").strip()
    if url:
        return url, "url"
    return "", "needs_direct_link"


def search_link(title: str) -> str:
    return f"https://scholar.google.com/scholar?q={urllib.parse.quote_plus(title)}"


def venue(entry: dict[str, str]) -> str:
    return entry.get("journal") or entry.get("booktitle") or entry.get("entry_type", "")


def first_author(entry: dict[str, str]) -> str:
    authors = entry.get("author", "")
    first = authors.split(" and ")[0].strip()
    return first or "Unknown"


def assign_category(entry: dict[str, str]) -> str:
    text = " ".join(
        [
            entry.get("key", ""),
            entry.get("title", ""),
            venue(entry),
            entry.get("note", ""),
        ]
    ).lower()
    for category, keywords in CATEGORIES:
        if any(keyword in text for keyword in keywords):
            return category
    return "Other Relevant Papers"


def format_item(entry: dict[str, str]) -> str:
    title = entry.get("title", "Untitled")
    year = entry.get("year", "n.d.")
    authors = first_author(entry)
    where = venue(entry)
    link, link_type = paper_link(entry)
    source = {
        "doi": "DOI",
        "arxiv": "arXiv",
        "url": "URL",
    }.get(link_type)
    if source:
        link_text = f" [[{source}]]({link})"
    else:
        link_text = f" [search only]({search_link(title)})"
    return f"- **{title}**. {authors} et al., {where}, {year}.{link_text} `bib:{entry['key']}`"


def main() -> None:
    entries = split_entries(BIB_PATH.read_text(encoding="utf-8"))
    rows = []
    for entry in entries:
        link, link_type = paper_link(entry)
        rows.append(
            {
                "key": entry["key"],
                "category": assign_category(entry),
                "title": entry.get("title", ""),
                "authors": entry.get("author", ""),
                "year": entry.get("year", ""),
                "venue": venue(entry),
                "paper_url": link,
                "search_url": search_link(entry.get("title", "")),
                "link_source": link_type,
                "doi": entry.get("doi", ""),
                "note": entry.get("note", ""),
            }
        )

    with PAPERS_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    grouped: dict[str, list[dict[str, str]]] = {}
    for entry in entries:
        grouped.setdefault(assign_category(entry), []).append(entry)

    lines = [
        "# Paper List",
        "",
        "Generated from `bibliography/references.bib`. DOI, arXiv, and URL links are derived only from explicit BibTeX fields. Entries marked `search only` do not yet have a verified direct paper/project/code link in this repository.",
        "",
    ]
    for category, _ in CATEGORIES + [("Other Relevant Papers", [])]:
        items = grouped.get(category, [])
        if not items:
            continue
        lines.append(f"## {category}")
        lines.append("")
        for entry in sorted(items, key=lambda e: (e.get("year", ""), e.get("title", "")), reverse=True):
            lines.append(format_item(entry))
        lines.append("")

    README_LIST_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {len(rows)} papers")


if __name__ == "__main__":
    main()
