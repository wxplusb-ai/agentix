# Skill Authoring Guide

How we write SKILL.md files. Follow this when creating a new skill or retrofitting an existing one. It is the standard the market-signal and innovation skills are held to.

The guide is opinionated on purpose: a house style makes skills predictable to read, cheap to review, and consistent for the agents that run them. Where it and a best-practice article disagree, this guide wins for Sciven skills.

---

## 1 Philosophy

Five ideas govern everything below. If a decision isn't covered by a later rule, decide it from these.

- **Write for a capable agent, not a novice.** The reader is a strong model. Add only what it *wouldn't* know without you — project conventions, non-obvious constraints, the exact schema, the gotcha that defies a reasonable assumption. Cut anything it already knows. The test for every sentence: *would the agent get this wrong without it?* If no, delete it. 
- **Don't command.** A `MUST` with no reason is brittle — the agent can't tell when it applies or how to adapt at the edges. Give the reason and the agent generalizes correctly. 
- **Teach a method, not an answer.** A skill should generalize across every instance of its task, not encode one instance. Derive from inputs; never import specifics from an example. Mark every example "illustrative — do not copy its content." Overfit skills send the agent down paths that don't fit the case in front of it.
- **One source of truth per fact.** State each path, schema, or rule in exactly one place and point to it from everywhere else. Method lives in `references/`; output locations live in one table; the skill body points, it does not restate. Duplication drifts and then lies. 
- **Calibrate control to fragility.** High freedom where many approaches are valid (judgment tasks) — describe what good looks like and trust the agent. Low freedom where operations are fragile (persistence, ordering, destructive steps) — give the exact command and say "do not modify it." Most skills mix both; calibrate each section independently. 
- **Generalize; don't overfit.** A skill is written once and used across many prompts. When you and the user iterate on a few familiar examples, it is tempting to patch the skill so it passes those cases. Resist it. Avoid fiddly example-specific fixes and oppressive all-caps MUSTs. When an issue is stubborn, try a different metaphor or a different working pattern rather than another constraint; it is cheap to try and often lands better.
- **Keep it lean.** The context window is a shared budget. Add only what the model does not already know, and challenge each sentence to justify its tokens; a capable model does not need PDFs explained. Cut anything that isn't pulling its weight. Read transcripts, not just final outputs: if the skill is making the model waste effort, remove the part causing it and observe the result.
- **Explain the why.** Modern models have good theory of mind and, given a good harness, go well beyond rote instructions. Transmit your reasoning, not just your rules. An all-caps ALWAYS or NEVER, or a rigid structure, is a yellow flag: reframe it as the reason the requirement matters. Understanding is more powerful and more durable than command.

---

## 2 Canonical structure

Order sections this way. Include the ones the skill needs; omit the rest — an empty section is noise.

1. **YAML frontmatter** — `name`, `description`, optional `metadata`. See §3.
2. **Title + role + guardrail.** One `#` title, then a short "You are …/Your job is …" and a **bold** do/don't line that names what this skill is *not* for. Example: *"You produce a plan. You do not execute discovery. If you find yourself searching, stop — that is the subagents' work."*
3. **Why this skill exists.** The highest-value section. State what goes wrong *by default* — the mistakes a capable agent makes without this skill — and the properties the skill forces to prevent them. This is where theory-of-mind lives: name the wrong assumption the agent will otherwise make.
4. **Critical constraints.** The few non-negotiables, each with its reason. These are the rules that, if broken, invalidate the output no matter how good the rest is. Keep the list short; if everything is critical, nothing is.
5. **Inputs / Output locations** (orchestration & producer skills). What the caller passes, and a single table of where every artifact goes (`name | folder | filename format`). This table is the sole source of truth for paths.
6. **Workflow.** Numbered, imperative steps in execution order. Mark which steps are interactive (pause for a human/lead) vs. autonomous. Gate risky steps ("do not proceed until validation passes"). For long or branching workflows, open with a copyable checklist.
7. **References.** A table (`name | description | filename`) of the `references/` files, with a one-line note on *when* to read each. See §5.
8. **Examples.** A few in-scope triggers (including an implicit one) and a few out-of-scope cases with the correct "do not use this skill, do X instead" response. Examples drive triggering more than prose does.
9. **Troubleshooting.** Symptom → cause → fix, for the failure modes you've actually seen. Grow this from real runs.

