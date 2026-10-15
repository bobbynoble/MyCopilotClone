"""Check watched sources for anything new since the last refresh.

Usage:  python -I scripts/check_sources.py            # report new items as JSON
        python -I scripts/check_sources.py --update   # also save new markers to knowledge/state.json

Stdlib only. Sources that need judgement (Microsoft Learn pages, socials) are handled by the
knowledge-refresh skill; this script covers the ones with machine-readable feeds.
"""
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "knowledge" / "state.json"
UA = {"User-Agent": "Mozilla/5.0 (MyClone knowledge-refresh)"}

RSS_FEEDS = {
    "devaney_blog": "https://www.matthewdevaney.com/feed/",
    "power_platform_devblog": "https://devblogs.microsoft.com/powerplatform/feed/",
}
ATOM_FEEDS = {
    "copilot_studio_kit_releases": "https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases.atom",
}
GITHUB_USERS = ["matthewdevaney"]
NUGET_PAC = "https://api.nuget.org/v3-flatcontainer/microsoft.powerapps.cli/index.json"


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def rss_items(url):
    root = ET.fromstring(fetch(url))
    for it in root.iter("item"):
        yield {
            "title": it.findtext("title"),
            "link": it.findtext("link"),
            "date": parsedate_to_datetime(it.findtext("pubDate")).isoformat(),
        }


def atom_items(url):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(fetch(url))
    for e in root.findall("a:entry", ns):
        link = e.find("a:link", ns)
        yield {
            "title": e.findtext("a:title", namespaces=ns),
            "link": link.get("href") if link is not None else None,
            "date": e.findtext("a:updated", namespaces=ns),
        }


def github_repos(user):
    data = json.loads(fetch(f"https://api.github.com/users/{user}/repos?sort=pushed&per_page=50"))
    for r in data:
        yield {
            "title": r["full_name"],
            "link": r["html_url"],
            "date": r["pushed_at"],
            "description": r.get("description"),
        }


def main():
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    report, errors = {}, {}

    sources = {k: (rss_items, u) for k, u in RSS_FEEDS.items()}
    sources |= {k: (atom_items, u) for k, u in ATOM_FEEDS.items()}
    sources |= {f"github_{u}": (github_repos, u) for u in GITHUB_USERS}

    for key, (fn, arg) in sources.items():
        try:
            items = list(fn(arg))
        except Exception as e:  # keep going; report the failure
            errors[key] = str(e)
            continue
        since = state.get(key, "")
        new = sorted((i for i in items if i["date"] > since), key=lambda i: i["date"], reverse=True)
        report[key] = new
        if items:
            state[key] = max(i["date"] for i in items)

    try:
        latest_pac = json.loads(fetch(NUGET_PAC))["versions"][-1]
        report["pac_cli"] = {"latest": latest_pac, "previously_seen": state.get("pac_cli")}
        state["pac_cli"] = latest_pac
    except Exception as e:
        errors["pac_cli"] = str(e)

    print(json.dumps({"new": report, "errors": errors}, indent=2))
    if "--update" in sys.argv:
        STATE.write_text(json.dumps(state, indent=2) + "\n")


if __name__ == "__main__":
    main()
