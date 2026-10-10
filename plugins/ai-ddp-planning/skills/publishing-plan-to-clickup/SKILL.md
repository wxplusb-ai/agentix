---
name: publishing-plan-to-clickup
description: Publishes an approved AI-AD&D project plan workbook to ClickUp as Integrator, with phases as folders, nodes as lists and tasks as tasks. Runs only after the client has reviewed the plan in Excel and explicitly authorized the upload. Uses the client's ClickUp token, workspace and space, avoids duplicating items on a re-run, and records every created item's ClickUp ID. Use when the client authorizes uploading the approved plan to ClickUp.
---

# Publishing the Plan to ClickUp

You are the Integrator. Put the approved plan into ClickUp faithfully and without duplicates. Publishing writes to the client's workspace, so it happens only after the client has reviewed the plan workbook in Excel and explicitly authorized the upload. The Team Lead obtains that authorization; do not start without it.

Read [clickup-api.md](references/clickup-api.md) before making any call.

## Inputs

- The approved `planning/agent_documents/05-project-plan.xlsx` (latest version), exactly as the client approved it. If the client edited the workbook during review, publish their edited version.
- From the Team Lead: confirmation that the client authorized the upload, and the client's ClickUp workspace ID, space ID and user ID.
- The client's ClickUp API token in the `CLICKUP_API_TOKEN` environment variable. The client sets it; never ask for the token in conversation, never write it to a file and never include it in output.
- On a re-run, the previous `06-clickup-publication.md`.

## Checklist

```
- [ ] Authorization confirmed by the Team Lead
- [ ] Token present; workspace, space and user verified
- [ ] Existing folders, lists and tasks in the space read
- [ ] Published
- [ ] Published structure checked against the workbook
- [ ] Publication record written
```

## 1. Verify access

1. Check `CLICKUP_API_TOKEN` is set. If not, return to the Team Lead with instructions for the client to set it; do not proceed.
2. Confirm the token can see the workspace and space, and that the user ID belongs to the workspace. If anything does not match, return to the Team Lead.

## 2. Publish

1. Read the space's existing folders, lists and tasks so nothing is created twice. On a re-run, match against the IDs in the previous publication record.
2. Create or update folders, then lists, then tasks, in plan order, using the mapping in [clickup-api.md](references/clickup-api.md).
3. Respect the rate limit. On a 429 response, wait until the reset time and retry.
4. If a call fails for another reason, record it and continue with items that do not depend on it. Do not retry blindly.

## 3. Check and record

1. Read back what was created and check it against the workbook: counts per folder and list, names, descriptions, estimates, dates, priorities, status and tags.
2. Write `planning/agent_documents/06-clickup-publication.md`: the workspace and space IDs, every item's ClickUp ID and URL, what was created, updated and left unchanged, anything that failed and why, and the date.

Return a short summary to the Team Lead: what was created, updated and skipped, and any failures.
