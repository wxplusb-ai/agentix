# ai-ddp-planning

A Claude Code plugin that runs an AI-AD&D planning engagement: a team of agents that produces a discovery-driven, rolling-wave project plan for an AI application and publishes it to ClickUp.

## The team

| Agent | Role |
|---|---|
| `team-lead` | Owns the client relationship, scope, orchestration and quality. Runs as the main session. |
| `architect` | Turns the overview and bets into catalog nodes organized into phases. |
| `analyst` | Runs estimation discovery, then estimates and builds the plan workbook. |
| `integrator` | Publishes the approved plan to ClickUp. |

## The process

1. **Project Overview:** what the project is and which catalog categories apply.
2. **Beliefs and Bets:** the beliefs the project rests on, and the bets to test first.
3. **Project Scope:** the catalog nodes the project needs, organized into phases.
4. **Estimation Discovery:** the answers the estimates depend on, from each node's Discovery for Planning section.
5. **Project Plan:** a three-tier plan (tasks, nodes, phases) in Excel.
6. **Publish:** after you review the plan in Excel and authorize it, the plan goes to ClickUp (phases as folders, nodes as lists, tasks as tasks).

Each step ends with your sign-off. Deliverables are written to `planning/` in the repo where you run it.

## Install

From the repo where you want to plan:

```bash
claude plugin marketplace add <path-to-agentix>      # or <github-owner>/agentix once pushed
claude plugin install ai-ddp-planning@agentix --scope project
```

To try it without installing:

```bash
claude --plugin-dir <path-to-agentix>/plugins/ai-ddp-planning --agent ai-ddp-planning:team-lead
```

## Run

```bash
claude --agent ai-ddp-planning:team-lead
```

To make the Team Lead the default for a repo, add `"agent": "ai-ddp-planning:team-lead"` to that repo's `.claude/settings.json`.

## Requirements

- The `xlsx` skill (from Anthropic's skills plugin) for building the plan workbook.
- For publishing: a ClickUp API token in the `CLICKUP_API_TOKEN` environment variable, and your ClickUp workspace, space and user IDs.

## Contents

```
ai-ddp-planning/
├── .claude-plugin/plugin.json
├── agents/        team-lead, architect, analyst, integrator
├── skills/        one skill per step, plus leading-ai-ddp-planning for the Team Lead
├── references/    shared methodology references and the framework context
└── catalog/       the AI-AD&D node catalog (v2), copied into planning/ at setup
```
