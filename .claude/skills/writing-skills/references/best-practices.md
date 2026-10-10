# Skill-Writing Best Practices

## Contents

1. Authoring mindset
2. Frontmatter for discoverability
3. Specific procedural instructions
4. Degrees of freedom
5. Progressive disclosure
6. Workflows and feedback loops
7. Durable content
8. Skills that ship code
9. Anti-patterns
10. Review checklist
11. Sources

---

## 1 Authoring mindset

Three principles govern every decision below. When a case is not covered later, decide it from these.

- **Generalize; don't overfit.** A skill is written once and used across many prompts. When iterating on a few familiar examples, it is tempting to patch the skill so it passes those cases. Resist it. Avoid fiddly example-specific fixes and oppressive all-caps MUSTs. When an issue is stubborn, try a different metaphor or a different working pattern rather than another constraint; it is cheap to try and often lands better.
- **Keep it lean.** The context window is a shared budget. Add only what the model does not already know, and challenge each sentence to justify its tokens: would the agent get this wrong without it? If not, cut it. A capable model does not need PDFs explained. Read transcripts, not just final outputs: if the skill makes the model waste effort, remove the part causing it and observe the result.
- **Explain the why.** Modern models have good theory of mind and, given a good harness, go well beyond rote instructions. Transmit reasoning, not just rules. An all-caps ALWAYS or NEVER, or a rigid structure, is a yellow flag: reframe it as the reason the requirement matters. Understanding generalizes to edge cases; a bare command does not.

## 2 Frontmatter for discoverability

The `name` and `description` are the only fields the agent sees before triggering a skill. If they are vague, the skill is invisible.

- **Name:** 1 to 64 characters; lowercase letters, numbers, and hyphens only; no leading, trailing, or consecutive hyphens; exactly matches the parent directory (`angular-testing/SKILL.md` has `name: angular-testing`). Prefer an action or gerund form. Avoid vague names such as `helper` or `tools`.
- **Description:** at most 1,024 characters, third person, stating what the skill does and when to use it, including negative triggers. Lean toward being explicit about the "when", since agents tend to under-trigger. A useful pattern: `<what it does>. Use when <triggers, including an implicit phrasing>. Not for <adjacent tasks>.`
    - Bad: "React skills." (too vague)
    - Good: "Creates and builds React components using Tailwind CSS. Use when the user wants to update component styles or UI logic. Don't use for Vue, Svelte, or vanilla CSS projects."

## 3 Specific procedural instructions

Write for an agent, not a human reader.

- **Imperative voice.** Frame instructions as direct commands ("Extract the text"), not "I will extract" or "The agent should extract". Keep one voice throughout.
- **Numbered steps and explicit decision points.** Define the workflow as a chronological sequence and map each branch clearly ("Step 2: if you need source maps, run `ng build --source-map`; otherwise skip to Step 3").
- **Concrete templates.** Agents pattern-match structure more reliably than they parse adjectives. Rather than describe an output format in prose, place a template in `assets/` and instruct the agent to copy its structure. Short templates can stay inline.
- **Consistent, domain-specific terminology.** Pick one term per concept and use it throughout. Prefer the most specific term native to the domain (in Angular, "template", not "html", "markup", or "view"). Inconsistent vocabulary makes the agent guess whether two names mean the same thing.
- **One source of truth per fact.** State each path, schema, or rule in one place and point to it elsewhere. Duplicates drift apart and then contradict each other.
- **Mark examples as illustrative.** An unlabeled example is likely to be copied verbatim into a real task.

## 4 Degrees of freedom

Calibrate specificity to how fragile and variable the task is. Picture the model as a robot crossing terrain.

| Terrain | When | Express as |
|---|---|---|
| Open field (high freedom) | Many valid paths; decisions depend on context | Text heuristics; describe what good looks like and trust the model |
| Established trail (medium freedom) | A preferred pattern exists; some variation is fine | Pseudocode or a parameterized template |
| Narrow bridge over cliffs (low freedom) | Fragile, consistency-critical, one sequence must hold | An exact command or script with few or no parameters, and an instruction not to deviate |

Over-constraining an open task wastes tokens and suppresses judgment; under-constraining a fragile one invites errors. Most skills contain more than one kind of terrain, so calibrate each section separately.

## 5 Progressive disclosure

