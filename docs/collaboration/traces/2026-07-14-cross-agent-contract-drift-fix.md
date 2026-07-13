# AI Work Trace

## Request

- Date: 2026-07-14
- User request: "llm_project_templateについて詳しく確認しロジックエラーや
  間違いが無いか調べて報告して" (audit the template for logic errors/
  mistakes and report), followed by "修正ブランチを切ってPRを作成して" (cut
  a fix branch and open a PR) to act on the findings.
- Current phase: docs-only (Architecture Path — contract file changes).
- Canonical issue or work plan: this trace covers fixes F1, F2, F3, F5, F6
  from the audit; F4 is recorded separately as
  `docs/issues/LISS-0011-update-script-new-file-placeholder-substitution.md`
  and not implemented here.
- AI planning record: none opened (audit + fix classified as directly
  actionable corrections to already-merged PR #6 content, not new design
  work; see Referee Decisions below).

## Context Ledger

- Included: all five agent operating contract files (`AGENTS.md`,
  `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`,
  `.cursor/rules/*.mdc`), `scripts/init-llm-context.sh`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/update-ai-collaboration-files.sh`, `docs/architecture/
  external-resource-adoption-contract.md`, `docs/architecture/
  io-reasoning-contracts.md`, `docs/collaboration/ai-failure-recovery.md`,
  `docs/collaboration/model-tool-capability-matrix.md`,
  `docs/issues/LISS-0008-*.md`, `docs/work-plans/WP-0001-*.md`.
- Omitted: application-level source (none exists in this template repo);
  full content of every architecture/collaboration doc (only grep-targeted
  sections were read for the audit itself).
- Assumptions: the audit was performed against the PR #6 branch content
  (post-merge-into-local-main state), which is the actual diff under
  review; findings apply equally regardless of whether PR #6 has been
  merged on GitHub yet.
- Open decisions: none for F1/F2/F3/F5/F6; F4's exact fix design is left
  open in LISS-0011 pending Referee input.

## Routing

- Model/assistant/tool: deterministic search (`grep`, `diff`, targeted
  `Read`) for the audit phase; direct edits for the fix phase. No web
  search needed (no external tool conventions were in question this round).
- Reason: the audit is a mechanical cross-file consistency check well
  suited to deterministic tools; per `docs/collaboration/
  model-tool-capability-matrix.md`, this keeps the task on the cheapest
  safe route rather than escalating.
- Privacy constraints: none.

## AI Execution Records

### Attempt 1

- Agent: Claude Code CLI
- Environment: Claude Code CLI
- Model as displayed: Claude Sonnet 5 (audit was performed under Claude
  Fable 5 per a `/model` switch immediately before the audit request; the
  fix implementation in this trace was performed after switching back to
  Claude Sonnet 5)
- Reasoning setting as displayed: N/A
- Token usage: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- N/A reason: no reasoning-effort label or token usage value is exposed to
  this agent in this environment's output.
- Scope: audit (15 deterministic checks: broken code spans, cross-file doc
  reference parity, referenced-path existence, script placeholder/mdc
  handling, agent-list consistency, gap-7 residue, LISS/WP status
  consistency, `.mdc` frontmatter, cursor-vs-grok content-equivalence) plus
  implementation of fixes F1, F2, F3, F5, F6 and LISS-0011 for F4.
- Result: 6 findings (F1-F6) reported; F1/F2/F3/F5/F6 fixed in this
  attempt; F4 recorded as LISS-0011, not implemented.
- Attempt boundary: the audit (under Fable 5) and the fix (under Sonnet 5)
  are treated as one attempt — the environment/model switch was a routine
  `/model` command between a report and its accepted follow-up action, not
  a replan or a resumption after an unresolved stop.
- Notes: F1-F4 were defects introduced by this same session's own earlier
  work (LISS-0008/0009/0010); the audit caught them before merge to
  `origin/main`, which is the reason PR-based review (rather than direct
  push) was valuable here.

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: N/A

## Cost / Reasoning Control

- Operating path: Architecture Path (agent operating contract files
  changed).
- Files read: ~20 for the audit (grep-targeted), ~10 re-read for the fix.
- Context intentionally omitted: full-file reads where a targeted grep/Read
  of the relevant section sufficed.
- Deterministic checks used: `grep` for cross-file reference parity, broken
  code-span detection, path-existence verification; `diff` for cursor-vs-
  grok content equivalence; `bash -n` for script syntax; local CI-check
  reproduction (see Verification).
- Escalation reason: none — the entire audit and fix stayed on
  deterministic-tool/direct-edit routing, no ambiguous design decision was
  needed for F1/F2/F3/F5/F6 (each has one unambiguous correct fix restoring
  parity with an existing pattern). F4 was explicitly *not* fixed here
  because its fix does require a Referee design decision (see LISS-0011),
  which is why it was deferred rather than guessed.
- Avoided LLM work: reused exact existing patterns (CLAUDE.md's reference
  lines, the working `*.mdc` glob fix's sibling script) instead of
  re-deriving wording.
- Rework caused by AI output: this entire trace *is* the rework-correction
  for defects introduced by the prior session's AI output (F1-F3, F5-F6);
  recorded here per `docs/collaboration/llm-cost-reduction.md`'s "make
  rework visible" goal.

## Referee Decisions

- 2026-07-14: requested a detailed logic-error audit of the template.
- 2026-07-14: approved proceeding with the proposed fix plan (fix F1, F2,
  F3, F5, F6 in a new branch/PR; record F4 as a separate Local Issue rather
  than fixing it now) by requesting "修正ブランチを切ってPRを作成して"
  without further amendment.

## Verification

- Commands/checks:
  - Re-ran the F1 cross-file reference-parity check: all five contract
    files now reference all three new documents (previously only
    `CLAUDE.md` did).
  - Re-ran the F5 broken-code-span check: zero remaining matches outside
    the two pre-existing, unrelated hits in `LISS-0004`/`LISS-0006` (not in
    scope for this fix).
  - `bash -n` on `scripts/init-llm-context.sh` after the F3 edit — pass.
  - (Additional checks below, run before finalizing this trace.)
- Result: see Changed Files and the final verification pass noted in the
  Next Safe Action.

## Changed Files

- `AGENTS.md`, `.github/copilot-instructions.md`, `.grok/rules/01-quickstart.md`,
  `.cursor/rules/01-quickstart.mdc` (F1: new-doc reference lines added)
- `.grok/rules/01-quickstart.md` (F2: mirror sentence + agent list now
  include Cursor)
- `scripts/init-llm-context.sh` (F3: `.cursor/rules/*.mdc` added to
  `required_files`)
- `docs/collaboration/model-tool-capability-matrix.md`,
  `docs/collaboration/ai-failure-recovery.md`,
  `docs/architecture/io-reasoning-contracts.md`,
  `docs/architecture/external-resource-adoption-contract.md` (3 spots),
  `docs/issues/LISS-0008-ai-failure-and-recovery-procedure.md` (2 spots)
  (F5: line-broken code spans unwrapped)
- `docs/work-plans/WP-0001-external-feedback-2026-07-13.md` (F6: abbreviated
  self-reference resolved to a real path)
- `docs/issues/LISS-0011-update-script-new-file-placeholder-substitution.md`
  (new; records F4 as a proposed issue)
- `docs/collaboration/traces/2026-07-14-cross-agent-contract-drift-fix.md`
  (new, this file)

## Next Safe Action

- Run the full local CI-equivalent verification suite (required-files,
  ADR-existence, contract-traceability, `git diff --check`), commit on
  `process/2026-07-13-cross-agent-contract-drift-fix` (branched from the
  PR #6 branch), push, and open a PR with base
  `process/2026-07-13-template-feedback-and-agent-updates` (stacked on PR
  #6, since the referenced files don't exist on `main` until PR #6 merges).

## Notes

- No secrets, API keys, or private data were included in this trace or the
  documents it covers.
