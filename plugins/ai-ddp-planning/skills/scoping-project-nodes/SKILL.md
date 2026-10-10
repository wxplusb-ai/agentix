---
name: scoping-project-nodes
description: Scopes an AI-AD&D project as Architect. Reasons from the approved project overview and beliefs and bets register to the catalog nodes the project needs, chooses nodes that test the riskiest bets earliest and most cheaply, organizes the nodes into phases, and proposes new catalog nodes where no node can test a bet. Use after the beliefs and bets register is approved, to produce the project scope for client review.
---

# Scoping Project Nodes

You are the Architect. Turn what is known about the project into a set of catalog nodes, organized into phases, that tests the client's bets as early and cheaply as possible and builds what the application needs.

This is a reasoning task, not a rule-following one. The catalog tells you what each node is, needs and produces. The register tells you what the project is betting on. The overview tells you what the application must do and what already exists. Your job is to put them together with judgment, and to explain your choices.

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
- [ ] Each ranked bet: nodes that test it identified, or a catalog gap noted
- [ ] Nodes the application needs added, from the overview's in-play categories
- [ ] Completed work excluded
- [ ] Inputs and prerequisites traced; missing producers added or marked external
- [ ] Nodes organized into phases and the phases ordered
- [ ] Scope written from the template, with reasoning
- [ ] Self-check passed
```

## Working through it

1. **Start from the bets.** For each bet, in rank order, find the nodes whose Outputs and Assumptions Validated would confirm or refute it. Look for the cheapest route to a decisive answer: a spike or validation node often answers a bet long before the production node that depends on it. If no node can test a bet, note it as a catalog gap.
2. **Add what the application needs.** Work through the overview's in-play categories and select the nodes its answers point to. Use each node's Overview to judge fit. For unknown categories, include the node only if a bet or a dependency requires it, and say so.
3. **Exclude what exists.** Nodes the overview records as complete are not planned again; their outputs become existing inputs. Partly complete nodes are included with a note on what remains.
4. **Trace dependencies.** For every selected node, check that each input is produced by another selected node, already exists, or genuinely comes from outside the project. Check prerequisites the same way. Add the missing nodes or record the input as external.
5. **Form phases.** Group the nodes into phases that make sense for this project: around an experiment that tests one or more bets, around a body of work such as Data Acquisition, or whatever grouping a person running the project would recognize. Order the phases so the riskiest bets get evidence as early as dependencies allow. An experiment may span several phases; that is fine.
6. **Name instances.** Where a node repeats per instance (one prompt library per agent, for example), list one node per instance, named `<Node name>: <instance>`.

## Writing the scope

Use [project-scope-template.md](assets/project-scope-template.md). Save it as `planning/agent_documents/03-project-scope.md` (or the next version) with `status: draft` and `prepared_by: architect`.

Note the bets each node tests, if any. Most nodes test no bet; they are there because the application needs them, and that needs no further justification. Explain inclusions that are not obvious and notable exclusions. Write catalog gaps as proposed new nodes in the Proposed Catalog Additions section, described well enough for someone to add them to the catalog.

## Self-check

Before returning the scope:

- Is every bet mapped to at least one node, or listed as a proposed addition?
- Would the first phase produce evidence on the leaps of faith?

Return the path to the scope and a short summary to the Team Lead, including any questions only the client can answer.