Only the frontmatter is always loaded. The SKILL.md body loads when the skill triggers. Bundled files load only when the body sends the agent to them. Design around that.

- SKILL.md is a table of contents and runtime procedure, not the whole manual. Keep its body under 500 lines and push depth into bundled files.
- Keep references **one level deep** from SKILL.md. The model may preview nested files with partial reads and miss content, so a referenced file must not point onward to another for essential information.
- Organize bundled files by domain so an unrelated request never loads irrelevant context.
- Put a table of contents at the top of any reference file over about 100 lines, so its full scope is visible even on a partial read.
- Say **when** to read each file, at the step where it matters, not just that it exists.
- State whether the model should **execute** a file or **read it as reference**. The two intents are easy to confuse and costly to get wrong.
- When the output depends on the agent using the skill's definitions rather than its own priors, tell it to read the reference in full before acting, and say why. A plausible output built on the wrong definition looks correct and is rarely caught.

## 6 Workflows and feedback loops

- For multi-step tasks, give an explicit numbered sequence.
- For complex tasks, provide a checklist the model copies into its response and ticks off. This prevents skipped steps.
- Where output quality matters, install a loop: produce, validate, fix, repeat, and proceed only when validation passes. The validator can be a script or a reference document the model checks against.
- For batch or high-stakes operations, insert a verifiable intermediate output: have the model emit a structured plan, validate the plan, then execute, so errors surface before they propagate.
- Mark steps that pause for a human versus steps that run autonomously.

## 7 Durable content

Exclude time-sensitive statements that will silently go stale ("as of this year", "the new API"). If legacy behavior must be recorded, isolate it in a clearly labeled "old patterns" section so it does not contaminate the current path.

## 8 Skills that ship code

- **Solve, don't punt.** Handle error conditions inside scripts rather than failing and leaving the model to improvise.
- **No voodoo constants.** Justify and document every configuration value; an unexplained constant is one the model cannot reason about.
- **Declare dependencies.** Do not assume a package is installed. State required packages and confirm they exist in the target environment, which may have no network access.
- **Fully qualify MCP tool names** as `ServerName:tool_name`. An unqualified name can fail to resolve when several servers are present.
- **Use forward slashes** in all paths. Backslash paths break on Unix.

## 9 Anti-patterns

| Anti-pattern | Why it hurts | Instead |
|---|---|---|
| Too many options | The agent stalls or picks inconsistently | One default, with at most a one-clause escape hatch |
| Deeply nested references | Content reached through another file is often only skimmed | Link every reference directly from SKILL.md |
| Assuming installation or environment | Scripts fail in environments without the package or network | Verify and state requirements |
| Windows-style paths | Break on Unix | Forward slashes |
| MUST-soup | The agent cannot prioritize or adapt at the edges | Give the reason; reserve absolute language for the few inviolable rules |
| Explaining the obvious | Spends shared context on what the model knows | Cut it |
| Restating a source of truth | Copies drift and contradict | Point to the single home |
| Copy-ready examples | The agent imports example specifics into real tasks | Label examples illustrative |
| Example-specific patches | The skill passes test cases and fails new ones | Fix the method, not the case |

## 10 Review checklist

- [ ] `name` matches the directory and follows the format rules.
- [ ] `description` is third person, says what and when, names negative triggers, and is under 1,024 characters.
- [ ] The body says what goes wrong by default and how the skill prevents it.
- [ ] Every sentence would change the agent's behavior if removed.
- [ ] Each hard constraint carries its reason; absolute language is rare.
- [ ] The workflow is numbered and imperative, with branches mapped and quality gates in place.
- [ ] Freedom level fits each section's fragility.
- [ ] Each fact lives in one place.
- [ ] References are one level deep, each with when-to-read and read-or-execute guidance; long files have a table of contents.
- [ ] Output formats are shown as templates, not described in prose.
- [ ] Terminology is consistent and domain-specific.
- [ ] No time-sensitive text; forward-slash paths; dependencies declared.
- [ ] Examples are labeled illustrative and include out-of-scope cases.
- [ ] Every instruction traces to a scenario, a baseline failure, or a success criterion.

## 11 Sources

Background reading for the skill author. The agent does not need to fetch these.

- Anthropic, Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Agent Skills, Best practices for skill creators: https://agentskills.io/skill-creation/best-practices
- Agent Skills best practices, complete guide: https://claudeskills.info/blog/agent-skills-best-practices/
