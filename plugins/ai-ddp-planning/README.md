# AI-DDP Planning

AI-DDP Planning is a Claude Code plugin that plans AI application projects the way an experienced consulting team would. You describe your project; a team of four agents interviews you, identifies the assumptions your project depends on, selects the work it needs from a catalog of AI engineering practice, estimates that work, and delivers a project plan as an Excel workbook. When you approve the plan, the team publishes it to ClickUp.

The plugin implements the AI Application Discovery and Development (AI-AD&D) planning framework. It works for a project that has not started and for one already under way.

## Why plan this way

Most project plans assume the work is understood before it begins. AI applications rarely allow that. Whether a model can perform the task, whether the data is good enough, and whether users will trust the result are usually unknown at the start, and a plan that treats them as settled fails when they turn out to be wrong.

AI-DDP Planning combines three established techniques to deal with this:

- **Discovery-driven planning** (McGrath and MacMillan) treats the plan as a way to learn. It identifies the beliefs the project rests on, singles out the consequential ones that have little evidence behind them, and schedules the work that tests those first, before money is committed to work that depends on them.
- **Rolling-wave planning** plans near-term work in detail and later work in outline. As the project learns, the next stretch is planned in detail.
- **A node catalog** of 71 units of AI engineering work across 20 categories, from a feasibility spike to a production retriever to a human review portal. Each node defines what it produces, what it needs, how to estimate its tasks, and which questions must be answered before it can be estimated. The plan is assembled from these nodes, so estimates rest on defined work rather than intuition.

## How the team works

The plugin provides four agents, modeled on a consulting engagement.

| Agent | Responsibility |
|---|---|
| **Team Lead** | Owns your relationship with the team, the overall scope and the quality of every deliverable. Conducts the interviews, reviews each deliverable before you see it, and asks for your approval at every step. This is the only agent that talks to you. |
| **Architect** | Converts what the team has learned into a scope: the catalog nodes your project needs, organized into phases. |
| **Analyst** | Prepares the estimation questions, then estimates the work and builds the plan workbook. |
| **Integrator** | Publishes the approved plan to ClickUp. |

The engagement runs in six steps. Each step produces a document in your repository, and the team does not move on until you have approved it.

1. **Project Overview.** The Team Lead reads any documents you provide and interviews you about your goals, market, users, workflow, data, technology, constraints and current progress. The interview adapts to your project: a personal tool running on your own machine is not asked about user accounts or billing. The overview ends by recording, for each of the catalog's 20 categories, whether it applies to your project.

2. **Beliefs and Bets.** The Team Lead works through the beliefs your project depends on: about your customers, the value of the solution, your data, what a model can do, cost, and adoption. Together you rate how damaging each would be if wrong and how much evidence supports it. The consequential, weakly supported beliefs become the project's bets. Everything that follows depends on this step.

3. **Project Scope.** The Architect selects the catalog nodes your application needs and the nodes that will test each bet, then organizes them into phases. A phase is whatever grouping makes sense for your project: an experiment that tests a bet, a body of work such as data acquisition, or a release. Work that tests the riskiest bets is placed as early as its dependencies allow. If no catalog node can test one of your bets, the Architect proposes a new one.

4. **Estimation Discovery.** The Analyst decides how far ahead the plan can be detailed with confidence, then gathers the questions each node in that range needs answered, taken from the catalog. The Team Lead puts them to you, as a questionnaire or in conversation. Where you are unsure of an answer, you give a low and a high value. Planning does not begin until every question has an answer.

5. **Project Plan.** The Analyst estimates the work and schedules it around the hours you have available. The plan has three levels of detail: individual tasks with dates for the near-term work, whole nodes with approximate ranges for the work after that, and whole phases for the work beyond.

6. **Publish.** You review the plan in Excel and make any changes you want. When you authorize it, the Integrator publishes the plan to ClickUp exactly as you approved it.

## Requirements

