# LISS-0026: Move remaining on-demand procedures into Agent Skills

## Metadata

- Local issue ID: LISS-0026
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/docs
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Owner/agent: Grok
- Related branch: process/liss-0026-more-agent-skills

## Summary

Continue ADR 0018: move four more existing on-demand procedures into
`.agents/skills/`. Keep typed Approval Model safety rules in the contract
files.

## Acceptance Notes

1. Skills exist at `.agents/skills/{process-lessons,adjudicator-review,ai-work-trace,execution-batch}/SKILL.md`.
2. Contract files name those skill paths for writing lessons, asking approval, tracing, and filling a batch record.
3. Standing Approval Model rules stay in the contract files: typed approvals, batch approval does not waive other rules, `batch/<batch-id>`, CI is not Adjudicator approval.
4. Canonical policy and templates remain the source of truth.
5. CI requires the four new `SKILL.md` files.

## Dependencies

- Related: ADR 0018, LISS-0025

## Adjudicator Decision Points

- Implementation requested 2026-08-26 as a continuation of the skills move.

## Context

- Included: remaining task-triggered procedures still named from contract files.
- Omitted: Session Entry thinning, vendor skill copies, hooks, custom agent profiles.
- Assumptions: ADR 0018 already decided the skill location and contract-file obligation pattern.

## AI Planning Records

### AIP-0026-001

- Status: accepted
- Created by:
  - Agent/environment: Grok Build
  - Model as displayed: Grok 4.6
  - Reasoning setting as displayed: N/A; not exposed
  - N/A reason: environment does not expose the setting
- Created at: 2026-08-26
- Planning size: M
- Intended execution route: process-only
- Intended scope: four additional skills and contract pointers
- Estimated token range: N/A
- Token metric: N/A
- Estimation basis: same pattern as LISS-0025
- Confidence: high

## References

- `docs/architecture/adr/0018-agent-skills-for-on-demand-procedures.md`

## Verification

- Copy smoke includes the eight skills.
- No fenced `[DESIGN CHECK]` scaffold returned to AGENTS.md or CLAUDE.md.
- Approval Model still states CI is not Adjudicator approval.
- `git diff --check` and repository CI (PR #37).

Process review: no operating-contract deviation or operational problem found.
