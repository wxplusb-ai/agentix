# Agentix

**A delivery accelerator for agentic AI.** Proven components that compress the distance between an idea and a working system, so every build starts from advantage rather than from zero.

---

## The tax nobody bills for

Most teams rebuild the same agentic scaffolding on every project. The harness. The evaluation discipline. The connector plumbing. The context strategy that took three rewrites to get right. That work is real, it is expensive, and it produces nothing anyone will pay for twice.

Agentix exists to end that tax. It is a curated body of reusable IP for agentic AI, assembled from production work and hardened through repeated deployment. Each asset arrives ready to install, versioned, and proven against real workloads. What used to take weeks of foundation-laying now takes an afternoon, and the effort that went into rebuilding goes into the problem that actually matters.

The compounding effect is the point. Every project returns something to the library, and the next one starts further ahead.

---

## The taxonomy

Agentic development is not one discipline. It is eleven, and most projects discover them one painful surprise at a time. Agentix names them, and holds assets against each.

The eleven dimensions group into four layers: what the agent knows, what it can act on, how it runs, and how you know it works.

---

## Layer 1: Knowledge
*What the agent brings to the task.*

### Skill Development
Procedural expertise, packaged so an agent can acquire it on demand. A skill encodes how to do something well: interrogate a codebase, structure a research pass, critique output before shipping it. Writing that down as an installable unit means quality stops depending on who wrote the prompt that day. Assets here cover skill authoring conventions, progressive disclosure patterns, bundled reference material, and the skills themselves.

### Context Engineering
Deciding what occupies the window, and what does not. This is the highest-leverage and least-understood dimension in agentic work: retrieval strategy, compaction and summarization, context isolation across sub-agents, prompt and output contracts, and the discipline of spending tokens on signal instead of sediment. Most agents that degrade over a long run degrade here.

### Memory Architecture
What survives the session. Persistence schemas, working scratchpads, checkpoint and resume, and the handoff of state from one run to the next. The difference between an agent that starts over every morning and one that accumulates useful ground.

---

## Layer 2: Capability
*What the agent can act on.*

### Tool Engineering
Tool design is an interface problem, and the interface is consumed by a model rather than a human. Schema shape, description quality, error surfaces that teach recovery rather than just reporting failure, and returns that are token-efficient by construction. Badly designed tools are the most common cause of agents that look capable and behave erratically.

### Integration and Connectors
Reaching the systems where the work actually lives. MCP servers and clients, authentication, rate discipline, pagination, and access to systems of record through a consistent surface. Built once, reused everywhere. This is the difference between an impressive demo and something that survives contact with a real environment.

### Execution Environment
The sandbox the agent acts in. Filesystem layout, shell access, containerization, network policy, and resource limits. Defines the blast radius of a mistake, which is a design decision whether or not anyone makes it deliberately.

---

## Layer 3: Control
*How the agent runs.*

### Harness Engineering
The loop itself. Turn control, stop conditions, retry and recovery paths, model selection and routing, token and cost budgets, and the ability to interrupt and steer a run in flight. The harness is where an agentic system becomes dependable rather than merely impressive, and it is almost always rebuilt from scratch on projects that did not plan for it.

### Orchestration and Topology
Multi-agent structure. Delegation, planner and executor splits, fan-out and gather, handoff contracts between agents, and sub-agent lifecycle. The decision of what to decompose and what to leave whole determines cost and reliability more than any model choice.

### Permissioning and Guardrails
What proceeds automatically and what stops for a human. Allowlists and approval gates, prompt injection defense, policy for irreversible actions, and the boundary between instructions from the user and content encountered through tools. The dimension that makes the difference between a system you can deploy and one you can only demo.

---

## Layer 4: Assurance
*How you know it works.*

### Evaluation
Turning subjective judgment into a number you can defend. Task sets, graders and rubrics, outcome scoring versus trajectory scoring, and regression suites that catch the day a model update quietly changes behavior. This is the answer to the question every serious stakeholder eventually asks.

### Observability
Seeing what actually happened. Traces and spans across a run, token and cost accounting, failure forensics, and run-to-run comparison. Debugging an agent without observability is guesswork, and it scales exactly as badly as it sounds.

---

## How assets are packaged

Nothing here forces adoption of the whole library. Pull a single connector into an existing stack. Take the harness and bring your own skills. Use the evaluation assets against a system built entirely elsewhere. Independence is a design requirement, not a happy accident.

What holds it together is a common contract rather than a common framework:

- **Every asset ships with its own manifest.** Name, version, dependencies, install path, and what it has been validated against. Portability is a property you engineer, not one you claim.
- **One documented way to adopt anything.** Installation is a command, not an archaeology project.
- **Maturity is declared, not implied.** Assets are labeled experimental, stable, or deprecated, so nobody discovers the hard way which is which.
- **No domain logic.** Anything specific to the project an asset came from is stripped before it enters the library. What remains is machinery.

Reference architectures and design decisions are documented across dimensions rather than filed under one. They record the trade-offs and failure modes discovered the expensive way, so they are not relitigated on the next build.

---

## Getting started

1. Identify the dimension that matches what you are building or what is currently failing.
2. Read the manifest of the asset you want for dependencies and validation status.
3. Install it using the documented adoption path.
4. Build.

Each asset carries its own documentation. Start there for anything specific.

---

## The growth loop

Agentix is designed to get better through use. When a project produces something that outlives it, that component returns to the library: generalized, documented, given a manifest, and labeled honestly for maturity. The bar for entry is one question. Would this save real time on the next build, or is it only interesting here?

Assets that stop earning their place get deprecated rather than quietly rotting. The value of the library is its curation, not its size.

---

## Status

Agentix is under active development. Coverage across the eleven dimensions is uneven by design, growing where real projects create real demand.
