# Design: Continuous software delivery

## Decisions and traceability

| Requirement | Implementation | Verification |
| --- | --- | --- |
| FR-001 | Three task routes in AGENTS.md and focused skill descriptions; root performs normal implementation | Small-fix and design-only behavioral cases |
| FR-002 | Conditional delegation guidance and one optional delivery-reviewer role | Investigation, review, and isolated-writer cases |
| FR-003 | Optional checkpoint and evidence record; event-triggered updates and evidence invalidation rules | Existing-evidence and unchanged-blocker cases |
| FR-004 | Observable acceptance, scoped external blockers, permissions inherited from parent | External-gate and authorization cases |
| FR-005 | software-delivery, requirements-design, release-readiness; resources owned inside each skill | Independent-copy and resource-integrity tests |
| FR-006 | Python package checker, unittest negative tests, and bounded independent forward testing | Package tests and evaluator results |

## Boundaries and contracts

- The main agent chooses a proportional route, owns integration, and stages/commits the verified task. Optional subagents receive an outcome, context, allowed paths/state, permissions, and return compact findings or artifacts. They never acquire authority from a handoff.
- Separate requirements and design remain useful when decisions are material. No script can approve their semantics. Existing repository documents take precedence over bundled examples; no exact headings or slice statuses are imposed.
- Skills are self-contained folders with YAML metadata, optional assets/references, and UI metadata. Only the optional reviewer uses a standalone TOML agent definition. No config.toml, aliases, migration adapters, or duplicated root templates are shipped.
- Checkpoints are optional working artifacts, updated on changed decisions, completed acceptance, new blockers, or handoff. Evidence records bind commands/results to the relevant code/diff, configuration, environment/time, and data snapshot. Review also covers new files and distinguishes pre-existing changes; materially changed reviewed content invalidates acceptance.
- Release records separate repository verification, deployment prerequisites, execution, and business acceptance. Absent external evidence limits the corresponding claim and does not block unrelated local work.

## Verification and error behavior

Python 3.11+, PyYAML, and markdown-it-py run the local package checker and unittest suite. The checker validates metadata, unique identities, supported role responsibilities, and local Markdown resource paths using a CommonMark parser; it never executes skill instructions or infers implementation readiness. Titled links, reference links, and images are checked; code examples are not treated as resource declarations. Missing or malformed resources return a nonzero exit and an actionable path. Tests build disposable copies and deliberate corruptions outside the checkout. Standalone skill copies must validate without sibling skills or root templates.

An independent evaluator receives realistic requests and the completed pack, uses only local disposable fixtures, and reports observable outcomes separately from code review findings. Root verification runs after acceptance. Package checks and bounded forward tests do not establish reduced token costs, faster delivery, or UAT/production behavior.

## Delivery boundary

One cohesive replacement owns AGENTS.md, README files, .agents/skills, .codex, templates, docs, scripts, tests, and requirements-dev.txt. LICENSE, .git internals, user-level skills/memory, other repositories, and external systems are excluded. Starting worktree is clean. No material product decisions remain; user authorization covers the replacement and ordinary verified commits.
