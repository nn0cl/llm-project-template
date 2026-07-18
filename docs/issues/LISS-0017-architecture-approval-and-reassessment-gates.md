# LISS-0017: Architecture approval and reassessment gates

## Metadata

- Local issue ID: LISS-0017
- GitHub issue:
- Status: in_progress
- Phase: process-only
- Type: process/docs
- Priority: high
- Initial planning size: L
- Current planning size: L
- Owner/agent: Codex; Adjudicator review required
- Related branch: process/architecture-approval-gates
- AI planning record: AIP-0017-001

## AI Planning Record: AIP-0017-001

- Status: accepted
- Authoring agent/environment: Codex desktop / local repository workspace
- Model and reasoning setting: N/A — not exposed by the executing environment
- Creation date: 2026-07-18
- Planning size: L
- Intended execution route: Architecture Path; documentation and contract
  alignment plus a CI-only review-record validator; no Hook or application
  implementation
- Estimated token range: N/A — no calibrated estimate is available
- Estimated midpoint and metric: N/A — no calibrated estimate is available
- Estimation basis: Multiple normative surfaces must be aligned while keeping
  `AGENTS.md` as the shared contract source and preserving agent-specific
  entry-point differences.
- Assumptions: the common rule must apply to Codex, Claude Code, Copilot,
  Grok, and Cursor; Hook enforcement remains out of scope while CI validation
  is in scope for the first implementation slice.
- Confidence: medium — the affected surfaces are identified, but the exact
  approval-state representation remains an Adjudicator decision.
- Revision links: none
- Payload included: agent entry points, quickstart/process documents, review
  and design templates, Definition of Done, issue/work-plan rules, the current
  CI workflow, and the existing external-feedback intake precedent.
- Payload omitted: target-project implementation, private chat logs, Claude
  Hooks, and unverified target ADR/trace contents.
- Deterministic verification planned: cross-surface terminology search,
  effective-content review, `git diff --check`, and documentation/contract
  checks after the accepted edit.

## Summary

External feedback from a game-server adopter reported that agreement to start
work on an administrative capability was interpreted by an agent as approval
for concrete technology selection, ADR completion, and implementation. During
the same flow, a new subsystem, write-contention concerns, an additional
implementation language, authentication boundaries, and the question of
in-process versus separate deployment were treated as local implementation
details rather than triggers for architecture reassessment.

This issue evaluates whether the template should make approval levels and
architecture-reassessment triggers explicit and reviewable.

## Problem Statement

The template distinguishes design, ADR, and implementation in prose, but it
does not yet provide one unambiguous vocabulary for separating:

```text
scope approval
  -> architecture approval
  -> technology selection approval
  -> AT-TDD phase approval
```

It also does not provide a named gate for revisiting an accepted architecture
when a proposed subsystem changes deployment, language, data-concurrency,
authentication, or responsibility boundaries.

## Candidate Acceptance Notes

These are proposals for review, not accepted requirements.

1. `docs/templates/adjudicator-review.md` and the design-intake guidance
   distinguish scope approval, architecture approval, technology-selection
   approval, phase approval, and implementation approval.
2. Architecture Path guidance defines an Architecture Reassessment Gate for
   new subsystems, new languages/frameworks/datastores, data-concurrency or
   transaction-boundary changes, authentication/authorization boundaries,
   deployment-boundary changes, and changes to accepted logic or ADR premises.
3. A proposed ADR is not implementation authorization. The review record must
   state the approved scope, current phase, and whether implementation is
   allowed.
4. The gate requires an impact summary covering existing ADRs, accepted logic,
   boundaries, alternatives, and the need for Adjudicator review.
5. Automated checks and explicit human approval are represented as separate
   completion conditions.
6. The guidance uses a canonical artifact and references rather than copying
   every decision into ADR, Issue, WorkPlan, and spec simultaneously.
7. A bounded execution-batch review record may pre-approve a named set of
   low-risk Issues with explicit allowed paths, phases, scope, expiry, and
   post-review requirement. It must not approve unknown architecture choices
   or make a proposed ADR equivalent to an accepted ADR.
8. CI validates the batch record, Issue references, declared allowed scope,
   and post-review status. For a matching `batch/<batch-id>` branch, CI also
   validates changed paths from the recorded approval commit against
   `allowed_paths`. CI success is not treated as Adjudicator approval.
9. If an architecture-reassessment trigger appears, the batch authorization
   is invalid for that work and the agent must stop for a new decision.

## Dependencies

- Parent: WP-0002
- Depends on: none
- Blocks: none
- Related: LISS-0005, LISS-0014, LISS-0015, LISS-0016

## Adjudicator Decision Points

- Should this remain one bundled process/docs issue or split approval semantics
  from architecture reassessment triggers?
- Should the approval state remain Markdown fields, or should a machine-readable
  review record be introduced?
- Should the Architecture Reassessment Gate be normative for all agents or a
  design-review checklist only?
- Should the same-turn ADR/implementation concern be expressed as a repository
  state rule rather than a blanket conversational-turn prohibition?
- Is a canonical-artifact rule required here, or should it remain in a separate
  document-sync issue?
- Should the bounded execution-batch record use a machine-readable JSON file,
  structured Markdown, or another repository-native format?
- Which document-only/process-only operations qualify as low risk, and which
  triggers invalidate the batch authorization?

## Context

- Included: the external Claude feedback supplied by the Adjudicator; current
  `AGENTS.md`; `docs/architecture/agent-quickstart.md`;
  `docs/architecture/implementation-readiness.md`;
  `docs/collaboration/ai-human-scheme.md`;
  `docs/collaboration/definition-of-done.md`;
  `docs/collaboration/local-issue-planning.md`;
  `docs/collaboration/branch-commit-pr-discipline.md`;
  `docs/work-plans/WP-0001-external-feedback-2026-07-13.md`;
  `docs/issues/LISS-0005-adopter-feedback-process-hygiene-improvements.md`.
- Omitted: the adopter repository's actual ADR 0017/0019/0022/0023 files and
  traces, implementation code, private chat logs, and any target-specific
  technology or deployment decision.
- Assumptions: the supplied report is an intake signal; its target-repository
  citations require verification before being treated as independently proven
  facts about this template.
- Open decisions: all candidate acceptance notes above remain unaccepted.

## References

- `docs/work-plans/WP-0002-architecture-approval-and-reassessment.md`
- `docs/work-plans/WP-0001-external-feedback-2026-07-13.md`
- `docs/issues/LISS-0005-adopter-feedback-process-hygiene-improvements.md`
- `docs/collaboration/definition-of-done.md`
- `docs/collaboration/branch-commit-pr-discipline.md`

## Work Notes

- 2026-07-18: Intake created from Adjudicator-provided Claude feedback.
- 2026-07-18: Formal AIP-0017-001 accepted for the CI-only first slice and
  common contract alignment after Adjudicator direction to proceed.
- 2026-07-18: Formal AIP-0017-001 created after confirming that the proposed
  common change affects Claude, Copilot, Grok, Cursor, and shared process
  surfaces. Hook changes remain out of scope; a CI-only validator is now a
  proposed first implementation slice.
- No template contract or CI workflow has been changed as part of this intake;
  the CI-only validator remains a proposed implementation slice.

## Verification

- Intake verification: confirm the candidate changes map to existing template
  documents and do not assume the adopter's unprovided repository artifacts.
- Implementation verification: in progress on
  `process/architecture-approval-gates`; Hook and application changes remain
  out of scope.

## Next Safe Action

- Adjudicator reviews the implementation branch and its CI/documentation
  changes before merge. Any unaccepted follow-up remains proposed.
