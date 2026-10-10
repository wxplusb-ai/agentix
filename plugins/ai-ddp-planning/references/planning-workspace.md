# Planning Workspace

Where AI-AD&D planning documents live and how they are named, versioned and signed off.

## Layout

```
planning/
├── discovery_driven_planning_node_catalog_v2.md
├── client_documents/
└── agent_documents/
```

- `discovery_driven_planning_node_catalog_v2.md`: a copy of the catalog shipped in the plugin (`${CLAUDE_PLUGIN_ROOT}/catalog/`), made at setup. Agents read the copy, so the plan stays tied to the catalog version it was built from.
- `client_documents/`: everything the client provides: briefs, decks, research, data descriptions, architecture notes, completed questionnaires. Agents never edit these.
- `agent_documents/`: everything the agents produce.

## Naming and versioning

Deliverables are numbered by step: `01-project-overview.md`, `02-beliefs-and-bets.md`, `03-project-scope.md`, `04-estimation-discovery.md`, `05-project-plan.xlsx`, `06-clickup-publication.md`.

When the process runs again, write a new version alongside the old one (`03-project-scope-v2.md`) and leave earlier versions in place. The latest version is the one with the highest suffix; a file with no suffix is version 1.

## Frontmatter

Every markdown deliverable starts with:

```yaml
---
project: <project name>
deliverable: <deliverable name>
version: 1
status: draft            # draft | in-review | approved
prepared_by: <agent role>
reviewed_by:             # team-lead, once reviewed
approved_by:             # client name, once approved
approved_on:             # YYYY-MM-DD
---
```

## Sign-off

A deliverable is approved when the client says so explicitly. Record it by setting `status: approved`, `approved_by` and `approved_on`, and by adding a short **Sign-off** section at the end listing any corrections the client made before approving. Silence or a change of subject is not approval.

For `05-project-plan.xlsx`, record the sign-off on the workbook's Summary sheet.
