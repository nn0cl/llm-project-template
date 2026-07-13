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
web search, 2026-07-14; see the accompanying trace). This does not remove
the need for dedicated per-tool files: Cursor's own documentation describes
`.cursor/rules/*.mdc` as the primary, more powerful mechanism (scoped rules,
`alwaysApply` control) with `AGENTS.md` support positioned as the simpler
fallback, and Grok Build's `.grok/rules/` was confirmed via a live adopter's
`grok inspect` output (2026-07-08) as a stronger-binding discovery surface
than generic context loading. The template keeps the full-mirror pattern
across all five files rather than relying on cross-tool `AGENTS.md` fallback
reading, so that every supported tool gets the same explicit, strongly-bound
entry point instead of a mix of native and fallback behavior.

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

## Consequences

Positive:

- Contract drift between `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` becomes visible in review instead of silently
  changing agent behavior.
- Every contract change has a recorded reason and expected behavior change.
- CI gives an automated signal instead of relying only on Referee memory.

Negative:

- Adds a mandatory trace step even for small wording changes to contract
  files.
- Requires keeping the file list in
  `docs/collaboration/prompt-instruction-change-control.md` up to date as new
  contract-like files are introduced.

## Enforcement

Code review should reject:

- agent operating contract changes without a stated reason or Referee review.
- agent operating contract changes without an accompanying trace under
  `docs/collaboration/traces/`.
- agent operating contract changes that leave `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` inconsistent with each other.

CI should reject:

- a pull request that changes a file listed in
  `docs/collaboration/prompt-instruction-change-control.md` without adding a
  trace file under `docs/collaboration/traces/`.
