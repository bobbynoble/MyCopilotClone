# Copilot Studio Feature Register

Maintained by `knowledge-refresh`. Status as of the date shown. Source: Microsoft Learn
*What's new* unless noted. Always re-check before you commit a client design to a feature.

| Feature | Status (as of 2026-10-15) | Since | Notes |
|---|---|---|---|
| New experience / GitHub Copilot harness | Production-ready preview | Jun 2026 | Enhanced orchestration runtime alongside the standard harness |
| Skills (SKILL.md + scripts + assets) | Harness feature | Jun 2026 | Reusable, exportable; Python runtime with 50+ packages (Devaney, Aug 2026) |
| Memory | Harness feature | Jun 2026 | Per-user persistent context |
| Work IQ | Harness feature / preview | Mar–Aug 2026 | Grounds agents in M365 mail, calendar, files and chats |
| Connected agents (other agents) on the harness | Preview | Jun 2026 | Front-door agent pattern |
| Agent-to-agent (A2A) protocol | GA | Apr 2026 | |
| Workflow / MCP server as a tool (harness) | Preview | Jul 2026 | |
| Entra Agent ID auto-created for every agent | Mandatory | Jul 2026 | Can't opt out |
| Real-time voice agents | Preview (digital messaging) | Apr–Jul 2026 | |
| Usage-based billing in Copilot Credits | Live | Aug 2026 | Use the agent usage estimator |
| Microsoft Agent 365 governance | Live | Aug 2026 | |
| Azure SQL tables as knowledge | Live | Aug 2026 | |
| Fabric IQ / Foundry IQ grounding | Preview | Jun–Aug 2026 | |
| Image rendering / embedded URL control | Live | Aug 2026 | Admin-centre setting |
| Extract node (workflows) | Live | Sep 2026 | Devaney tutorial Oct 2026 |
| Copilot node (workflows) | Preview | Sep 2026 | Runs Copilot Chat / Cowork tasks, Researcher, Analyst |
| Model picker incl. experimental models | Live | Sep 2026 | |
| Content safety evaluation method | Live | Sep 2026 | |
| File attachments (Word / Excel / PowerPoint) | GA | Sep 2026 | |
| Dataverse tables as knowledge (+ unstructured columns preview) | Live / preview | Sep 2026 | |
| Agent evaluations + multi-turn tests | GA | Mar 2026 | REST API (preview) and connector for automation |
| Computer use | GA | May 2026 | Standalone computer use tools in preview |
| Async responses for agent flows (beyond 2 min) | Live | May 2026 | |
| Prompt node in agent flows | Live | May 2026 | |
| Condition groups | Live | Jun 2026 | |
| VS Code Copilot Studio extension | GA | Jan 2026 | |
| Human review / request information action | Preview → in use | Nov 2025 | Devaney tutorial Sep 2026 |

## Devaney build patterns (recent)
| Date | Pattern | Link |
|---|---|---|
| 2026-10-11 | Extract node: document fields into a SharePoint library | https://www.matthewdevaney.com/how-to-extract-data-from-pdfs-word-excel-in-copilot-studio/ |
| 2026-09-27 | Human review on AI decisions with an audit trail | https://www.matthewdevaney.com/copilot-studio-ask-for-human-review-on-ai-decisions/ |
| 2026-09-13 | Multi-agent workflows: narrow agents, parallel branches, deterministic rules | https://www.matthewdevaney.com/how-to-build-multi-agent-workflows-in-copilot-studio/ |
| 2026-08-30 | Send and receive SMS in Copilot Studio | https://www.matthewdevaney.com/how-to-send-and-receive-sms-text-messages-in-copilot-studio/ |
| 2026-08-16 | Agent skills: build, review, package as zip | https://www.matthewdevaney.com/how-to-create-agent-skills-in-copilot-studio/ |

Tutorial source files: https://github.com/matthewdevaney/Copilot-Studio-Tutorials (also covers
Dataverse and Azure SQL knowledge, fuzzy search in Dataverse, Word documents from templates,
replying to emails, publishing to the web with SSO, and multi-agent orchestration).

Other recent repos worth knowing: `copilot-studio-transcript-viewer` (Power Apps code app),
`powerapps-custom-functions`, `M365-Agent-Tutorials`, `maf-firstagent` (Microsoft Agent
Framework), `fastmcp-mcpapps-quickstart` and `M365-MCP-Apps-Dataverse-Calendar` (MCP Apps).
