# Evaluating a Skill

A skill's value is the difference between agent behavior with it and without it. Evaluation measures that difference so changes to the skill are driven by observed behavior rather than assumptions.

## Develop against evaluations

1. **Write scenarios first.** Before writing extensive instructions, write three to five scenarios with concrete inputs and expected behavior. This keeps the skill aimed at real gaps rather than imagined ones.
2. **Set a baseline.** Run each scenario without the skill and record the specific failures. If the agent already succeeds without the skill, the skill may be unnecessary, or it should target a narrower gap.
3. **Write the minimum.** Add only the instructions needed to fix the baseline failures and meet the success criteria.
4. **Iterate on observed behavior.** Run with the skill, compare with the baseline, read the transcripts, refine, repeat.
5. **Test every target model and executor.** Guidance that suffices for a stronger model may underserve a weaker one.

## Scenario coverage

Include each of these types:

| Type | Purpose |
|---|---|
| Explicit trigger | The user names the task directly. Tests the core workflow. |
| Implicit trigger | The user describes the need without the obvious keywords. Tests description recall. |
| Negative trigger | An adjacent task that should not load the skill. Tests description precision. |
| Edge case | Missing input, unusual format, or a branch in the workflow. Tests robustness. |

Make scenarios realistic: real file types, real phrasing, the level of detail an actual user gives. Vary them so the skill cannot pass by overfitting to one shape of request.

## Metrics

| Metric | Definition | How to measure |
|---|---|---|
| Trigger recall | Share of should-trigger scenarios where the skill loads | Check the transcript for the skill being loaded |
| Trigger precision | Share of loads that were on should-trigger scenarios | Same, across negative scenarios |
| Success criteria pass rate | Share of success criteria met per run | Scripted assertions where objective; rubric otherwise |
| Baseline delta | Pass rate with skill minus pass rate without | Same scenarios, same model, both conditions |
| Instruction adherence | Share of workflow steps actually followed | Transcript review against the checklist |
| Efficiency | Tokens, tool calls, or wall time per run | Harness logs; compare with baseline |
| Consistency | Variance of pass rate across repeated runs | Several runs per scenario |

Prefer scripted assertions for anything objective (file exists, schema valid, name matches directory). Use a rubric, graded by a human or a model, for judgment qualities such as clarity or appropriate scope. Write rubric criteria so two graders would agree.

## Read the transcript

Final outputs hide the most useful signals:

- **Wasted exploration** usually means instructions are too vague or a needed fact is missing.
- **Ignored instructions** usually mean they are not prominent enough, or they did not seem to apply to the case.
- **Repeated identical work across runs** (for example, writing the same helper each time) is a candidate for a bundled script.
- **The same correction made twice** should become part of the skill, as a general principle rather than a patch for that case.

## Evaluating the skill-writing output itself

When the skill under evaluation is a written skill, also score:

- Validator result (`scripts/validate-skill.py` exit code and warnings).
- Review checklist items met (best-practices section 10).
- Body length and token cost of SKILL.md relative to the behavior it changes.
