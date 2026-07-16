# AI Work Trace

## Request

- Date: 2026-07-13
- User request: evaluate external feedback on this template and incorporate
  the parts that fit its intent; on approval, create the ADR, then plan and
  implement it (Part 2 of the approved implementation plan).
- Current phase: process-only (docs)
- Canonical issue or work plan: `docs/issues/LISS-0009-external-resource-adoption-contract.md`,
  `docs/work-plans/WP-0001-external-feedback-2026-07-13.md`
- AI planning record: AIP-0009-002 (revises AIP-0009-001)

## Context Ledger

- Included: `docs/architecture/io-reasoning-contracts.md`,
  `docs/architecture/dependency-policy.md`,
  `docs/collaboration/model-tool-capability-matrix.md`,
  `docs/collaboration/ai-work-trace-log.md`,
  `docs/architecture/adr/0002-input-output-reasoning-contracts.md`,
  `docs/collaboration/template-benefits.md`, `CLAUDE.md`,
  `docs/architecture/README.md`, `.github/workflows/ci.yml`, the
  Adjudicator-supplied external feedback document (2026-07-13, not stored as a
  separate file), the Adjudicator's mid-session rescope correction (chat,
  2026-07-13).
- Omitted: the feedback source repository's game-specific safe-area
  dimensions, adult-content experiment details, Studio/provider-specific API
  shapes.
- Assumptions: doc-only change; no application code or test suite exists in
  this template repository.
- Open decisions: none remaining for this issue.

## Routing

- Model/assistant/tool: strong reasoning agent for design/boundary
  decisions and the mid-session rescope; deterministic search/grep/diff for
  verification and rename tracking.
- Reason: cross-document consistency work spanning collaboration docs,
  architecture docs, an ADR, and CI config, plus a substantive scope
  correction mid-plan.
- Privacy constraints: none; no private or user data involved.

## AI Execution Records

### Attempt 1

- Agent: Claude Code CLI
- Environment: Claude Code CLI
- Model as displayed: Claude Sonnet 5
- Reasoning setting as displayed: N/A
- Token usage: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- N/A reason: no reasoning-effort label or token usage value is exposed to
  this agent in this environment's output.
- Scope: original media-artifact-specific design of LISS-0009 and ADR 0011
  (candidate/promotion state machine, image-specific output-shape contract,
  deterministic-vs-human boundary table naming image properties). Entered
  Plan Mode with this design as part of the overall implementation plan.
- Result: rejected by the Adjudicator during Plan Mode review — the media-
  specific vocabulary in ADR 0011 items 4-5 violated the template's
  technology-neutrality principle. Not implemented as files beyond the
  already-written (and since-rewritten) ADR 0011/LISS-0009 drafts.
