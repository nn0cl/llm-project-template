# LISS-0018: Another adopter's finding (qpex) — `@AGENTS.md` import does not guarantee behavioral adherence for Claude Code

## Metadata

- Local issue ID: LISS-0018
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/docs
- Priority: high
- Owner/agent: Claude Sonnet 5 (proposal + implementation); Adjudicator to
  assign
- Related branch: `process/liss-0018-claude-md-full-mirror`

## Summary

- Another adopter (qpex, a QPex language toolchain project also running this
  template's agent contract) reported that `CLAUDE.md`'s `@AGENTS.md` import
  worked correctly at the technical level — the current `AGENTS.md` content
  was verifiably present in a live Claude Code session's context — but Claude
  Code still failed to follow two specific instructions from that imported
  content in the same session (one omitted repeatedly, one missed once).
- This is independent of, and not a continuation of, LISS-0005 (second
  adopter feedback); it is a distinct incident about a different mechanism.
- This repo's own `docs/architecture/adr/0006-prompt-instruction-change-control.md`
  currently argues the opposite of what qpex observed: it calls the
  `@AGENTS.md` import "a guaranteed content-inlining mechanism... removes the
  ['thin pointers aren't reliable'] objection" for Claude Code specifically.
  That reasoning is now contradicted by a concrete incident, so the ADR is
  revised alongside `CLAUDE.md` in this same change (per the same revisit
  pattern already used once in this ADR, by LISS-0015).
- External verification (Anthropic's own official Claude Code docs) partially
  supports and partially complicates qpex's causal explanation; both are
  recorded honestly in Context/References below rather than only the
  supporting half, per this template's evidence-based process-design
  practice (`docs/research/2026-07-06-rationale-evidence-based-process-design.md`).

## Acceptance Notes

1. `CLAUDE.md` is rewritten as a full mirror of `AGENTS.md`'s effective
   content plus its existing Claude-specific sections, and the `@AGENTS.md`
   import line is removed — matching the pattern already used for
   `.github/copilot-instructions.md` and `.grok/rules/*.md`. The rewrite is a
   condensed, Claude-native restatement (following
   `.github/copilot-instructions.md`'s own condensation style, not a literal
   splice of `AGENTS.md` plus the old Claude-only sections), because a literal
   concatenation would land north of 350 lines against Anthropic's own
   documented "under 200 lines... longer files... reduce adherence" guidance
   — i.e., the fix must not recreate the adherence problem it targets. Result
   is 245 lines (`AGENTS.md` is 179; old `CLAUDE.md` was 201 with only an
   import plus Claude-only sections). The overage above ~200 is a noted,
   deliberate trade-off, not an oversight: an earlier condensed draft reached
   231 lines by collapsing the itemized collaboration/architecture document
   list into prose, but that dropped concrete filenames an agent needs to
   locate the right document, so the list was restored in full, accepting
   the extra ~14 lines as a fidelity-over-brevity trade-off.
   (Observed: qpex session on branch `bug/liss-0048-operator-return-typecheck`
   — `@AGENTS.md` import confirmed present in context, including same-day
   Approval Model / Explicit Batch and Approval Source Rules additions — yet
   Claude Code (A) repeatedly omitted the mandatory `[DESIGN CHECK]` scaffold
   for Feature/Architecture Path requests across multiple turns, and (B) on
   one occasion began Phase 2 Green implementation without stopping at an
   unchecked Adjudicator Decision Point left open in
   `docs/issues/LISS-0048-operator-return-typecheck-gap.md`.)
2. `docs/architecture/adr/0006-prompt-instruction-change-control.md` gets a
   new dated decision round (same pattern as its existing LISS-0015 revisit)
   recording the qpex finding, the Anthropic-docs verification below, and the
   updated per-vendor decision: `CLAUDE.md` no longer "resolves through its
   `@AGENTS.md` import" — it joins Copilot/Grok as a full mirror. Cursor's
   union-of-`.mdc`-plus-native-`AGENTS.md` approach is unaffected (different
   mechanism, not implicated by this finding).

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0005 (second adopter feedback; same adopter-feedback
  category, no direct content overlap — this issue is an independent
  incident, not a follow-up to LISS-0005's still-unimplemented items).

## Adjudicator Decision Points

- The causal mechanism behind the qpex incident is **not settled by this
  issue**. Anthropic's own docs do not say `@import` and literal duplication
  load identically — only that imported content still enters the context
  window at launch ("Splitting into imports helps organization but doesn't
  reduce context, since imported files load at launch"), so it is not exempt
  from the documented adherence drivers: total line count, instruction
  specificity, and absence of cross-file conflicts. The
  full-mirror fix may help only incidentally (if the rewrite is also more
  concise/specific than the content it replaced), not because it stopped
  being an import. Left open for future re-examination if the gap recurs
  after this change.
- Whether to add `PreToolUse`-hook enforcement for failure mode B (the
  Decision-Gate skip) as follow-up work: technically plausible per
  Anthropic's hooks documentation (a hook can `deny` an `Edit`/`Write` tool
  call before it executes, regardless of permission mode), but requires first
  reshaping `docs/issues/LISS-*.md` "Adjudicator Decision Points" into a
  machine-checkable format (e.g. `- [ ]`/`- [x]` checkboxes instead of free
  bullets), which this issue does not do. Deferred; raise as its own issue if
  pursued. Failure mode A (omitting required text in the assistant's own
  reply) is not naturally hook-gatable by the same mechanism, since
  `PreToolUse` hooks key off tool calls/inputs, not prior assistant prose.
- Whether recurrence of this class of gap should prompt reconsidering Claude
  Code's status among this template's supported/adopted agents. Explicitly
  deferred per Adjudicator instruction; not acted on in this issue. Current
  working position: treat this as an agent-specific reliability gap to fix
  (full mirror), not evidence to drop support, unless it recurs after this
  change.

## Context

- Included: the qpex incident report (user-provided, treated as factual
  record — ADR 0006 revision dated 2026-07-25 and trace
  `docs/collaboration/traces/2026-07-25-claude-md-full-mirror.md` in the
  qpex repository); this repo's own `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, and
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`; two
  Anthropic official documentation pages (see References).
- Omitted: qpex's own repository code, its full LISS-0048/LISS-0021 issue
  history, and its Cursor-audit finding (explicitly a separate, unrelated
  incident about textual drift between Copilot/Grok mirrors, not this
  `@AGENTS.md` incident).
- Assumptions: the qpex incident report is accurate as relayed (this issue
  does not have direct access to the qpex repository to re-verify the trace
  file or ADR revision). The two Anthropic doc pages were fetched live on
  2026-07-25 and are treated as current, not archived — they may change in
  future Claude Code releases.

## References

- qpex adopter-feedback incident report (relayed by the Adjudicator in session,
  2026-07-25), citing qpex's own ADR 0006 revision and
  `docs/collaboration/traces/2026-07-25-claude-md-full-mirror.md`.
- Anthropic, *How Claude remembers your project*.
  https://code.claude.com/docs/en/memory (fetched 2026-07-25). Key quotes:
  "Claude treats them \[CLAUDE.md / auto memory] as context, not enforced
  configuration." "Size: target under 200 lines per CLAUDE.md file. Longer
  files consume more context and reduce adherence." "Splitting into imports
  helps organization but doesn't reduce context, since imported files load at
  launch." "To block an action regardless of what Claude decides, use a
  PreToolUse hook instead."
- Anthropic, *Automate actions with hooks*.
  https://code.claude.com/docs/en/hooks-guide (fetched 2026-07-25). Key
  quote: "`PreToolUse` hooks fire before any permission-mode check, in every
  permission mode, including `dontAsk`... blocks the tool even in
  `bypassPermissions` mode."
- `docs/architecture/adr/0006-prompt-instruction-change-control.md` (this
  repo, prior to this issue's revision) for the contradicted reasoning.
- `docs/research/2026-07-06-rationale-evidence-based-process-design.md` for
  this template's evidence-discipline practice (verified citations, honest
  reporting of complicating evidence, Adjudicator judgment over automatic
  rule promotion).

## Work Notes

-

## Verification

- Docs-only: markdown lint / CI docs checks pass.
- CI's contract-file trace check passes for the `CLAUDE.md` change (trace
  under `docs/collaboration/traces/`, per
  `docs/collaboration/prompt-instruction-change-control.md`).
- `docs/architecture/adr/0006-prompt-instruction-change-control.md`'s
  file-by-file description no longer contradicts `CLAUDE.md`'s actual
  mechanism.
- `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/*.md`, `.cursor/rules/*.mdc` still agree in effective content
  after the change.
- 2026-08-26: Status synchronized to `done` during LISS-0024 ledger hygiene
  after the work had already merged.

Process review: no remaining open acceptance notes in the merged
implementation. Status was stale after merge and was corrected later.
