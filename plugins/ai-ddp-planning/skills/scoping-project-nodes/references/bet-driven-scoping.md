# Bet-Driven Scoping

How to reason from bets to the nodes and phases that validate them, how to shape and order phases, and how to propose a new catalog node.

## Contents

- From a bet to the nodes that validate it
- Shaping phases
- Proposing a new node

## From a bet to the nodes that validate it

For each bet, starting with the core bet, ask:

1. **What result would confirm it?** Beliefs and Bets records this: an accuracy figure on real data, a share of interviewed users reporting the problem, a measured cost per task.
2. **What result would refute it?** Also recorded in Beliefs and Bets.
3. **What work produces that result?** Search the catalog's Outputs and Assumptions Validated sections for nodes that produce the evidence. Prefer the work that answers decisively with the least effort.

The answer is rarely a single node. "The model can answer from our documents" may need a domain knowledge corpus, a benchmark evaluation dataset and a feasibility spike working together. A bet about user trust in autonomous actions may need a thin working slice of the application in front of real users, spread across more than one phase. And one node may contribute evidence to several bets. Judge the combination; do not map one bet to one node.

### Cheap before expensive

Many bets can be validated by discovery nodes long before the production nodes that depend on them. The Product Strategy nodes (1.3 AI Feasibility Spike, 1.4 Customer Problem Validation, 1.5 Alternatives Landscape Analysis, 1.6 Solution Concept Validation, 1.7 Business Viability Assessment) exist for exactly this. A refuted bet discovered by a two-week spike costs far less than one discovered after building the production retriever.

### Some bets need building to validate

Some bets can only be validated with a working slice of the application. In that case, include the nodes that slice needs, kept as thin as the validation allows, and let later phases harden them.

## Shaping phases

A phase is a collection of nodes that a person running the project would recognize as a coherent stretch of work. Common shapes:

- **A validation phase:** the nodes that together produce the evidence for one or more related bets, ending when the evidence is in. Example: "Prove extraction accuracy".
- **A body-of-work phase:** nodes that together build a capability. Example: "Data Acquisition".
- **A hardening or release phase:** nodes that take a validated slice to production.

A bet may be validated lightly in an early phase and fully later, or need nodes from a body-of-work phase. Record which beliefs each node helps validate; the plan carries those belief IDs as tags so the work behind a bet can be followed across phases.

### Later phases without nodes

Beyond the planning horizon, a phase's contents often depend on what earlier phases learn. A later phase is still part of the scope: give it a name, describe what it is expected to accomplish, say what will decide its contents (for example, "if the feasibility spike shows a single agent is enough, this phase hardens it; if not, it introduces orchestration"), and list the likely candidate nodes. The plan carries it as a phase-level row with an approximate range.

### Ordering

Order phases so that:

- The core bet and the leaps of faith get evidence first.
- A phase does not start before the phases producing its inputs.
- Expensive, hard-to-reverse work comes after the bets it depends on have evidence.

Where these pull against each other, explain the trade-off you chose.

## Proposing a new node

If nothing in the catalog, alone or in combination, can produce the evidence a belief needs, or the application needs work the catalog does not describe, propose a new node. Do not force an ill-fitting node. A proposal must meet the full definition of a catalog node, so it can be estimated and planned like any other and added to the catalog if approved.

### Node definition

Give the proposed node a name and the category it belongs to, and the reason it is proposed (the belief it validates, or the need it meets). Then all eight sections:

1. **Overview:** a description of the overall asset the node represents.
2. **Prerequisites:** the conditions that must be true before work starts.
3. **Inputs:** the required input assets, each with its type.
4. **Outputs:** the assets produced by the node, each with its type.
5. **Tasks:** the tasks required to produce the node (see Task definition).
6. **Discovery for Planning:** the information the tasks' estimation guidelines need, as questions.
7. **Best Practices:** recommendations from practitioners and published sources.
8. **Assumptions Validated:** the assumptions the outcome confirms or rejects.

### Task definition

Every task in the proposed node must have:

1. **id:** a `snake_case_id`.
2. **name:** a human-readable name.
3. **Description:** what the task does.
4. **Estimation Guideline:**
   1. *Required Information:* what information is required to estimate it.
   2. *Formula:* the formula for estimating the task in hours.
   3. *Example 1* and *Example 2:* two worked example estimates.

Follow the format of existing nodes in the catalog: read one or two nearby nodes in the same category before writing.

The Team Lead reviews proposals and puts them to the client with the scope. Approved proposals are planned like any other node and are candidates for addition to the catalog.
