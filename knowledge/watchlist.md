# Watchlist

Sources the `knowledge-refresh` skill checks. Automated = handled by `scripts/check_sources.py`.

## Matthew Devaney
| Source | URL | How checked |
|---|---|---|
| Blog (RSS) — tutorials + weekly video posts | https://www.matthewdevaney.com/feed/ | Automated |
| GitHub — tutorial files, samples, MCP/agent repos | https://github.com/matthewdevaney | Automated (repo pushes) |
| Key repo: Copilot Studio tutorial files | https://github.com/matthewdevaney/Copilot-Studio-Tutorials | Read folder list on refresh |
| Power Platform coding standards guides | https://www.matthewdevaney.com/power-platform-coding-standards/ | Check on refresh for revisions |
| X / Twitter | https://twitter.com/mattbdevaney | **Manual** — paste into `knowledge/inbox.md` |
| LinkedIn | https://www.linkedin.com/in/matthew-devaney-6499271b7/ | **Manual** — paste into `knowledge/inbox.md` |
| Weekly newsletter | Subscribe on matthewdevaney.com | **Manual** — forward/paste notable issues into inbox |

X and LinkedIn aren't scraped. Their terms prohibit it and they block automated access, and his
blog republishes the substantive content anyway.

## Microsoft (the "is this still current?" check)
| Source | URL | How checked |
|---|---|---|
| Copilot Studio — What's new | https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new | Refresh skill reads sections newer than last `ms.date` |
| Power Platform release plans | https://learn.microsoft.com/en-us/power-platform/release-plan/ | Refresh skill (monthly) |
| Power Platform developer blog | https://devblogs.microsoft.com/powerplatform/feed/ | Automated |
| Power Platform / Copilot Studio product blogs | https://www.microsoft.com/en-us/power-platform/blog/ | Refresh skill via web fetch (feed blocks scripts) |
| Power CAT Copilot Studio Kit releases | https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases | Automated |
| Power Platform CLI (pac) versions | https://www.nuget.org/packages/Microsoft.PowerApps.CLI | Automated |

## Adding a source
Add a row here; if it has RSS/Atom or is a GitHub user, also add it to `scripts/check_sources.py`.
