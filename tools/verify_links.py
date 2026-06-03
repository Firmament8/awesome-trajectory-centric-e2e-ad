import csv
import datetime as dt
import ssl
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS_PATH = ROOT / "papers" / "papers.tsv"
REPORT_PATH = ROOT / "papers" / "link_check.tsv"


def check_url(url: str) -> tuple[int | str, str]:
    context = ssl.create_default_context()
    headers = {
        "User-Agent": "Mozilla/5.0 literature-link-checker",
    }
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=20, context=context) as response:
                return response.status, response.geturl()
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in {403, 405, 429}:
                continue
            return exc.code, exc.geturl()
        except Exception as exc:  # noqa: BLE001 - report external link failures.
            if method == "HEAD":
                continue
            return "ERROR", str(exc)
    return "ERROR", "unreachable"


def main() -> None:
    checked_at = dt.datetime.now(dt.UTC).isoformat(timespec="seconds")
    rows = []
    with PAPERS_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for paper in reader:
            if paper["link_source"] not in {"doi", "arxiv", "url"}:
                continue
            status, final_url = check_url(paper["paper_url"])
            rows.append(
                {
                    "checked_at": checked_at,
                    "key": paper["key"],
                    "link_source": paper["link_source"],
                    "paper_url": paper["paper_url"],
                    "status": status,
                    "final_url": final_url,
                }
            )

    with REPORT_PATH.open("w", encoding="utf-8", newline="") as f:
        fieldnames = ["checked_at", "key", "link_source", "paper_url", "status", "final_url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    ok = sum(1 for row in rows if str(row["status"]).startswith(("2", "3")))
    print(f"Checked {len(rows)} direct links: {ok} OK, {len(rows) - ok} need review")


if __name__ == "__main__":
    main()
