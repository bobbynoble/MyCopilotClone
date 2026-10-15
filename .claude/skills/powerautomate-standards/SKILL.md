---
name: powerautomate-standards
description: Standards for Power Automate cloud flows and Copilot Studio agent flows — naming, error handling, expressions, performance and solution awareness. Use when designing, writing or reviewing any flow.
---

# Power Automate Standards

## Flow naming
`<Trigger type> - <Purpose>` e.g. `Automated - New Request Notify Approver`,
`Scheduled - Daily Overdue Reminder`, `Instant - Generate Contract PDF`,
`Agent - Lookup Order Status`.

## Action naming
- Rename **every** action to describe what it does: `Get Request Item`, `Compose Approver Email`.
- Keep the original action type visible when helpful: `Get items - Open Requests`.
- No default names (`Compose 2`, `Apply to each 3`) in delivered flows.

## Structure: Try / Catch / Finally
```
Initialize variables (all at top)
Scope: Try        → main logic
Scope: Catch      → Configure run after: has failed, has timed out
                    - Filter result('Try') for Failed actions
                    - Log error (Dataverse error table or Teams/email to support)
                    - Terminate: Failed
Scope: Finally    → (optional) runs after Try/Catch for cleanup
```
Error message expression:
`first(filter(result('Try'), item()?['status'] == 'Failed'))?['error']?['message']`

## Expressions & data
- Use `Compose` for intermediate values rather than many variables.
- Use `Select` + `Filter array` instead of loops where possible.
- Use OData filter queries and `$select` on Get items/List rows; set Top Count deliberately.
- Use `coalesce()` and `?[]` safe navigation for optional fields.
- Add a note to complex expressions explaining what they do.

## Performance
- Avoid `Apply to each` over large sets; if needed, enable concurrency (and make sure order
  doesn't matter and no variables are appended inside).
- Add trigger conditions to stop unnecessary runs.
- Use pagination thresholds consciously.
- Use child flows for reusable logic (solution-aware, "Run a Child Flow").

## Solution awareness
- Create flows **inside a solution**.
- Connections via **connection references** only.
- Site URLs, list names, emails, thresholds → **environment variables**.
- Set a run-only user / service account strategy for production flows.

## Agent flows (Copilot Studio)
- Trigger: "When an agent calls the flow"; respond with "Respond to the agent".
- Define clear, typed inputs/outputs with descriptions (the orchestrator reads them).
- Agent flows have a two-minute response limit. For longer work, use **asynchronous responses**
  so the result is returned when it completes.
- Always return a friendly error output rather than failing silently.
- Use workflow nodes (Agent, Extract, Prompt, Human review, Copilot) where they fit. See
  `copilot-studio-builder` §5. Use deterministic actions for rules and AI nodes for fuzzy work.
