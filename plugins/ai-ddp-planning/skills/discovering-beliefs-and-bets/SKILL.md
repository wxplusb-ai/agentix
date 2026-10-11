---
name: discovering-beliefs-and-bets
description: Runs the AI-AD&D Beliefs and Bets step as a structured discussion with the client. Walks through the belief areas that apply to the project, starting with the core bet of the whole application; the client articulates their beliefs, each is sharpened into a testable statement and rated for consequence and evidence, and the bets are named and ranked. Writes the Beliefs and Bets document the client approves. Use after the Project Overview is approved and before scoping.
---

# Discovering Beliefs and Bets

This is a conversation, not a drafting exercise. You walk the client through the areas their project rests on, and the client articulates what they believe. Your job is to ask, listen, help sharpen each belief into a testable statement, and agree its ratings with them.

Everything after this step depends on it. The Architect selects nodes that validate the bets, orders phases so the riskiest bets get evidence first, and the Analyst sets priority by them. A missed bet becomes an untested assumption that the plan treats as fact.

Read [discovery-driven-planning.md](${CLAUDE_PLUGIN_ROOT}/references/discovery-driven-planning.md) and [beliefs-and-bets.md](references/beliefs-and-bets.md) before starting.

## Checklist

```
- [ ] Areas selected for this project, skipped areas noted with a reason
- [ ] Core bet articulated and rated
- [ ] Each selected area discussed: beliefs articulated, sharpened, rated
- [ ] Bets named, leaps of faith flagged, bets ranked with the client
- [ ] Beliefs and Bets document written from assets/beliefs-and-bets-template.md
- [ ] Self-check passed
- [ ] Reviewed and approved by client
```

## 1. Select the areas

From the approved `01-project-overview.md`, decide which areas in the Areas table of [beliefs-and-bets.md](references/beliefs-and-bets.md) apply to this project. Every project has a core bet. A personal tool has no beliefs about willingness to pay; an internal tool may have none about alternatives. Tell the client which areas you will cover and which you are skipping, and why, so they can add one back.

On a re-run, read the previous `02-beliefs-and-bets.md` first. The discussion then starts from those beliefs: what has been learned, which are confirmed, refuted or reshaped, and what is new.

## 2. Start with the core bet

Ask the client to state, in one sentence, what the whole application is staking its existence on: the proposition that, if false, makes everything else pointless. Help them sharpen it until it names the outcome, for whom, and the threshold that would count as success. Rate it with them like any other belief. It is almost always a bet.

## 3. Walk through the areas

Take the selected areas one at a time, in whatever order follows the conversation.

- Open the area with a question in the client's terms, not the area's name. "What has to be true about your data for this to work?" rather than "Let's discuss data beliefs."
- Let the client articulate their beliefs. Use the prompts in [beliefs-and-bets.md](references/beliefs-and-bets.md) to draw out the ones they hold without noticing, and use what the overview says about the project.
- Help sharpen each into a testable statement. Propose wording; the client decides.
- Agree how consequential it is if wrong (High, Medium, Low) and how much evidence supports it (Strong, Some, None). Name the evidence for anything rated Strong or Some. The client's ratings stand: if you disagree, say why once, then record theirs.
- Separate knowledge from belief as you go: a statement the client can back with evidence is knowledge, and is recorded as such.

Keep it a few questions at a time. Summarize each area's beliefs back to the client before moving on.

## 4. Name and rank the bets

- A bet is a belief rated High consequence with Some or None evidence.
- A bet with None evidence is a leap of faith.
- Rank the bets with the client: leaps of faith first; within a group, the ones whose failure would change the most of the project first.

Beliefs that are not bets stay in the document. They may become bets as the project learns more.

Do not design tests here. Each bet will be validated through catalog nodes the Architect selects at scoping, and a bet may need several nodes or whole phases. If no node in the catalog can validate a belief, the Architect proposes a new node. Record what would confirm and what would refute each bet, because that is what the Architect needs.

## 5. Write the document

Use [beliefs-and-bets-template.md](assets/beliefs-and-bets-template.md). Save it as `planning/agent_documents/02-beliefs-and-bets.md` (or the next version) with `status: draft`. Give each belief an ID (B01, B02 and so on); the core bet is B00. IDs are stable across versions so tags in the plan stay meaningful.

On a re-run, carry forward every belief from the previous version with its status updated (Open, Confirmed, Refuted, Reshaped) and the evidence that changed it.

## 6. Self-check

- Could someone tell from each statement's wording alone what evidence would confirm or refute it?
- Is the core bet stated, and is it the first-ranked bet or explained if not?
- Are there beliefs about customers and money, where those areas apply, not only technology?
- Would the ranking hold if the client asked why one bet is above another?

If not, go back to the client before review.

## 7. Review and sign-off

Review against the Beliefs and Bets criteria in the Team Lead's quality review, then take it to the client for approval. Scoping does not start until it is approved.
