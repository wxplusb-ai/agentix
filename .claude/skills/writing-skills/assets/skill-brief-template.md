# Skill Brief: <skill-name>

Working document for the skill author. Not shipped with the skill.

## Goal

<One or two sentences: what the agent accomplishes when this skill runs, and why it needs a skill to do it well.>

## Trigger

- Should trigger: <explicit requests, implicit phrasings, file types or contexts>
- Should not trigger: <adjacent tasks and where they belong instead>

## Inputs

| Input | Source | Required | Notes |
|---|---|---|---|
| <name> | <user prompt, file, tool, prior step> | <yes/no> | <format, constraints> |

## Output

| Artifact | Location | Format |
|---|---|---|
| <name> | <path or "in response"> | <structure or template> |

## Success criteria

Each criterion must be observable in the output or transcript. "It works" is not a criterion.

- <criterion>

## Failure modes to mitigate

What a capable agent gets wrong without this skill, and how the skill will prevent it.

| Failure mode | Why it happens | Mitigation in the skill |
|---|---|---|
| <failure> | <cause> | <instruction, template, script, or validation gate> |

## Assumptions

- <anything inferred rather than stated by the user>
