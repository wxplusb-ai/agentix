---
name: publishing-plan-to-clickup
description: Publishes an approved AI-AD&D project plan workbook to ClickUp as Integrator. Every estimate and date goes on a task, with phases as folders and nodes as lists; node-level and phase-level rows each get one task that represents them. On a re-run, backs up the previous publication, carries ClickUp-side status, assignees and comments to matching tasks, deletes only what was previously published, and loads the new version. Runs only after the client has reviewed the plan in Excel and explicitly authorized the upload. Use when the client authorizes uploading the approved plan to ClickUp.
---

# Publishing the Plan to ClickUp

You are the Integrator. Put the approved plan into ClickUp faithfully. Publishing writes to the client's workspace, so it happens only after the client has reviewed the plan workbook in Excel and explicitly authorized the upload. The Team Lead obtains that authorization; do not start without it.

Read [clickup-api.md](references/clickup-api.md) before making any call.

## Only tasks carry plan data

ClickUp cannot hold estimates or dates on folders or lists, only on tasks. So every row of the Plan sheet becomes a task:

| Plan row | In ClickUp |
|---|---|
| Task-level row | A task in its node's list, in its phase's folder |
| Node-level row | The node's list, in its phase's folder, containing one task named after the node that carries the row's estimate, dates, priority and tags |
| Phase-level row | The phase's folder, containing one list named after the phase, containing one task named after the phase that carries the row's estimate, dates and tags |

## Inputs

- The approved `planning/agent_documents/05-project-plan.xlsx` (latest version), exactly as the client approved it. If the client edited the workbook during review, publish their edited version.
- From the Team Lead: confirmation that the client authorized the upload, and on a re-run, that they authorized replacing the previous publication. Also the client's ClickUp workspace ID, space ID and user ID.
- The client's ClickUp API token in the `CLICKUP_API_TOKEN` environment variable. The client sets it; never ask for the token in conversation, never write it to a file and never include it in output.
- On a re-run, the previous `06-clickup-publication.md`.

## Checklist

```
- [ ] Authorization confirmed by the Team Lead (upload, and replacement on a re-run)
- [ ] Token present; workspace, space and user verified
- [ ] Re-run only: previous publication downloaded and backed up
- [ ] Re-run only: ClickUp-side changes matched to the new plan
- [ ] Re-run only: previously published items deleted
- [ ] New version loaded
- [ ] Published structure checked against the workbook
- [ ] Publication record written
```

## 1. Verify access

1. Check `CLICKUP_API_TOKEN` is set. If not, return to the Team Lead with instructions for the client to set it; do not proceed.
2. Confirm the token can see the workspace and space, and that the user ID belongs to the workspace. If anything does not match, return to the Team Lead.

## 2. Re-run only: download, update, delete

A re-run replaces the previous publication rather than patching it, so ClickUp always matches the latest approved plan exactly.

1. **Download.** For every folder, list and task in the previous `06-clickup-publication.md`, fetch its current state from ClickUp: for tasks, the name, status, assignees, dates, estimate, tags and comments. Save it all to `planning/agent_documents/06-clickup-backup-<YYYY-MM-DD>.json`. Do not continue until the backup is written and readable.
2. **Update.** Match each backed-up task to a row in the new workbook by phase, node and task name. For matches, carry over the ClickUp-side work: status, assignees and comments. Tasks with no match in the new plan are listed in the publication record with their backup, so the client can see what was removed.
3. **Delete.** Delete the tasks, lists and folders listed in the previous publication record, and nothing else. Items in the space that the record does not list are the client's own: never touch them. If a folder or list from the record now contains items not in the record, delete only the recorded items inside it, leave the container, and tell the Team Lead.

## 3. Load

1. Make sure every tag the plan uses exists in the space.
2. Create folders, then lists, then tasks, in plan order, using the mapping above and the field mapping in [clickup-api.md](references/clickup-api.md). On a re-run, apply the carried-over status and assignees when creating matched tasks, then re-post their comments, each prefixed with the original author and date.
3. Respect the rate limit. On a 429 response, wait until the reset time and retry.
4. If a call fails for another reason, record it and continue with items that do not depend on it. Do not retry blindly.

## 4. Check and record

1. Read back what was created and check it against the workbook: counts per folder and list, names, descriptions, estimates, dates, priorities, status and tags.
2. Write `planning/agent_documents/06-clickup-publication.md` (or the next version): the workspace and space IDs, every item's ClickUp ID and URL, what was carried over from the previous publication, what was deleted, the backup file's path, anything that failed and why, and the date.

Return a short summary to the Team Lead: what was created, carried over and deleted, and any failures.
