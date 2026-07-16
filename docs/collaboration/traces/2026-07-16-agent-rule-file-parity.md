# AI Work Trace

## Request

- Date: 2026-07-16
- User request: consider mt4-orchestration adopter feedback item 2 ("rule
  modularization"); scope to agent rule-file organization; find current
  official grounds for consolidating vs. keeping the full-mirror pattern
  across the five agent contract files; reconsider the blanket full-mirror
  decision itself rather than treating it as fixed precedent.
- Current phase: process-only (docs), Architecture Path (contract files
  changed).
- Canonical issue or work plan: `docs/issues/LISS-0015-agent-rule-file-parity.md`.
- AI planning record: AIP-0015-001 (in the issue above).

## Context Ledger

- Included: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/*.md`, `.cursor/rules/*.mdc`,
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/collaboration/adoption-guide.md`, `.github/workflows/ci.yml`,
  LISS-0006/LISS-0010 and their traces.
- Omitted: application source; adopter feedback items 1 (resolved by
  LISS-0014) and 3 (explicitly out of scope, per Adjudicator instruction).
- Assumptions: vendor conventions confirmed live on 2026-07-16 are accurate as
  of that date; Grok's conventions were not re-verified this round and rely on
  LISS-0006/LISS-0010's existing findings.
- Open decisions: whether the Cursor `.cursor/rules/*.mdc` shrink-to-reference
  trial actually works — requires a live Cursor session to verify, which this
  agent cannot perform. Recorded as a blocking pending item, not resolved
  here.

## Routing

- Model/assistant/tool: Claude Code CLI, live WebSearch/WebFetch for current
  vendor documentation (required by this template's anti-hallucination rules
  for external tool conventions; training-data memory was not used for
  vendor-capability claims).
- Reason: Architecture Path work changing agent operating contract files.
- Privacy constraints: none; no private or target-specific data involved.

## AI Execution Records

### Attempt 1

- Agent: Claude Code CLI
- Environment: Claude Code CLI (claude-sonnet-5)
- Model as displayed: Claude Sonnet 5
- Reasoning setting as displayed: N/A
- Estimated token range: 8,000-16,000 (per AIP-0015-001)
- Estimated token midpoint: 12,000
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not exposed by this environment's output.
- Estimate variance: N/A
- Variance reason: N/A
- Scope: research current vendor conventions (Copilot, Claude Code, Cursor)
  via live WebSearch/WebFetch; reconsider the blanket full-mirror decision
  from LISS-0006/LISS-0010 per vendor; consolidate `CLAUDE.md` via
  `@AGENTS.md` import; trial-shrink `.cursor/rules/*.mdc` to `@AGENTS.md`
  references; keep `.github/copilot-instructions.md` and `.grok/rules/*.md`
  as full mirrors per Adjudicator decision; update ADR 0006 and
  `prompt-instruction-change-control.md` in place; add a new
  stack-specific-scoped-rules section to `adoption-guide.md`.
- Result: completed, with one item left open (Cursor live verification,
  recorded as a blocking follow-up, not claimed as done).
- Attempt boundary: single cohesive execution across one chat session.
- Notes: two rounds of Adjudicator direction shaped scope — first round excluded
  adopter feedback item 3; second round asked for the full-mirror decision
  itself to be re-grounded rather than assumed. An `AskUserQuestion` was used
  to get an explicit Adjudicator decision on Copilot (keep full mirror) and
  Cursor (attempt the trial) once the trade-offs were evidenced.

## Optional Reference Total

- Value:
- Metric:
- Source:
- Compatibility statement:

## Cost / Reasoning Control

- Operating path: Architecture Path (agent operating contract files changed).
- Files read: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/*.md` (read for comparison in a prior turn), `.cursor/rules/*.mdc`,
  ADR 0006, `prompt-instruction-change-control.md`, `adoption-guide.md`,
  `.github/workflows/ci.yml`, LISS-0006, LISS-0010.
- Context intentionally omitted: application source; unrelated CI jobs;
  Grok-specific re-verification (out of scope this round).
- Deterministic checks used: `grep` over CI workflow to confirm it does not
  byte-diff contract files against `AGENTS.md` (so no CI change was needed);
  manual line-by-line comparison of `AGENTS.md` vs. `CLAUDE.md` before editing
  to identify genuinely duplicate vs. Claude-specific sections.
- Escalation reason: none.
- Avoided LLM work: none.
- Rework caused by AI output: none.

## Adjudicator Decisions

- 2026-07-16 (first round): scope this issue to rule-file organization only,
  excluding adopter feedback item 3.
- 2026-07-16 (second round): the full-mirror decision itself needs current
  grounds, not inherited precedent; reconsider it.
- 2026-07-16 (via AskUserQuestion): keep `.github/copilot-instructions.md` as
  a full mirror; attempt the `.cursor/rules/*.mdc` shrink-to-reference trial.
- 2026-07-16: proceed with implementation as described.

## Verification

- Commands/checks: manual re-read of the edited `CLAUDE.md` to confirm no
  content was silently dropped (only sections verbatim-identical to
  `AGENTS.md` were removed: Session Entry, Clean Architecture Dependency
  Rule, External Resources Must Be Ports, Adjudicator Interaction); `grep` over
  `.github/workflows/ci.yml` confirming its required-files and
  contract-traceability checks do not depend on literal content matching, so
  no CI changes were required.
- Result: pass for the checks above. The Cursor live-verification step is
  explicitly NOT done and is recorded as the next safe action, not as passed.

## Changed Files

- `AGENTS.md`
- `CLAUDE.md`
- `.cursor/rules/01-quickstart.mdc`
- `.cursor/rules/02-architecture-boundaries.mdc`
- `.cursor/rules/03-collaboration-and-completion.mdc`
- `docs/architecture/adr/0006-prompt-instruction-change-control.md`
- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/collaboration/adoption-guide.md`
- `docs/issues/LISS-0015-agent-rule-file-parity.md`
- `docs/collaboration/traces/2026-07-16-agent-rule-file-parity.md` (this file)

## Next Safe Action

- Completed by follow-up: live Cursor verification (2026-07-16) showed native
  `AGENTS.md` auto-apply makes `.mdc` `@AGENTS.md` references redundant;
  references removed; primary-source grounds attached; Adjudicator approved —
  see `docs/collaboration/traces/2026-07-16-cursor-mdc-drop-agents-ref.md`.
- Open PR for branch `process/agent-rule-file-parity` (contract files;
  human PR review still required for merge).

## Notes

- This issue supersedes LISS-0006's and LISS-0010's blanket "full mirror
  across all five files" framing with a per-vendor policy; it does not
  invalidate their file-existence decisions (Grok and Cursor still get
  dedicated files; Codex still needs none).
