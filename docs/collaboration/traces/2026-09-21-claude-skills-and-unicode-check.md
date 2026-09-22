# AI Work Trace

## Request

- Date: 2026-09-21
- User request: 「.claude/skillsが必要だと分かった。.agentsを参考にし、.claude用のskillsを追加して。また、不可視Unicode検出のCIチェックを追加して。」
- Current phase: process-only
- Canonical issue or work plan: `docs/issues/LISS-0028-claude-skills-and-invisible-unicode-check.md`
- AI planning record: AIP-0028-001

## Context Ledger

- Included: Claude Code skills/memory docs (fetched 2026-09-21), ADR 0006, ADR 0018, prompt-instruction-change-control, adoption-guide, collaboration-template-paths.sh, ci.yml, scripts/tests.
- Omitted: other vendors' skill discovery (unchanged by this work).
- Assumptions: no allowlist for invisible characters (zero occurrences before introduction); symlink rejected because copy/update distribute regular files only.
- Open decisions: implementation review and merge approval.

## Routing

- Model/assistant/tool: host agent (Claude Code) + deterministic tools (unittest, diff, local replay of CI steps).
- Reason: contract-file and ADR change; Architecture Path.
- Privacy constraints: public documentation only.

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: desktop app, macOS
- Model as displayed: claude-opus-5
- Reasoning setting as displayed: N/A (not displayed by host)
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: host does not expose per-task token counts.
- Estimate variance: N/A
- Variance reason: N/A
- Scope: skill mirror, invisible Unicode checker and tests, CI, distribution paths, ADR 0006/0018, change-control and adoption docs.
- Result: completed; one in-attempt fix (see Notes).
- Attempt boundary: single session on branch `process/liss-0028-claude-skills-and-unicode-check`.
- Notes: the first all-blocking replay failed because the new checker found literal invisible characters in its own test fixtures. Fixtures now use `chr()`; commit `a3dbf26`.

## Cost / Reasoning Control

- Operating path: Architecture Path
- Files read: listed in Context Ledger.
- Context intentionally omitted: research documents, unrelated ADRs.
- Deterministic checks used: unittest, `diff -r`, checker run on the repository, YAML parse, local replay of every non-PR-only CI step.
- Escalation reason: agent operating contract and ADR change.
- Avoided LLM work: parity enforced by `diff -r` instead of review judgment.
- Rework caused by AI output: test fixtures written with literal invisible characters; caught by the new check.

## Adjudicator Decisions

- 2026-09-21: add `.claude/skills/`; form is a full copy (not thin wrappers).
- 2026-09-21: invisible Unicode check covers all Git-tracked text.

## Verification

- Commands/checks:
  - Focused: `python3 -m unittest test_invisible_unicode` (8 tests: 5 rejection, 3 pass paths); `test_distribution.DistributionTests.test_copy_distributes_claude_skill_mirror` (failed with `.claude/skills` removed from the distribution list, passes with it); `diff -r` exits 1 after an appended drift line and 0 after restore.
  - All-blocking: every non-PR-only step of `.github/workflows/ci.yml` replayed locally, including `scripts/run-regression-tests.py`.
- Result:
  - At `fc22b49`: all steps passed except the new invisible Unicode step (fixture defect above). Regression suite 40 tests, 0 failures.
  - After the fix and this trace: see the final all-blocking rerun reported in the PR (tested SHA recorded there).
  - Not run locally: PR-only contract traceability step (runs in CI).
  - Environment: macOS (Darwin 27.0.0), Python 3.14.6; CI uses ubuntu-latest.

## Changed Files

- `.claude/skills/*/SKILL.md` (8 files, byte-identical to `.agents/skills/`)
- `.github/workflows/ci.yml`
- `scripts/check-invisible-unicode.py`
- `scripts/lib/collaboration-template-paths.sh`
- `scripts/tests/support.py`, `scripts/tests/test_distribution.py`, `scripts/tests/test_invisible_unicode.py`
- `docs/architecture/adr/0006-prompt-instruction-change-control.md`
- `docs/architecture/adr/0018-agent-skills-for-on-demand-procedures.md`
- `docs/collaboration/adoption-guide.md`
- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/issues/LISS-0028-claude-skills-and-invisible-unicode-check.md`

## Next Safe Action

- Adjudicator reviews the PR. After merge, mark LISS-0028 done with a process review.

## Notes

- Expected agent behavior change: Claude Code can load template skills by description from `.claude/skills/`; contract files still name `.agents/skills/` paths. Any tracked file containing invisible Unicode now fails CI in this repository and in adopters after sync.
