---
name: conducting-estimation-discovery
description: Runs AI-AD&D Estimation Discovery, the step between the approved project scope and the project plan. The Analyst sets the planning horizon and builds the questions from each in-scope node's Discovery for Planning section and its tasks' required information; the Team Lead puts them to the client in a session or questionnaire; the Analyst checks every question has an answer. Use after the project scope is approved. Planning does not start until every question is answered.
---

# Conducting Estimation Discovery

Planning cannot rest on guesses. This step gathers every answer the estimates and schedule depend on, using what the catalog says each node needs. It has two roles:

- **Analyst** (subagent): sets the planning horizon, prepares the questions, checks the answers.
- **Team Lead** (main session): conducts the session or sends the questionnaire and records the answers.

Read [rolling-wave-planning.md](${CLAUDE_PLUGIN_ROOT}/references/rolling-wave-planning.md), [planning-hierarchy-and-catalog.md](${CLAUDE_PLUGIN_ROOT}/references/planning-hierarchy-and-catalog.md) and [estimation-discovery-session.md](references/estimation-discovery-session.md).

## Checklist

```
- [ ] Analyst: planning horizon set
- [ ] Analyst: questions drafted, merged and phrased for the client
- [ ] Analyst: session or questionnaire recommended
- [ ] Team Lead: questions put to the client, answers recorded
- [ ] Analyst: every answer checked; gaps returned and resolved
```

## Analyst: prepare

1. **Set the planning horizon.** From the approved `03-project-scope.md`, decide which nodes will be planned at task level (the current nodes, and perhaps the next), which at node level, and which phases only in outline. The horizon reaches as far as the project can see with confidence; usually the first phase, sometimes into the second. State your reasoning.
2. **Collect the questions.**
    - For each task-level node: every question in its Discovery for Planning section, and the Required Information in each of its tasks' estimation guidelines.
    - For each node-level node: the questions needed to judge whether it is closer to the small or the large worked example in its tasks' guidelines.
    - Phase-level work needs no questions; it is approximated from scope.
    - For scheduling: the start date, who will do the work, hours per week available, working days, and any known waits (recruiting, procurement, data access approvals, client review time).
3. **Shape the questions.** Merge questions that ask the same thing across nodes. Phrase each in the client's terms, as something they can observe or count ("How many different document types will the application read?"), not in catalog variables. Note which nodes and tasks each answer feeds.
4. **Leave out what is already known.** If the Project Overview, Beliefs and Bets or client documents already answer a question, record the answer and its source instead of asking again.
5. **Recommend a format.** A written questionnaire suits factual, countable questions the client can look up. A live session suits questions that need discussion, judgment or several people. Mixed is fine.
6. Write `planning/agent_documents/04-estimation-discovery.md` from [estimation-discovery-template.md](assets/estimation-discovery-template.md), with the answers column empty except for questions already answered. Return its path to the Team Lead.

## Team Lead: conduct

1. Review the questions against the Estimation Discovery criteria in the quality review.
2. Run the session or send the questionnaire as recommended. In a session, follow [estimation-discovery-session.md](references/estimation-discovery-session.md). A completed questionnaire goes in `planning/client_documents/`.
3. Record every answer in `04-estimation-discovery.md` with its source. When the client is unsure, get a low and high value and their reasoning rather than accepting "don't know".
4. Note anything the client says that changes an earlier deliverable.
5. Send the document back to the Analyst.

## Analyst: check

Check every question has a usable answer: a value, or a low and high range with reasoning. Check that answers are consistent with each other and with the earlier deliverables. Return any gaps or contradictions to the Team Lead as specific follow-up questions. Repeat until none remain, then mark the document complete and tell the Team Lead planning can begin.
