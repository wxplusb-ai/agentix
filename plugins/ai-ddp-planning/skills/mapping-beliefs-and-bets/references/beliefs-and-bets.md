# Beliefs and Bets

How to surface the beliefs an AI application rests on, tell them from knowledge, judge them, and recognize the bets.

## Finding beliefs people do not know they hold

Clients state some beliefs outright ("users will pay for this"). Most are buried in plans, numbers and enthusiasm. Ways to surface them:

- **Read every number as a belief.** "We'll save analysts 10 hours a week" contains beliefs about the current time spent, the share the application can take on, and analysts' willingness to use it.
- **Ask what must be true.** For the outcome the client described, ask what would have to be true for it to happen, then ask the same of each answer.
- **Look for "obviously" and "of course".** These mark beliefs the client has stopped noticing.
- **Walk the workflow.** At each step the application performs, there is a belief that it can do that step well enough, often enough, cheaply enough.
- **Walk the money.** Who pays, how much, how often, and what it costs to serve them. Each link is a belief.
- **Use the unknown categories.** Every category the overview marked unknown hides at least one belief.
- **Use the catalog.** The Assumptions Validated sections of the nodes likely to apply list assumptions that projects like this commonly rest on. Use them as prompts, not as a list to copy.

## Areas to cover

| Area | Typical beliefs |
|---|---|
| Customer problem | The problem exists, is frequent and costly, for an identifiable group |
| Value | Solving it is worth paying for, or saves enough to matter |
| Alternatives | Existing alternatives, including general chat assistants, do not already solve it well enough |
| Data | The data needed exists, is accessible, and is good enough |
| Model capability | A model can perform the task to the required quality |
| Cost | Inference cost per task fits inside what the value supports |
| Trust and adoption | Users will trust the output enough to change how they work |
| Autonomy | The application can act without a person in the loop where intended |
| Operations | The client can run, monitor and support it once live |
| Safety and compliance | It can meet regulatory, privacy and security obligations |

## Belief or knowledge?

A statement is knowledge only if the client can point to evidence: data, interview results, a working prototype, contracts, measured results. Opinion, experience elsewhere, an analyst report about the market in general, or a demo on hand-picked examples is not evidence for this project. When in doubt, it is a belief.

## Writing a testable statement

A testable statement names what is believed, about whom or what, with a threshold that evidence can meet or miss.

- Weak: "The model will be accurate."
- Testable: "A current frontier model extracts the required fields from our supplier invoices with at least 95% field-level accuracy."
- Weak: "Customers want this."
- Testable: "At least 6 of 10 interviewed operations managers report spending more than 5 hours a week on manual invoice reconciliation."

Thresholds are proposals; the client sets them.

## Judging consequence

Ask: if this turns out to be false, what happens to the project?

- **High:** the project fails, or must change its customer, value proposition or core approach.
- **Medium:** a significant part of the plan changes, but the venture survives.
- **Low:** a local adjustment.

## Judging evidence

- **Strong:** direct evidence from this project's own customers, data or prototypes.
- **Some:** indirect or partial evidence: a few interviews, a small trial, a comparable product's results.
- **None:** belief only.

## Recognizing the bets

A bet is a High-consequence belief with Some or None evidence. A bet with None evidence is a leap of faith: the project is staking everything on something nobody has checked. These are what discovery-driven planning exists to test first, at the lowest cost that gives a decisive answer.
