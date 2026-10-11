# ClickUp API

The parts of the ClickUp API v2 the Integrator uses, and how the plan maps onto ClickUp. Make calls with `curl` from the shell. Check the current documentation at https://developer.clickup.com/reference if a call behaves differently from what is described here.

## Contents

- Authentication
- Endpoints
- Mapping the plan
- Re-runs: backup and replace
- Rate limits and errors

## Authentication

Every request carries the personal token in the `Authorization` header, with no `Bearer` prefix:

```bash
curl -s https://api.clickup.com/api/v2/team \
  -H "Authorization: $CLICKUP_API_TOKEN"
```

Read the token from `CLICKUP_API_TOKEN`. Never echo it, log it or write it to a file.

## Endpoints

Base URL: `https://api.clickup.com/api/v2`

| Purpose | Method and path | Body |
|---|---|---|
| List workspaces | `GET /team` | |
| List spaces | `GET /team/{team_id}/space` | |
| List folders | `GET /space/{space_id}/folder` | |
| Create folder | `POST /space/{space_id}/folder` | `{"name": "..."}` |
| List lists in a folder | `GET /folder/{folder_id}/list` | |
| Create list | `POST /folder/{folder_id}/list` | `{"name": "...", "content": "..."}` |
| List tasks in a list | `GET /list/{list_id}/task` | Paged: add `?page=0`, `1` and so on until fewer than 100 are returned |
| Get task | `GET /task/{task_id}` | |
| Create task | `POST /list/{list_id}/task` | See Mapping the plan |
| Delete task | `DELETE /task/{task_id}` | |
| Delete list | `DELETE /list/{list_id}` | |
| Delete folder | `DELETE /folder/{folder_id}` | |
| List task comments | `GET /task/{task_id}/comment` | |
| Create task comment | `POST /task/{task_id}/comment` | `{"comment_text": "..."}` |
| List space tags | `GET /space/{space_id}/tag` | |
| Create space tag | `POST /space/{space_id}/tag` | `{"tag": {"name": "..."}}` |

Send JSON bodies with `-H "Content-Type: application/json"`.

## Mapping the plan

| Plan | ClickUp |
|---|---|
| Phase | Folder |
| Node | List, in its phase's folder |
| Task | Task name (`name`) |
| Task Description | Description content (`markdown_content`; see the note below) |
| (none) | Status (`status`): `Open`, or the carried-over status on a re-run |
| (none) | Assignees (`assignees`): the carried-over user IDs on a re-run; omit otherwise |
| Estimate (Hours) | Time estimate (`time_estimate`), in milliseconds: hours x 3,600,000 |
| Start Date | Start date (`start_date`), a Unix timestamp in milliseconds, with `start_date_time` set to `false` |
| End Date | Due date (`due_date`), a Unix timestamp in milliseconds, with `due_date_time` set to `false` |
| Priority | Priority (`priority`): `1` Urgent, `2` High, `3` Normal, `4` Low; omit when blank |
| Tags | Tags (`tags`): the Tags column split on commas |

Notes:

- **Description field.** The documentation names the field `markdown_content`, but its example uses `markdown_description`. Check on the first task which key the workspace accepts.
- **Status.** If the list has no status called `Open`, stop and tell the Team Lead rather than choosing another status. On a re-run, if a carried-over status does not exist in the new list, use `Open` and record the original status in the publication record.
- **Tags.** Make sure each tag exists in the space before creating tasks that use it: list the space tags and create any that are missing.
- **Rows without a task.** Only tasks carry estimates and dates. A node-level row has no Task: create its list and one task named after the node. A phase-level row has no Node or Task: create its folder, one list named after the phase, and one task named after the phase. These tasks carry the row's description, estimate, dates, priority and tags like any other.

## Re-runs: backup and replace

A re-run never patches the previous publication. It backs it up, deletes it and loads the new plan, as the skill describes.

- The previous `06-clickup-publication.md` is the only list of what may be deleted. Never delete folders, lists or tasks it does not list: they may be the client's own.
- Back up with `GET /task/{task_id}` and `GET /task/{task_id}/comment` for every recorded task, before any delete.
- Delete tasks first, then lists, then folders. Before deleting a list or folder, check it contains nothing outside the record.
- The backup file is the record of what was deleted; keep it with the publication record.

## Rate limits and errors

Limits are per token, by the plan of the workspace: 100 requests per minute on Free Forever, Unlimited and Business; 1,000 on Business Plus; 10,000 on Enterprise. When exceeded, the API returns HTTP 429 with `X-RateLimit-Reset` (a Unix timestamp). Wait until then and retry.

Any other 4xx response means the request is wrong: record the response body and do not retry unchanged. A 5xx response may be retried once after a short wait.
