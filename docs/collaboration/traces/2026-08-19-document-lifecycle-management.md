# AI Work Trace

## Request

- Date: 2026-08-19
- User request: analyze operational feedback from qpex and adopt the suitable
  document and Trace lifecycle rules in `llm-project-template`.
- Current phase: process-only, Architecture Path implementation after approval.
- Canonical issue or work plan:
  `docs/issues/LISS-0023-document-lifecycle-management.md`
  (issued as LISS-0017 on 2026-08-19; renumbered 2026-08-26 to resolve an
  ID collision with architecture-approval LISS-0017).
- AI planning record: AIP-0023-001 in the issue above (originally recorded
  as AIP-0017-001).

## Context Ledger

- Included: quickstart/readiness rules, adoption and session-start guidance,
  Trace log, Definition of Done, CI required-file checks, ADR conventions, and
  existing template sync policy.
- Omitted: application source, target-specific domain specifications,
  provider choices, retention periods, automatic deletion, and deprecated-term
  catalogs.
- Assumptions: the Canonical Register and Review Summary are derived
  navigation/review artifacts and do not alter the existing agreement unit.

## Routing

- Model/assistant/tool: Codex desktop for design and documentation; Python and
  shell checks for deterministic verification.
- Reason: Architecture Path process change with no application runtime.
- Privacy constraints: no secrets, private exports, or target-project data.

## AI Execution Records

### Attempt 1

- Agent: Codex desktop
- Environment: Codex desktop
- Model as displayed: GPT-5
- Reasoning setting as displayed: N/A; not exposed by this environment.
- Actual tokens: N/A; not exposed by this environment.
- Scope: add lifecycle policy, register/review templates, Trace compression
  rules, CI validation, ADR, and acceptance issue.
- Result: completed; verification listed below.

## Referee Decisions

- 2026-08-19: Architecture approval granted for the scoped lifecycle design.
- 2026-08-19: Existing agreement units remain unchanged. Register and Review
  Summary must not replace or widen Issue, specification, ADR, Work Plan, or
  Adjudicator approval boundaries.

## Verification

- `python3 scripts/check-document-lifecycle.py`: passed.
- `python3 -m py_compile scripts/check-document-lifecycle.py`: passed.
- `bash -n scripts/copy-ai-collaboration-files.sh scripts/update-ai-collaboration-files.sh scripts/init-llm-context.sh scripts/lib/collaboration-template-paths.sh`: passed.
- `git diff --check`: passed.
- Template copy smoke check was run by copying into a temporary target and
  validating the supplied register template; target-specific register rows
  remain unpopulated in this template repository.

## Changed Files

- `.github/workflows/ci.yml`
- `docs/architecture/README.md`
- `docs/architecture/adr/0013-document-lifecycle-and-canonical-register.md`
- `docs/collaboration/adoption-guide.md`
- `docs/collaboration/ai-work-trace-log.md`
- `docs/collaboration/definition-of-done.md`
- `docs/collaboration/document-lifecycle.md`
- `docs/collaboration/session-start-and-resume.md`
- `docs/issues/LISS-0023-document-lifecycle-management.md`
- `docs/templates/canonical-document-register.md`
- `docs/templates/review-summary.md`
- `scripts/check-document-lifecycle.py`
- `docs/collaboration/traces/2026-08-19-document-lifecycle-management.md`

## Next Safe Action

Adopters can copy the Canonical Register template and maintain it as a derived
navigation aid. No further action is required for this approved scope.
