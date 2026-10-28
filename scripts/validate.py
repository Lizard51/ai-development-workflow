#!/usr/bin/env python3
"""Validate the skill distribution; does not evaluate model behavior."""

import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("ai-development-workflow", "grilling", "domain-modeling")
REQUIRED = (
    "README.md", "README.en.md", "LICENSE", "THIRD_PARTY_NOTICES.md",
    "CONTRIBUTING.md", "CHANGELOG.md", "docs/installation.md",
    "docs/examples.md", "docs/validation.md", ".github/workflows/validate.yml",
    "skills/ai-development-workflow/references/workflow.md",
    "skills/ai-development-workflow/references/model-routing.md",
    "skills/domain-modeling/ADR-FORMAT.md",
    "skills/domain-modeling/CONTEXT-FORMAT.md",
) + tuple(
    f"skills/ai-development-workflow/assets/{name}.template.md"
    for name in ("SPEC", "PLAN", "TASKS", "STATUS", "VALIDATION")
)


def prose(text):
    """Remove fenced examples before resolving Markdown links and headings."""
    output = []
    marker = None
    for line in text.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence:
            token = fence.group(1)
            if marker is None:
                marker = token
            elif token[0] == marker[0] and len(token) >= len(marker):
                marker = None
            continue
        if marker is None:
            output.append(line)
    return "\n".join(output)


def anchors(text):
    result, counts = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M):
        slug = "".join(
            char for char in heading.lower()
            if char in " -_" or unicodedata.category(char)[0] in "LN"
        ).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def validate(root):
    root = Path(root).resolve()
    errors = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    for name in SKILLS:
        directory = root / "skills" / name
        for relative in ("SKILL.md", "agents/openai.yaml", "LICENSE"):
            if not (directory / relative).is_file():
                errors.append(f"Missing skill resource: {name}/{relative}")
        entrypoint = directory / "SKILL.md"
        if not entrypoint.is_file():
            continue
        try:
            text = entrypoint.read_text(encoding="utf-8")
            match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
            if not match:
                raise ValueError("missing YAML frontmatter")
            metadata = yaml.safe_load(match.group(1))
            if not isinstance(metadata, dict) or metadata.get("name") != name:
                raise ValueError("frontmatter name must match folder")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                raise ValueError("invalid skill name")
            description = metadata.get("description")
            if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
                raise ValueError("description must contain 1-1024 characters")
            ui = yaml.safe_load((directory / "agents/openai.yaml").read_text(encoding="utf-8"))
            interface = ui.get("interface", {})
            for field in ("display_name", "short_description"):
                if not isinstance(interface.get(field), str) or not interface[field].strip():
                    raise ValueError(f"missing interface.{field}")
        except (ValueError, AttributeError, OSError, yaml.YAMLError) as exc:
            errors.append(f"{name}: {exc}")

    texts = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in {".git", ".venv", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        relative = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"Non-UTF-8 or unreadable file: {relative}")
            continue
        texts[path] = text
        for pattern in (
            r"(?i)[A-Z]:[\\/]Users[\\/][^\s/\\]+",
            r"\bgh[pousr]_[A-Za-z0-9]{30,}\b",
            r"\bgithub_pat_[A-Za-z0-9_]{50,}\b",
            r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        ):
            if re.search(pattern, text):
                errors.append(f"Potential private data: {relative}")
                break
        if path.suffix in {".yaml", ".yml"}:
            try:
                yaml.safe_load(text)
            except yaml.YAMLError:
                errors.append(f"Invalid YAML: {relative}")

    for path, text in texts.items():
        if path.suffix != ".md":
            continue
        for destination in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", prose(text)):
            destination = destination.strip().split(' "', 1)[0].strip("<>")
            parts = urlsplit(destination)
            if parts.scheme or parts.netloc:
                continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if root != target and root not in target.parents:
                errors.append(f"Link escapes package: {path.relative_to(root)} -> {destination}")
            elif not target.exists():
                errors.append(f"Broken link: {path.relative_to(root)} -> {destination}")
            elif parts.fragment and target.suffix == ".md":
                if unquote(parts.fragment) not in anchors(texts.get(target, "")):
                    errors.append(f"Broken anchor: {path.relative_to(root)} -> {destination}")
    return errors, len(texts)


if __name__ == "__main__":
    failures, count = validate(ROOT)
    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        sys.exit(1)
    print(f"PASS: {len(SKILLS)} skills, {count} text files; metadata, resources, links, and private-data patterns checked.")
