---
name: conducting-project-overview
description: Conducts the AI-AD&D Project Overview, the first planning step. Reviews the client's documents, interviews the client across the interview topics that apply to the project, and writes a project overview that describes the project as it is today, which the client approves. Gathers a complete picture of the project, not estimating detail, beliefs or plans. Use at the start of an AI-AD&D planning engagement, for a new project or one already in progress.
---

# Conducting the Project Overview

Learn and record what the project IS: its goals, market, users, workflow, data, technology, constraints and current state. This is not a planning step and not an estimating interview. You need to know whether the application has signed-in users, not how many roles it has; you are not deciding what work the project needs.

Beliefs, assumptions and risks are not part of this step. They are the subject of Step 2, Beliefs and Bets. If the client raises one, acknowledge it, note it in your working notes for Step 2, and move on.

The test of success: a reader who has never met the client finishes the overview with a complete, accurate picture of the project as it stands, in the client's terms.

## Checklist

```
- [ ] Client documents reviewed and inventoried
- [ ] Interview planned: relevant topics selected, topics already answered by documents marked
- [ ] Interview conducted across the relevant topics
- [ ] Overview drafted from assets/project-overview-template.md
- [ ] Self-check passed
- [ ] Reviewed (Team Lead quality review) and approved by client
```

## 1. Review what the client has provided

Read everything in `planning/client_documents/`. For each document, note what it is and what it tells you against the interview topics. If this is a re-run, also read the latest versions of the earlier deliverables in `planning/agent_documents/`: they are your starting point, and the interview focuses on what has changed and what was learned.

## 2. Plan the interview

Read [interview-topics.md](references/interview-topics.md). Decide which topics are relevant to this project: not every topic applies in every case. A personal tool running on the client's own machine needs no questions about sign-in, hosting at scale or billing. Mark the topics the documents already answer, so you confirm those quickly rather than asking the client to repeat themselves. Spend the interview on what is missing.

## 3. Interview

Talk to the client conversationally, a few questions at a time, following their lead where it is productive. Ask follow-up questions when an answer is vague enough that a reader could picture the project two different ways.

When you rule a topic out as irrelevant, tell the client in one line so they can correct you.

For an in-flight project, establish what is complete, what is in progress and what is planned, and what the completed work produced and showed.

You have enough when every relevant topic is covered: you can describe what the interview topic asks you to learn, in the client's terms, without guessing. Counts, volumes and sizes for estimating are not needed; they come in Estimation Discovery.

## 4. Write the overview

Use [project-overview-template.md](assets/project-overview-template.md). Save it as `planning/agent_documents/01-project-overview.md` (or the next version) with `status: draft`.

Describe the project, not the plan. The overview contains no catalog categories, node names or node numbers, no beliefs or risks, and no recommendations about what work to do.

## 5. Self-check

Re-read the overview as someone who has never met the client:

- Is every relevant topic covered, and every skipped topic listed with its reason?
- Does anything rest on your inference rather than the client's words or documents, without being marked as such?
- Is there any catalog content, belief, risk or recommendation in it? If so, remove it.

If any answer is wrong, go back to the client or the documents before handing it to review.

## 6. Review and sign-off

Review it against the overview criteria in the Team Lead's quality review, then take it to the client. Ask them to correct and add to it. Record approval as described in the planning workspace reference.
