# Evaluation Methods: <skill-name>

## Purpose

<What the skill is supposed to change about agent behavior, in one or two sentences.>

## Approach

- Comparison: with skill vs. without skill, same prompts, same model.
- Models and executors tested: <list every model and harness the skill will run on>
- Runs per scenario: <number, and why that is enough to see variance>
- Grading: <scripted assertions, rubric graded by a human, rubric graded by a model, or a mix>

## Scenarios

| ID | Type | Prompt and inputs | Expected behavior |
|---|---|---|---|
| S1 | should trigger | <prompt> | <observable behavior> |
| S2 | should trigger (implicit) | <prompt> | <observable behavior> |
| S3 | should not trigger | <prompt> | <skill not loaded; correct alternative taken> |

## Baseline

Observed (or predicted, if labeled) failures without the skill.

| Scenario | Failure | Observed or predicted |
|---|---|---|
| <ID> | <what went wrong> | <observed/predicted> |

## Metrics

| Metric | Definition | How measured | Target |
|---|---|---|---|
| Trigger precision | <definition> | <method> | <target> |
| Trigger recall | <definition> | <method> | <target> |
| Success criteria pass rate | <definition> | <method> | <target> |
| <skill-specific metric> | <definition> | <method> | <target> |

## Results

| Scenario | Without skill | With skill | Notes from transcript |
|---|---|---|---|
| <ID> | <result> | <result> | <wasted steps, ignored instructions, surprises> |

## How to rerun

<Exact steps or command to rerun the evaluation after the skill changes.>
