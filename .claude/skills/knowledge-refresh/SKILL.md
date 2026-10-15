---
name: knowledge-refresh
description: Check Matthew Devaney's blog, GitHub and the Microsoft Copilot Studio / Power Platform release sources for new methods and features, write a dated digest, and update the build skills so new features are used and considered. Use when asked to refresh, update or check for new Copilot/Power Platform knowledge, or on a schedule.
---

# Knowledge Refresh

Goal: keep `copilot-builder` and its skills current. Every run produces a digest and either
updates the skills or explains why nothing changed.

## 1. Gather
1. Run `python -I scripts/check_sources.py` (do **not** pass `--update` yet). It reports new
   blog posts, GitHub repo pushes, the Power Platform dev blog, Copilot Studio Kit releases and
   the latest pac CLI version since `knowledge/state.json`.
2. Read `knowledge/watchlist.md` and check the sources marked "Refresh skill":
   - Copilot Studio **What's new**: compare its `ms.date` to `copilot_studio_whats_new` in
     `knowledge/state.json` and read only sections newer than that.
   - Power Platform release plans: monthly, or when a new wave is published.
3. Process every item in `knowledge/inbox.md`.
4. For each new Devaney post, read the article (written posts first; "Video:" posts usually
   pair with a written post a week later). For new or updated repos, read the README and folder list.

## 2. Assess each item
Classify each item:
- **New feature/capability.** Note its name, where it lives (agent / workflow / topic / admin),
  and its GA vs preview status.
- **New method/pattern.** A better way to build something we already do.
- **Change/deprecation.** Something in our skills that is now wrong, retired or renamed.
- **Not relevant.** Record it in one line so it isn't re-read next time.

Treat Microsoft Learn as the authority on feature names, status and limits. Devaney's posts are
the authority on practical build patterns. Where the two conflict, note the conflict and prefer Learn.

## 3. Write the digest
Create `knowledge/updates/YYYY-MM-DD.md`:
```
# Knowledge refresh — YYYY-MM-DD
## Headlines            (3–5 bullets: what changes how we build)
## New features         | Feature | Status | Where | Use it when | Source |
## New methods          | Pattern | Summary | Source |
## Changes / deprecations
## Skill updates made   (file → what changed)
## Proposed, not applied (anything needing Robert's decision)
## Ignored              (one line each)
```
Summarise in your own words and link to the source. Don't copy articles.

## 4. Update skills
- Edit the relevant skill files (`copilot-studio-builder`, `powerautomate-standards`,
  `powerapps-standards`, `alm-solution-review`) so new features appear in design and review
  guidance. Mark preview features `(preview)`.
- Remove or correct guidance that's now wrong. Don't just append.
- Keep each skill concise. Move long feature detail to `knowledge/features.md` and link to it.
- Never weaken the non-negotiables in `copilot-builder.md` without listing it under "Proposed".
- If a new pac CLI version is out, say so in the digest. Don't install it.

## 5. Finish
1. Run `python -I scripts/check_sources.py --update` to move the markers forward.
2. Update `copilot_studio_whats_new` in `knowledge/state.json` to the page's `ms.date`.
3. Clear processed items from `knowledge/inbox.md`.
4. Reply with the Headlines section and the path to the digest.
