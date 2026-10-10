# Planning Hierarchy and Catalog

The structure of an AI-AD&D plan, the process that produces it, and how to use the node catalog.

## Plan hierarchy

- **Phase:** a collection of nodes, defined for the project and named for what it accomplishes. It may be an experiment ("Prove extraction accuracy"), a body of work ("Data Acquisition") or whatever grouping makes sense for the project. It does not have to match a catalog category.
- **Node:** a node from the catalog. A node that repeats per instance is named `<Node name>: <instance>`, for example `System Instruction Prompt Library: Intake agent`.
- **Task:** a task from the node in the catalog, adapted to the project's context and terminology. If the client uses Dagster, a task about orchestration says Dagster.

## Process

| Step | Owner | Deliverable |
|---|---|---|
| Setup and context | Team Lead | `planning/` folder with the catalog |
| 1. Project Overview | Team Lead | `01-project-overview.md` |
| 2. Beliefs and Bets | Team Lead | `02-beliefs-and-bets.md` |
| 3. Project Scope | Architect | `03-project-scope.md` |
| 4. Estimation Discovery | Analyst prepares, Team Lead conducts | `04-estimation-discovery.md` |
| 5. Project Plan | Analyst | `05-project-plan.xlsx` |
| 6. Publish | Integrator | `06-clickup-publication.md` |

Each step after Setup has a gate. Steps 1, 2, 3 and 5 need client sign-off. Step 4 is complete when every question has an answer. Step 6 starts only when the client has reviewed the plan in Excel and explicitly authorized the upload to ClickUp. No step starts before the previous gate is passed.

The process is the same for a new project and an in-flight one.

## The node catalog

The catalog (`planning/discovery_driven_planning_node_catalog_v2.md`) is the source of truth for what work exists and how to plan it. It has 20 categories and 71 nodes. Do not restate it in deliverables; refer to nodes by number and name.

Each node has eight sections:

| Section | Use it for |
|---|---|
| 1. Overview | What the node produces; whether it fits the project |
| 2. Prerequisites | What must be true before it starts |
| 3. Inputs | Artifacts it consumes, which link it to the nodes that produce them |
| 4. Outputs | Artifacts it produces |
| 5. Tasks | Each task's id, name, description and estimation guideline (required information, formula, two worked examples) |
| 6. Discovery for Planning | The questions that must be answered before the node can be estimated |
| 7. Best Practices | Guidance for doing the work well |
| 8. Assumptions Validated | The assumptions the node confirms or rejects; the link between nodes and bets |

### Reading the catalog

The catalog is over 3,600 lines. Do not read it whole. Search for the heading you need and read from there:

- Categories: lines starting `## Category`
- Nodes: lines starting `### Node` (for example `### Node 6.4:`)
- A section within a node: read the node from its heading to the next `### Node` heading, or search for the section heading after it

To survey the catalog, list the `## Category` and `### Node` headings, and read section 1 of each node that might apply.
