---
name: software-delivery
description: Implement or fix a software capability through an observable end-to-end result, relevant verification, and a cohesive commit. Use for implementation work; use requirements-design for design-only requests and release-readiness for release assessment.
---

# Software Delivery

Keep one main agent accountable for the complete result. Target repository instructions and the user's scope and authorization govern the work.

## Start with the outcome

Read applicable repository instructions and inspect the current branch and working changes. Name the observable result, exclusions, affected path, permitted environments, and how completion will be demonstrated. Preserve unrelated edits, including staged and new files.

Use the smallest sufficient process. A clear small fix needs no new planning document or subagent. For ordinary capabilities, reuse current requirements/design and resolve reversible implementation choices. Material product ambiguity, contract changes, or architectural decisions need separate requirements and design before the dependent implementation; use the repository's format or the requirements-design skill if available. A design-only request does not authorize implementation.

For large work, track independently useful outcomes and dependencies in one short plan. Keep ownership continuous; do not split by directory, team, or technical layer alone. Do not require a fresh agent, a Goal tool, or a commit for every internal step. Use special tools only when available and their invocation conditions and user authorization are satisfied.

## Deliver and integrate

Trace the relevant execution path from user or caller through affected services/data and back. Establish the smallest runnable end-to-end path early, then complete the required success, failure, authorization, and recovery behavior. Test real risks and contracts rather than mirroring implementation. Unit tests do not replace required runtime, database, UI, or packaging acceptance.

Batch independent tool reads/checks in the main loop before introducing another agent. Delegate only when an independent context, a genuinely parallel investigation, an isolated implementation, or an independent review materially helps. Give it one bounded result, necessary sources, path/state ownership, permissions, stopping condition, and compact return format. Use built-in roles or an available project role; no named role is required. Keep one writer per worktree and coordinate shared services, databases, ports, and output directories. Retain integration ownership in the main agent.

Use an independent review for material authorization, money, persistence, migration, compatibility, concurrency, or similarly consequential risk, or when repository rules/user instructions require it. Pass requirements and the actual complete change, including new files and the pre-existing worktree baseline. The reviewer checks the change before consulting the implementation narrative. Review acceptance binds to that content; material changes invalidate it. If independent review is required but unavailable, report that limit instead of claiming it happened.

## Verify without repeating work

Reuse passing evidence only while the relevant code/diff, configuration, environment, and data assumptions remain valid. Capture enough identity to tell when it expires; a commit SHA alone does not identify uncommitted content or changing runtime state. Recheck affected evidence after those inputs change. Reviewers inspect coverage and reproduce doubts; the main agent performs the final critical check, without automatically running every suite three times.

External gaps block only dependent work or claims. Continue authorized independent implementation; identify the missing permission, decision, or evidence and its next action. Do not substitute a mock for real acceptance or infer authority to deploy, publish, or mutate live systems.

## Keep state small and finish

Use [the checkpoint example](assets/checkpoint.md) only when interruption or handoff makes it useful. Update on a changed decision, completed acceptance, new blocker, or handoff. Keep raw logs/test output in artifacts and link to them; do not transcribe tool traces or poll unchanged state to generate progress. Notify on meaningful changes, completion, failure, or required user action; honor explicitly requested reporting cadence. Batch routine status updates with cohesive work.

Inspect the full task delta and staged diff, run the final critical verification, and commit a cohesive verified change when repository/user instructions authorize commits. A delegated writer returns its artifacts without staging or committing. Report what works, how it was verified, the commit if any, and material remaining limits. Local completion, release prerequisites, deployment, and business acceptance are separate claims.
