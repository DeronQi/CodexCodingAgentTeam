# Requirements: Continuous software delivery

## Outcome and scope

Replace the historical AgentTeam pack with a small workflow that keeps one agent accountable for an observable business result. The user accepted the assessment and explicitly requested a complete replacement without compatibility layers. This change owns the pack's instructions, skills, roles, templates, and local checks. It does not change another repository, install global assets, deploy, or modify live systems.

## Requirements

- **FR-001 — Proportional process:** Small fixes can proceed directly; ordinary capabilities have one continuous owner; separate requirements/design are used for material ambiguity and architectural or contract decisions; large work may use outcome-based milestones without mandatory agent handoffs.
- **FR-002 — Selective delegation:** Delegate only bounded work that benefits from independent context, parallel investigation, isolated implementation, or independent review. Maintain one writer per worktree and the main agent's integration ownership.
- **FR-003 — Useful state:** Update a short checkpoint only for meaningful changes or a handoff. Keep raw evidence in artifacts; reuse evidence while its code, configuration, environment, and data assumptions remain valid. Do not commit routine status updates or wake an agent merely to repeat unchanged state.
- **FR-004 — Honest acceptance:** Define observable completion, exercise the affected end-to-end path, distinguish local completion from external acceptance, and block only dependent work. Preserve mutation permissions and do not treat role instructions as a sandbox.
- **FR-005 — Simple distribution:** Ship software-delivery, requirements-design, and release-readiness, plus one optional delivery-reviewer. Keep each template in one place inside its owning skill. Remove old names, fixed slice orchestration, regex design gates, duplicate templates, and project configuration that forces agent features. No old-name aliases, format adapters, or migration support are required.
- **FR-006 — Verifiable pack:** Provide portable package checks, negative tests for broken packaging, and realistic behavioral evaluation cases. Package checks must not claim semantic design approval or prove productivity improvements.

## Acceptance

The three skills can be copied independently with their resources. Local checks reject malformed metadata, missing/escaping resource links, duplicate identities, and misleading agent permission overrides. A separate evaluator exercises representative prompts in an isolated workspace and reviews the complete change. The root reruns critical checks before one cohesive commit.

## Sources and external limits

The current pack at b2d902b and the user's accepted assessment establish the starting behavior and desired replacement. Previous validator negative tests demonstrated that structural passes did not establish readiness. Runtime permission and delegation constraints come from the current session; target repository instructions remain authoritative. Comparative cost, speed, and business acceptance require future controlled runs in actual target repositories and are not acceptance claims for this pack change.
