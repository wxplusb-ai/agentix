---
name: mapping-beliefs-and-bets
description: Runs the AI-AD&D Beliefs and Bets step with the client. Surfaces the beliefs the project rests on, turns each into a testable statement, rates its consequence and evidence with the client, names and ranks the bets (consequential beliefs with little evidence) and writes the register the client approves. Use after the Project Overview is approved and before scoping, because scope, ordering and priority all follow from the bets.
---

# Mapping Beliefs and Bets

Everything after this step depends on it. The Architect scopes nodes to test the bets, orders phases so the riskiest are tested first, and the Analyst sets priority by them. A missed bet becomes an untested assumption that the plan treats as fact.

Read [discovery-driven-planning.md](${CLAUDE_PLUGIN_ROOT}/references/discovery-driven-planning.md) and [beliefs-and-bets.md](references/beliefs-and-bets.md) before starting.

## Checklist

```
- [ ] Draft beliefs prepared from the approved overview
- [ ] Session held: beliefs added, merged, reworded, rated with the client
- [ ] Bets named, leaps of faith flagged, bets ranked
- [ ] Register written from the template
- [ ] Self-check passed
- [ ] Reviewed and approved by client
```

## 1. Prepare a draft

From the approved `01-project-overview.md`, especially its beliefs and risks, its unknown categories and its current state, draft the beliefs the project rests on. Cover the whole venture: customers and their problem, value and willingness to pay, data availability and quality, model capability, cost per task, user trust and adoption, operations, safety and compliance. Many beliefs are implicit; [beliefs-and-bets.md](references/beliefs-and-bets.md) describes how to find them.

Write each as a testable statement: it must be clear what evidence would confirm or refute it.

## 2. Work through them with the client

Present the draft and work through it together:

- Ask the client to add beliefs you missed, and to merge or reword yours.
- For each belief, agree how consequential it is if wrong (High, Medium, Low) and how much evidence supports it (Strong, Some, None). Name the evidence for anything rated Strong or Some.
- The client's ratings stand. If you disagree, say why once, then record theirs.

## 3. Name and rank the bets

- A bet is a belief rated High consequence with Some or None evidence.
- A bet with None evidence is a leap of faith.
- Rank the bets: leaps of faith first; within a group, the ones whose failure would change the most of the plan first. Confirm the ranking with the client.

Beliefs that are not bets stay in the register. They may become bets as the project learns more.

## 4. Write the register

Use [beliefs-and-bets-register-template.md](assets/beliefs-and-bets-register-template.md). Save it as `planning/agent_documents/02-beliefs-and-bets.md` (or the next version) with `status: draft`. Give each belief an ID (B01, B02 and so on); IDs are stable across versions so tags in the plan stay meaningful.

On a re-run, carry forward every belief from the previous version with its status updated (Open, Confirmed, Refuted, Reshaped) and the evidence that changed it.

## 5. Self-check

- Could someone design a test for every belief from its wording alone?
- Are there beliefs about customers and money, not only technology?
- Would the ranking hold if the client asked why one bet is above another?

If not, revise before review.

## 6. Review and sign-off

Review against the Beliefs and Bets criteria in the Team Lead's quality review, then take it to the client for approval. Scope does not start until it is approved.
