# AI Work Trace

## Request

- Date: 2026-07-06
- User request: Research current best practices and research on branch
  strategy, report the findings, then implement the ones worth adopting.
- Current phase: Architecture Path / process rule addition (new ADR).

## Context Ledger

- Included: `docs/collaboration/branch-commit-pr-discipline.md`,
  `docs/architecture/adr/0005-local-issue-planning.md`, `README.md`,
  `.github/workflows/ci.yml`, web search results on trunk-based development,
  DORA research, git worktrees for parallel AI agents, and stacked PRs
  (2026 sources).
- Omitted: concrete merge-queue or feature-flag vendor choice, target-project
  CI implementation, private data.
- Assumptions: short-lived branches, mandatory CI-before-merge, worktree
  isolation for concurrent agents, and stacked branches for phase splitting
  are compatible with existing Red/Green/Refactor discipline and the
  issue-per-branch rule (ADR 0005); feature flags are not, so they are
  deferred rather than adopted.
- Open decisions: whether a future project adopts feature flags for
  trunk-based shipping of incomplete work (left to a future ADR).

## Routing

- Model/assistant/tool: WebSearch for current (2026) practice research;
  direct documentation edit for the ADR and process doc changes.
- Reason: process rule change affecting future agent branching behavior.
- Privacy constraints: no private data used.

## Adjudicator Decisions

- User reviewed the research report and approved implementing the findings.

## Verification

- Commands/checks: manual review of edited files for consistency; confirmed
  `.github/workflows/ci.yml` ADR-existence check now includes 0007.
- Result: passed.

## Changed Files

- `docs/collaboration/branch-commit-pr-discipline.md`
- `docs/architecture/adr/0007-trunk-oriented-branching.md`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/collaboration/traces/2026-07-06-trunk-oriented-branching.md`

## Next Safe Action

- Commit and push if the Adjudicator accepts the wording.

## Notes

- Feature flags were intentionally left as a non-decision; ADR 0007 records
  this explicitly so a future agent does not assume they are approved.
