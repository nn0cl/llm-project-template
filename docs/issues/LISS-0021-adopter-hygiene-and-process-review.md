# LISS-0021: Adopter hygiene, placeholders, lessons, and completion process review

## Metadata

- Local issue ID: LISS-0021
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/docs
- Priority: high
- Initial planning size: L
- Current planning size: L
- Reclassification reason:
- Owner/agent: Grok
- Related branch: process/liss-0021-adopter-hygiene-and-process-review

## Summary

Stop shipping this template's own issue and work-plan identifiers into
adopting repositories. Require unfilled placeholders to be set. Keep
`CLAUDE.md` a full mirror with no `@AGENTS.md` import in Canonical contract
text. Record review outcomes as meta-level lessons and reuse them. When an
issue or work plan completes, run a same-context process review and, on
agreed problems, leave template-feedback records.

## Acceptance Notes

1. Copy and update exclude `docs/work-plans/WP-*.md` and
   `docs/collaboration/reviews/*.md`. CI smoke asserts they are absent in a
   fresh target.
2. Citation direction: agents do not open ISSUE or work-plan files as current
   rules; they read policy documents, ADRs, and specifications. ADRs and
   specifications may cite ISSUES and work plans. Context files do not link
   to an ADR or ISSUE as the reason those context files changed. The reverse
   (ADR/ISSUE lists changed files) remains. Copy still excludes this
   template's planning ledger. Naming-format examples such as `LISS-0000`
   remain.
3. Agent contracts require unfilled `<...>` placeholders in relied-on
   contract or architecture files to be set before implementation; agents
   stop and ask rather than treating placeholder text as a fact.
4. Canonical contract-change rules state that `CLAUDE.md` is a full
   effective-content mirror and does not import `@AGENTS.md`.
5. Review outcomes that should affect later work are recorded as meta-level
   lessons (patterns and process risks), not incident narratives, and are
   read at the next design intake and implementation.
6. Marking a local issue or work plan `done` includes a same-context
   development-process review against the operating contract. Deviations or
   operational problems are agreed with the Adjudicator and written as
   template-feedback records.

## Dependencies

- Parent:
- Depends on: ADR 0006, ADR 0008, ADR 0013
- Blocks:
- Related: ADR 0016

## Adjudicator Decision Points

- Implementation requested 2026-08-26 for all six acceptance notes.

## Context

- Included: copy/update path lists, shipped ADRs and collaboration docs,
  agent contracts, DoD, issue/work-plan templates.
- Omitted: application code, provider SDKs, this template's historical
  traces and issue files (they stay uncopied).
- Assumptions: process ADR numbers 0001–0015 remain; only template-local
  issue/work-plan IDs are removed from shipped Canonical text.

## AI Planning Records

### AIP-0021-001

- Status: accepted
- Created by:
  - Agent/environment: Grok Build
  - Model as displayed: Grok 4.6
  - Reasoning setting as displayed: N/A; not exposed
  - N/A reason: environment does not expose the setting
- Created at: 2026-08-26
- Planning size: L
- Intended execution route: process-only; docs, contract alignment, copy
  exclusion, throwaway-target smoke tests
- Intended scope: adopter ID hygiene, placeholders, Claude full-mirror
  Canonical text, meta lessons, completion process review
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: multiple contract surfaces and shipped ADRs
- Assumptions: no provider SDK
- Confidence: medium

## References

- `docs/architecture/adr/0006-prompt-instruction-change-control.md`
- `docs/architecture/adr/0008-template-update-propagation.md`
- `docs/architecture/adr/0016-process-lessons-and-completion-review.md`

## Work Notes

- Implementation on `process/liss-0021-adopter-hygiene-and-process-review`.

## Verification

- Throwaway copy: no `WP-*.md`, no `reviews/*.md`, no template-local
  `LISS-NNNN` / `WP-NNNN` in shipped Canonical files except naming-format
  examples: passed.
- `bash -n` on touched scripts: passed.
- `git diff --check`: passed after trimming template trailing whitespace.

Process review: no operating-contract deviation or operational problem found.
