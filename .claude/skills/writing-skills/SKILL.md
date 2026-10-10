---
name: writing-skills
description: Writes a single agent skill (SKILL.md plus any references, assets, or scripts it needs) and a separate evaluation methods document, following skill-writing best practices. Use when the user asks to create, draft, or write a new skill, turn notes or a procedure into a skill, or package a repeatable workflow so an agent can trigger it. Also use when rewriting an existing skill that triggers poorly or behaves inconsistently. Not for writing subagent definitions, slash commands, CLAUDE.md files, or general documentation for human readers.
---

# Writing Skills

Your job is to produce one skill and one evaluation methods document. The request covers exactly one skill; do not design a family of skills or reference skills that do not exist.

## Why this skill exists

A capable model writing a skill without guidance tends to fail in predictable ways:

- **It writes documentation, not instructions.** It explains the domain to a human reader instead of telling an agent what to do, so the skill spends tokens on things the agent already knows.
- **It writes a vague description.** The description is the only text the agent sees before deciding to trigger, so a vague one makes the skill invisible, and one without negative triggers makes it fire on adjacent tasks.
- **It overfits to the examples in front of it.** It encodes the one case the user mentioned instead of the method that generalizes.
- **It commands instead of explaining.** Walls of MUST and NEVER give the agent nothing to reason from at the edges.
- **It skips evaluation.** It ships instructions for imagined gaps instead of observed ones, with no way to tell whether the skill helps.

The workflow below forces the opposite of each.

## Workflow

Copy this checklist into your response and tick it off as you go:

```
- [ ] Step 1: Skill brief complete and confirmed
- [ ] Step 2: Evaluation scenarios and baseline recorded
- [ ] Step 3: Freedom level chosen per section
- [ ] Step 4: Skill files written
- [ ] Step 5: Validator passes and self-review done
- [ ] Step 6: Evaluation methods document written
```

### Step 1: Complete the skill brief

Copy [assets/skill-brief-template.md](assets/skill-brief-template.md) and fill in every field: goal, trigger, inputs, output, success criteria, and failure modes to mitigate. Derive answers from the user's request, notes, and any example skill they supplied.

If the goal, trigger, or output is missing and cannot be inferred, ask the user before continuing; those three fields shape every later decision. Make a reasonable assumption for any other gap and record it in the brief.

The brief is a working document. It is not part of the shipped skill.

### Step 2: Define evaluations before writing instructions

Read [references/evaluation-methods.md](references/evaluation-methods.md). Then:

1. Write three to five scenarios with concrete inputs and expected behavior. Include at least one prompt that should trigger the skill, one implicit phrasing that should also trigger it, and one adjacent prompt that should not.
2. If you can run the task without the skill, do so and record the specific failures as the baseline. If you cannot, predict the baseline failures from the brief's failure modes and label them as predicted.

Write evaluations first because they keep the skill aimed at real gaps. Every instruction you add in Step 4 should trace to a baseline failure or a success criterion.

### Step 3: Choose the degree of freedom for each part

For each part of the task, decide how fragile it is, using the terrain model in [references/best-practices.md](references/best-practices.md) section 4:

- Open field: judgment tasks with many valid paths. Write heuristics and say what good looks like.
- Established trail: a preferred pattern with some variation. Write a parameterized template or pseudocode.
- Narrow bridge: fragile, ordering-critical, or destructive operations. Write exact commands or a script and say not to deviate.

Most skills mix levels. Decide per section, not per skill.

### Step 4: Write the skill files

Read [references/best-practices.md](references/best-practices.md) in full before writing. You arrive with strong priors about what a skill looks like, and several of them (explaining the domain, menus of options, nested references) are the failure modes this skill exists to prevent.

Then write the files using the layout below. Create only the directories the skill actually needs.

```
<skill-name>/
  SKILL.md          frontmatter + runtime procedure, under 500 lines
  references/       depth the agent reads on demand
  assets/           templates the agent copies
  scripts/          code the agent executes
```

Write SKILL.md in this order, omitting sections the skill does not need:

1. Frontmatter: `name` and `description`, per best-practices section 2.
2. Title, then one or two sentences on the agent's job and what the skill is not for.
3. Why this skill exists: the mistakes the agent makes by default, and how the skill prevents them.
4. Critical constraints: the few rules that invalidate the output if broken, each with its reason.
5. Inputs and outputs: what the caller provides and where each artifact goes, stated once.
6. Workflow: numbered imperative steps with explicit branches and validation gates.
7. References: each bundled file, when to read it, and whether to read or execute it.
8. Examples: in-scope and out-of-scope requests, marked illustrative.

### Step 5: Validate and self-review

Run the validator (execute it; do not read it as reference):

```bash
python scripts/validate-skill.py <path-to-skill-directory>
```

It checks the mechanical rules: name format and directory match, description length, body length, link targets, nested references, missing tables of contents, backslash paths. Fix every error and rerun until it exits 0. Treat warnings as prompts to reconsider, not as failures.

Then review against the checklist at the end of [references/best-practices.md](references/best-practices.md). The validator cannot judge voice, overfitting, or whether each sentence earns its tokens; you must.

If you ran a baseline in Step 2, run the scenarios again with the skill and compare. Revise on observed behavior, then repeat this step.

### Step 6: Write the evaluation methods document

Copy [assets/evaluation-methods-template.md](assets/evaluation-methods-template.md) and fill it in from Step 2 and Step 5: the scenarios, the baseline, the metrics, and how to run them. Save it next to the skill directory, not inside it, because it is for the people maintaining the skill and the agent never needs to load it.

## References

| File | Read when | Use |
|---|---|---|
| [references/best-practices.md](references/best-practices.md) | Before Step 3; in full before Step 4 | Read as reference |
| [references/evaluation-methods.md](references/evaluation-methods.md) | Before Step 2 and Step 6 | Read as reference |
| [assets/skill-brief-template.md](assets/skill-brief-template.md) | Step 1 | Copy and fill in |
| [assets/evaluation-methods-template.md](assets/evaluation-methods-template.md) | Step 6 | Copy and fill in |
| [scripts/validate-skill.py](scripts/validate-skill.py) | Step 5 | Execute; requires Python 3.10+, standard library only |

## Examples

These are illustrative. Do not copy their content into the skill you write.

Use this skill:

- "Write a skill that reviews Terraform plans for risky changes."
- "Turn these onboarding notes into something the agent can pick up automatically."
- "Our PDF extraction skill never triggers. Can you rewrite it?"

Do not use this skill:

- "Create a subagent that reviews PRs." Write an agent definition instead.
- "Add a /deploy slash command." Write a command file instead.
- "Write a README for this repo." That is human documentation.
