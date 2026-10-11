# Quality Review

What a sound deliverable looks like at each step. The Team Lead checks every deliverable against these criteria before the client sees it. The criteria describe outcomes, not procedures: judge whether the deliverable achieves them.

## Contents

- All deliverables
- 01 Project Overview
- 02 Beliefs and Bets
- 03 Project Scope
- 04 Estimation Discovery
- 05 Project Plan
- 06 ClickUp Publication

## All deliverables

- Frontmatter is complete and the status is correct.
- The deliverable stands alone: complete narration, explained at length in the client's terms. A reader who has never opened the catalog can follow it, and a non-technical sponsor could understand it.
- Every claim about the client's situation traces to something the client said or provided. Inferences are marked as inferences.
- Open questions are listed, not buried.

## 01 Project Overview

- It describes the project as it is today: goals, market, users, workflow, data, technology, constraints and current state.
- Every relevant interview topic is covered. Topics that do not apply to this project are listed with the reason.
- It contains no catalog content (no categories, nodes or node numbers), no beliefs, assumptions or risks, and no recommendations about what work to do.
- For an in-flight project: what is complete, in progress and planned is clear, with what the completed work produced and showed.

## 02 Beliefs and Bets

- The core bet of the whole application is stated as a testable statement and rated.
- The areas covered were selected for this project, and skipped areas have a reason.
- Each belief is a testable statement: it is clear what evidence would confirm or refute it.
- Consequence and evidence ratings are the client's, or agreed with the client.
- Bets are ranked, and the ranking would survive the question "why is this one above that one?"
- Leaps of faith are flagged.
- Knowledge is separated from belief: anything with real evidence names the evidence.
- No experiments or other test entities are defined: validation is left to the nodes selected at scoping.

## 03 Project Scope

- The core bet and every ranked bet are validated by a combination of nodes or phases the scope explains, or by a proposed new node. Coverage is reasoned, not a one-to-one mapping.
- Every phase and every node is narrated in full: what it is, what it produces, why this project needs it, what it depends on and which beliefs it helps validate.
- Later phases whose nodes are not yet chosen are included, named and described, with what will decide their contents.
- No node duplicates work the overview records as complete.
- Node inputs are produced by an earlier or concurrent node, already exist, or are explicitly external.
- Phases are coherent, with names that say what each accomplishes, and their order puts evidence for the core bet and the riskiest bets early.
- Notable exclusions are explained.
- Every proposed new node meets the full node definition: all eight sections, and every task with an id, name, description and estimation guideline (required information, formula and two worked examples).

## 04 Estimation Discovery

- The planning horizon is stated: which nodes will be planned at task level, which at node level, which phases in outline.
- Every task-level node's Discovery for Planning questions, and the Required Information of each of its tasks, are covered.
- Questions are merged where they overlap and phrased in the client's terms.
- Every question has an answer: a value, or a low and high range with the client's reasoning. "Unknown" is not an answer.
- Answers that contradict earlier deliverables are flagged.

## 05 Project Plan

- The workbook matches the structure in the Analyst's `plan-workbook.md` exactly: its sheets, the Plan sheet's columns in order, and the content of task-level, node-level and phase-level rows.
- Its phases and nodes match the approved scope, including later phases carried as phase-level rows.
- Task-level rows use catalog tasks, adapted to the project's terms, with estimates that follow from the task's estimation guideline and an answered question.
- Node-level and phase-level rows are presented as approximations with ranges, not as commitments.
- Dates respect the client's stated capacity and the dependencies between nodes.
- Priority (Urgent, High, Normal, Low) is sensible: work on the core bet, the leaps of faith and hard deadlines is near the top.
- Tags carry each node's catalog category and the IDs of the beliefs it helps validate.
- Totals on the Summary sheet agree with the rows.

## 06 ClickUp Publication

- What was published matches the approved workbook, and every estimate and date is on a task: one folder per phase, one list per node, one task per task-level row, one task representing each node-level row, and one list with one task representing each phase-level row.
- On a re-run: the previous publication was backed up before anything was deleted, ClickUp-side status, assignees and comments were carried to matching tasks, and only items listed in the previous publication record were deleted.
- The record lists every created item with its ClickUp ID, and anything that failed.
- Nothing was published or deleted before the client reviewed the plan in Excel and authorized the upload.
