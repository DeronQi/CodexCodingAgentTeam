---
name: release-readiness
description: Assess a software release candidate using repository, deployment, and business evidence. Use for go/no-go decisions or UAT/production readiness; execute a release only when explicitly authorized and a target runbook exists.
---

# Release Readiness

Read target instructions/runbooks and the authorized release scope. Identify the exact commit/tag/artifact or image digest, components, environment, and rollback target. Reuse existing valid evidence; do not reopen unrelated investigation or require every possible scan for every change.

Use [the release record](assets/release-record.md) when a durable record is useful. Evaluate applicable gates with evidence, identity/time, owner, and next action. Mark each Passed, Failed, Blocked, or Not Applicable with a reason. Missing evidence is not a pass.

Keep four facts separate:

- Repository result: the affected behavior, tests, and package/contract checks pass for the candidate.
- Deployment prerequisites: required authority, configuration, migrations/backups, capacity, release window, and rollback preparation are satisfied where relevant.
- Execution: the intended artifact actually reached the intended environment; capture version and runtime health.
- Business acceptance: representative success and relevant failure/authorization/scope behavior work in that environment.

Report a go/no-go/blocked decision for the requested stage. A candidate can be repository-ready while production prerequisites or acceptance remain blocked. Do not call pre-deployment readiness a deployed or accepted release. Evidence expires when its relevant code, artifact, configuration, environment, or data assumptions change; rerun affected checks only.

Assessment does not authorize external mutations. If release execution was already explicitly authorized, follow the target runbook within that authority, preserve component boundaries, capture actual outcomes, and apply documented failure/rollback triggers. Do not seek the same permission again. Otherwise report the remaining gate and smallest next action. Do not create credentials, change grants, or mutate live data merely to make a readiness record pass.