Producer/subagent skills lean on 5–7; planner/lead skills lean on 3–4 and 6; a pure-instruction skill may be just 1–4 and 8.

---
## Frontmatter

- **`name`** — lowercase, hyphens only, ≤64 chars, matches the directory name. Prefer gerund/action form: `leading-market-signal-detection`, `detecting-latent-consumer-market-demand-signals`. Never `anthropic`/`claude` or vague names (`helper`, `tools`).
- **`description`** — third person, ≤1024 chars, ~2–4 sentences. It is the *only* thing the agent sees when deciding whether to trigger the skill, so it must carry both **what** the skill does and **when** to use it, and be pushy about the when. Include concrete trigger phrases and, critically, **negative triggers** — what this skill is *not* for. Pattern: `<what it does>`. Use when `<triggers, including an implicit phrasing>`. Not for `<adjacent things>` — `<where those go instead>`.
- ``
- **`metadata`** (optional) — `version`, `category`, `tags`. Use for skills that ship or that a router selects among.


### ⁠7.2. Optimize the frontmatter for discoverability

The `name` and `description` are the only fields the agent sees before triggering a skill. If they are vague, the skill is invisible.

- **Name:** 1-64 characters, lowercase letters, numbers, and hyphens only, no consecutive hyphens, and it must exactly match the parent directory name (`angular-testing` lives in `angular-testing/SKILL.md`).
- **Description:** maximum 1,024 characters, third person, stating both what the skill does and when to use it, and including negative triggers.
    - **Bad:** "React skills." (too vague)
    - **Good:** "Creates and builds React components using Tailwind CSS. Use when the user wants to update component styles or UI logic. Don't use for Vue, Svelte, or vanilla CSS projects."

---
## Writing style

The prose is instructions to an agent, not documentation for a human. Make it scannable and unambiguous.

- **Imperative and consistent voice.** "Read the catalog." "Write the plan." Address the agent as "you"; keep that person throughout. Do not drift between "the agent should," "you should," and "I will."
- **One term per concept.** Pick a word and keep it: *source*, *signal*, *workbook*, *reflection* — not a rotating cast of synonyms. Inconsistent terms make the agent guess whether two names mean the same thing.
- **Why-clauses on judgment calls; bare imperatives on fragile mechanics.** Attach a short "because …" to instructions the agent must adapt; drop it on instructions that are literally exact.
- **Templates over description.** To fix an output format, show the structure (a fenced markdown or JSON block) rather than describing it in prose. Agents pattern-match structures far more reliably than they parse adjectives. Keep short templates inline; move long ones to `references/` or `assets/` and point to them.
- **No time-sensitive text** in instructions (dates belong only inside illustrative examples). No Windows paths — forward slashes only.


### ⁠7.3. Write specific procedural instructions

Write for an agent, not a human reader.

- **Third-person imperative.** Frame instructions as direct commands ("Extract the text..."), not "I will extract..." or "You should extract...".
- **Numbered steps and explicit decision points.** Define the workflow as a chronological sequence; map any branch clearly ("Step 2: if you need source maps, run `ng build --source-map`; otherwise skip to Step 3").
- **Concrete templates.** Agents pattern-match well. Rather than describe an output format in prose, place a template in `assets/` and instruct the agent to copy its structure.
- **Consistent, domain-specific terminology.** Pick one term per concept and use it throughout, and prefer the most specific term native to the domain (in Angular, "template", not "html", "markup", or "view"). Inconsistent vocabulary is a frequent, avoidable cause of misreading.

---

## ⁠7.4. Match degrees of freedom to the task

Calibrate specificity to how fragile and variable the task is. Picture the model as a robot crossing terrain.

- **Open field (high freedom):** many valid paths, decisions depend on context. Give direction and trust the model. Express as text heuristics.
- **Established trail (medium freedom):** a preferred pattern exists, some variation is fine. Express as pseudocode or a parameterized template.
- **Narrow bridge over cliffs (low freedom):** fragile, consistency-critical, one sequence must hold. Give exact commands and forbid deviation. Express as a specific script with few or no parameters.

