# Bet-Driven Scoping

How to reason from bets to nodes, shape phases around experiments and bodies of work, and propose new catalog nodes.

## From a bet to the nodes that test it

For each bet, ask three questions:

1. **What result would confirm it?** Name the observable outcome: an accuracy figure on real data, a share of interviewed users reporting the problem, a measured cost per task.
2. **What result would refute it?** The opposite outcome, or a threshold the client agreed would make them change course.
3. **What is the smallest set of nodes that produces that result?** Search the catalog's Outputs and Assumptions Validated sections for nodes that produce the evidence. Prefer the set that answers decisively with the least effort.

That smallest set is the experiment. It may be one node (an AI Feasibility Spike for a model capability bet) or several working together (a Raw Domain Knowledge Corpus, a Golden Benchmark Evaluation Dataset and a Feasibility Spike for "the model can answer from our documents").

### Cheap before expensive

Many bets can be tested by a discovery node long before the production node that depends on them. Product Strategy nodes (1.3 AI Feasibility Spike, 1.4 Customer Problem Validation, 1.5 Alternatives Landscape Analysis, 1.6 Solution Concept Validation, 1.7 Business Viability Assessment) exist for exactly this. A refuted bet discovered by a two-week spike costs far less than one discovered after building the production retriever.

### Some bets need building to test

Some bets can only be tested with a working slice: user trust in autonomous actions, for example, may need a minimal agent with human review in front of real users. In that case the experiment includes the nodes needed for that slice, kept as thin as the test allows, and later phases harden them.

## Shaping phases

A phase is a collection of nodes that a person running the project would recognize as a coherent stretch of work. Common shapes:

- **An experiment phase:** the nodes that test one or more related bets, ending when the evidence is in. Example: "Prove extraction accuracy".
- **A body-of-work phase:** nodes that together build a capability. Example: "Data Acquisition".
- **A hardening or release phase:** nodes that take a validated slice to production.

Experiments motivate the organization but are not required to map one-to-one onto phases. A bet might be tested lightly in an early phase and fully later; an experiment might need nodes from a body-of-work phase. Record which bets each node tests; the plan will carry those bet IDs as tags so an experiment can be followed across phases.

### Ordering

Order phases so that:

- Leaps of faith get evidence first.
- A phase does not start before the phases producing its inputs.
- Expensive, hard-to-reverse work comes after the bets it depends on have evidence.

Where these pull against each other, explain the trade-off you chose.

## When the catalog has no node for a bet

If no node, or combination of nodes, can produce the evidence a bet needs, the catalog has a gap. Do not force an ill-fitting node. Propose a new node with:

- **Name** and the category it would belong to.
- **Overview:** what it produces.
- **Bet it tests:** the bet ID and the result it would produce.
- **Inputs and outputs.**
- **Rough tasks:** names and one-line descriptions.

The Team Lead reviews proposals and puts them to the client with the scope. Approved proposals are planned like any other node and are candidates for addition to the catalog.
