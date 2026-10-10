---
name: conducting-project-overview
description: Conducts the AI-AD&D Project Overview, the first planning step. Reviews the client's documents, interviews the client across thirteen topics, confirms every catalog category is in play, out of play or unknown, and writes a project overview the client approves. Gathers what node scoping needs, not estimating detail. Use at the start of an AI-AD&D planning engagement, for a new project or one already in progress.
---

# Conducting the Project Overview

Learn enough about the project for the Architect to decide which catalog nodes belong in the plan. This is not an estimating interview: you need to know whether the application needs authentication, not how many roles it has.

The test of success: an Architect reading only your overview could form a first view of the project's nodes, and would not have to come back to the client to decide whether any catalog category applies.

## Checklist

```
- [ ] Client documents reviewed and inventoried
- [ ] Interview planned: topics already answered by documents marked
- [ ] Interview conducted across all thirteen topics
- [ ] Category coverage check: all 20 categories marked
- [ ] Overview drafted from the template
- [ ] Self-check passed
- [ ] Reviewed (Team Lead quality review) and approved by client
```

## 1. Review what the client has provided

Read everything in `planning/client_documents/`. For each document, note what it is and what it tells you against the interview topics. If this is a re-run, also read the latest versions of the earlier deliverables in `planning/agent_documents/`: they are your starting point, and the interview focuses on what has changed and what was learned.

## 2. Plan the interview

Read [interview-topics.md](references/interview-topics.md). Mark the topics the documents already answer, so you confirm those quickly rather than asking the client to repeat themselves. Drop topics the project's nature makes irrelevant: a personal tool needs no questions about billing or user roles. Spend the interview on what is missing.

## 3. Interview

Talk to the client conversationally, a few questions at a time, following their lead where it is productive. Ask follow-up questions when an answer would change which nodes apply. Record their beliefs and risks in their own words: Step 2 depends on them.

For an in-flight project, establish what is complete, what is in progress and what is planned, and what evidence the completed work produced. Completed work is not planned again.

## 4. Check category coverage

Before closing the interview, mark each of the 20 catalog categories:

- **In play:** the application needs work in this category.
- **Out of play:** it clearly does not, with the reason.
- **Unknown:** the client does not know yet. Each unknown becomes a follow-up question or a candidate bet for Step 2.

Use what you have learned to rule categories out without asking about each one. A personal project running on the client's own machine has no need for Identity and Access Management, Usage Metering and Monetization, Product Analytics or a production hosting cluster. An internal tool with no external users needs no payments. Mark these out of play with the reason, and skip their topics in the interview.

Ask only about categories you genuinely cannot mark. When you have ruled several out by inference, list them for the client in one line so they can correct you. This check is what makes the overview sufficient for scoping.

## 5. Write the overview

Use [project-overview-template.md](assets/project-overview-template.md). Save it as `planning/agent_documents/01-project-overview.md` (or the next version) with `status: draft`.

## 6. Self-check

Re-read the overview as the Architect would. Could you decide, for every category, whether it is in scope and roughly why? Does anything rest on your inference rather than the client's words, without being marked as such? If any answer is no, go back to the client or the documents before handing it to review.

## 7. Review and sign-off

Review it against the overview criteria in the Team Lead's quality review, then take it to the client. Ask them to correct and add to it. Record approval as described in the planning workspace reference.
