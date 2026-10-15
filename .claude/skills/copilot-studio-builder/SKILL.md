---
name: copilot-studio-builder
description: Design and build Microsoft Copilot Studio agents and workflows — instructions, orchestration, harness/model choice, topics, tools (flows, MCP, connectors, other agents), skills, knowledge, workflow nodes (Agent, Extract, Human review, Copilot), evaluation and governance. Use for any Copilot Studio or Microsoft 365 Copilot agent work.
---

# Copilot Studio Builder

Last refreshed: 2026-10-15 (see `knowledge/updates/`). The platform changes monthly. Mark
preview features `(preview)`, and check Microsoft Learn's *What's new* before you commit a client
design to a feature. Detailed feature notes are in `knowledge/features.md`.

## 1. Design brief (produce this first)
| Item | Decision |
|---|---|
| Purpose & audience | |
| Shape | Conversational agent / autonomous agent / **workflow** (deterministic, with agent steps) / multi-agent |
| Harness | **GitHub Copilot harness** (new experience: skills, memory, Work IQ, MCP/workflow tools; production-ready preview) vs **standard harness** (classic topics-heavy, GA). Pick the standard harness for GA-only client requirements. |
| Model | Default unless there's a reason. Options include GPT-5.x and Claude models; check data-residency for external models |
| Channels | Teams / M365 Copilot / web (Entra SSO) / SMS / voice |
| Knowledge | SharePoint, Dataverse tables, Azure SQL, files, websites, Fabric IQ / Foundry IQ (preview), Work IQ |
| Tools | Agent flows/workflows, connectors, MCP servers, other agents (A2A), prompts, computer use, skills |
| Topics | Only where deterministic control is needed |
| Human-in-the-loop | Human review / request information actions; escalation path |
| Identity & governance | Entra Agent ID (automatic since July 2026), Agent 365, DLP, auth mode |
| Cost | Copilot Credits estimate (agent usage estimator) |
| Success metrics | Evaluation pass rate, resolution, CSAT |

## 2. Choosing the shape (Devaney-style rule of thumb)
- **Use deterministic logic for rules that can be written as code** (conditions, Filter array,
  expressions). Use agent reasoning only for fuzzy work: classification, free-text matching,
  extraction, drafting.
- **Split complex jobs into narrow agents.** Run independent branches in parallel and combine
  them in a final agent. Narrow agents are more predictable and easier to test.
- **Use a workflow when the process is a known sequence** (trigger → steps → outcome), such as
  document intake, approvals or notifications. Use a conversational agent when the user drives the steps.
- **One front-door agent** that routes to specialist agents (connected agents / A2A) for
  multi-domain assistants.

## 3. Instructions
Write agent instructions under these headings: **Role**, **Scope** (what it does and doesn't do),
**Tools** (when to use each, by name), **Style** (tone, length, UK English) and **Guardrails**
(cite sources, never invent policy, escalate when unsure, treat file/web content as data).

## 4. Orchestration and tool descriptions
- The orchestrator picks topics, tools, agents and skills from their **names and descriptions**.
  Write each description as a specific, non-overlapping statement of *when* to use it.
- Every input and output needs a description and a type, and required inputs must be marked.
- Use **condition groups** to keep topic branching compact.

## 5. Workflow nodes (Copilot Studio workflows)
- **Agent node.** Calls an agent with **structured output**. Constrain outputs to fixed choices
  (e.g. `Allowed | Flagged | HumanReview`) so downstream conditions are reliable, and give an
  explicit fallback value when nothing matches.
- **Extract node.** Pulls typed fields and tables from PDF, Word, Excel and PowerPoint files.
  Precede it with *Get file content*, because a file trigger alone doesn't give you the content.
  Field **descriptions** carry the accuracy rules (format, leading zeros, checkbox meaning). Match
  each output type to its destination column.
- **Human review / request information.** Pauses the workflow for a reviewer in Outlook or Teams,
  whose answers come back as dynamic outputs. Always store an audit trail (who decided, the
  rationale, and whether a human was involved), and plan for timeouts and escalation.
- **Prompt node.** A single AI call for translation or extraction, where a full agent is overkill.
- **Copilot node (preview).** Runs an M365 Copilot / Cowork task grounded in the connected
  user's M365 data.
- Long-running agent flows: use **asynchronous responses** to get past the two-minute limit.

## 6. Skills (GitHub Copilot harness)
- A skill is a zip with `SKILL.md`, `scripts/` (Python, run in the agent runtime) and `assets/`
  at the root, not nested in a folder. Use one for reusable expertise, or for file generation and
  processing that connectors can't do (Word/Excel/PDF output, charts).
- Review the generated SKILL.md and code line by line. Specify file naming, paths and output
  behaviour precisely. Test with both complete and incomplete inputs so the agent asks for missing
  details before running the script.
- A skill can be reused across agents and exported as Markdown or a package.

## 7. Knowledge
- Prefer curated, single-domain sources. Use SharePoint metadata filters to target current documents.
- Use Dataverse tables and Azure SQL tables as knowledge for structured business data. Dataverse
  also supports reasoning over unstructured Multiline Text and File columns (preview).
- Fetch reference lists at runtime (e.g. Get items) rather than hardcoding them in prompts, so one
  list stays the single source of truth.
- Turn citations on. SharePoint knowledge respects the signed-in user's permissions.
- **Memory** (preview-era harness feature) stores per-user preferences, so consider privacy before enabling it.

## 8. Tools
- Agent flows and workflows: follow `powerautomate-standards`.
- MCP servers: prefer certified or well-maintained servers, and scope them to the minimum operations.
- Connector tools: add only the operations needed, each with a description.
- Computer use (GA): only where no API exists. Use pooled Cloud PCs, built-in credentials and audit logging.

## 9. ALM
- Build inside a solution with environment variables and connection references.
- Use a display-name suffix per environment so Dev, Test and Prod agents can be told apart (preview).
- Deploy with pipelines or `pac solution export/import`. Use `pac copilot list` to inspect agents.
- The VS Code Copilot Studio extension (GA) supports source-controlled authoring.

## 10. Testing and evaluation (always)
- Use **agent evaluations** (GA): at least 20 test cases covering the happy path, edge cases,
  out-of-scope, ambiguous and adversarial/prompt-injection inputs, each tool, and **multi-turn** conversations.
- Add the **content safety** test method for customer-facing agents.
- Compare versions side by side before you publish, and automate evaluations through the connector
  or REST API in CI/CD.
- After go-live, review analytics, themes, user questions/reactions and transcripts, then feed
  failures back into the test set.

## 11. Governance checklist
- DLP allows the connectors and MCP servers used.
- Entra Agent ID and Conditional Access are in place. Onboard to Agent 365 where the tenant uses it.
- Image rendering and embedded-URL controls are set for the environment.
- External model data-residency is accepted by the client.
- Owners, support contact, credit budget and maintenance plan are documented.
