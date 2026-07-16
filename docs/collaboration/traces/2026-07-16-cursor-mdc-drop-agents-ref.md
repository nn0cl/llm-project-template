# AI Work Trace

## Request

- Date: 2026-07-16
- User request: after confirming Cursor auto-applies root `AGENTS.md`
  independently of `.cursor/rules`, remove redundant `@AGENTS.md` references
  from `.mdc` rules ("optimize"); then attach primary-source grounds and
  record Adjudicator approval ("根拠を付けて修正して。承認します。").
- Current phase: process-only (docs), Architecture Path (contract files
  changed).
- Canonical issue or work plan: `docs/issues/LISS-0015-agent-rule-file-parity.md`.
- AI planning record: AIP-0015-001 (prior); this follow-up executes Adjudicator
  refinement after live Cursor verification.

## Context Ledger

- Included: `.cursor/rules/*.mdc`, ADR 0006,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/collaboration/adoption-guide.md`, LISS-0015, prior parity trace,
  Cursor Rules docs (fetched), this session's always-applied rule injection
  evidence.
- Omitted: `CLAUDE.md` `@AGENTS.md` import (Claude Code mechanism; out of
  scope), copilot/grok full mirrors, application source.
- Assumptions: Cursor continues to auto-apply root `AGENTS.md` as a Rules
  type separate from `.cursor/rules`.
- Open decisions: none — Adjudicator approved the grounded revision 2026-07-16.

## Routing

- Model/assistant/tool: Cursor agent (Composer); cursor-guide; WebFetch of
  Cursor docs for citation URLs.
- Reason: Architecture Path; contract-file optimization after live
  verification.
- Privacy constraints: none.

## Evidence (grounds for omitting `@AGENTS.md` from `.mdc`)

1. **Product taxonomy**: Cursor lists four rule types — Project Rules
   (`.cursor/rules`), User Rules, Team Rules, and **AGENTS.md** — as peer
   mechanisms ([Rules](https://cursor.com/docs/rules.md), fetched
   2026-07-16). Shared contract in root `AGENTS.md` is therefore loaded by a
   different binding than Project Rules.
2. **Automatic pickup**: Help documents that placing `AGENTS.md` in the
   project root means "Cursor picks it up automatically"
   ([Help: Rules](https://cursor.com/help/customization/rules.md), fetched
   2026-07-16). Nested `AGENTS.md` is likewise "automatically applied" for
   matching paths ([Rules § AGENTS.md](https://cursor.com/docs/rules.md)).
3. **`@filename` is not required for AGENTS.md**: FAQ confirms `@filename`
   includes a file in a Project Rule's context
   ([Rules FAQ](https://cursor.com/docs/rules.md)). That mechanism remains
   useful for templates/examples; for root `AGENTS.md` it re-attaches what
   (1)–(2) already load.
4. **Live session outcome (this repo, 2026-07-16)**: Agent context included
   root `AGENTS.md` as its own always-applied workspace rule with full body
   (Expected Workflow, Session Entry, Clean Architecture Dependency Rule,
   External Resources Must Be Ports, Adjudicator Interaction) *and* the three
   `alwaysApply: true` `.mdc` files. Literal `See @AGENTS.md` text inside
   `.mdc` was present as prose, not an expanded inline paste. Therefore
   shared rules survived without depending on `@` resolution inside `.mdc`.
5. **Policy choice**: Keep `.mdc` for Cursor-only complements (Phase Gate
   detail, Anti-Hallucination, Decision Gates, Handoff/Completion). Omit
   shared-section mirrors and omit `@AGENTS.md` from `.mdc` to avoid a
   second, redundant binding path.

Regression watch: if a future Cursor release stops auto-applying root
`AGENTS.md`, restore shared sections into `.mdc` or another binding (ADR
0006 Negative).

## AI Execution Records

### Attempt 1

- Agent: Cursor agent
- Environment: Cursor IDE
- Model as displayed: Composer
- Reasoning setting as displayed: N/A
- Estimated token range: 4,000-8,000
- Estimated token midpoint: 6,000
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not exposed by this environment.
- Estimate variance: N/A
- Variance reason: N/A
- Scope: drop `@AGENTS.md` from three `.mdc` files; update ADR 0006,
  change-control, adoption-guide, LISS-0015; add this trace; attach
  primary-source URLs and live-session evidence; record Adjudicator approval.
- Result: completed.
- Attempt boundary: single cohesive follow-up on branch
  `process/agent-rule-file-parity`.
- Notes: Causation (`@` vs native load) remains inconclusive; policy rests on
  (1)–(2) plus outcome (4), not on proving `@` fails.

## Optional Reference Total

- Value:
- Metric:
- Source:
- Compatibility statement:

## Cost / Reasoning Control

- Operating path: Architecture Path (agent operating contract files changed).
- Files read: three `.mdc`, ADR 0006, change-control, adoption-guide,
  LISS-0015, prior trace, ai-work-trace template; fetched Cursor docs.
- Context intentionally omitted: application source; copilot/grok bodies.
- Deterministic checks used: `rg '@AGENTS\.md' .cursor/rules/` after edit
  (expect zero matches for the import token).
- Escalation reason: none — Adjudicator requested optimization, then approved
  grounded revision.
- Avoided LLM work: no full-mirror restore after outcome evidence.
- Rework caused by AI output: none.

## Adjudicator Decisions

- 2026-07-16: live verification only (prior turn).
- 2026-07-16: if Cursor auto-applies `AGENTS.md` independently, `.mdc`
  references are unnecessary — optimize.
- 2026-07-16: attach grounds; approve ("根拠を付けて修正して。承認します。").

## Verification

- Commands/checks: `rg '@AGENTS\.md' .cursor/rules/` after edits; re-fetch
  Cursor docs URLs for citation accuracy.
- Result: no `@AGENTS.md` import token under `.cursor/rules/`; ADR/issue/trace
  cite https://cursor.com/docs/rules.md and
  https://cursor.com/help/customization/rules.md.

## Changed Files

- `.cursor/rules/01-quickstart.mdc`
- `.cursor/rules/02-architecture-boundaries.mdc`
- `.cursor/rules/03-collaboration-and-completion.mdc`
- `docs/architecture/adr/0006-prompt-instruction-change-control.md`
- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/collaboration/adoption-guide.md`
- `docs/issues/LISS-0015-agent-rule-file-parity.md`
- `docs/collaboration/traces/2026-07-16-agent-rule-file-parity.md`
- `docs/collaboration/traces/2026-07-16-cursor-mdc-drop-agents-ref.md` (this
  file)

## Next Safe Action

- Open PR for branch `process/agent-rule-file-parity` (contract-file change;
  merge still expects human PR review per change-control, even after chat
  approval of the decision).

## Notes

- Does not change `CLAUDE.md`'s `@AGENTS.md` import.
- Chat approval records the Architecture Path decision; PR merge remains a
  separate gate for the branch as a whole.
