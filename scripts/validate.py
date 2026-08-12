#!/usr/bin/env python3
"""Validate every apps/<id>.json against schema/app.schema.json.

Beyond the schema, this enforces the repo rules that a schema cannot express:
filename/id agreement, duplicate detection, dates that are not in the future,
and the protocol traps described in CONTRIBUTING.md.

Exit 0 when clean, 1 when any entry fails.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("missing dependency: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
APPS_DIR = ROOT / "apps"
SCHEMA = ROOT / "schema" / "app.schema.json"

# Protocol traps, encoded so they cannot silently reappear.
# Each is (compiled pattern, explanation).
FORBIDDEN = [
    (re.compile(r'io\.modelcontextprotocol/apps'),
     'extension ID is "io.modelcontextprotocol/ui", not "/apps"'),
    (re.compile(r'"type"\s*:\s*"app"'),
     'there is no type:"app" field in the protocol'),
    (re.compile(r'"spec_version"'),
     'use spec.apps_spec_version and spec.mcp_spec_version, never one collapsed field'),
    (re.compile(r'ui/resourceUri'),
     '_meta["ui/resourceUri"] is the deprecated flat form, use _meta.ui.resourceUri'),
]


class Problems:
    def __init__(self) -> None:
        self.items: list[tuple[str, str]] = []

    def add(self, where: str, msg: str) -> None:
        self.items.append((where, msg))

    def report(self) -> int:
        if not self.items:
            return 0
        by_file: dict[str, list[str]] = {}
        for where, msg in self.items:
            by_file.setdefault(where, []).append(msg)
        for where in sorted(by_file):
            print(f"\n{where}")
            for msg in by_file[where]:
                print(f"  - {msg}")
        print(f"\n{len(self.items)} problem(s) in {len(by_file)} file(s)")
        return 1


def main() -> int:
    if not SCHEMA.exists():
        sys.exit(f"schema not found: {SCHEMA}")
    validator = Draft202012Validator(json.loads(SCHEMA.read_text()))

    files = sorted(APPS_DIR.glob("*.json")) if APPS_DIR.exists() else []
    if not files:
        print("no entries in apps/ yet, nothing to validate")
        return 0

    p = Problems()
    seen_ids: dict[str, str] = {}
    seen_apps: dict[tuple[str, str], str] = {}
    today = dt.date.today()

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        raw = path.read_text()

        try:
            entry = json.loads(raw)
        except json.JSONDecodeError as e:
            p.add(rel, f"invalid JSON: {e}")
            continue

        for pattern, why in FORBIDDEN:
            if pattern.search(raw):
                p.add(rel, f"forbidden pattern {pattern.pattern!r}: {why}")

        for err in sorted(validator.iter_errors(entry), key=lambda e: list(e.path)):
            loc = ".".join(str(x) for x in err.path) or "(root)"
            p.add(rel, f"{loc}: {err.message}")

        entry_id = entry.get("id")
        if isinstance(entry_id, str):
            if entry_id != path.stem:
                p.add(rel, f'id "{entry_id}" does not match filename "{path.stem}"')
            if entry_id in seen_ids:
                p.add(rel, f'duplicate id "{entry_id}", also in {seen_ids[entry_id]}')
            seen_ids[entry_id] = rel

        # One server may ship several apps, so repo_url alone is not unique.
        # What must be unique is the app: this ui:// resource in this repo.
        repo = (entry.get("server") or {}).get("repo_url")
        ui_res = entry.get("ui_resource")
        if isinstance(repo, str) and isinstance(ui_res, str):
            key = (repo.rstrip("/").lower(), ui_res)
            if key in seen_apps:
                p.add(rel, f"duplicate app, {ui_res} in this repo is already "
                           f"listed by {seen_apps[key]}")
            seen_apps[key] = rel

        for field, value in (("added", entry.get("added")),
                            ("updated", entry.get("updated")),
                            ("verification.last_checked",
                             entry.get("verification", {}).get("last_checked"))):
            if isinstance(value, str):
                try:
                    if dt.date.fromisoformat(value) > today:
                        p.add(rel, f"{field} is in the future: {value}")
                except ValueError:
                    p.add(rel, f"{field} is not a real date: {value}")

    rc = p.report()
    if rc == 0:
        print(f"{len(files)} entr{'y' if len(files) == 1 else 'ies'} valid")
    return rc


if __name__ == "__main__":
    sys.exit(main())
