# Plan Workbook

The structure of `05-project-plan.xlsx`.

## Sheets

1. **Plan:** the plan itself.
2. **Summary:** project details, phase totals and sign-off.
3. **Estimate Basis:** how each estimate was reached.
4. **Bets:** the bets the plan tests and the nodes that test them.

## Plan sheet

Exactly these columns, in this order:

| Column | Task-level row | Node-level row | Phase-level row |
|---|---|---|---|
| Phase | Phase name | Phase name | Phase name |
| Node | Node number and name (with instance, if any) | Node number and name | Blank |
| Task | Adapted task name | Blank | Blank |
| Task Description | Adapted task description | "Approximation: <low> to <high> hours. <basis>" | "Approximation: <low> to <high> hours. <basis>" |
| Estimate (Hours) | Point estimate | Midpoint of the range | Midpoint of the range |
| Start Date | Scheduled start | Tentative start | Approximate start |
| End Date | Scheduled end | Tentative end | Approximate end |
| Priority | Urgent, High, Normal or Low | Urgent, High, Normal or Low | Blank |
| Tags | Category, bet IDs | Category, bet IDs, `tentative` | Bet IDs, `approximate` |

Rows run in schedule order, grouped by phase. Dates use the format `YYYY-MM-DD`. Tags are comma-separated. Category tags use a short lowercase form, for example `knowledge-retrieval-engineering`. No totals rows on this sheet.

## Summary sheet

- Project name, plan version, date prepared.
- Start date, people, hours per week, working days.
- Total estimate: point and range (sum of lows to sum of highs).
- Planning horizon: which nodes are at task level, their total hours, and the end date.
- Phase table: Phase | Detail level | Estimate (Hours) | Range | Start | End | Bets tested.
- Sign-off: approved by, date.

## Estimate Basis sheet

One row per task-level task, node-level node and phase-level phase:

| Column | Content |
|---|---|
| Phase | Phase name |
| Node | Node, if any |
| Task | Task id from the catalog, if any |
| Basis | The guideline or worked example used |
| Inputs | The answers used, with their estimation discovery question numbers |
| Calculation | How the estimate was reached |
| Adjustment | Any adjustment and why |
| Low | Low estimate |
| Point | Point estimate |
| High | High estimate |

Tasks left out as not applicable are listed here with the reason.

## Bets sheet

| Column | Content |
|---|---|
| Rank | Bet rank |
| ID | Bet ID |
| Bet | The bet, short form |
| Tested by | Nodes that test it |
| Phase(s) | Phases containing those nodes |
| Evidence expected by | End date of the last node producing its evidence |
