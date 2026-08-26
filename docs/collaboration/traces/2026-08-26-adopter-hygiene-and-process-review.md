# AI Work Trace

## Request

- Date: 2026-08-26
- User request: keep template-local issue/ADR identifiers out of adopting
  repositories; require unfilled placeholders to be set; Canonical text must
  say CLAUDE.md is a full mirror with no import; record reviews as meta-level
  lessons; run a same-context process review when an issue or work plan
  completes and leave template-feedback records after Adjudicator agreement.
- Current phase: process-only, Architecture Path implementation.
- Canonical issue or work plan:
  `docs/issues/LISS-0021-adopter-hygiene-and-process-review.md`.
- AI planning record: AIP-0021-001 in the issue above.

## Context Ledger

- Included: copy/update path lists, shipped ADRs and collaboration docs,
  agent contracts, DoD, issue/work-plan templates.
- Omitted: application source, provider SDKs, historical traces (remain
  uncopied).
- Assumptions: process ADR numbers stay; only template-local issue and
  work-plan IDs are removed from shipped Canonical text.

## Routing

- Model/assistant/tool: Grok Build; Bash throwaway copy for verification.
- Reason: contract and adoption-tooling change.
- Privacy constraints: no secrets or adopter data.

## AI Execution Records

### Attempt 1

- Agent: Grok Build
- Environment: Grok Build
- Model as displayed: Grok 4.6
- Reasoning setting as displayed: N/A; not exposed.
- Actual tokens: N/A; not exposed.
- Scope: copy exclusions, Canonical ID scrub, placeholder mandate, Claude
  full-mirror contract text, process lessons, completion process review,
  template-feedback records, ADR 0016, LISS-0021, CI smoke.
- Result: completed; verification recorded in the issue after the smoke run.

## Adjudicator Decisions

- 2026-08-26: implementation requested for all six acceptance notes.
- CLAUDE.md remains a full mirror and must not import `@AGENTS.md`.
- Lessons are meta-level, not incident narratives.

## Verification

- Commands/checks: throwaway copy, ID grep on shipped Canonical files,
  `bash -n`, `git diff --check`.
- Result: recorded after the local smoke run.

## Changed Files

- See the commit on `process/liss-0021-adopter-hygiene-and-process-review`.

## Next Safe Action

Review the branch and CI before merge.
