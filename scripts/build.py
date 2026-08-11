#!/usr/bin/env python3
"""Generate apps.json and README.md from apps/<id>.json.

Both outputs are build artifacts. Never hand-edit them.

  python3 scripts/build.py           write the artifacts
  python3 scripts/build.py --check   fail if the artifacts are stale (used by CI)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPS_DIR = ROOT / "apps"
TEMPLATE = ROOT / "templates" / "README.template.md"
OUT_JSON = ROOT / "apps.json"
OUT_README = ROOT / "README.md"

CATEGORY_TITLES = {
    "data-visualization": "Data Visualization",
    "dashboards": "Dashboards",
    "3d-graphics": "3D and Graphics",
    "maps-geo": "Maps and Geo",
    "forms-workflows": "Forms and Workflows",
    "media": "Media",
    "developer-tools": "Developer Tools",
    "productivity": "Productivity",
    "finance": "Finance",
    "science": "Science",
    "games": "Games",
    "other": "Other",
}

STATUS_BADGE = {
    "probed": "✅",
    "source-inspected": "🔍",
    "claimed": "📋",
}


def load_entries() -> list[dict]:
    if not APPS_DIR.exists():
        return []
    entries = [json.loads(p.read_text()) for p in sorted(APPS_DIR.glob("*.json"))]
    return sorted(entries, key=lambda e: (e.get("category", "other"), e["id"]))


def render_media_links(entry: dict) -> str:
    media = entry.get("media", {})
    bits = []
    if media.get("demo_video"):
        bits.append(f"[video]({media['demo_video']})")
    if media.get("gif"):
        bits.append(f"[gif]({media['gif']})")
    elif media.get("screenshot"):
        bits.append(f"[shot]({media['screenshot']})")
    return " ".join(bits)


def render_table(entries: list[dict]) -> str:
    if not entries:
        return ("_No entries yet. The list opens with hand verified apps, so it starts "
                "small on purpose._\n")

    out: list[str] = []
    by_cat: dict[str, list[dict]] = {}
    for e in entries:
        by_cat.setdefault(e.get("category", "other"), []).append(e)

    for cat in CATEGORY_TITLES:
        rows = by_cat.get(cat)
        if not rows:
            continue
        out.append(f"### {CATEGORY_TITLES[cat]}\n")
        out.append("| App | What it does | Checked | Media |")
        out.append("| --- | --- | :---: | --- |")
        for e in rows:
            v = e.get("verification", {})
            badge = STATUS_BADGE.get(v.get("status", "claimed"), "📋")
            checked = f'{badge}<br><sub>{v.get("last_checked", "")}</sub>'
            name = f'[{e["name"]}]({e["repo_url"]})'
            out.append(f'| {name} | {e["description"]} | {checked} | {render_media_links(e)} |')
        out.append("")
    return "\n".join(out)


def render_counts(entries: list[dict]) -> str:
    if not entries:
        return "none yet"
    tally: dict[str, int] = {}
    for e in entries:
        s = e.get("verification", {}).get("status", "claimed")
        tally[s] = tally.get(s, 0) + 1
    parts = [f'{STATUS_BADGE[s]} {tally[s]} {s}' for s in ("probed", "source-inspected", "claimed")
             if s in tally]
    return ", ".join(parts)


def build() -> tuple[str, str]:
    entries = load_entries()
    apps_json = json.dumps(entries, indent=2, ensure_ascii=False) + "\n"

    if not TEMPLATE.exists():
        sys.exit(f"template not found: {TEMPLATE}")
    readme = (TEMPLATE.read_text()
              .replace("{{APPS_TABLE}}", render_table(entries))
              .replace("{{COUNT}}", str(len(entries)))
              .replace("{{VERIFICATION_COUNTS}}", render_counts(entries)))
    return apps_json, readme


def main() -> int:
    apps_json, readme = build()
    check = "--check" in sys.argv

    if check:
        stale = []
        for path, wanted in ((OUT_JSON, apps_json), (OUT_README, readme)):
            current = path.read_text() if path.exists() else None
            if current != wanted:
                stale.append(path.relative_to(ROOT).as_posix())
        if stale:
            print("stale generated files: " + ", ".join(stale))
            print("run: python3 scripts/build.py")
            return 1
        print("generated files are up to date")
        return 0

    OUT_JSON.write_text(apps_json)
    OUT_README.write_text(readme)
    n = len(json.loads(apps_json))
    print(f"wrote apps.json and README.md ({n} entr{'y' if n == 1 else 'ies'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
