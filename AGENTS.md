# CodexCodingAgentTeam

Use this repository as a reusable Codex AgentTeam asset pack.

## Target Project Configuration

> When copying these assets into a real project, fill this section from the project itself. Keep unknown items as `TODO: <evidence needed>`; do not invent commands, paths, environments, or permissions. The target project's existing rules override this pack.

- Project name and purpose: {{PROJECT_NAME_AND_PURPOSE}}
- Repository root and primary branch: {{REPOSITORY_ROOT}}; {{PRIMARY_BRANCH}}
- Primary languages, frameworks, and build runtime: {{TECHNOLOGY_BASELINE}}
- Source roots and architecture boundaries: {{SOURCE_ROOTS_AND_BOUNDARIES}}
- Test roots and test categories: {{TEST_ROOTS_AND_CATEGORIES}}
- Configuration, schema, and infrastructure roots: {{CONFIG_SCHEMA_INFRA_ROOTS}}
- Active documentation roots and ownership rules: {{DOCUMENTATION_ROOTS_AND_OWNERSHIP}}
- Archived/reference material policy: {{ARCHIVE_REFERENCE_POLICY}}
- Standard build command: {{BUILD_COMMAND}}
- Targeted test command pattern: {{TARGETED_TEST_COMMAND_PATTERN}}
- Integration, runtime, database, UI, package, and architecture checks: {{ADDITIONAL_VERIFICATION_COMMANDS}}
- Git/commit convention and protected paths: {{GIT_CONVENTION_AND_PROTECTED_PATHS}}
- Environments and mutation permissions: {{ENVIRONMENTS_AND_MUTATION_PERMISSIONS}}
- Release runbooks, readiness checks, and rollback procedure: {{RELEASE_ENTRY_POINTS_AND_ROLLBACK}}
- Sensitive paths, secret policy, and redaction rules: {{SENSITIVE_DATA_POLICY}}

## Team roles

- Root agent: own scope, planning, delegation, final verification, staging, and commits.
- Evidence explorer: read-only evidence mapping.
- Slice implementer: edit one bounded slice; never stage or commit.
- Contract reviewer: read-only independent acceptance.

## Collaboration rules

1. Read and fill the target-project configuration above, then read the target repository's existing `AGENTS.md`; its rules win.
2. Keep one writer per worktree. Parallelize only independent read-only work or isolated worktrees with disjoint files and state.
3. Use an approved slice plan for medium or large work; use positive allowed paths and hard excluded paths.
4. Require independent reviewer acceptance before staging an implementation slice.
5. Rerun the narrow critical verification after acceptance and before commit.
6. Never infer permission to deploy, publish, change a database, or mutate another live system.
7. Preserve unrelated changes and inspect status before editing and staging.

## Bootstrap a target repository

1. Read this file and the target repository's existing `AGENTS.md`.
2. Fill `Target Project Configuration` from current paths, scripts, configuration, and runbooks before using the team workflow.
3. Read `README.md` and `templates/codex-bootstrap-prompt.md` from this asset pack.
4. Copy `templates/repository-delivery-profile.template.md` into the target repository's documentation location (or use the repository's equivalent) and fill all `{{PLACEHOLDER}}` values from evidence.
5. Keep an unknown value as `TODO: <evidence needed>`; do not fabricate a repository convention, runtime boundary, permission, or verification command.
6. Copy `templates/implementation-slice-plan.template.md` when a durable delivery plan is needed. Do not delegate a slice that has material unresolved placeholders.

## Required delivery sequence

1. Clarify the requested outcome from repository evidence and create separate requirements.
2. Create a coding-ready technical design with requirement traceability, boundaries, contracts, state/error/auth/audit behavior, and verification strategy.
3. Resolve or explicitly block material decisions and external evidence gaps.
4. Split only the approved design into vertically complete delivery slices.
5. Implement one slice, independently accept the complete diff, run fresh root verification, and commit only the accepted slice.
6. Finish with an explicit closure slice when UAT, infrastructure, packaging, or production evidence cannot be proven by repository tests.
7. Record material design choices in a decision record, contract changes in an interface contract, and release evidence in a release record. Do not claim an environment state without current evidence.

## Included assets

- `.codex/agents/`: reusable role definitions.
- `.agents/skills/agentteam-slice-delivery/`: orchestration, plan contract, acceptance gates, and validator.
- `.agents/skills/agentteam-requirements-design/`: requirements clarification and technical design gate.
- `.agents/skills/agentteam-release-readiness/`: release-readiness evidence and closure.

Copy the asset folders into a target repository, fill `Target Project Configuration`, and merge these rules into its `AGENTS.md`; never overwrite target-specific authority, architecture, release, or verification rules.
