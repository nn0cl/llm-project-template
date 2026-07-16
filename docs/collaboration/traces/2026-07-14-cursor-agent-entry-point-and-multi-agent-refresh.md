# AI Work Trace

## Request

- Date: 2026-07-14
- User request: "grok/cursor/codexの最新の情報を調べてテンプレートが働くよう
  に対応して" (research the latest information on Grok/Cursor/Codex and make
  the template work with them).
- Current phase: docs-only (Architecture Path — new agent operating
  contract files, per the same classification LISS-0006 used).
- Canonical issue or work plan:
  `docs/issues/LISS-0010-cursor-agent-entry-point-and-multi-agent-refresh.md`.
- AI planning record: AIP-0010-001.

## Context Ledger

- Included: `AGENTS.md`, `.grok/rules/*.md` (mirror source),
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`,
  `.github/workflows/ci.yml`, `README.md`, `README.ja.md`,
  `docs/collaboration/adoption-guide.md`,
  `docs/issues/LISS-0006-grok-agent-entry-point.md` and its trace.
- Omitted: full vendor documentation pages beyond what answered the
  specific discovery-order/file-format questions; no adopter-specific or
  private data (this round was Adjudicator-initiated research, not triggered by
  a specific adopter report).
- Assumptions: live web search results (2026-07-14) for Cursor and Grok
  Build reflect current vendor behavior; Codex behavior re-confirmed
  unchanged from LISS-0006 (2026-07-08).
- Open decisions: none blocking.

## Routing

- Model/assistant/tool: strong reasoning agent for research synthesis and
  cross-file consistency; three WebSearch calls (Cursor, Codex, Grok Build)
  plus two WebFetch calls (Grok Build overview page, Cursor rules docs page)
  to verify vendor-specific claims against current documentation rather than
  training knowledge, matching this template's own anti-hallucination rule
  against inventing external tool conventions. One WebFetch (a guessed
  `docs.x.ai/build` URL) 404'd; a follow-up WebSearch with a more specific
  query recovered the needed information instead.
- Reason: this repository explicitly requires verifying, not guessing,
  third-party tool conventions before documenting them (see LISS-0006's own
  trace for the same principle).
- Privacy constraints: none; all fetched/searched content was public vendor
  documentation.

## AI Execution Records

### Attempt 1

- Agent: Claude Code CLI
- Environment: Claude Code CLI
- Model as displayed: Claude Sonnet 5
- Reasoning setting as displayed: N/A
- Token usage: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- N/A reason: no reasoning-effort label or token usage value is exposed to
  this agent in this environment's output.
- Scope: research (3 WebSearch, 2 WebFetch, 1 recovered via a second
  WebSearch after a 404); create `.cursor/rules/*.mdc` (3 files, mirroring
  `.grok/rules/*.md`); fix `*.mdc` missing from the placeholder-substitution
  glob in `copy-ai-collaboration-files.sh`; add `.cursor/rules` to
  `collaboration-template-paths.sh`; update CI required-files and
  contract-traceability patterns; extend ADR 0006 in place; update
  README.md, README.ja.md, adoption-guide.md; write LISS-0010 and this
  trace.
- Result: implementation complete, verification passed (see below), pending
  Adjudicator review and commit decision.
- Attempt boundary: single cohesive session; no replanning or resumption.
- Notes: found and fixed a pre-existing bug while implementing (the `*.mdc`
  glob gap), verified by a live dry-run/non-dry-run execution of the copy
  script against a throwaway target directory — before the fix, placeholder
  substitution would have silently left `<PROJECT_NAME...>` and stack
  placeholders unfilled in any adopted project's `.cursor/rules/*.mdc`
  files.

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: N/A

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: approximately 15 (see Context Ledger), plus 5 live web
  fetches/searches.
- Context intentionally omitted: full vendor documentation beyond the
  specific questions needed; no adopter repository or private data involved.
- Deterministic checks used: `bash -n` on both touched shell scripts; local
  reproduction of CI's required-files check (with the 3 new `.cursor/rules`
  paths) and `git diff --check`; a live dry-run and real run of
  `copy-ai-collaboration-files.sh` against a throwaway `mktemp -d` target,
  confirming `.cursor/rules/*.mdc` files are copied and both project-name
  and stack placeholders are substituted correctly.
- Escalation reason: live web search/fetch was required specifically to
  verify current (2026) Cursor and Grok Build project-configuration
  conventions rather than relying on possibly-stale training knowledge.
- Avoided LLM work: reused the existing `.grok/rules/*.md` content verbatim
  as the mirror source instead of re-deriving the operating contract from
  `AGENTS.md` from scratch; reused LISS-0006's investigation method and
  acceptance-note structure directly.
- Rework caused by AI output: none in this session; this session itself
  fixed a small rework-causing bug (the `*.mdc` glob gap) left over from
  LISS-0006, before it could affect a real adopter.

## Adjudicator Decisions

- 2026-07-14: confirmed scope is "make Grok/Cursor/Codex work with the
  template" via live research, following the LISS-0006 precedent.
- (Implicit, consistent with LISS-0006's explicit decision, not
  re-litigated): full-mirror `.cursor/rules/*.mdc` over relying on Cursor's
  native `AGENTS.md` fallback support.

## Verification

- Commands/checks:
  - `bash -n` on `scripts/copy-ai-collaboration-files.sh` and
    `scripts/lib/collaboration-template-paths.sh` — pass.
  - Local reproduction of CI's "Check required project documents" step,
    including the 3 new `.cursor/rules/*.mdc` paths — pass.
  - `git diff --check` — pass (no whitespace errors).
  - Live dry-run and real run of `copy-ai-collaboration-files.sh --target
    <mktemp -d throwaway dir> --project-name "Demo Project" --stack "Demo
    stack"`: confirmed `.cursor/rules/{01,02,03}-*.mdc` are copied and both
    `<PROJECT_NAME...>` and the stack placeholder are substituted (no
    leftover `PROJECT_NAME` or `FILL IN: e.g. backend language` strings in
    the copied `.cursor/rules/` tree).
- Result: passed.

## Changed Files

- `.cursor/rules/01-quickstart.mdc` (new)
- `.cursor/rules/02-architecture-boundaries.mdc` (new)
- `.cursor/rules/03-collaboration-and-completion.mdc` (new)
- `scripts/copy-ai-collaboration-files.sh` (bug fix: `*.mdc` added to
  placeholder-substitution glob)
- `scripts/lib/collaboration-template-paths.sh` (`.cursor/rules` added)
- `.github/workflows/ci.yml` (required-files and contract-traceability
  patterns extended)
- `docs/collaboration/prompt-instruction-change-control.md` (contract file
  list extended)
- `docs/architecture/adr/0006-prompt-instruction-change-control.md`
  (extended in place)
- `README.md`, `README.ja.md` (agent list, directory guide,
  placeholder-fill instructions)
- `docs/collaboration/adoption-guide.md` (placeholder-fill step, LLM
  Session Setup notes)
- `docs/issues/LISS-0010-cursor-agent-entry-point-and-multi-agent-refresh.md`
  (new)
- `docs/collaboration/traces/2026-07-14-cursor-agent-entry-point-and-multi-agent-refresh.md`
  (new, this file)

## Next Safe Action

- Ask the Adjudicator whether to commit this branch
  (`process/cursor-agent-entry-point`) and, if so, whether to merge it into
  `main` now (no conflicts expected — `main` is already up to date with the
  LISS-0008/LISS-0009 merges from earlier in this session).

## Notes

- No secrets, API keys, or private data were included in this trace or the
  documents it covers.
