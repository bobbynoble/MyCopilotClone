---
name: alm-solution-review
description: Export, unpack and review a Power Platform solution against standards, and guide safe deployment between environments with pac CLI. Use when asked to review, audit, deploy, export or import a solution.
---

# ALM & Solution Review

## Safety first
1. `pac auth list` and `pac org who` — show the user which environment is active.
2. Export/unpack/review are read-only and fine anywhere.
3. `pac solution import`, `pac solution delete`, publishing or anything that changes an
   environment → Dev only, unless the user explicitly names the target environment.

## Export & unpack (PowerShell)
```powershell
$name = "<SolutionUniqueName>"
$proj = "projects/<project>"
pac solution export --name $name --path "$proj/solutions/$name.zip" --managed false --overwrite
pac solution unpack --zipfile "$proj/solutions/$name.zip" --folder "$proj/src/$name" --processCanvasApps --allowDelete
```
Canvas apps unpack to `.pa.yaml` source under `CanvasApps/src/` — review formulas there.
Flows are JSON under `Workflows/`. Copilot Studio agents appear under `bots/` and `botcomponents/`.

## Review checklist
### Solution
- [ ] Custom publisher with a meaningful prefix (not `new_` / `cr123_`)
- [ ] All components in the solution (no missing dependencies)
- [ ] Environment variables used for config; no hardcoded URLs/emails/IDs
- [ ] Connection references for every connector; sensibly named
- [ ] Security roles included where needed

### Power Apps (see `powerapps-standards`)
- [ ] Control and variable naming conventions
- [ ] No delegation warnings left unmitigated
- [ ] Minimal `App.OnStart`; named formulas used
- [ ] Errors handled on writes (`IfError`/`Notify`)
- [ ] Accessible labels present

### Power Automate (see `powerautomate-standards`)
- [ ] Flow and action names meaningful (no `Compose 2`)
- [ ] Try/Catch scopes with run-after configured
- [ ] Trigger conditions / OData filters to limit work
- [ ] No secrets in plain text; use Key Vault-backed env vars where appropriate

### Copilot Studio (see `copilot-studio-builder`)
- [ ] Instructions cover role, scope, tools, style, guardrails
- [ ] Topic/tool descriptions are specific and non-overlapping
- [ ] Authentication configured appropriately
- [ ] Test/evaluation set exists and passes

## Report format
| Severity | Component | Issue | Fix |
|---|---|---|---|
| 🔴 Blocking / 🟠 Should fix / 🟢 Nice to have | | | |

Lead with blocking issues; finish with a short summary and recommended next step.

## Deployment
- Dev: unmanaged. Test/Prod: **managed** solutions only.
- Prefer Power Platform Pipelines or GitHub Actions / Azure DevOps (Power Platform Build Tools).
- Use a deployment settings file for env var values + connection references:
  `pac solution create-settings --solution-zip <zip> --settings-file settings.json`
