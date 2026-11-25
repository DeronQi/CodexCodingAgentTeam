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

Batch independent tool reads/checks in the main loop before introducing another agent. Delegate only when an independent context, a genuinely parallel investigation, an isolated implementation, or an independent review materially helps. Give it one bounded result, necessary sources, path/state ownership, permissions, stopping condition, and compact return format. Use built-in roles or an available project role; no named role or specific agent/model is required. Report upfront if a user-requested agent, model, or reasoning tier cannot be targeted explicitly instead of silently substituting another.

For parallel implementation, the coordinator creates and assigns dedicated isolated `git worktree` checkouts and feature branches, coordinates shared local runtime dependencies, databases, ports, and output directories, and establishes a **shared-file contract** (keep new logic and tests in separate modules where practical; constrain edits in shared hotspot files such as routes, controllers, views, or CI entrypoints to minimal non-overlapping anchors). Keep one writer per worktree and retain main-branch integration ownership in the coordinator. Prefer runtime read-only isolation for reviewers and workspace-scoped sandboxes for implementers; widen implementer sandbox access only when verified local tooling requires it, with explicit authorization and explicit non-target exclusions.

Use an independent review for material authorization, money, persistence, migration, compatibility, concurrency, or similarly consequential risk, or when repository rules/user instructions require it. When multiple reviewers or complementary agent/model perspectives are available, split focus across complementary concerns (for example, security/concurrency/contracts/CI baseline vs. business logic/edge cases/UI/test coverage) rather than duplicating identical checks. Pass requirements and the actual complete change (`base...HEAD`, including new files and any pre-existing worktree baseline). The reviewer inspects the change before consulting the implementation narrative and classifies real defects as `BLOCKING`, `MAJOR`, or `MINOR` (or `NO_ISSUES`). Review acceptance binds to that content; material changes invalidate it. If independent review is required but unavailable, report that limit instead of claiming it happened.

For review/rework loops, the coordinator triages and verifies reviewer findings against actual code before forwarding consolidated actionable items. Trigger rework only on `BLOCKING` or `MAJOR` findings (`MINOR` style suggestions do not force extra rounds). Resume the original implementer's session/context when supported, cap rework rounds (default max 3) and escalate unresolved `BLOCKING` issues to the user, and use targeted verification of prior findings plus the rework delta on Round 2+ unless rework changes architecture broadly.

## Verify without repeating work

Reuse passing evidence only while the relevant code/diff, configuration, environment, and data assumptions remain valid. Capture enough identity to tell when it expires; a commit SHA alone does not identify uncommitted content or changing runtime state. Recheck affected evidence after those inputs change. Reviewers inspect coverage and reproduce doubts. In coordinated worktree delivery, isolated implementers verify unit and contract checks inside their worktrees; after merging to the main branch, the coordinator runs the final critical regression checks plus available interactive, UI, or cross-component smoke checks before cleanup, without automatically running every suite in every role.

External gaps block only dependent work or claims. Continue authorized independent implementation; identify the missing permission, decision, or evidence and its next action. Do not substitute a mock for real acceptance or infer authority to deploy, publish, or mutate live systems.

## Keep state small and finish

Use [the checkpoint example](assets/checkpoint.md) only when interruption or handoff makes it useful. Update on a changed decision, completed acceptance, new blocker, or handoff. Keep raw logs/test output in artifacts and link to them; do not transcribe tool traces or poll unchanged state to generate progress. Notify on meaningful changes, completion, failure, or required user action; honor explicitly requested reporting cadence. Batch routine status updates with cohesive work.

Inspect the full task delta and staged diff, run the final critical verification, and commit a cohesive verified change when repository/user instructions authorize commits. Commit ownership follows isolation: delegated writers in a shared worktree do not stage or commit; delegated implementers in a dedicated isolated `git worktree` on their own feature branch may commit cohesive local changes to that branch, while the coordinator owns main-branch integration, conflict resolution, merge commits, and safe worktree/branch cleanup. Report what works, how it was verified, the commit if any, and material remaining limits. Local completion, release prerequisites, deployment, and business acceptance are separate claims.
