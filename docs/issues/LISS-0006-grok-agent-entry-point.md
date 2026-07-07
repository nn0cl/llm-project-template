# LISS-0006: Grok agent entry point (.grok/rules/), Codex confirmed as no-op

## Metadata

- Local issue ID: LISS-0006
- GitHub issue:
- Status: review
- Phase: docs-only
- Type: process/docs
- Priority: medium
- Owner/agent: Claude Fable 5 (proposal and implementation); Referee to review
- Related branch: process/grok-agent-entry-point (create on implementation)

## Summary

- A third adopter round (a rhythm/music-learning game adopting the template
  with Grok as its coding agent) reported that Grok auto-loads `AGENTS.md`
  and `CLAUDE.md` as context, but the template's phase/branch/trace
  discipline still "did not feel like it was taking hold" in practice,
  unlike with Claude/Copilot.
- Investigation (this session) confirmed Grok Build (xAI's CLI) has a
  distinct, stronger-binding "rules" discovery surface at `.grok/rules/`
  (verified via `grok inspect` in the adopter's own report, and via current
  xAI CLI documentation search), separate from generic context-file loading.
  The template ships dedicated entry points for Claude (`CLAUDE.md`) and
  Copilot (`.github/copilot-instructions.md`) but none for Grok, even though
  `README.md` already lists Grok-class tooling informally.
- Separately investigated whether Codex (OpenAI's CLI) needs an equivalent
  addition. Confirmed via current OpenAI documentation that Codex reads
  `AGENTS.md` directly (search order: `AGENTS.override.md` -> `AGENTS.md` ->
  `TEAM_GUIDE.md` -> `.agents.md`) and that its own `~/.codex/rules/`
  directory is a user-home-level setting, not a project-distributable
  convention. Codex needs no dedicated file; this issue records that finding
  so it is not re-litigated by a future adopter or agent.
- A brief investigation into "Fugu" (referenced by the Referee as
  "codex-fugu") found it to be Sakana AI's multi-agent orchestration model
  (https://sakana.ai/fugu-release/), not itself a project-config-reading
  coding agent; its own material describes pairing with "tools like Codex
  for coding and code review" rather than reading `AGENTS.md`-style files.
  No template action applies to Fugu directly.

## Acceptance Notes

1. Add `.grok/rules/01-quickstart.md`, `.grok/rules/02-architecture-boundaries.md`,
   and `.grok/rules/03-collaboration-and-completion.md`, mirroring the full
   content of `AGENTS.md` (Prime Directive, Expected Workflow, Clean
   Architecture Dependency Rule, External Resources Must Be Ports, Referee
   Interaction) with a short Grok-specific persona header, matching the
   existing full-mirror pattern used by `CLAUDE.md` and
   `.github/copilot-instructions.md` (Referee's explicit choice: full mirror
   over thin pointer, to keep the pattern consistent across vendors even
   though it adds a fourth file set to keep in sync).
2. Add `.grok/rules` to `scripts/lib/collaboration-template-paths.sh` so
   `copy-ai-collaboration-files.sh` and `update-ai-collaboration-files.sh`
   distribute and sync it like the other contract files, including
   placeholder substitution (`<PROJECT_NAME...>`, stack placeholder).
3. Add the three new files to the CI `repository-sanity` required-files
   check in `.github/workflows/ci.yml`.
4. Add `.grok/rules/*.md` to the Agent Operating Contract Files list in
   `docs/collaboration/prompt-instruction-change-control.md`, and extend the
   cross-file agreement check to include it alongside `AGENTS.md`,
   `CLAUDE.md`, and `.github/copilot-instructions.md`.
5. Update `README.md` and `README.ja.md`: mention Grok alongside
   Claude/Copilot/Codex in the agent list, and add `.grok/rules/` to the
   Directory Guide tree.
6. Update `docs/collaboration/adoption-guide.md` step 2 (fill placeholders)
   to include `.grok/rules/*.md`, and add a short note in the LLM Session
   Setup section recording that Codex needs no dedicated entry-point file
   (reads `AGENTS.md` natively).

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0002, LISS-0005 (same adopter-feedback-to-template-change
  precedent).

## Referee Decision Points

- Full-mirror vs. thin-pointer for `.grok/rules/`: resolved by the Referee
  in-session as full mirror, matching the existing `CLAUDE.md`/
  `copilot-instructions.md` pattern. Revisit if the 4-way sync cost (raised
  by the same adopter round as a separate complaint) is addressed later by a
  single-source-of-truth restructuring -- that would be a separate ADR-level
  change, not folded into this issue.
- Whether the browser-specific "ports cookbook" item from the same feedback
  round (Web Audio unlock, bound fetch, localStorage) belongs in the
  template: Referee explicitly declined -- stack-specific concerns are the
  adopting project's responsibility, not the template's. Not tracked as a
  future item.

## Context

- Included: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`, `.github/workflows/ci.yml`,
  `README.md`, `docs/collaboration/adoption-guide.md`.
- Omitted: the adopter's actual game repository/code; the CI-detection idea
  for unfilled `<FILL IN>` placeholders and the legacy-spec-backlog /
  monolith-transition-guide ideas raised in the same feedback round (left for
  a separate issue, not bundled here, since they are unrelated docs content
  rather than multi-agent entry-point support).
- Assumptions: Grok Build's `.grok/rules/` directory convention and file
  discovery behavior are stable enough to template against; if xAI changes
  this convention, the fix is confined to this file set.

## References

- Third adopter review (2026-07-08, rhythm/music-learning game, Grok-based),
  provided verbatim by the Referee in session.
- xAI Grok Build docs/community references confirming `grok inspect` reports
  discovered config sources, instructions, and rules
  (https://docs.x.ai/build/overview, https://github.com/superagent-ai/grok-cli
  as secondary corroboration of the CLI's rule-discovery behavior).
- OpenAI Codex CLI documentation confirming `AGENTS.md` search order and that
  `~/.codex/rules/` is a user-home-level, not project-level, path
  (https://developers.openai.com/codex/guides/agents-md,
  https://developers.openai.com/codex/config-reference).
- Sakana AI Fugu release page confirming Fugu is a multi-agent orchestration
  model, not itself an `AGENTS.md`-reading coding agent
  (https://sakana.ai/fugu-release/).

## Work Notes

- Implemented 2026-07-08: see
  `docs/collaboration/traces/2026-07-08-grok-agent-entry-point.md` for the
  full change list and verification. Also fixed an unrelated pre-existing
  bug found while testing: `copy-ai-collaboration-files.sh` was not
  substituting the `<PROJECT_NAME: ...>` placeholder when it line-wrapped
  (confirmed present, unfixed, in `.github/copilot-instructions.md` before
  this change).
- Not yet committed/branched: currently sitting as uncommitted changes on
  `docs/research-rationale-essays`, which has unrelated pending work. Needs
  its own `process/grok-agent-entry-point` branch before a PR.

## Verification

- Docs-only: markdown lint / CI docs checks pass.
- `bash -n` on any touched shell scripts.
- CI required-files check passes with the three new `.grok/rules/*.md`
  paths added.
- A trace under `docs/collaboration/traces/` accompanies the implementing
  PR, per `prompt-instruction-change-control.md` (contract files touched).
