# LISS-0012: Token variance reasons

## Metadata

- Local issue ID: LISS-0012
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/docs
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason:
- Owner/agent: Claude Code CLI (Claude Sonnet 5)
- Related branch: process/2026-07-14-token-variance-and-distribution-hygiene

## Summary

- Adapts a proposal originally drafted on branch
  `codex/process/token-variance-reasons` (Codex desktop, 2026-07-10, never
  merged, no PR) as `LISS-0008: Token variance reasons`. That branch's
  `LISS-0008` ID now collides with this session's own (different, already
  merged) `LISS-0008: AI failure and recovery procedure`, so this issue
  re-numbers and re-scopes the content against current `main` instead of
  reusing the original branch as-is.
- Update AI planning and execution record guidance so each execution attempt
  keeps the accepted token estimate (range and midpoint) near actual usage,
  records `N/A` when actual usage is unavailable, and still captures
  meaningful variance reasons when the work clearly expanded or contracted
  from the estimate — without inventing a token count.
- Deviation from the original codex branch: that branch's `ai-work-trace.md`
  diff dropped the existing `Token metric` field from the Execution Record
  section while keeping it in the Planning Record section (an inconsistency,
  not an intentional simplification — nothing in its trace or issue text
  explains removing it). This issue keeps `Token metric` in both sections.

## Acceptance Notes

- `docs/templates/ai-work-trace.md`'s AI Execution Record gains: `Estimated
  token range`, `Estimated token midpoint`, `Actual tokens`, `Actual token
  unavailable reason`, `Estimate variance`, `Variance reason` — added
  alongside the existing `Token metric`, `Token source`, and `Token
  attribution boundary` fields (not replacing them).
- `docs/templates/local-issue.md` and `docs/templates/work-plan.md`'s AI
  Planning Record gain `Estimated token midpoint` next to the existing
  `Estimated token range`.
- ADR 0009 (`docs/architecture/adr/
  0009-bug-planning-and-ai-usage-records.md`) Decision section is extended
  in place (not superseded, matching the precedent already used for this
  same ADR in LISS-0007's implementation): planning records reference token
  midpoint when available; execution records reference the planning
  estimate and record variance reasons without inventing actual usage;
  Enforcement gains a rejection rule for omitted variance reasons on
  clearly-expanded-or-shrunk work.
- `docs/collaboration/llm-cost-reduction.md`'s AI Planning Estimates and AI
  Execution Records sections are updated to mention midpoint and variance
  reasons, consistent with the Non-Goals section's existing "not
  billing-grade exact token accounting" stance (variance reasons are
  qualitative, not a computed delta).
- `docs/collaboration/local-issue-planning.md`'s AI Planning Records section
  gains "estimated token range, midpoint, and metric" (currently "range and
  metric").
- No change to the trace-requirement rules themselves (when a trace is
  mandatory) — this issue only enriches the fields a trace/record already
  captures.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: ADR 0009, LISS-0007 (prior ADR 0009 work), LISS-0013 (same source
  branch, implemented together in this session for efficiency but tracked
  as separate concerns).

## Adjudicator Decision Points

- Resolved 2026-07-14: adopt the token-variance proposal, renumbered to
  avoid the LISS-0008 collision with this session's own issue of that
  number.
- Resolved 2026-07-14: keep the `Token metric` field in the Execution
  Record (deviating from the source branch, which dropped it without
  stated reason).

## Context

- Included: the `codex/process/token-variance-reasons` branch's two commits
  (`08d0d88` "Record token variance reasons", `6ed7a7d` "Improve template
  distribution hygiene") fetched and diffed against their merge-base with
  `main` (`80edcdd`); `docs/architecture/adr/
  0009-bug-planning-and-ai-usage-records.md`; `docs/templates/
  ai-work-trace.md`, `local-issue.md`, `work-plan.md`;
  `docs/collaboration/llm-cost-reduction.md`,
  `local-issue-planning.md`.
- Omitted: the source branch's distribution-hygiene changes (tracked
  separately as LISS-0013); application source (none exists in this
  template repo).
- Assumptions: the source branch's commits represent a complete, coherent
  proposal even though they were never opened as a PR; re-implementing them
  against current `main` rather than attempting a literal `git cherry-pick`
  is appropriate given the intervening ADR 0010/0011 work has changed
  several of the same files.

## AI Planning Records

### AIP-0012-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-14
- Planning size: M
- Intended execution route: deterministic diff/review of the source branch
  content, direct edits to re-implement against current `main`
- Intended scope: `ai-work-trace.md`, `local-issue.md`, `work-plan.md`, ADR
  0009, `llm-cost-reduction.md`, `local-issue-planning.md`
- Estimated token range: 6,000-12,000
- Token metric: approximate total model tokens for this process task
- Estimation basis: small, well-scoped field additions to five already-read
  documents, following an existing complete draft
- Assumptions: no application code changes; no new ADR needed (ADR 0009
  extended in place)
- Confidence: high
- Revises:
- Revision reason:
- Superseded by:

## References

- `codex/process/token-variance-reasons` (GitHub branch, unmerged, no PR),
  commit `08d0d88`.
- `docs/architecture/adr/0009-bug-planning-and-ai-usage-records.md`.
- Adjudicator request, 2026-07-14 (chat): asked to evaluate the branch's
  content and adapt it to current `main` if worthwhile.

## Work Notes

- The original branch's own `docs/issues/LISS-0008-token-variance-reasons.md`
  and `docs/collaboration/traces/2026-07-10-token-variance-reasons.md`
  remain on the `codex/process/token-variance-reasons` branch as historical
  record of the original proposal; they are not copied into this
  repository's `main` history since this issue supersedes them with a
  collision-free ID.

## Verification

- Local reproduction of CI's required-files, ADR-existence, and
  conflict-marker checks — pass.
- `git diff --check` — pass.
- LISS local-ID collision scan — no duplicates.
- See `docs/collaboration/traces/
  2026-07-14-token-variance-and-distribution-hygiene.md` for the combined
  verification record (this issue and LISS-0013 were implemented and
  verified together in one session).