- Attempt boundary: ended when the Adjudicator's correction required a
  materially different plan (attempt boundary per `docs/collaboration/
  ai-work-trace-log.md`: "a materially different plan replaces the previous
  one").
- Notes: none.

### Attempt 2

- Agent: Claude Code CLI
- Environment: Claude Code CLI
- Model as displayed: Claude Sonnet 5
- Reasoning setting as displayed: N/A
- Token usage: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- N/A reason: same as Attempt 1.
- Scope: rescoped LISS-0009 and ADR 0011 (renamed both files from
  "media-artifact-output-contract"/"generated-artifact-output-contract" to
  "external-resource-adoption-contract") to state the general adoption-check
  principle instead of media-specific rules; wrote
  `docs/architecture/external-resource-adoption-contract.md`; added
  one-line pointers to `io-reasoning-contracts.md`,
  `dependency-policy.md`, and `ai-work-trace-log.md`; updated CLAUDE.md,
  architecture README, and CI's ADR-existence loop.
- Result: Part 2 implementation complete, pending Adjudicator verification and
  commit decision.
- Attempt boundary: continuous from the rescope decision through
  implementation; no further replanning occurred.
- Notes: the rescope specifically dropped "orientation, resolution, crop,
  alpha channel" and the tool-name-based boundary table, replacing them with
  a generic `intake -> checked -> accepted|rejected|needs_recheck ->
  adopted` lifecycle and a judgment-category (not property-name) tool-vs-
  human steer.

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: N/A

## Cost / Reasoning Control

- Operating path: Architecture Path (ADR authored and substantially
  rewritten; collaboration/architecture contract files changed).
- Files read: approximately 15 for this part (plus the ~25 already read for
  Part 1, reused from session context).
- Context intentionally omitted: feedback source repository internals,
  Studio/provider-specific configuration, adult-content experiment details.
- Deterministic checks used: `grep` for section-header structure and
  leftover technology-specific vocabulary; planned CI-equivalent checks
  (required-file existence, ADR-loop existence, contract-traceability) to
  run before marking this issue `review`.
- Escalation reason: ADR rewrite and cross-document boundary decisions
  (vs. `dependency-policy.md`) require strong reasoning per
  `docs/collaboration/model-tool-capability-matrix.md`'s routing table.
- Avoided LLM work: reused ADR 0002's source-reference/review-status shape
  and `dependency-policy.md`'s checklist style instead of inventing a new
  schema for the new document.
- Rework caused by AI output: significant — the entire original
  media-specific design (Attempt 1) was rejected and rewritten. This is
  recorded as the primary lesson of this trace: verify a template
  document's technology-neutrality against the project's stated principle
  before treating a first draft as final, even after an ADR has been
  "accepted."

## Adjudicator Decisions

- 2026-07-13: rejected ADR 0011's image-specific output-shape contract and
  deterministic-vs-human boundary table.
- 2026-07-13: specified the general principle — no external or AI-generated
  resource is adopted without a recorded check, regardless of who produced
  it, who adopts it, or who performs the check.
- 2026-07-13: confirmed the broader scope (AI-generated artifacts + general
  human-sourced external resources, not just media) and confirmed this is
  distinct from `dependency-policy.md`'s software-dependency scope.
- 2026-07-13: approved the revised Part 2 plan.

## Verification

- Commands/checks: see Task #15 (pending) — `grep -c "^## "` structure
  check; leftover-technology-vocabulary re-read; local reproduction of CI's
  required-file, ADR-existence, and contract-traceability checks;
  `git diff --check`.
- Result: pending, to be filled in when Task #15 completes.

## Changed Files

- `docs/architecture/adr/0011-external-resource-adoption-contract.md`
  (renamed from `0011-media-artifact-output-contract.md`, content rewritten)
- `docs/issues/LISS-0009-external-resource-adoption-contract.md` (renamed
  from `LISS-0009-generated-artifact-output-contract.md`, content rewritten)
- `docs/architecture/external-resource-adoption-contract.md` (new)
- `docs/architecture/io-reasoning-contracts.md` (edit: one-line pointer)
- `docs/architecture/dependency-policy.md` (edit: one-line pointer/boundary
  statement)
- `docs/collaboration/ai-work-trace-log.md` (edit: one-line pointer)
- `CLAUDE.md` (edit)
- `docs/architecture/README.md` (edit)
- `.github/workflows/ci.yml` (edit)
- `docs/work-plans/WP-0001-external-feedback-2026-07-13.md` (edit, pending)

## Next Safe Action

- Run the Part 2 verification checklist (Task #15), update WP-0001's final
  state, then stop and ask the Adjudicator whether to commit this branch. Note
  for the eventual merge: `CLAUDE.md`, `docs/architecture/README.md`'s
  Accepted Decisions list, and `.github/workflows/ci.yml`'s ADR-existence
  loop were each edited independently on both this branch and
  `process/ai-failure-recovery-and-runner-cli-contract` (Part 1); expect a
  small, easily-resolved merge conflict on `ci.yml`'s single-line loop when
  both branches merge to `main`.

## Notes

- No secrets, API keys, or private data were included in this trace or the
  documents it covers.
