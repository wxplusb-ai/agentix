"""Validate the mechanical rules of an agent skill directory.

Usage: python validate-skill.py <path-to-skill-directory>

Exits 0 when there are no errors (warnings allowed), 1 on errors, 2 on bad usage.
Standard library only, so it runs in environments without network access.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Limits from the Agent Skills specification.
NAME_MAX_CHARS = 64
DESCRIPTION_MAX_CHARS = 1024
# Body length above which SKILL.md should push depth into references.
BODY_MAX_LINES = 500
# Reference files longer than this need a table of contents for partial reads.
TOC_THRESHOLD_LINES = 100

NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TOC_PATTERN = re.compile(r"^#+\s*(contents|table of contents)\b", re.IGNORECASE | re.MULTILINE)
BACKSLASH_PATH_PATTERN = re.compile(r"\b[\w.-]+\\[\w.-]+")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | None:
    """Return (fields, body) or None if no frontmatter block is present."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("\"'")
    body = text[end + 4 :].lstrip("\n")
    return fields, body


def local_links(text: str) -> list[str]:
    """Return relative link targets, ignoring URLs, anchors, and env-var paths."""
    targets = []
    for target in LINK_PATTERN.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith(("#", "$")):
            continue
        targets.append(target.split("#", 1)[0])
    return targets


def check_frontmatter(skill_dir: Path, fields: dict[str, str], errors: list[str]) -> None:
    name = fields.get("name", "")
    if not name:
        errors.append("frontmatter: missing 'name'")
    else:
        if len(name) > NAME_MAX_CHARS or not NAME_PATTERN.match(name):
            errors.append(
                f"frontmatter: name '{name}' must be 1-{NAME_MAX_CHARS} chars of "
                "lowercase letters, digits, and single hyphens"
            )
        if name != skill_dir.name:
            errors.append(f"frontmatter: name '{name}' does not match directory '{skill_dir.name}'")
    description = fields.get("description", "")
    if not description:
        errors.append("frontmatter: missing 'description'")
    elif len(description) > DESCRIPTION_MAX_CHARS:
        errors.append(
            f"frontmatter: description is {len(description)} chars (max {DESCRIPTION_MAX_CHARS})"
        )


def check_description_quality(description: str, warnings: list[str]) -> None:
    lowered = description.lower()
    if "use when" not in lowered and "use for" not in lowered:
        warnings.append("description: no 'Use when' clause; say when the skill should trigger")
    if not re.search(r"\b(not for|don't use|do not use)\b", lowered):
        warnings.append("description: no negative trigger ('Not for ...')")
    if re.search(r"\b(i|we|you)\b", lowered.split(".")[0]):
        warnings.append("description: first sentence is not third person")


def check_bundled_files(skill_dir: Path, body: str, errors: list[str], warnings: list[str]) -> None:
    for target in local_links(body):
        if not (skill_dir / target).exists():
            errors.append(f"SKILL.md: link target '{target}' does not exist")
    for path in sorted(skill_dir.rglob("*.md")):
        if path.name == "SKILL.md":
            continue
        rel = path.relative_to(skill_dir).as_posix()
        text = path.read_text(encoding="utf-8")
        if len(text.splitlines()) > TOC_THRESHOLD_LINES and not TOC_PATTERN.search(text):
            warnings.append(f"{rel}: over {TOC_THRESHOLD_LINES} lines with no table of contents")
        if rel.startswith("references/"):
            nested = [t for t in local_links(text) if t.endswith(".md")]
            if nested:
                warnings.append(f"{rel}: links to other files {nested}; keep references one level deep")


def check_paths(skill_dir: Path, warnings: list[str]) -> None:
    for path in sorted(skill_dir.rglob("*.md")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if BACKSLASH_PATH_PATTERN.search(line):
                rel = path.relative_to(skill_dir).as_posix()
                warnings.append(f"{rel}:{lineno}: possible backslash path; use forward slashes")


def validate(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill_md.as_posix()} not found"], warnings
    parsed = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if parsed is None:
        return ["SKILL.md: missing YAML frontmatter delimited by '---' lines"], warnings
    fields, body = parsed
    check_frontmatter(skill_dir, fields, errors)
    check_description_quality(fields.get("description", ""), warnings)
    body_lines = len(body.splitlines())
    if body_lines > BODY_MAX_LINES:
        errors.append(f"SKILL.md: body is {body_lines} lines (max {BODY_MAX_LINES})")
    check_bundled_files(skill_dir, body, errors, warnings)
    check_paths(skill_dir, warnings)
    return errors, warnings


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    skill_dir = Path(argv[1]).resolve()
    if not skill_dir.is_dir():
        print(f"error: {argv[1]} is not a directory", file=sys.stderr)
        return 2
    errors, warnings = validate(skill_dir)
    for message in errors:
        print(f"ERROR   {message}")
    for message in warnings:
        print(f"WARNING {message}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
