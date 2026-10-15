# MyCopilotClone

A Claude Code build assistant for Microsoft Copilot Studio and Power Platform projects, from RN Consultancy.

Its working style follows the published methods of community practitioners, especially
[Matthew Devaney](https://www.matthewdevaney.com): standards-first, solution-aware, and every build
explained tutorial-style. This is an independent project, not affiliated with or endorsed by him.

## What's inside
- **`copilot-builder` agent** (`.claude/agents/`): designs, builds and reviews agents, apps, flows and solutions.
- **Skills** (`.claude/skills/`): Power Apps standards, Power Automate standards, Copilot Studio
  builder, ALM/solution review, and knowledge refresh.
- **Knowledge** (`knowledge/`): watchlist, feature register, dated update digests.
- **`scripts/check_sources.py`**: checks the blog, GitHub, Microsoft feeds and pac CLI versions for anything new.

## Use
Open this folder in Claude Code, then:
- `Use copilot-builder to design a Copilot Studio agent that…`
- `Use copilot-builder to export and review my <Solution> solution`
- `/knowledge-refresh` pulls in new methods and features and updates the skills
