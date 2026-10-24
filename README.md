# CodexCodingAgentTeam

[简体中文](README.zh-CN.md)

A reusable Codex multi-agent collaboration asset pack that can be copied into any code repository. It provides general delivery mechanisms without carrying product, technology-stack, or directory assumptions from a specific repository.

The core model is simple: the root agent orchestrates; an implementation agent completes one bounded slice; an acceptance agent independently reviews the complete diff in read-only mode; each slice closes with fresh verification and a separate commit.

## Contents

| Asset | Purpose |
| --- | --- |
| `.codex/agents/agentteam-evidence-explorer.toml` | Read-only mapping of requirements, code, data, behavior, tests, and verification evidence. |
| `.codex/agents/agentteam-slice-implementer.toml` | Implementation of one complete slice within explicit path boundaries. |
| `.codex/agents/agentteam-contract-reviewer.toml` | Independent acceptance of the complete diff. |
| `.agents/skills/agentteam-slice-delivery/` | Slice orchestration, acceptance gates, and plan validator for medium and large requirements. |
| `.agents/skills/agentteam-capability-delivery/` | Evidence-to-delivery workflow for a single capability family. |
| `.agents/skills/agentteam-requirements-design/` | Evidence-backed requirements clarification, coding-ready technical design, and readiness gate. |
| `.agents/skills/agentteam-release-readiness/` | Evidence-backed release readiness assessment and UAT/production closure records. |

## Quick start

### For people

1. Copy or merge `.codex/agents`, `.agents/skills`, `templates`, and the collaboration rules in [AGENTS.md](AGENTS.md) into the target repository. Do not overwrite target-specific instructions.
2. Open the target repository in Codex and ask it to follow [the bootstrap prompt](templates/codex-bootstrap-prompt.md). It first maps the repository, fills the target configuration from evidence, and records unknowns as `TODO: <evidence needed>`.
3. For a medium or large change, review and approve the separately produced requirements and technical design before implementation starts. Then use the slice plan to track implementation, independent acceptance, verification, and one commit per accepted slice.
4. For a release decision, use the release-readiness skill and review its separate repository, UAT, and production evidence. Deployment still needs explicit authorization.

### For Codex agents

1. Read the target repository's `AGENTS.md` first, then this asset pack's [AGENTS.md](AGENTS.md); target-repository rules always win.
2. Establish repository facts before editing: fill the target configuration only from current evidence, preserve unknowns as `TODO: <evidence needed>`, and do not infer environment permissions.
3. Use `$agentteam-requirements-design` when the request or design is incomplete. Do not begin implementation or slice planning while material decisions, contracts, or evidence gaps remain unresolved.
4. Use `$agentteam-slice-delivery` only for an approved, coding-ready design. Implement one bounded slice, obtain independent read-only acceptance, rerun its critical verification, then let the root agent stage and commit it.
5. Use `$agentteam-capability-delivery` for one clearly bounded capability family, and `$agentteam-release-readiness` to record a go/no-go decision. Never deploy, publish, or change external systems without explicit authorization.

## Detailed workflow

1. Copy or merge `.codex/agents` and `.agents/skills` into the target repository.
2. Merge the collaboration rules from [AGENTS.md](AGENTS.md) into the target repository and fill its `Target Project Configuration` placeholders with real repository paths, commands, boundaries, environment permissions, and release/rollback entry points. The target repository's own architecture, permission, release, and verification rules always take precedence.
3. Use `$agentteam-requirements-design` first when requirements or design are incomplete; it produces the approved baseline needed by `$agentteam-slice-delivery`.
4. Use `$agentteam-slice-delivery` for medium or large approved requirements; use `$agentteam-capability-delivery` for implementation of one clearly bounded capability family.
5. Create and validate a slice plan before delegating implementation and independent acceptance. Only a slice with an `ACCEPTED` verdict may be staged and committed by the root agent.
6. Use `$agentteam-release-readiness` for the final readiness decision. It distinguishes repository-ready from UAT-ready and production-ready; release execution remains separately authorized.

## Bootstrap with Codex

Ask Codex to read [templates/codex-bootstrap-prompt.md](templates/codex-bootstrap-prompt.md) and execute it in the target repository. The prompt directs Codex through evidence-backed requirements clarification, technical design, the readiness gate, and only then slice planning.

The included placeholders use `{{UPPER_SNAKE_CASE}}`. Codex must replace them only from repository evidence; otherwise it must leave `TODO: <evidence needed>` and report the blocking question or closure item.

```powershell
pwsh .agents/skills/agentteam-requirements-design/scripts/validate-design-readiness.ps1 -RequirementsPath docs/requirements/my-capability.md -DesignPath docs/design/my-capability.md
pwsh .agents/skills/agentteam-slice-delivery/scripts/validate-slice-plan.ps1 -Path docs/plans/my-slice-plan.md
```

This is a workflow asset pack, not a project template or release tool. It does not replace a target repository's `AGENTS.md` and does not grant permission to deploy, publish, change databases, or write to external systems.