Over-constraining an open task wastes tokens and suppresses judgment; under-constraining a fragile one invites errors. Choose deliberately.

---

## ⁠7.5. Use progressive disclosure

SKILL.md is a table of contents, not the whole manual. Keep its body under 500 lines and push depth into bundled files the model loads only when needed.

- Keep references **one level deep** from SKILL.md. The model may preview nested files with partial reads and miss content, so a referenced file must not point onward to another for essential information.
- Organize bundled files by domain so an unrelated request never loads irrelevant context.
- For any reference file over ~100 lines, place a table of contents at the top so the full scope is visible even on a partial read.
- State whether the model should **execute** a file or **read it as reference**; the two intents are easy to confuse and costly to get wrong.

---

## ⁠7.6. Build workflows and feedback loops

For multi-step tasks, give an explicit numbered sequence; for complex ones, provide a checklist the model copies into its response and ticks off, which prevents skipped steps. Where output quality matters, install a loop: produce, validate, fix, repeat, and proceed only when validation passes. The validator can be a script or a reference document the model checks against. For batch or high-stakes operations, insert a verifiable intermediate output: have the model emit a structured plan, validate the plan, then execute, so errors surface before they propagate.


### Workflow Sections
Use the following as a template for defining the workflow.

```markdown
## Research synthesis workflow

Copy this checklist and track your progress:

Research Progress:
- [ ] Step 1: Read all source documents
- [ ] Step 2: Identify key themes
- [ ] Step 3: Cross-reference claims
- [ ] Step 4: Create structured summary
- [ ] Step 5: Verify citations


**Step 1: Read all source documents**

Review each document in the `sources/` directory. Note the main arguments and supporting evidence.

**Step 2: Identify key themes**

Look for patterns across sources. What themes appear repeatedly? Where do sources agree or disagree?

**Step 3: Cross-reference claims**

For each major claim, verify it appears in the source material. Note which source supports each point.

**Step 4: Create structured summary**

Organize findings by theme. Include:
- Main claim
- Supporting evidence from sources
- Conflicting viewpoints (if any)

**Step 5: Verify citations**

Check that every claim references the correct source document. If citations are incomplete, return to Step 3.
```

---

## ⁠7.7. Keep content durable

Exclude time-sensitive statements that will silently go stale. If legacy behavior must be recorded, isolate it in a clearly labeled "old patterns" section so it does not contaminate the current path.

---

## ⁠7.8. For skills that ship code

- **Solve, don't punt.** Handle error conditions inside scripts rather than failing and leaving the model to improvise.
- **No voodoo constants.** Justify and document every configuration value; an unexplained constant is one the model cannot reason about.
- **Declare dependencies.** Never assume a package is installed. State required packages and confirm they exist in the target environment, which may have no network access.
- **Fully qualify MCP tool names** as `ServerName:tool_name`; an unqualified name can fail to resolve when several servers are present.
- **Use forward slashes** in all paths for cross-platform safety.

---
## ⁠7.9. Develop against evaluations

Write the evaluations before writing extensive instructions, so the skill solves a real, observed gap rather than an imagined one. Run the task without the skill to set a baseline and document the specific failures. Build a handful of representative scenarios with concrete inputs and expected behaviors. Write the minimum instruction needed to pass them, then iterate: run, compare against baseline, refine on observed behavior rather than assumptions. Test against every executor and model the skill will run on, since guidance that suffices for a stronger model may underserve a weaker one. These evaluations are the source of truth for the evaluation methods deliverable in §5.

