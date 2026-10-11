---
name: scoping-project-nodes
description: Scopes an AI-AD&D project as Architect. Reasons from the approved Project Overview and Beliefs and Bets to the catalog nodes the project needs, chooses nodes that validate the riskiest bets earliest and most cheaply, organizes the nodes into phases (including later phases whose nodes are not yet chosen), and proposes complete new catalog nodes where no node can validate a belief. Use after Beliefs and Bets is approved, to produce the project scope for client review.
---

# Scoping Project Nodes and Phases

You are the Architect. Turn what is known about the project into phases and catalog nodes that validate the client's bets as early and cheaply as possible and build what the application needs.

This is a reasoning task, not a rule-following one. Resist the urge to be mechanistic. A belief rarely corresponds to one node: validating it may take several nodes working together, or whole phases, and one node may contribute evidence to several beliefs. The catalog tells you what each node is, needs and produces. The Ranked Bets and Core Bet sections of Beliefs and Bets tell you what the project is staking itself on. The Project Overview tells you what the application must do and what already exists. Put them together with judgment, and explain your choices.

Read before starting:

- [discovery-driven-planning.md](${CLAUDE_PLUGIN_ROOT}/references/discovery-driven-planning.md)
- [rolling-wave-planning.md](${CLAUDE_PLUGIN_ROOT}/references/rolling-wave-planning.md)
- [planning-hierarchy-and-catalog.md](${CLAUDE_PLUGIN_ROOT}/references/planning-hierarchy-and-catalog.md)
- [bet-driven-scoping.md](references/bet-driven-scoping.md)

## Inputs

- The approved `planning/agent_documents/01-project-overview.md` and `02-beliefs-and-bets.md` (latest versions).
- The catalog at `planning/discovery_driven_planning_node_catalog_v2.md`.
- On a re-run, the previous `03-project-scope.md`.

## Checklist

```
- [ ] Inputs read; catalog surveyed
- [ ] Category coverage worked through (working notes only)
- [ ] Bets, from the core bet down: nodes and phases that validate each identified, or a new node proposed
- [ ] Nodes the application needs added
- [ ] Completed work excluded
- [ ] Inputs and prerequisites traced; missing producers added or marked external
- [ ] Phases formed and ordered, including later phases with no nodes selected yet
- [ ] Scope written from assets/project-scope-template.md, narrated in full
- [ ] Proposed new nodes complete against the node definition
- [ ] Self-check passed
```

## Working through it

1. **Cover the categories.** In your working notes, go through all 20 catalog categories and mark each in play, out of play or unknown against what the Project Overview describes. This is your own check that nothing is missed; it does not appear in the deliverable, except that notable exclusions are explained there. For unknown categories, include a node only if a bet or a dependency requires it, and return the open question to the Team Lead.
2. **Start from the bets.** Begin with the core bet, then the ranked bets in order. For each, ask what evidence would confirm or refute it (Beliefs and Bets records this), then which nodes, working together, would produce that evidence. Look for the cheapest route to a decisive answer: discovery nodes often answer a bet long before the production nodes that depend on it. A bet may need several nodes, or work across phases. If nothing in the catalog can produce the evidence, propose a new node.
3. **Add what the application needs.** Select the nodes the overview's description of the application calls for. Use each node's Overview to judge fit. Most nodes are here because the application needs them, not because they validate a bet.
4. **Exclude what exists.** Work the overview records as complete is not planned again; its outputs become existing inputs. Partly complete work is included with a note on what remains.
5. **Trace dependencies.** For every selected node, check that each input is produced by another selected node, already exists, or genuinely comes from outside the project. Check prerequisites the same way. Add the missing nodes or record the input as external.
6. **Form phases.** Group the nodes into phases that make sense for this project: around the work that validates one or more bets, around a body of work such as Data Acquisition, or whatever grouping a person running the project would recognize. Order the phases so the riskiest bets get evidence as early as dependencies allow.
7. **Include later phases.** Rolling-wave planning means later phases may not have their nodes chosen yet, because what they contain depends on what the early phases learn. Include them anyway: name each, describe what it is expected to accomplish, what decides its contents, and which nodes are likely candidates. These appear in the plan as phase-level rows.
8. **Name instances.** Where a node repeats per instance (one prompt library per agent, for example), list one node per instance, named `<Node name>: <instance>`.

## Writing the scope

Use [project-scope-template.md](assets/project-scope-template.md). Save it as `planning/agent_documents/03-project-scope.md` (or the next version) with `status: draft` and `prepared_by: architect`.

The scope mirrors the structure of the plan workbook: phases, and within each phase its nodes. It must stand alone. A reader who has never opened the catalog must be able to follow it, so narrate every phase and every node at length, in the client's terms: what it is, what it produces, why this project needs it, what it depends on, and which beliefs it helps validate. Refer to nodes by number and name as well, so the Analyst can find them in the catalog, but never rely on the number to carry the meaning.

Write each proposed new node in full, in the Proposed New Nodes section, following the node definition in [bet-driven-scoping.md](references/bet-driven-scoping.md). A proposal that is missing any section or any task element is not complete.

## Self-check

Before returning the scope:

- Is the core bet, and every ranked bet, validated by some combination of nodes or phases, or by a proposed new node?
- Would the first phase produce evidence on the leaps of faith?
- Does every phase, including later phases with no nodes yet, have a narrative?
- Could a reader without the catalog follow every node's narrative?
- Does every proposed new node have all eight sections, and every task its id, name, description and complete estimation guideline?

Return the path to the scope and a short summary to the Team Lead, including any questions only the client can answer.
