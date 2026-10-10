# Skills

Project skills for Claude Code. Each skill is a directory, discovered automatically from this folder:

```
<skill-name>/
  SKILL.md          frontmatter (name, description) + runtime procedure
  references/       depth the agent reads on demand
  assets/           templates the agent copies
  scripts/          code the agent executes
```

Convention: kebab-case directory names, and the `name` in frontmatter must match the directory. Only `SKILL.md` is required; add the other folders when a skill needs them.

To create a new skill, use the `writing-skills` skill. Check one with:

```bash
python .claude/skills/writing-skills/scripts/validate-skill.py .claude/skills/<skill-name>
```
