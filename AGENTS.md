# Codex Delivery Workflow

## Repository facts

This repository authors reusable Codex instructions and skills; it is not an application or deployment tool. The primary branch is `main`. Skills and their single-source resources live in `.agents/skills/`; the optional reviewer is in `.codex/agents/`. Requirements and design for this replacement live in `docs/`. Package checks are in `scripts/`, and tests/evaluation cases are in `tests/`.

Use Python 3.11+ with `requirements-dev.txt`. Run `python scripts/check_pack.py` and `python -m unittest discover -s tests -v`. There is no application build, database, UAT environment, or production release in this pack. No repository task grants permission to change another repository, user-level configuration, or an external system.

All rules in this file must be written in English. Preserve unrelated work and inspect status before edits and staging. Unless the user requests otherwise, commit cohesive verified changes; batch routine status updates with the work. Do not create progress-only commits.

## Choose the smallest sufficient route

- For a small, clear fix, implement directly, verify affected behavior, inspect the delta, and commit when authorized. No new planning document or subagent is required.
- For an ordinary capability, the main agent owns exploration, necessary design, implementation, integration, and acceptance. Use `software-delivery`. Reuse current sources and resolve reversible technical choices without another approval round.
- For design-only work or material product, architecture, or contract uncertainty, use `requirements-design`. Keep requirements and technical design separate; resolve implementation blockers before dependent code. Continue implementation only when already authorized.
- For large work, use a short outcome-based plan and dependency order. Keep one continuous owner rather than a fixed agent per layer. Use `release-readiness` only for a release decision or authorized release work.

## Delegate selectively

Use subagents when a bounded independent context, parallel investigation, isolated implementation, or independent review materially improves the result. Prefer batching independent tool operations in the main loop first. Give each delegated task a specific result, necessary context, path/state ownership, permissions, and stopping condition; return compact findings and artifact links.

Keep one writer per worktree. Isolated writers must also avoid shared runtime/database/port/output state. The main agent owns integration, staging, and commits; delegated writers do not stage or commit. Use the optional `delivery-reviewer`, another available reviewer, or a suitable independent agent for material correctness/authorization/persistence/compatibility risk and when review is explicitly required. Role instructions are behavioral limits, not independent permission sandboxes.

Do not require a fixed team, mandatory agent handoffs, a Goal tool, or a commit per internal step. Honor actual tool availability, invocation conditions, and higher-priority authorization rules. If a required review or check is unavailable, report that limit and do not claim it occurred.

## Evidence, state, and completion

Define observable completion and integrate the smallest runnable end-to-end path early. Passing local tests does not establish external runtime, deployment, or business acceptance. Missing evidence blocks dependent work or claims only. Never infer authority to deploy, publish, change grants, or mutate live data.

Reuse verification while its relevant code/diff, configuration, environment, and data assumptions remain valid. Recheck affected evidence after those inputs change. Independent reviews cover the actual task delta, including new files and pre-existing worktree changes; acceptance binds to that content and expires after material changes. The main agent performs the final critical check before committing without rerunning every suite by default.

Maintain a short checkpoint only when recovery or handoff needs it. Update on meaningful decisions, completed acceptance, new blockers, or handoff. Reference original artifacts instead of copying logs. Do not poll, wake agents, or edit status merely to restate unchanged progress; honor a user-requested reporting cadence. Report working outcomes, verification, commit, and material limits.

## Using these assets elsewhere

Copy the needed skill folders with their resources, and optionally the reviewer role. Read the target repository's own instructions first. Merge only relevant workflow rules; never replace its authority, architecture, permission, or release rules. Discover actual commands and paths from that repository as needed; retain consequential unknowns explicitly. No full repository-profile bootstrap is required before a bounded task.
