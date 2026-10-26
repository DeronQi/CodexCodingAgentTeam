---
name: requirements-design
description: Clarify material software requirements and produce a coding-ready technical design. Use for design-only requests, unresolved product behavior, architectural decisions, or contract changes; skip for self-evident fixes and reuse existing adequate documents.
---

# Requirements and Design

Read repository instructions and the current sources needed for the decision. Reuse authoritative requirements and designs; do not rewrite them to match a template. Distinguish current behavior, requested behavior, proposals, and external unknowns. Resolve reversible technical choices from evidence; ask only for material product, scope, permission, or irreversible decisions that remain unresolved.

Keep requirements separate from technical design. Requirements describe the outcome, boundaries, observable behavior, and acceptance. Design explains how affected components and contracts satisfy them, including validation, authorization, errors, state, concurrency, recovery, and verification where relevant. Give material requirements stable identifiers and map them to design and acceptance. Record important choices in the owning design or existing decision log; create a separate record only when useful.

If the repository has no suitable format, adapt [the requirements example](assets/requirements.md) and [the design example](assets/design.md). Omit irrelevant sections. Unknown facts remain explicit; do not invent paths, commands, ownership, or permissions. Evidence may live inline with links to original code, schemas, traces, and decisions. Historical material is supporting evidence until verified against current authority.

Judge readiness semantically: material requirements have an implementable design and observable acceptance; contradictions and dependent blockers are resolved. A formatting script cannot approve a design. Separate implementation blockers from deployment or business-acceptance gaps, and stop only dependent work. Do not turn every external unknown into a global stop.

For a design-only request, deliver the documents and unresolved decisions without implementing. When implementation is already authorized, continue with the main agent after the relevant design is ready, using software-delivery if available. Do not add a user approval round for routine technical decisions or force slice planning. Delegate a bounded independent investigation only if its result would improve the decision.
