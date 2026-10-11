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

1. **Project Overview.** The Team Lead reads any documents you provide and interviews you about your goals, market, users, workflow, data, technology, constraints and current progress. The interview adapts to your project: a personal tool running on your own machine is not asked about user accounts or billing. Topics that do not apply are skipped, and the overview says which and why. The overview describes your project as it is today; it does not plan anything.

2. **Beliefs and Bets.** A structured discussion. The Team Lead walks you through the areas your project depends on, starting with its core bet (the one proposition the whole application stakes its existence on), then the areas that apply to you: your customers, the value of the solution, your data, what a model can do, cost, adoption and so on. You state what you believe; the Team Lead helps sharpen each belief into something that can be tested. Together you rate how damaging each would be if wrong and how much evidence supports it. The consequential, weakly supported beliefs become the project's bets. Everything that follows depends on this step.

3. **Project Scope.** The Architect selects the catalog nodes your application needs and the nodes that will produce evidence for each bet (often several nodes, sometimes whole phases), then organizes them into phases. A phase is whatever grouping makes sense for your project: the work that validates a bet, a body of work such as data acquisition, or a release. Later phases are included even when their nodes cannot be chosen yet. Work on the riskiest bets is placed as early as its dependencies allow. Every phase and node is explained in full, so the scope reads on its own without the catalog. If no catalog node can validate one of your beliefs, the Architect proposes a complete new node.

4. **Estimation Discovery.** The Analyst decides how far ahead the plan can be detailed with confidence, then gathers the questions each node in that range needs answered, taken from the catalog. The Team Lead puts them to you, as a questionnaire or in conversation. Where you are unsure of an answer, you give a low and a high value. Planning does not begin until every question has an answer.

5. **Project Plan.** The Analyst estimates the work and schedules it around the hours you have available. The plan has three levels of detail: individual tasks with dates for the near-term work, whole nodes with approximate ranges for the work after that, and whole phases for the work beyond.

6. **Publish.** You review the plan in Excel and make any changes you want. When you authorize it, the Integrator publishes the plan to ClickUp exactly as you approved it.

## Requirements

