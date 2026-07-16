# AI Work Trace

## Request

- Date: 2026-07-08
- User request: Examine a third adopter's feedback (a Grok-based rhythm/music
  learning game) for elements worth incorporating, focused specifically on
  adding a Grok entry point (`.grok/`) and clarifying support for
  "codex-fugu"; the Referee explicitly declined the same feedback's
  stack-specific "browser ports cookbook" item as out of scope for the
  template.
- Current phase: Architecture Path (new agent operating contract files;
  tracked as LISS-0006).

## Context Ledger

- Included: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`, `scripts/init-llm-context.sh`,
  `.github/workflows/ci.yml`, `README.md`, `README.ja.md`,
  `docs/collaboration/adoption-guide.md`, `docs/issues/LISS-0005-*.md` (prior
  precedent for bundling adopter feedback into a LISS).
- Omitted: the adopter's actual game repository/code; the CI
  placeholder-detection, legacy-spec-backlog, and monolith-transition-guide
  ideas from the same feedback round (left for a future, separate issue).
- Assumptions: Grok Build's `.grok/rules/` convention and Codex's
  `AGENTS.md`-reading behavior, both confirmed via live web search this
  session (see References), are accurate as of 2026-07-08.
- Open decisions: none blocking; the full-mirror vs. thin-pointer choice for
  `.grok/rules/` was resolved in-session by the Referee (full mirror).

## Routing

- Model/assistant/tool: direct implementation (bash + Markdown); two
  WebFetch/WebSearch calls to verify third-party tool behavior (Sakana Fugu,
  Grok Build, Codex CLI) before writing template guidance about them.
- Reason: verifying vendor-specific claims against current documentation
  rather than relying on possibly-stale training knowledge, since this
  repository explicitly warns against inventing external tool conventions.
- Privacy constraints: no private data used; all fetched URLs were public
  vendor documentation.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: see Context Ledger.
- Context intentionally omitted: adopter's own repository/code; unrelated
  feedback items already deferred to a future issue.
- Deterministic checks used: `bash -n` on all touched shell scripts; YAML
  parse check on `ci.yml`; a real dry-run and non-dry-run execution of
  `scripts/copy-ai-collaboration-files.sh` against a throwaway target
  directory to confirm `.grok/rules/` is distributed and placeholders are
  substituted.
- Escalation reason: escalated to live web search/fetch specifically to
  confirm Grok Build's and Codex's actual project-file conventions (not
  guessed), and to identify what "Fugu" is before designing around it.
- Avoided LLM work: did not fabricate a `.codex/rules/` project convention
  for Codex once documentation confirmed that path is user-home-level, not
  project-level.
- Rework caused by AI output: none.

## Referee Decisions

- Reject the browser-specific "ports cookbook" item from the same feedback
  round: stack-specific concerns are the adopting project's responsibility,
  not the template's.
- Add `.grok/` and address "codex-fugu": confirmed as (a) add a Grok entry
  point, (b) Codex needs no dedicated file (reads `AGENTS.md` natively), (c)
  Fugu is Sakana AI's multi-agent orchestration model, not itself a
  project-config-reading coding agent -- no template action applies to it.
- `.grok/rules/` content model: full mirror of `AGENTS.md`'s content
  (matching the existing `CLAUDE.md`/`copilot-instructions.md` pattern),
  not a thin pointer, even though this adds a fourth file set to the
  cross-file consistency requirement.

## Verification

- Commands/checks:
  - `bash -n` on `copy-ai-collaboration-files.sh`,
    `collaboration-template-paths.sh`, `update-ai-collaboration-files.sh`,
    `init-llm-context.sh` -- all pass.
  - YAML parse of `.github/workflows/ci.yml` -- passes.
  - Live run of `copy-ai-collaboration-files.sh --target <throwaway dir>
    --project-name "Demo" --stack "Demo stack"`: confirmed
    `.grok/rules/{01,02,03}-*.md` are copied and both `<PROJECT_NAME...>` and
    stack placeholders are substituted in the new files.
  - Same run surfaced a pre-existing bug: `replace_placeholders` had no
    line-wrapped variant of the `<PROJECT_NAME: ...>` pattern (only the
    stack placeholder had one), so any contract file where that placeholder
    line-wraps (confirmed present, unfixed, in
    `.github/copilot-instructions.md` before this change) silently kept the
    placeholder after adoption. Fixed by adding the missing wrapped-pattern
    variant, mirroring the existing stack-placeholder handling. Re-verified
    with the same dry run: no `.md` file in the copied tree retains
    `PROJECT_NAME` after substitution.
- Result: passed.

## Changed Files

- `.grok/rules/01-quickstart.md` (new)
- `.grok/rules/02-architecture-boundaries.md` (new)
- `.grok/rules/03-collaboration-and-completion.md` (new)
- `scripts/lib/collaboration-template-paths.sh`
- `scripts/copy-ai-collaboration-files.sh` (also fixes the PROJECT_NAME
  line-wrap substitution bug)
- `scripts/init-llm-context.sh`
- `.github/workflows/ci.yml`
- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/architecture/adr/0006-prompt-instruction-change-control.md`
- `README.md`
- `README.ja.md`
- `docs/collaboration/adoption-guide.md`
- `docs/issues/LISS-0006-grok-agent-entry-point.md` (new)
- `docs/collaboration/traces/2026-07-08-grok-agent-entry-point.md` (new,
  this file)

## Next Safe Action

- Open a PR from `process/grok-agent-entry-point` against `main` for Referee
  review, per `docs/collaboration/prompt-instruction-change-control.md`.
  Note: this session's work is currently uncommitted on branch
  `docs/research-rationale-essays`, which already has unrelated pending
  changes (research-essay renumbering); commit this work on its own branch
  rather than mixing it with that pending rename.
- If the Referee wants the CI placeholder-detection gate or the
  legacy-spec-backlog / monolith-transition guidance from the same feedback
  round pursued, open those as a separate LISS rather than folding them into
  LISS-0006.

## Notes

- ADR 0006 was edited in place (Context/Consequences/Enforcement extended to
  name `.grok/rules/*.md` and note Codex's no-file status) rather than
  superseded, since this is a refinement of the same accepted decision, not
  a reversal -- same precedent as the 2026-07-06 sync-feedback trace's
  handling of ADR 0008.