- Write **2–3 test cases** per skill in `evals/evals.json`: `{id, prompt, expected_output/behavior, files}`. Include at least one prompt that *should* trigger the skill and one adjacent prompt that should *not*.
- Grade **with vs. without** the skill on the same prompts — the delta is the skill's value. If the agent already succeeds without it, the skill may be unnecessary.
- **Read the trace, not just the output.** Wasted exploration usually means instructions too vague; ignored instructions usually mean they don't apply to the case or aren't prominent enough. Fix the cause.
- When you correct the same agent mistake twice, encode the correction — as a constraint, a gotcha, or (for Sciven's detection skills) a reflection.

---

## ⁠7.10. Avoid the common anti-patterns

- **Too many options.** Give one default with at most a narrow escape hatch, not a menu of interchangeable libraries.
- **Deeply nested references.** Restated from §6.5 because the failure is severe.
- **Assuming installation or environment.** Verify and state; never assume.
- **Windows-style paths.** They break on Unix; always forward slashes.
- **MUST-soup.** Walls of capitalized imperatives with no reasons. The agent can't prioritize or adapt. Replace with reasons; reserve `MUST`/`never` for the few truly inviolable rules.
- **Menus.** "You could use A, or B, or C…" Pick a default; mention the escape hatch in one clause ("for scanned PDFs, use B instead").
- **Restating a source of truth.** Writing a path, schema, or rule into a phase when it already lives in a table or reference. Point instead.
- **Copy-ready examples.** Examples the agent will lift verbatim into a real task. Label them illustrative and, for planners, add "never import its domain content."
- **Explaining the obvious.** Paragraphs on what a PDF/HTTP/database is. Cut.
- **Deeply nested or vaguely-signaled references.** Files the agent won't reliably find or read completely.- 

---

## References and progressive disclosure

Only the frontmatter is always loaded; the SKILL.md body loads when the skill triggers; reference files load only when the body sends the agent to them. Exploit that.

- **Keep SKILL.md under ~500 lines.** It is the overview and the runtime procedure — not the curriculum. Push depth into `references/`.
- **One level deep.** Every reference links directly from SKILL.md. Avoid reference-→-reference chains: the agent may only skim a file reached through another, and miss it.
- **Say when to load each file**, not just that it exists. "Score each signal as per `evaluating-…md`" at the point of scoring beats a generic "see references for details."
- **Table of contents for any reference over ~100 lines**, so a partial read still reveals the file's full scope.
- **Front-load references only when shared definitions are load-bearing — and say why.** Some skills can load references on demand. Others cannot: when the quality of the output depends on the agent using *the project's* definition of a term rather than its own, the agent must read those references end-to-end before it acts. State the reason, because it is not obvious and the failure is silent:

  > Read every reference front to back before detecting. You arrive with strong priors about what a "signal" is, what it means to "evaluate" one, and how to "document" it — and if you act on those priors instead of these references, you will produce plausible, well-formatted, wrong output. A fabricated or mis-scored signal is indistinguishable from a real one downstream, so the mistake is never caught. The references overwrite your assumptions with ours; that is their whole purpose.

  Put that rationale in the skill so the agent understands the stakes of skipping, not merely the instruction to read.

---

## Authoring checklist

Before calling a skill done:

- [ ] `name` matches the directory; `description` is third-person, pushy on *when*, and has negative triggers.
- [ ] "Why this skill exists" names the default failure the skill prevents.
- [ ] Critical constraints are few and each carries its reason.
- [ ] Workflow is imperative, ordered, with interactive vs. autonomous steps marked and risky steps gated.
- [ ] Every path/schema/rule has exactly one home; the body points, never restates.
- [ ] References are one level deep, each with a when-to-read note; files over ~100 lines have a TOC.
- [ ] Where shared definitions are load-bearing, the read-front-to-back instruction carries its rationale.
- [ ] Examples are illustrative-only; in-scope and out-of-scope both shown.
- [ ] Imperative voice, one term per concept, no time-sensitive text, forward-slash paths.
- [ ] SKILL.md under ~500 lines; depth pushed to references.
- [ ] `evals/evals.json` has ≥2 cases, including a should-not-trigger.


---
## ⁠8. References

- Skill Authoring Best Practices — Anthropic: [https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Best Practices for Skill Creators: [https://agentskills.io/skill-creation/best-practices](https://agentskills.io/skill-creation/best-practices)
- Agent Skills Best Practices, Complete Guide: [https://claudeskills.info/blog/agent-skills-best-practices/](https://claudeskills.info/blog/agent-skills-best-practices/)

