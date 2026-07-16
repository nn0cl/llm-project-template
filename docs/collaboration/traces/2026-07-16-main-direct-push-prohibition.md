# AI Work Trace

## Request

- Date: 2026-07-16
- User request: Prohibit direct pushes to the `main` branch.
- Current phase: process-only (docs).
- Canonical issue or work plan: none; explicit Adjudicator process-rule request.
- AI planning record: direct-push prohibition review.

## Context Ledger

- Included: `docs/collaboration/branch-commit-pr-discipline.md`,
  `docs/collaboration/local-issue-planning.md`, and the pull-request workflow
  guidance.
- Omitted: application source and unrelated CI jobs.
- Assumptions: `main` is the repository trunk branch unless a repository
  adopts another documented trunk name.
- Open decisions: repository administrators must configure the corresponding
  hosting-provider branch protection settings.

## Routing

- Model/assistant/tool: deterministic repository inspection and document edit.
- Reason: this is a process-rule change with no implementation behavior.
- Privacy constraints: none.

## AI Execution Records

### Attempt 1

- Agent: Codex
- Environment: Codex desktop workspace
- Model as displayed: GPT-5
- Reasoning setting as displayed: N/A
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not exposed by the environment.
- Estimate variance: N/A
- Variance reason: N/A.
- Scope: make the direct-push prohibition explicit and document the required
  server-side branch protection.
- Result: completed.
- Attempt boundary: single cohesive execution.
- Notes: no direct push to `main` was attempted.

## Cost / Reasoning Control

- Operating path: Architecture Path because an agent operating contract file changed.
- Files read: branch/commit/PR discipline, local issue planning, and PR guidance.
- Context intentionally omitted: application implementation and unrelated workflows.
- Deterministic checks used: `git diff --check` and working-tree inspection.
- Escalation reason: none.
- Avoided LLM work: none.
- Rework caused by AI output: none.

## Adjudicator Decisions

- 2026-07-16: Adjudicator requested that direct pushes to `main` be prohibited.

## Verification

- Commands/checks: `git diff --check`; review of the affected operating-contract file.
- Result: pass.

## Changed Files

- `docs/collaboration/branch-commit-pr-discipline.md`
- `docs/collaboration/traces/2026-07-16-main-direct-push-prohibition.md`

## Next Safe Action

- Configure branch protection for `main` in the repository hosting settings.

## Notes

- This change documents the policy; GitHub branch protection is required for
  technical enforcement.
