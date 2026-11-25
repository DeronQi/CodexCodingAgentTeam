# Design: Continuous software delivery

## Decisions and traceability

| Requirement | Implementation | Verification |
| --- | --- | --- |
| FR-001 | Proportional routes in AGENTS.md and focused skill descriptions, plus optional coordinated mode for parallel/high-risk work | Small-fix, design-only, and parallel worktree behavioral cases |
| FR-002 | Agent-/model-agnostic delegation, honest routing, shared-file contracts, and isolation-scoped commit ownership | Investigation, parallel worktree, routing-limit, and isolated-writer cases |
| FR-003 | Optional checkpoint and evidence record; event-triggered updates and evidence invalidation rules | Existing-evidence and unchanged-blocker cases |
| FR-004 | Observable acceptance, operational baseline inspection, tiered review/rework with severity gating, and sandbox honesty | External-gate, authorization, and multi-round review cases |
| FR-005 | software-delivery, requirements-design, release-readiness; resources owned inside each skill | Independent-copy and resource-integrity tests |
| FR-006 | Python package checker, unittest negative tests, and bounded independent forward testing | Package tests and evaluator results |

## Boundaries and contracts

- The workflow stays coding-agent- and model-agnostic: roles are defined by capability (coordinator, isolated implementer, independent reviewer) without binding to specific tools or model families. If a requested agent, model, or reasoning tier cannot be routed explicitly, the coordinator reports that limit rather than silently substituting another.
- The main agent chooses a proportional route, owns integration into the target integration branch, conflict resolution, post-integration verification, and verified worktree/branch cleanup. Delegated writers in a shared worktree never stage or commit; delegated implementers in dedicated isolated `git worktree` checkouts (verified against required base/uncommitted inputs) may commit cohesive local changes to their own feature branches under a coordinator-defined shared-file contract.
- Separate requirements and design remain useful when decisions are material, backed by read-only operational baseline checks where relevant (global middleware, CI/release allowlists, config/schema bootstrap, environment routing/auth) and optional pre-coding design cross-review before freezing a baseline. No script can approve their semantics. Existing repository documents take precedence over bundled examples; no exact headings or slice statuses are imposed.
- Tiered review classifies findings as `BLOCKING`, `MAJOR`, or `MINOR` (or `NO_ISSUES`). The coordinator triages findings and triggers resumable rework only for `BLOCKING`/`MAJOR` defects up to a bounded round cap (stopping automatic rework with acceptance pending and escalating any unresolved `BLOCKING` or `MAJOR` findings), using full-delta review on Round 1 and targeted incremental re-review on Round 2+ unless architecture changes broadly. Prefer runtime-enforced read-only isolation for reviewers and workspace-scoped sandboxes for implementers.
- Skills are self-contained folders with YAML metadata, optional assets/references, and UI metadata. Only the optional reviewer uses a standalone TOML agent definition. No config.toml, aliases, migration adapters, or duplicated root templates are shipped.
- Checkpoints are optional working artifacts, updated on changed decisions, completed acceptance, new blockers, or handoff. Evidence records bind commands/results to the relevant code/diff, configuration, environment/time, and data snapshot. Review also covers new files and distinguishes pre-existing changes; materially changed reviewed content invalidates acceptance.
- Release records separate repository verification, deployment prerequisites, execution, and business acceptance. Absent external evidence limits the corresponding claim and does not block unrelated local work.

## Verification and error behavior

Python 3.11+, PyYAML, and markdown-it-py run the local package checker and unittest suite. The checker validates metadata, unique identities, supported role responsibilities, and local Markdown resource paths using a CommonMark parser; it never executes skill instructions or infers implementation readiness. Titled links, reference links, and images are checked; code examples are not treated as resource declarations. Missing or malformed resources return a nonzero exit and an actionable path. Tests build disposable copies and deliberate corruptions outside the checkout. Standalone skill copies must validate without sibling skills or root templates.

An independent evaluator receives realistic requests and the completed pack, uses only local disposable fixtures, and reports observable outcomes separately from code review findings. Root verification runs after acceptance. Package checks and bounded forward tests do not establish reduced token costs, faster delivery, or UAT/production behavior.

## Delivery boundary

One cohesive replacement owns AGENTS.md, README files, .agents/skills, .codex, templates, docs, scripts, tests, and requirements-dev.txt. LICENSE, .git internals, user-level skills/memory, other repositories, and external systems are excluded. Starting worktree is clean. No material product decisions remain; user authorization covers the replacement and ordinary verified commits.
