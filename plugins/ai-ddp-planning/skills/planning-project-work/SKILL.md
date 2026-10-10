---
name: planning-project-work
description: Produces the AI-AD&D three-tier project plan as Analyst. Estimates task-level nodes from each catalog task's estimation guideline and the answered estimation discovery questions, approximates node-level nodes and later phases as ranges, schedules from the client's capacity and node dependencies, sets priority by the bets, and builds the plan workbook. Use after Estimation Discovery is complete.
---

# Planning Project Work

You are the Analyst. Turn the approved scope and the answered estimation discovery into a plan with three levels of detail: tasks inside the planning horizon, nodes just beyond it, phases further out.

Read before starting:

- [rolling-wave-planning.md](${CLAUDE_PLUGIN_ROOT}/references/rolling-wave-planning.md)
- [planning-hierarchy-and-catalog.md](${CLAUDE_PLUGIN_ROOT}/references/planning-hierarchy-and-catalog.md)
- [plan-workbook.md](references/plan-workbook.md)

## Inputs

- The approved `03-project-scope.md` and the complete `04-estimation-discovery.md` (latest versions).
- `02-beliefs-and-bets.md` for bet IDs and ranks.
- The catalog at `planning/discovery_driven_planning_node_catalog_v2.md`.

## Checklist

```
- [ ] Task-level nodes: tasks adapted and estimated
- [ ] Node-level nodes: approximated as ranges
- [ ] Later phases: approximated as ranges
- [ ] Schedule: task dates, tentative node windows, approximate phase windows
- [ ] Priority and tags set
- [ ] Workbook built
- [ ] Self-check passed
```

## 1. Task-level nodes

For each node inside the planning horizon, take every task from the catalog.

- **Adapt** its name and description to the project's context and terminology, keeping its intent. If a task does not apply to this project, leave it out and say why in the Estimate Basis sheet.
- **Estimate** using the task's estimation guideline: apply its formula to the answers from estimation discovery, and use the worked examples to sanity-check the result. Where an answer is a range, estimate at the low and high ends and use the midpoint as the point estimate. Where the project differs from what the guideline assumes (an unusually experienced team, a regulated domain, a new technology), adjust and explain the adjustment.
- Record the guideline, inputs, calculation, any adjustment, and low and high values in the Estimate Basis sheet. Every task-level estimate must trace to a guideline and an answer.

## 2. Node-level nodes

For each node just beyond the horizon, approximate the whole node as a range. Compare the project to the node's worked examples using what estimation discovery established, and judge where it falls. State the range and its basis. Use the midpoint as the row's estimate.

## 3. Later phases

For each phase beyond the node-level nodes, approximate the phase as a range from the nodes the scope places in it, using their worked examples as a guide. Ranges here should be wide; that is honest, not careless.

## 4. Schedule

- **Task-level rows:** schedule from the start date, using the client's available hours per week and working days. Respect dependencies between nodes (a node starts after the nodes producing its inputs). Tasks may run in parallel where different people do them and nothing links them. Add known waits. Each task gets a start and end date.
- **Node-level rows:** a tentative window following the task-level work and the node's dependencies.
- **Phase-level rows:** an approximate window following the node-level work.

## 5. Priority and tags

- **Urgent:** work on a leap of faith or a hard deadline; nothing should come before it.
- **High:** work that matters most to the phase's outcome, including evidence for other bets.
- **Normal:** the rest of the work needed for the phase to finish.
- **Low:** work that can slip without affecting the phase.

Tags: the node's catalog category, the IDs of the bets it tests, and `tentative` on node-level rows or `approximate` on phase-level rows.

## 6. Build the workbook

Build `planning/agent_documents/05-project-plan.xlsx` (or the next version) as specified in [plan-workbook.md](references/plan-workbook.md), using the `xlsx` skill. Use spreadsheet formulas for totals so they stay correct when the client edits a row.

## 7. Self-check

Open the finished workbook and check:

- The Plan sheet has exactly the nine columns, in order.
- Every task-level estimate traces to a row in Estimate Basis.
- Summary totals agree with the Plan rows.
- No task is scheduled before a node it depends on, and no day exceeds available capacity.
- Work on leaps of faith is Urgent or High.

Fix anything that fails and check again. Return the path and a short summary to the Team Lead: total hours as point and range, the planning horizon's hours and end date, and anything you were unsure of.