- **Claude Code**, with plugin support.
- **The `xlsx` skill**, which the Analyst uses to build the workbook. It is part of the `document-skills` plugin in Anthropic's skills marketplace. See [Installation](#installation).
- **A ClickUp account**, only if you want to publish the plan. See [Publishing to ClickUp](#publishing-to-clickup).

## Installation

The plugin is distributed through the Agentix marketplace, published from the [wxplusb-ai/agentix](https://github.com/wxplusb-ai/agentix) repository. Run these commands from the repository where you want to plan your project.

Add the Agentix marketplace and install the plugin for this repository:

```bash
claude plugin marketplace add wxplusb-ai/agentix
claude plugin install ai-ddp-planning@agentix --scope project
```

Project scope records the plugin in the repository's `.claude/settings.json`, so anyone who works on the repository can see it is in use. Each person still installs the plugin on their own machine.

Then add Anthropic's skills marketplace and install `document-skills`, which provides the `xlsx` skill the Analyst uses to build the plan workbook:

```bash
claude plugin marketplace add anthropics/skills
claude plugin install document-skills@anthropic-agent-skills
```

The same commands work inside a Claude Code session with a leading slash, for example `/plugin marketplace add wxplusb-ai/agentix`.

To try the plugin from a local clone of the repository without installing it, load it for a single session:

```bash
claude --plugin-dir <path-to-agentix>/plugins/ai-ddp-planning --agent ai-ddp-planning:team-lead
```

## Usage

Start Claude Code with the Team Lead as the main agent:

```bash
claude --agent ai-ddp-planning:team-lead
```

Then describe your project and ask for a plan. The Team Lead creates a `planning/` folder in your repository and guides you through each step.

If you will plan in this repository often, make the Team Lead the default agent by adding this line to the repository's `.claude/settings.json`:

```json
{
  "agent": "ai-ddp-planning:team-lead"
}
```

With that setting, running `claude` on its own starts the engagement.

### Providing documents

If you already have material about your project, such as a brief, a pitch deck, research notes, a data description or architecture diagrams, place it in `planning/client_documents/` before or during the first step. The Team Lead reads everything there and asks only about what the documents do not answer.

### What the team produces

All deliverables are written to `planning/agent_documents/`:

| File | Contents |
|---|---|
| `01-project-overview.md` | Your project, its current state, and which catalog categories apply |
| `02-beliefs-and-bets.md` | Every belief the project rests on, rated, with the bets ranked |
| `03-project-scope.md` | The phases, the nodes in each, and which bets each node tests |
| `04-estimation-discovery.md` | The estimation questions and your answers |
| `05-project-plan.xlsx` | The project plan |
| `06-clickup-publication.md` | A record of what was published to ClickUp, with item IDs |

The workbook's **Plan** sheet has one row per task, node or phase, with these columns: Phase, Node, Task, Task Description, Estimate (Hours), Start Date, End Date, Priority and Tags. Three further sheets support it. **Summary** gives the totals for each phase and the overall estimate as a range. **Estimate Basis** shows how every estimate was reached, so you can check or challenge it. **Bets** lists each bet and the nodes that test it.

Priority takes one of four values: Urgent, High, Normal or Low. Work that tests a bet with no supporting evidence, or that a hard deadline depends on, is Urgent. Tags carry each node's catalog category and the IDs of the bets it tests, so you can filter the plan, or ClickUp, to follow a single experiment across phases.

## Publishing to ClickUp

Nothing is written to ClickUp until you have reviewed the plan in Excel and explicitly told the Team Lead to publish it. Before you do, prepare the following:

1. **An API token.** Create a personal token in ClickUp under your user settings, then set it in the shell you launch Claude Code from:

   ```bash
   export CLICKUP_API_TOKEN=pk_your_token
   ```

   The team never asks for the token in conversation and never writes it to a file.

2. **Your workspace, space and user IDs.** The Team Lead asks for these when you authorize publishing.

3. **An `Open` status** in the space where the plan will be published. Every task is created with that status. If it does not exist, the Integrator stops and tells you rather than choosing a different status.

The plan maps onto ClickUp as follows:

| Plan | ClickUp |
|---|---|
| Phase | Folder |
| Node | List |
| Task | Task name |
| Task Description | Description |
| (all tasks) | Status `Open` |
| Estimate (Hours) | Time estimate |
| Start Date | Start date |
| End Date | Due date |
| Priority | Priority |
| Tags | Tags |

Rows planned at node or phase level have no individual tasks yet. Each is published as a single task named after its node or phase, carrying the estimate and dates from the plan.

Publishing is safe to repeat. The Integrator reads what already exists in the space and updates matching items instead of creating duplicates. It never deletes anything without your explicit instruction.

## Planning again

Plans made this way are meant to be revisited. Run the engagement again when the project reaches a milestone, typically when a bet has been tested and the team knows something it did not know before.

On a second run, the Team Lead starts from the earlier deliverables. The overview records what has been completed and what was learned, the bets are updated with the evidence that confirmed or refuted them, and the next stretch of work is planned in detail. Each deliverable is saved as a new version, such as `03-project-scope-v2.md`, and earlier versions are kept. Publishing again updates the existing ClickUp folders and lists.

You decide when to plan again. The agents do not revise the plan on their own.

## The node catalog

The catalog is in `catalog/discovery_driven_planning_node_catalog_v2.md`. At the start of an engagement the Team Lead copies it into your `planning/` folder, so each plan stays tied to the catalog version it was built from.

The catalog's 20 categories range from Product Strategy, through engineering disciplines such as Knowledge Retrieval Engineering, Cognitive Agent Architecture and Runtime Safety and Moderation, to Model Adaptation and Continuous Improvement. Every node in it is described in eight sections: an overview, prerequisites, inputs, outputs, tasks with estimation guidelines, the questions needed before estimating, best practices, and the assumptions the node validates.

When the Architect proposes a new node for a bet the catalog cannot test, the proposal appears in the scope document. If you approve it, it is planned like any other node, and it is a candidate for adding to the catalog.

## Plugin contents

```
ai-ddp-planning/
├── .claude-plugin/
│   └── plugin.json          Plugin manifest
├── agents/                  The Team Lead, Architect, Analyst and Integrator
├── skills/                  One skill for each step, and the Team Lead's skill for running the engagement
├── references/              The planning methodology shared by all agents, and the AI-AD&D framework
├── catalog/                 The AI-AD&D node catalog
└── README.md
```

The skills follow the steps of the engagement:

| Skill | Used by | Step |
|---|---|---|
| `leading-ai-ddp-planning` | Team Lead | The whole engagement |
| `conducting-project-overview` | Team Lead | 1. Project Overview |
| `mapping-beliefs-and-bets` | Team Lead | 2. Beliefs and Bets |
| `scoping-project-nodes` | Architect | 3. Project Scope |
| `conducting-estimation-discovery` | Analyst and Team Lead | 4. Estimation Discovery |
| `planning-project-work` | Analyst | 5. Project Plan |
| `publishing-plan-to-clickup` | Integrator | 6. Publish |
