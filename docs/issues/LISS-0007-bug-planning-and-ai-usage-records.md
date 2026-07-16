# LISS-0007: Bug planning and AI usage records

## Metadata

- Local issue ID: LISS-0007
- GitHub issue:
- Status: review
- Phase: process-only
- Type: process/docs
- Priority: medium
- Initial planning size: L
- Current planning size: L
- Owner/agent: Codex desktop
- Related branch: codex/process/bug-ai-planning-records

## Summary

- Extend local planning to cover bugs, preserve strict phase gates, add
  planning sizes, and record vendor-neutral AI planning revisions and
  per-attempt execution evidence.

## Acceptance Notes

- A bug is recorded in a local issue or existing work plan unless it is an
  approved-scope, one-attempt `S` correction.
- The `S` exception waives only a separate planning artifact, never a phase.
- Planning-size definitions and reclassification rules are documented.
- `M` or larger work has a versioned, vendor-neutral AI planning record.
- `M` or larger work, and any second or later attempt, has an AI work trace.
- Attempts remain separate; compatible reference totals may be added but do
  not replace attempts.
- Unavailable model, reasoning, and token values use `N/A` with a reason.
- Cursor and other environments follow the same generic unavailable-value
  rule instead of receiving guessed values.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: ADR 0005, ADR 0009

## Adjudicator Decision Points

- Resolved 2026-07-10: phase gates are never waived for bug fixes.
- Resolved 2026-07-10: use vendor-neutral, versioned AI planning records.
- Resolved 2026-07-10: require traces for `M` or larger work or multiple
  attempts; do not require them for a one-attempt `S` fix.

## Context

- Included: agent quickstart, local issue planning, work and issue templates,
  trace policy and template, cost policy, prompt change control, bug report
  template, related ADRs, CI documentation checks, and Adjudicator feedback.
- Omitted: application source, stack-specific model pricing, provider billing
  exports, and unrelated ADRs.
- Assumptions: token estimates and actual usage are planning evidence rather
  than billing-grade accounting; displayed values differ by environment.

## AI Planning Records

### AIP-0007-001

- Status: accepted
- Created by:
  - Agent/environment: Codex desktop
  - Model as displayed: GPT-5 (agent identity supplied by the environment)
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-setting label is exposed to this agent
- Created at: 2026-07-10
- Planning size: L
- Intended execution route: strong reasoning agent plus deterministic search,
  diff, YAML parsing, and repository checks
- Intended scope: ADR, planning policy/templates, trace policy/template, cost
  policy, quickstart, GitHub bug template, CI, issue, and work trace
- Estimated token range: 18,000-35,000
- Token metric: approximate total model tokens for this process task
- Estimation basis: cross-contract policy change spanning more than ten files,
  including consistency review and deterministic verification
- Assumptions: no application code or external research is required
- Confidence: medium
- Revises:
- Revision reason:
- Superseded by:

## References

- Adjudicator-approved project feedback supplied on 2026-07-10.
- `docs/architecture/adr/0009-bug-planning-and-ai-usage-records.md`.

## Work Notes

- Architecture Path scope and the three policy decisions were approved by the
  Adjudicator on 2026-07-10.

## Verification

- Passed `git diff --check`.
- Passed Ruby YAML parse for `.github/workflows/ci.yml` and
  `.github/ISSUE_TEMPLATE/bug_report.md`.
- Passed local reproduction of CI required-file and ADR checks.
- Passed local reproduction of the contract-change trace check.
