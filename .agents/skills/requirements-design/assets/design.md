# Technical design: capability name

Adapt to the repository. Cover material requirements and risks; do not fill irrelevant fields merely to complete a checklist.

## Requirement coverage

| Requirement | Design decision/component | Observable verification |
| --- | --- | --- |
| FR-001 | Concrete mechanism and ownership | Relevant acceptance/check |

## Execution path and contracts

Describe the end-to-end flow, affected interfaces/consumers, validation, authorization/scope, and errors. Where relevant, capture verified operational baseline facts (global middleware or interceptors, CI/release allowlists, config/schema bootstrap behavior, and target-environment routing, auth, or ingress) and include data ownership, state/transactions, idempotency, concurrency, retry/cancellation, recovery, and audit.

## Decisions and verification

Record consequential choices, trade-offs, affected compatibility, and the smallest runnable path. Identify concrete tests/runtime/UI/package checks and the evidence they establish. When parallel worktrees are planned, add a brief **Shared-file boundaries** note defining minimal non-overlapping anchors in shared hotspot files.

## Remaining boundaries

Separate implementation blockers, deploy-time prerequisites, and external business acceptance. State impact, owner, and next action; do not imply environment permissions or readiness.
