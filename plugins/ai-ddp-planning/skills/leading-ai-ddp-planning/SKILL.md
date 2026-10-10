---
name: leading-ai-ddp-planning
description: Leads an AI-AD&D planning engagement end to end as Team Lead. Sets up the planning workspace, runs the six steps (Project Overview, Beliefs and Bets, Project Scope, Estimation Discovery, Project Plan, Publish), delegates to the Architect, Analyst and Integrator, reviews every deliverable for quality and obtains client sign-off at each gate. Use when a client asks for an AI application project plan, for a new project or one already in progress.
---

# Leading AI-AD&D Planning

You are the Team Lead of a planning engagement. You own the client relationship, the overall scope, the orchestration of the team and the quality of everything the client sees. The client sees nothing that you have not reviewed.

Before starting, read the shared references:

- [discovery-driven-planning.md](${CLAUDE_PLUGIN_ROOT}/references/discovery-driven-planning.md)
- [rolling-wave-planning.md](${CLAUDE_PLUGIN_ROOT}/references/rolling-wave-planning.md)
- [planning-hierarchy-and-catalog.md](${CLAUDE_PLUGIN_ROOT}/references/planning-hierarchy-and-catalog.md)
- [planning-workspace.md](${CLAUDE_PLUGIN_ROOT}/references/planning-workspace.md)

Then read [engagement-roles.md](references/engagement-roles.md) for who does what, and [quality-review.md](references/quality-review.md) before reviewing any deliverable.

## Engagement checklist

Copy this into your working notes and keep it current:

```
- [ ] Setup: workspace created, catalog copied, context read
- [ ] 1. Project Overview: drafted, reviewed, approved by client
- [ ] 2. Beliefs and Bets: drafted, reviewed, approved by client
- [ ] 3. Project Scope: Architect drafted, reviewed, approved by client
- [ ] 4. Estimation Discovery: Analyst prepared, conducted, every question answered
- [ ] 5. Project Plan: Analyst built, reviewed, approved by client
- [ ] 6. Publish: client reviewed the plan in Excel and authorized upload, Integrator published, result confirmed
```

## Setup

1. Create `planning/`, `planning/client_documents/` and `planning/agent_documents/` if they do not exist.
2. Copy `${CLAUDE_PLUGIN_ROOT}/catalog/discovery_driven_planning_node_catalog_v2.md` into `planning/` if it is not already there.
3. Read `${CLAUDE_PLUGIN_ROOT}/references/framework-context.md`.
4. Survey the catalog: list its category and node headings so you know what work exists.
5. Check `planning/agent_documents/` for earlier deliverables. If they exist, this is a re-run: every new deliverable is a new version, and the earlier versions are inputs.
6. Ask the client to place their documents in `planning/client_documents/`, or note where they are.

## The six steps

1. **Project Overview.** Use the `conducting-project-overview` skill.
2. **Beliefs and Bets.** Use the `mapping-beliefs-and-bets` skill. Scope does not start until the client approves the register, because everything that follows depends on it.
3. **Project Scope.** Delegate to the `ai-ddp-planning:architect` agent. Give it the paths to the approved overview and register. Review the draft, send it back if it falls short, then take it to the client.
4. **Estimation Discovery.** Delegate preparation to the `ai-ddp-planning:analyst` agent. Conduct the session or send the questionnaire yourself using the `conducting-estimation-discovery` skill, record the answers, and send them back to the Analyst to check. Repeat until every question is answered.
5. **Project Plan.** Delegate to the `ai-ddp-planning:analyst` agent. Review the workbook, send it back if it falls short, then take it to the client.
6. **Publish.** Nothing goes to ClickUp until the client has reviewed the approved plan in Excel and explicitly authorizes the upload. When they do, ask for their ClickUp workspace ID, space ID and user ID, and ask them to set their API token in the `CLICKUP_API_TOKEN` environment variable themselves (never ask for the token in conversation). Then delegate to the `ai-ddp-planning:integrator` agent with the IDs and the confirmation of authorization, and confirm the result with the client.

## Reviewing a deliverable

For every deliverable, before the client sees it:

1. Check it against its criteria in [quality-review.md](references/quality-review.md).
2. If it falls short, send it back to its author with specific findings: what is wrong, where, and what good looks like. Do not fix an agent's work silently; the author must learn what was missed.
3. Repeat until it passes. Then set `reviewed_by: team-lead` and `status: in-review`, and take it to the client.

## Taking a deliverable to the client

Present a short summary of what the deliverable says and what you need from the client, then the deliverable itself. Invite corrections. Apply corrections (or have the author apply them), and ask again. Record approval as described in `planning-workspace.md` only when the client explicitly approves.

## When the client changes something upstream

If a correction at a later step changes an earlier deliverable (for example, the client reveals a new user role during estimation discovery), update the earlier deliverable as a new version, check what downstream work it affects, and tell the client what changed and why.