- **A paid Claude plan** (Pro, Max, Team or Enterprise) or an Anthropic Console account with API credit. Claude Code does not work on the free plan.
- **The Claude Code command-line tool.** The Claude extension for VS Code on its own is not enough: the installation and launch commands below run `claude` in a terminal.
- **Python 3**, which the Analyst uses to build the plan workbook.
- **Git for Windows**, on Windows only. Claude Code uses it to run commands.
- **The `xlsx` skill**, from the `document-skills` plugin in Anthropic's skills marketplace.
- **A ClickUp account**, only if you want to publish the plan. See [Publishing to ClickUp](#publishing-to-clickup).

[Setting up your computer](#setting-up-your-computer) covers everything except ClickUp, and [Installing the plugin](#installing-the-plugin) adds the plugin and the `xlsx` skill to a project folder.

## Setting up your computer

You do this once per computer. Follow the section for where you will run Claude Code:

- **[Windows](#windows)** runs Claude Code directly on Windows. Choose this if you are unsure.
- **[Linux and WSL2](#linux-and-wsl2)** is for Linux, and for Windows users who already work in WSL2 (Windows Subsystem for Linux). macOS users can follow it too, installing Python from [python.org](https://www.python.org/downloads/) or Homebrew instead of `apt`.

Each step's heading tells you how to check whether it is already done. If the check passes, skip the step.

### Windows

Run the commands in this section in **PowerShell**: open the Start menu and search for "PowerShell". The terminal in VS Code also runs PowerShell on Windows by default.

#### Step 1: Install Git for Windows (skip if `git --version` prints a version number)

Download Git for Windows from [git-scm.com/download/win](https://git-scm.com/download/win), run the installer and accept the defaults. You do not need to use Git yourself; Claude Code needs the Git Bash shell that comes with it.

#### Step 2: Install Python (skip if `python --version` prints Python 3)

If `python --version` opens the Microsoft Store or reports that Python was not found, Python is not installed.

Download the installer from [python.org/downloads](https://www.python.org/downloads/). On the first screen of the installer, **tick "Add python.exe to PATH"** before clicking Install. Without it, Claude Code cannot find Python.

#### Step 3: Install Claude Code (skip if `claude --version` prints a version number)

In PowerShell, run:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Then **close every PowerShell window and quit VS Code completely**, and open them again. A terminal that was open during the installation does not see the new `claude` command, and VS Code keeps its old settings until it is fully restarted.

Run `claude --version` in a new window. If it still reports that `claude` is not recognized, add the folder the installer used to your PATH:

1. Open the Start menu, search for **Edit environment variables for your account** and open it.
2. Select **Path** in the top list and click **Edit**.
3. Click **New** and enter `%USERPROFILE%\.local\bin`.
4. Click **OK** in both windows, then close and reopen your terminals and VS Code again.

#### Step 4: Sign in to Claude Code (skip if you have used Claude Code on this computer before)

Run `claude`. It opens your browser so you can sign in to your Claude account. When Claude Code shows its prompt, type `/exit` to leave.

Your computer is ready. Continue with [Installing the plugin](#installing-the-plugin).

### Linux and WSL2

#### Step 1: Set up WSL2 (skip if you are on Linux or macOS, or if `wsl -l -v` in PowerShell lists a distribution with VERSION 2)

Open PowerShell as administrator (right-click it in the Start menu and choose **Run as administrator**) and run:

```powershell
wsl --install
```

Restart Windows when asked. After the restart, an Ubuntu window opens and asks you to create a Linux username and password. These are separate from your Windows account.

If you use VS Code, install the **WSL** extension from the Extensions view. It lets VS Code open folders and terminals inside WSL.

From here on, run every command in the **Ubuntu terminal**, not PowerShell. Claude Code installed on Windows and Claude Code installed in WSL are separate installations; installing one does not give you the other.

#### Step 2: Install curl and Python (skip if `curl --version` and `python3 --version` both print version numbers)

On Ubuntu and Debian, including the default WSL2 distribution:

```bash
sudo apt update
sudo apt install -y curl python3 python3-pip
```

On other distributions, install `curl`, `python3` and `pip` with your package manager.

#### Step 3: Install Claude Code (skip if `claude --version` prints a version number)

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Open a new terminal and run `claude --version`. If it reports `command not found`, add the installation folder to your PATH:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

If your shell is zsh, use `~/.zshrc` instead of `~/.bashrc`.

#### Step 4: Sign in to Claude Code (skip if you have used Claude Code on this computer before)

Run `claude` and follow the prompts to sign in to your Claude account. In WSL2 the browser may not open by itself; if not, copy the link Claude Code prints into your Windows browser. When Claude Code shows its prompt, type `/exit` to leave.

Your computer is ready. Continue with [Installing the plugin](#installing-the-plugin).

## Installing the plugin

The plugin is distributed through the Agentix marketplace, published from the [wxplusb-ai/agentix](https://github.com/wxplusb-ai/agentix) repository.

You install it into the folder where you want to plan your project. Any folder works: a code repository, a documents folder or an Obsidian vault. It does not need to be a Git repository. The commands are the same on Windows, Linux and WSL2.

### Step 1: Open your project folder in a terminal

**In VS Code on Windows**, choose **File > Open Folder** and select your project folder, then choose **Terminal > New Terminal**. For an Obsidian vault, select the vault's top-level folder: the one that contains the `.obsidian` folder.

**In VS Code with WSL2**, click the blue remote indicator in the bottom-left corner and choose **Connect to WSL**, then choose **File > Open Folder** and **Terminal > New Terminal**. Windows drives appear under `/mnt`, so a vault at `C:\Users\Jane\Documents\MyVault` is at `/mnt/c/Users/Jane/Documents/MyVault`.

**In any other terminal**, change to the folder with `cd`, for example `cd "C:\Users\Jane\Documents\MyVault"` in PowerShell.

Check that the terminal prompt shows your project folder before going on. The plugin is installed into whichever folder the terminal is in.

### Step 2: Add the Agentix marketplace (skip if you have added it on this computer before)

```bash
claude plugin marketplace add wxplusb-ai/agentix
```

### Step 3: Install the planning plugin in this folder (skip if this folder's `.claude/settings.json` already lists `ai-ddp-planning@agentix`)

```bash
claude plugin install ai-ddp-planning@agentix --scope project
```

Project scope records the plugin in the folder's `.claude/settings.json`, so anyone who works in the folder can see it is in use. Each person still installs the plugin on their own computer.

Obsidian hides folders whose names start with a dot, so the new `.claude` folder does not appear in your vault. That is expected.

### Step 4: Install the `xlsx` skill (skip if you have installed `document-skills` on this computer before)

Add Anthropic's skills marketplace and install `document-skills`, which provides the `xlsx` skill the Analyst uses to build the plan workbook:

```bash
claude plugin marketplace add anthropics/skills
claude plugin install document-skills@anthropic-agent-skills
```

The same commands work inside a Claude Code session with a leading slash, for example `/plugin marketplace add wxplusb-ai/agentix`.

### Trying the plugin without installing it

To try the plugin from a local clone of the repository, load it for a single session instead of following Steps 2 and 3:

```bash
claude --plugin-dir <path-to-agentix>/plugins/ai-ddp-planning --agent ai-ddp-planning:team-lead
```

You still need the `xlsx` skill from Step 4 to build the plan workbook.

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
| `01-project-overview.md` | Your project as it is today, including its current state |
| `02-beliefs-and-bets.md` | Every belief the project rests on, rated, with the bets ranked |
| `03-project-scope.md` | The phases, the nodes in each explained in full, and how the bets will be validated |
| `04-estimation-discovery.md` | The estimation questions and your answers |
| `05-project-plan.xlsx` | The project plan |
| `06-clickup-publication.md` | A record of what was published to ClickUp, with item IDs |

The workbook's **Plan** sheet has one row per task, node or phase, with these columns: Phase, Node, Task, Task Description, Estimate (Hours), Start Date, End Date, Priority and Tags. Three further sheets support it. **Summary** gives the totals for each phase and the overall estimate as a range. **Estimate Basis** shows how every estimate was reached, so you can check or challenge it. **Bets** lists each bet and the nodes that test it.

Priority takes one of four values: Urgent, High, Normal or Low. Work that tests a bet with no supporting evidence, or that a hard deadline depends on, is Urgent. Tags carry each node's catalog category and the IDs of the bets it tests, so you can filter the plan, or ClickUp, to follow a single experiment across phases.

## Publishing to ClickUp

Nothing is written to ClickUp until you have reviewed the plan in Excel and explicitly told the Team Lead to publish it. Before you do, prepare the following:

1. **An API token.** Create a personal token in ClickUp under your user settings, then set it in the shell you launch Claude Code from:

   On Linux, macOS or WSL2:

   ```bash
   export CLICKUP_API_TOKEN=pk_your_token
   ```

   In PowerShell on Windows:

   ```powershell
   $env:CLICKUP_API_TOKEN = "pk_your_token"
   ```

   Either way, the token lasts only as long as that terminal window, so set it again in each new terminal before starting Claude Code.

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

ClickUp holds estimates and dates only on tasks, not on folders or lists. Rows planned at node level have no individual tasks yet, so each is published as its node's list containing one task named after the node. Rows planned at phase level are published as the phase's folder, containing one list and one task named after the phase. These tasks carry the estimate and dates from the plan.

Publishing again replaces the previous publication. The Integrator first downloads everything it published last time to a backup file in `planning/agent_documents/`, carries your status changes, assignees and comments over to the matching tasks in the new plan, deletes only the items it published last time, and then loads the new version. Anything else in the space is never touched. The Team Lead asks for your explicit authorization before any of this happens.

## Planning again

Plans made this way are meant to be revisited. Run the engagement again when the project reaches a milestone, typically when a bet has been tested and the team knows something it did not know before.

On a second run, the Team Lead starts from the earlier deliverables. The overview records what has been completed and what was learned, the bets are updated with the evidence that confirmed or refuted them, and the next stretch of work is planned in detail. Each deliverable is saved as a new version, such as `03-project-scope-v2.md`, and earlier versions are kept. Publishing again replaces the previous ClickUp publication, after backing it up.

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
| `discovering-beliefs-and-bets` | Team Lead | 2. Beliefs and Bets |
| `scoping-project-nodes` | Architect | 3. Project Scope |
| `conducting-estimation-discovery` | Analyst and Team Lead | 4. Estimation Discovery |
| `planning-project-work` | Analyst | 5. Project Plan |
| `publishing-plan-to-clickup` | Integrator | 6. Publish |
