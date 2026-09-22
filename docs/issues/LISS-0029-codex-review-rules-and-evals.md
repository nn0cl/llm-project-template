# LISS-0029: Codex Code Review rules and evaluation examples

## Metadata

- Local issue ID: LISS-0029
- GitHub issue: none
- Status: in_progress
- Phase: process-only
- Type: process / agent-instructions
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: none
- Owner/agent: Codex
- Related branch: process/codex-review-rules-evals

## Summary

Evaluate and adopt the reusable part of Codex Code Review's repository-rules
feature. Add a small, explicitly scoped Code Review Rules section to
`AGENTS.md`, then add synthetic evaluation cases that check both intended
findings and safe counterexamples. Keep CI and human Adjudicator approval as
the enforcement gates; Code Review is advisory.

## Acceptance Notes

1. `AGENTS.md` has no more than three concise Code Review rules. Each names
   the invariant, its applicable change scope, and the safe disposition.
   Rules summarize existing accepted policy and link to canonical documents;
   they do not establish new approval, phase, or test policy.
2. The rules target consequential review judgments that are not already
   enforced deterministically, or add useful semantic context to a CI check.
   CI remains responsible for mechanical checks, and human review remains
   required where existing policy says so.
3. `docs/evaluation/criteria/` contains a rubric mapping each rule to its
   canonical policy, a triggering synthetic change, an expected finding, and
   a safe counterexample that should not produce a finding.
4. Evaluation cases contain no private data or secrets. They do not claim a
   Codex Code Review run passed unless that feature was actually exercised;
   unavailable execution is recorded as unassessed.
5. No Codex API, GitHub Action, new dependency, model pin, or external service
   is added. Existing distribution rules continue to copy the evaluation
   directories and `AGENTS.md` without copying private review settings.
6. The contract change has a work trace, passes contract-file traceability,
   and receives Adjudicator review before merge.

## Dependencies

- Parent: none
- Depends on: none
- Blocks: none
- Related: ADR 0006, ADR 0018, `docs/collaboration/evaluation-and-golden-examples.md`

## Adjudicator Decision Points

- [x] Accept the proposed scope and acceptance notes (Adjudicator, 2026-09-23).
- [x] Select process-only implementation (Adjudicator, 2026-09-23).
- [ ] Review the completed implementation before merge.

## Context

- Included: `AGENTS.md`, Codex Code Review guidance, evaluation policy and
  directories, prompt/instruction change control, current CI/distribution and
  review policies.
- Omitted: app-specific installation, API integration, and unrelated model or
  pricing changes.
- Assumptions: Code Review is an additional reviewer; this template must not
  require its availability or treat its output as approval.

## AI Planning Records

### AIP-0029-001

- Status: accepted
- Created by:
  - Agent/environment: Codex / desktop app
  - Model as displayed: GPT-6
  - Reasoning setting as displayed: N/A
  - N/A reason: host does not expose a separate reasoning setting
- Created at: 2026-09-23
- Planning size: M
- Intended execution route: host agent plus deterministic repository checks;
  actual Codex Code Review behavior only if an approved, callable review path
  is available.
- Intended scope: `AGENTS.md`, one evaluation rubric under
  `docs/evaluation/criteria/`, synthetic golden examples under
  `docs/evaluation/golden-examples/`, a work trace, and this local issue.
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: multiple contract/evaluation artifacts and full repository
  verification; current execution plan remains subject to Adjudicator review.
- Assumptions: no application code or new runtime dependency is needed.
- Confidence: medium
- Revises: none
- Revision reason: none
- Superseded by: none

## References

- OpenAI, “Custom Code Review rules for Codex,” fetched 2026-09-23:
  https://developers.openai.com/blog/custom-code-review-rules-for-codex
- OpenAI, “Testing Agent Skills Systematically with Evals,” fetched
  2026-09-23: https://developers.openai.com/blog/eval-skills
- Codex changelog, fetched 2026-09-23:
  https://learn.chatgpt.com/docs/changelog

## Work Notes

- The latest official guidance recommends concise, scoped review rules and
  treating deterministic checks separately from judgment-based review.
- The repository already has empty golden-example and criteria directories;
  the proposal uses them rather than introducing a review service.
- The Adjudicator accepted this scope and its acceptance notes on 2026-09-23.

## Verification

- Pre-commit focused/regression: `PYTHONDONTWRITEBYTECODE=1 python3
  scripts/run-regression-tests.py` passed 40 tests, 0 failures/errors/skips on
  base SHA `6bdb8f09c081f9192036a533addfe666efe8ad8b` with a dirty tree
  (macOS 27.0 arm64, Python 3.14.6). This is not final-SHA evidence.
- `python3 scripts/check-invisible-unicode.py`: passed (236 text files).
- `python3 scripts/check-document-lifecycle.py`: passed (1 register).
- `python3 scripts/check-execution-batch-reviews.py --branch
  process/codex-review-rules-evals`: passed (0 applicable records).
- Shell syntax and `.agents/skills` / `.claude/skills` mirror: passed.
- Distribution smoke: pre-commit attempt stopped as designed because the
  source tree was dirty; rerun against committed source is pending.
- Distribution unit tests: passed 13 tests using
  `PYTHONPATH=scripts/tests python3 -m unittest test_distribution`.
- Initial direct unittest module invocation failed because it omitted the
  test support import path; corrected invocation passed. No product failure.
- Full CI-equivalent blocking suite and final-SHA rerun: pending commit.
- Live Codex Code Review evaluation: unassessed; no review run was invoked.

## Process Review

- Outcome: not yet
- Lesson written: not applicable
- Template-feedback path: none
