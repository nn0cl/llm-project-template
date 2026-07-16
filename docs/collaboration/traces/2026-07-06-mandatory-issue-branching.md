# AI Work Trace

## Request

- Date: 2026-07-06
- User request: Add a constraint that work on an issue must always happen on
  a dedicated branch; report the current branch strategy first.
- Current phase: Architecture Path / process rule tightening.

## Context Ledger

- Included: `docs/collaboration/branch-commit-pr-discipline.md`,
  `docs/collaboration/local-issue-planning.md`,
  `docs/architecture/adr/0005-local-issue-planning.md`.
- Omitted: unrelated CI file lists, other ADRs, target-project branch
  history.
- Assumptions: the rule applies to both local (`LISS-*`) and GitHub issues,
  and forbids committing issue work directly to `main` regardless of size.
- Open decisions: none.

## Routing

- Model/assistant/tool: direct documentation edit; no external tool needed.
- Reason: process rule change affecting future agent behavior.
- Privacy constraints: no private data used.

## Adjudicator Decisions

- User requested the constraint be added after asking about current branch
  strategy.

## Verification

- Commands/checks: manual review of the three edited files for consistency.
- Result: passed.

## Changed Files

- `docs/collaboration/branch-commit-pr-discipline.md`
- `docs/collaboration/local-issue-planning.md`
- `docs/architecture/adr/0005-local-issue-planning.md`
- `docs/collaboration/traces/2026-07-06-mandatory-issue-branching.md`

## Next Safe Action

- Commit and push if the Adjudicator accepts the wording.

## Notes

- This closes the previous gap where ADR 0005 only rejected feature branches
  without a related issue, but did not forbid issue work landing directly on
  `main`.
