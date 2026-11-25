# Agent Delivery Workflow

[简体中文](README.zh-CN.md)

An agent- and model-agnostic workflow pack for completing observable software outcomes. One main agent owns exploration, necessary design, implementation, integration, and verification. Use subagents or external worker sessions only when independent context, parallel work, isolated ownership, or review adds value.

This replaces the historical AgentTeam experiment. The former skills, role graph, slice-plan formats, validators, and duplicate templates have been removed. There are no compatibility aliases or migration adapters. Historical versions remain in Git. [MIT License](LICENSE).

## Choose a skill

| Skill | Use it for |
| --- | --- |
| [software-delivery](.agents/skills/software-delivery/SKILL.md) | Implementing or fixing a capability through its end-to-end acceptance. Default for ordinary development, plus optional coordinated parallel worktree delivery. |
| [requirements-design](.agents/skills/requirements-design/SKILL.md) | Design-only work, operational baseline inspection, and material product, architecture, or contract decisions. Reuse adequate existing documents. |
| [release-readiness](.agents/skills/release-readiness/SKILL.md) | Assessing the exact release candidate and separating repository checks, prerequisites, deployment, and business acceptance. |

A clear small fix can be completed directly without a new planning document or agent. Large work may use a short plan of independently useful outcomes; it does not require a dedicated implementer or a commit for each internal step. Parallel multi-feature or high-risk work may optionally add pre-coding design cross-review, isolated worktrees with shared-file contracts, and tiered review/rework loops.

## Use in a repository

1. Read the target repository's own instructions. Copy the needed folders from `.agents/skills/` into its `.agents/skills/`, with their resources intact. Each skill is independently usable across coding agents and models.
2. Optionally copy [delivery-reviewer.toml](.codex/agents/delivery-reviewer.toml) into `.codex/agents/` for independent review. Built-in or external reviewers remain usable; this pack does not hardcode models, agents, thread limits, sandbox policies, or Goals.
3. Merge relevant workflow guidance from [AGENTS.md](AGENTS.md), preserving the target's architecture, authority, permissions, and release rules. Discover commands and paths from actual evidence as needed; no full-profile bootstrap is required.
4. Ask for the outcome and acceptance, for example: `Use $software-delivery to fix the failing save workflow and verify the affected success and failure paths.`

Skill templates live only under their owning skill's `assets/`. Adapt them when useful; do not create documents just to fill a template. Role instructions request behavior and do not create an independent read-only sandbox; prefer host-enforced sandboxes when available.

## Delivery discipline

- Integrate the smallest runnable end-to-end path early, then finish required behavior and meaningful failure checks. For consequential changes, inspect global middleware, CI/release allowlists, config/schema bootstrap, and environment routing before freezing design.
- Delegate bounded independent tasks rather than copying an organization chart into agents. Keep one writer per worktree, coordinate shared runtime state, and define shared-file contracts before parallel worktrees diverge.
- Keep commit ownership aligned with isolation: delegated writers in a shared worktree do not stage or commit; implementers in dedicated isolated worktrees may commit to their feature branches, while the coordinator owns main-branch integration and cleanup.
- Use independent review (and complementary perspectives when available) for consequential risk or when required. Triage findings before rework, gate rework on `BLOCKING`/`MAJOR` defects with resumable sessions and bounded rounds, and use incremental re-review on follow-up rounds.
- Report upfront if a user-requested coding agent, model, or reasoning tier cannot be targeted explicitly; never silently substitute another.
- Reuse evidence while relevant code/diff, configuration, environment, and data assumptions hold. The coordinator performs the final critical check (plus available UI/smoke checks after merge) without automatically running every suite in every role.
- Keep a short checkpoint only for useful recovery/handoff. Update on material events; store raw evidence in artifacts and batch routine status updates with the work.
- Missing external evidence blocks dependent work or claims only. Deployment and live mutations require explicit authority; local tests do not prove production acceptance.

## Check the pack

Requires Python 3.11+ and the development dependencies. From the repository root:

```sh
python -m pip install -r requirements-dev.txt
python scripts/check_pack.py
python -m unittest discover -s tests -v
```

To check a separately copied skill: `python scripts/check_pack.py --skill /path/to/software-delivery`.

The checker validates packaging, metadata, and local resource links. It does not judge design semantics, authorize operations, or establish business acceptance. [Behavioral evaluation cases](tests/scenarios.md) cover task routing, evidence reuse, external gaps, and coordination behavior. [Requirements](docs/requirements.md) and [design](docs/design.md) explain this replacement.

Measure future workflow changes by cost/time per accepted outcome, first end-to-end pass, and rework/regressions under matched conditions. This revision does not claim measured token savings or delivery speedups.
