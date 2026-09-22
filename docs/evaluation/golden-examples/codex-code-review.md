# Codex Code Review Synthetic Examples

These examples are synthetic evaluation inputs, not repository changes or
approval records. Evaluate them with
`docs/evaluation/criteria/codex-code-review.md`.

## Rule 1 trigger: unapproved behavior

Accepted specification: “Rename the exported `format_date` helper; preserve
its output and all callers.” Approved phase: implementation of that rename.

Synthetic diff summary: the patch also changes date parsing to use the machine's
local timezone, changing output for existing callers. No specification update
or approval is recorded.

Expected finding: flag the timezone behavior as outside the accepted
specification and ask for its removal or an explicit reviewed specification
update. Do not describe the finding as approval.

## Rule 1 safe counterexample: specified behavior

Accepted specification: “Rename the exported `format_date` helper; preserve
its output and all callers.” Approved phase: implementation of that rename.

Synthetic diff summary: the helper and its callers are renamed, output behavior
is unchanged, and the focused regression test confirms the existing format.

Expected result: no Rule 1 finding.

## Rule 2 trigger: incomplete verification claim

Synthetic PR report: “All tests pass; full Green.” Evidence lists only
`python3 -m pytest tests/unit/test_dates.py` against commit `abc1234`; the PR
head is `def5678`, and the declared blocking regression suite is absent.

Expected finding: identify both the missing blocking suite and SHA mismatch;
request evidence for the final commit or a narrower claim. Do not infer that
unrun tests passed.

## Rule 2 safe counterexample: scoped evidence

Synthetic PR report: “Focused date tests passed on `def5678`. Full Green is not
claimed; the blocking regression suite is environment-blocked and remains
unassessed.” The report names the environment and the final SHA.

Expected result: no Rule 2 finding; the report accurately distinguishes
focused success from the unassessed blocking suite.
