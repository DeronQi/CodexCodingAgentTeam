"""Check distributable resources and metadata, never semantic delivery readiness."""

from __future__ import annotations

import argparse
from pathlib import Path, PureWindowsPath
import re
import sys
import tomllib
from urllib.parse import unquote, urlsplit

import yaml
from markdown_it import MarkdownIt


def markdown_links(text: str):
    parser = MarkdownIt("commonmark")
    # Inspect all explicit destinations, including schemes the renderer would reject.
    # No HTML is rendered and no destination is opened by this package check.
    parser.validateLink = lambda _destination: True
    pending = list(parser.parse(text))
    while pending:
        token = pending.pop()
        if token.type == "link_open":
            yield token.attrGet("href")
        elif token.type == "image":
            yield token.attrGet("src")
        pending.extend(token.children or [])


def markdown_errors(path: Path, boundary: Path) -> list[str]:
    errors = []
    for link in markdown_links(path.read_text(encoding="utf-8")):
        url = urlsplit(link)
        if url.scheme in {"https", "http", "mailto"}:
            continue
        target = unquote(url.path)
        if url.scheme or url.netloc or target.startswith(("/", "\\")) or PureWindowsPath(target).is_absolute():
            errors.append(f"{path}: resource must use a portable relative path: {link}")
            continue
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(boundary.resolve()):
            errors.append(f"{path}: resource escapes its package: {link}")
        elif not resolved.exists():
            errors.append(f"{path}: missing resource: {link}")
    return errors


def read_yaml(text: str, path: Path, errors: list[str]) -> dict:
    try:
        value = yaml.safe_load(text)
    except yaml.YAMLError as error:
        errors.append(f"{path}: invalid YAML: {error}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path}: expected a YAML mapping")
        return {}
    return value


def check_skill(folder: Path) -> list[str]:
    errors: list[str] = []
    entry = folder / "SKILL.md"
    if not entry.is_file():
        return [f"{folder}: missing SKILL.md"]
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", entry.read_text(encoding="utf-8"), re.S)
    if not match:
        return [f"{entry}: missing YAML frontmatter"]
    metadata = read_yaml(match.group(1), entry, errors)
    name = metadata.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"{entry}: invalid skill name")
    elif name != folder.name:
        errors.append(f"{entry}: name must match its distribution folder")
    if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
        errors.append(f"{entry}: description must be nonempty text")
    interface_path = folder / "agents" / "openai.yaml"
    if interface_path.exists():
        interface = read_yaml(interface_path.read_text(encoding="utf-8"), interface_path, errors).get("interface", {})
        if not isinstance(interface, dict):
            errors.append(f"{interface_path}: interface must be a mapping")
        else:
            for key in ("display_name", "short_description", "default_prompt"):
                if not isinstance(interface.get(key), str) or not interface[key].strip():
                    errors.append(f"{interface_path}: missing interface.{key}")
            prompt = interface.get("default_prompt")
            if isinstance(name, str) and isinstance(prompt, str) and f"${name}" not in prompt:
                errors.append(f"{interface_path}: default_prompt must name ${name}")
    for path in sorted(folder.rglob("*.md")):
        errors.extend(markdown_errors(path, folder))
    return errors


def check_pack(root: Path) -> list[str]:
    errors: list[str] = []
    skills_root = root / ".agents" / "skills"
    folders = [p for p in sorted(skills_root.glob("*")) if p.is_dir() and any(f.is_file() for f in p.rglob("*"))]
    if not folders:
        errors.append(f"{skills_root}: no skills found")
    names: set[str] = set()
    for folder in folders:
        errors.extend(check_skill(folder))
    for path in sorted((root / ".codex" / "agents").glob("*.toml")):
        try:
            agent = tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as error:
            errors.append(f"{path}: invalid TOML: {error}")
            continue
        for key in ("name", "description", "developer_instructions"):
            if not isinstance(agent.get(key), str) or not agent[key].strip():
                errors.append(f"{path}: missing agent {key}")
        name = agent.get("name")
        if isinstance(name, str):
            if name in names:
                errors.append(f"{path}: duplicate agent identity: {name}")
            names.add(name)
        for key in ("sandbox_mode", "approval_policy", "model_provider", "mcp_servers"):
            if key in agent:
                errors.append(f"{path}: {key} cannot override inherited session settings")
    for path in (root / "AGENTS.md", root / "README.md", root / "README.zh-CN.md"):
        if path.exists():
            errors.extend(markdown_errors(path, root))
    for path in sorted((root / "docs").rglob("*.md")):
        errors.extend(markdown_errors(path, root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--skill", type=Path, help="Check one independently copied skill instead of a pack")
    args = parser.parse_args()
    try:
        errors = check_skill(args.skill.resolve()) if args.skill else check_pack(args.root.resolve())
    except (OSError, ValueError) as error:
        print(f"Package check failed: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: package metadata and local resource links; semantic readiness is not evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
