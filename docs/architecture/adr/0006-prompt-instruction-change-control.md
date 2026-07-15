# ADR 0006: Prompt and Instruction Change Control

## Status

Accepted

## Context

`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
`.grok/rules/*.md`, and `.cursor/rules/*.mdc` are near-duplicate operating
contracts for different AI coding tools, together with
`docs/at-tdd/process.md`, `docs/collaboration/*.md`, and
`docs/templates/*.md`. Agent behavior depends directly on these files.
(Codex reads `AGENTS.md` directly and does not need its own contract file.)

As of 2026, several of these tools also read `AGENTS.md` (and in Grok
Build's case, `CLAUDE.md` too) natively, independent of their own dedicated
rule surface: Cursor documents `AGENTS.md` as a "simple alternative to
`.cursor/rules`", and current Grok Build documentation states it reads
`AGENTS.md` at three levels (`~/.grok/AGENTS.md`, `<repo-root>/AGENTS.md`,
`<cwd>/AGENTS.md`) plus `CLAUDE.md` "for compatibility" (verified via live
web search, 2026-07-14; see the accompanying trace).

LISS-0006 and LISS-0010 originally resolved this with one blanket rule: full
mirror across all five files, no thin pointers, so every tool gets the same
explicit, strongly-bound entry point. LISS-0015 (2026-07-16) revisited that
blanket rule on Referee instruction, on the grounds that "we decided this
once before" is not itself evidence, and found the picture differs per
vendor:

- **GitHub Copilot** now reads `AGENTS.md` natively (coding agent since
  2025-08-28, code review GA since 2026-06-18), but GitHub's own
  documentation states this reading is "read-and-apply, not strict
  enforcement" and does not guarantee adherence as literal as Claude Code
  following `CLAUDE.md`. This is the same category of evidence that
  originally justified Grok's dedicated file (generic context loading proving
  insufficient in practice) applied to a different vendor.
- **Claude Code** supports `@path/to/file` imports that expand inline into
  context at session launch — a guaranteed content-inlining mechanism, not a
  hope-based pointer — and Anthropic's own documentation explicitly
  recommends `@AGENTS.md` specifically to avoid duplicating instructions
  between `AGENTS.md` and `CLAUDE.md`. This is a materially different
  mechanism from a plain-text cross-reference, and removes the original
  "thin pointers aren't reliable" objection for this one vendor pair.
- **Cursor** has no confirmed guaranteed-inline import directive for `.mdc`
  files as of 2026-07-16; `@filename` references exist and Cursor's own
  community best practice favors referencing over embedding, but this is not
  confirmed with the same certainty as Claude Code's `@import`.
- **Grok**'s `.grok/rules/` stronger-binding finding (LISS-0006's live `grok
  inspect` test, 2026-07-08) was not re-examined this round.

Decision, per vendor (Referee-confirmed 2026-07-16):

- `CLAUDE.md` now imports `AGENTS.md` (`@AGENTS.md`) instead of duplicating
  its body, keeping only genuinely Claude Code-specific sections.
- `.cursor/rules/*.mdc` replaces its literal duplicate-of-`AGENTS.md` content
  (Clean Architecture Dependency Rule, External Resources Must Be Ports,
  Referee Interaction's design-intake paragraphs, Session Entry, Expected
  Workflow) with `@AGENTS.md` references, as a **trial**: this must be
  verified live in a Cursor session (confirming the reference actually loads
  `AGENTS.md` content into every application of the always-apply rules)
  before being treated as settled; if verification fails or is inconclusive,
  revert to full-mirror content for Cursor.
- `.github/copilot-instructions.md` and `.grok/rules/*.md` keep the full
  mirror. For Copilot, the Referee weighed GitHub's documented weaker-adherence
  risk against the duplication cost and chose to keep the stronger, dedicated
  binding. For Grok, the original empirical grounding was not revisited.

These files can drift from each other silently: one file can gain a required
read step that the others do not, and none of them require the
operating-contract files themselves to be reviewed with the same rigor as
application code. The AI Work Trace Log already asks for a trace when
contract files change, but that alone does not name the exact file set,
require Referee review specifically, or get enforced by CI.

This gap is tracked in `docs/collaboration/process-gap-register.md`.

## Decision

Adopt `docs/collaboration/prompt-instruction-change-control.md` as the
canonical definition of the agent operating contract file set.

- Name the exact files and glob patterns that count as the agent operating
  contract.
- Require Referee review, a stated reason, and a cross-file consistency
  check whenever a contract file changes.
- Require an AI work trace under `docs/collaboration/traces/` for every
  contract change, including small wording changes.
- Enforce the trace requirement in CI: a pull request that changes a
  contract file must also add a trace file.
- Per LISS-0015: the consistency check means the five files resolve to
  equivalent effective content, not that they are literal duplicates.
  `CLAUDE.md` resolves through its `@AGENTS.md` import; `.cursor/rules/*.mdc`
  is a trial pending live verification (see Context); `copilot-instructions.md`
  and `.grok/rules/*.md` remain literal full mirrors.

## Consequences

Positive:

- Contract drift between `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` becomes visible in review instead of silently
  changing agent behavior.
- Every contract change has a recorded reason and expected behavior change.
- CI gives an automated signal instead of relying only on Referee memory.
- `CLAUDE.md`'s `@AGENTS.md` import removes one full hand-maintained
  duplicate; a future change to `AGENTS.md`'s imported sections no longer
  needs a matching manual edit in `CLAUDE.md`.

Negative:

- Adds a mandatory trace step even for small wording changes to contract
  files.
- Requires keeping the file list in
  `docs/collaboration/prompt-instruction-change-control.md` up to date as new
  contract-like files are introduced.
- The consistency check can no longer be a simple text diff for `CLAUDE.md`
  (and, if the Cursor trial holds, `.cursor/rules/*.mdc`); a reviewer must
  confirm the import/reference actually resolves to the same effective rules
  as `AGENTS.md`, which is a judgment call rather than a byte comparison.
- The Cursor trial carries a real regression risk until verified: if
  `@AGENTS.md` inside a `.mdc` rule does not reliably load on every
  application of the rule, Cursor would silently lose rules it used to have
  inline.

## Enforcement

Code review should reject:

- agent operating contract changes without a stated reason or Referee review.
- agent operating contract changes without an accompanying trace under
  `docs/collaboration/traces/`.
- agent operating contract changes that leave `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` inconsistent with each other in effective content
  (literal text for `copilot-instructions.md` and `.grok/rules/*.md`; resolved
  content via the import/reference chain for `CLAUDE.md` and, pending
  verification, `.cursor/rules/*.mdc`).
- merging the `.cursor/rules/*.mdc` shrink-to-reference trial without a
  recorded live Cursor verification result (see Context).

CI should reject:

- a pull request that changes a file listed in
  `docs/collaboration/prompt-instruction-change-control.md` without adding a
  trace file under `docs/collaboration/traces/`.
