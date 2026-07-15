# LISS-0015: Agent rule file parity and duplication cleanup

## Metadata

- Local issue ID: LISS-0015
- GitHub issue:
- Status: review
- Phase: process-only
- Type: process/docs
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason:
- Owner/agent: Claude Code CLI (Claude Sonnet 5); Cursor live verification +
  optimization by Cursor agent 2026-07-16
- Parent: -
- Depends on: -
- Blocks: -
- Related branch: process/agent-rule-file-parity

## Summary

- Adopter feedback (mt4-orchestration project, 2026-07-16) observed that
  cramming all rules into one file bloats context and buries instructions,
  and suggested splitting rules so agents load only what is relevant to the
  file they are touching.
- Current state: `.cursor/rules/*.mdc` and `.grok/rules/*.md` are already
  split into three files each (`01-quickstart`, `02-architecture-boundaries`,
  `03-collaboration-and-completion`), per LISS-0006 and LISS-0010.
  `.github/copilot-instructions.md` remains a single 165-line file. `AGENTS.md`
  and `CLAUDE.md` remain single files by design (project-wide overview role).
  None of the existing rule files use path-scoped loading (Cursor `globs` is
  empty with `alwaysApply: true` on every file), so the "load only what's
  relevant to the touched file" part of the feedback is not yet realized
  anywhere.
- Referee direction (2026-07-16, chat, first round): focus this issue on
  organizing/aligning the per-agent rule files (not on the separate
  safety-rule feedback about push restriction or search-scope limiting, which
  is explicitly out of scope for this issue).
- Referee direction (2026-07-16, chat, second round): the blanket "full
  mirror across all five contract files, do not re-open" framing from
  LISS-0006/LISS-0010 is itself required to have current grounds, not just be
  inherited as precedent. Live research (below) found real per-vendor
  differences, so the full-mirror question is decided per vendor rather than
  as one blanket rule, and this issue now supersedes the blanket framing in
  ADR 0006 with a per-vendor policy.

## Research Findings (2026-07-16, live WebSearch/WebFetch)

- **GitHub Copilot**: natively reads `AGENTS.md` (coding agent since
  2025-08-28, code review GA since 2026-06-18), including nested `AGENTS.md`
  files. GitHub's own documentation states this reading is "read-and-apply,
  not strict enforcement" and does not guarantee adherence as literal as
  Claude Code following `CLAUDE.md`. Copilot also supports path-scoped
  `.github/instructions/*.instructions.md` files with an `applyTo` glob,
  which combine with the repository-wide `copilot-instructions.md`.
- **Claude Code**: supports `@path/to/file` imports that are expanded inline
  into context at session launch (recursive, max 4 hops) — a guaranteed
  content-inlining mechanism, not a hope-based text pointer. Anthropic's own
  documentation explicitly recommends `@AGENTS.md` (or a symlink) specifically
  to avoid duplicating instructions between `AGENTS.md` and `CLAUDE.md`.
  Claude Code also has its own `.claude/rules/*.md` directory with a `paths:`
  frontmatter field, functionally equivalent to Cursor's `globs`.
- **Cursor**: root `AGENTS.md` is a first-class Rules type alongside Project
  Rules / User / Team ([Rules](https://cursor.com/docs/rules.md)). Help states
  Cursor "picks it up automatically"
  ([Help: Rules](https://cursor.com/help/customization/rules.md)). FAQ still
  documents `@filename` inside `.mdc` to attach files to rule context, but for
  root `AGENTS.md` that duplicates native loading. Live Cursor session
  2026-07-16 confirmed separate always-applied injection of `AGENTS.md` and
  the three `.mdc` files; `@AGENTS.md` text in `.mdc` was not inlined. Core
  `globs`/`alwaysApply` behavior is unchanged since LISS-0010 (2026-07-14).
- **Grok**: not re-verified this round; LISS-0006's live `grok inspect` test
  (2026-07-08) and LISS-0010's 2026-07-14 findings stand as the evidence base.
- **Codex**: unchanged; reads `AGENTS.md` directly, no dedicated file, no
  duplication exists here to begin with.

## Per-Vendor Decision (Referee-confirmed 2026-07-16; Cursor refined and approved same day)

- **Codex**: no change. Already the optimal case (zero duplication).
- **Claude Code — consolidate**: replace `CLAUDE.md`'s duplicated body with an
  `@AGENTS.md` import plus only the content that is genuinely Claude
  Code-specific (if any remains after the import). Grounds: Anthropic's own
  documentation recommends exactly this for this exact deduplication purpose,
  and the import mechanism does not carry the "agent might not follow a
  pointer" risk that motivated the original full-mirror choice.
- **GitHub Copilot — keep full mirror**: Referee decision, given GitHub's own
  documentation states adherence is weaker when relying on `AGENTS.md` alone.
  The duplication cost is accepted in exchange for the stronger, dedicated
  binding. Do not split or shrink `copilot-instructions.md` in this issue.
- **Cursor — omit shared sections; rely on native `AGENTS.md`**: after the
  shrink-to-`@AGENTS.md` trial, live verification plus primary docs showed
  root `AGENTS.md` is already loaded as its own Rules type. Referee directed
  optimization (2026-07-16): drop `@AGENTS.md` from `.mdc`; keep
  Cursor-complementary content only. Grounds recorded in ADR 0006 Cursor
  evidence items 1–5. Referee approved the grounded revision the same day.
- **Grok — keep full mirror**: not revisited this round. LISS-0006's
  empirical `grok inspect` finding (generic `AGENTS.md` loading was
  insufficient in practice) is the strongest evidence of any vendor in this
  set and was not questioned by the Referee in this round.

## Acceptance Notes

1. Record the research findings and per-vendor decision above (done in this
   issue).
2. Update `CLAUDE.md` to import `AGENTS.md` (`@AGENTS.md`) instead of
   duplicating its body; keep only genuinely Claude Code-specific content
   below the import, if any.
3. Attempt the Cursor trial shrink on `.cursor/rules/*.mdc`; verify live in a
   Cursor session before treating it as final; fall back to full-mirror
   content and record why if verification fails or cannot be performed.
4. Leave `.github/copilot-instructions.md` and `.grok/rules/*.md` as full
   mirrors; no split, no shrink.
5. Extend ADR 0006
   (`docs/architecture/adr/0006-prompt-instruction-change-control.md`) in
   place: replace its blanket "keep the full-mirror pattern across all five
   files" statement in Context/Decision/Consequences with the per-vendor
   policy above and its sources.
6. Update `docs/collaboration/prompt-instruction-change-control.md`'s
   cross-file consistency-check wording so it no longer expects `CLAUDE.md`
   (and, if the Cursor trial succeeds, `.cursor/rules/*.mdc`) to literally
   match `AGENTS.md` prose; it should instead expect them to resolve to
   equivalent effective content (via the import/reference chain).
7. Add exactly one new section, in `docs/collaboration/adoption-guide.md`,
   documenting how to add a stack-specific, glob/`applyTo`/`paths`-scoped rule
   file once a stack ADR is accepted (Cursor `globs`, Claude Code
   `.claude/rules/*.md` `paths:`, Copilot `applyTo` instructions files). Other
   documents link to this section instead of re-explaining it.
8. Do not restate the contract-file list or the per-vendor policy rationale
   in more than one document; the list and rationale live in
   `prompt-instruction-change-control.md` and ADR 0006 respectively. README.md,
   README.ja.md, and `adoption-guide.md` link to them instead of copying them.
9. Update README.md / README.ja.md directory guide and the CI
   `repository-sanity` required-files / contract-traceability checks in
   `.github/workflows/ci.yml` if the Cursor trial changes what CI should check
   (e.g., CI can no longer byte-diff `.cursor/rules/*.mdc` against `AGENTS.md`
   if they're no longer literal copies).
10. Explicitly out of scope: no-auto-push rule and search-scope-limiting
    guidance (adopter feedback item 3). Do not fold that work into this issue.

## Dependencies

- Parent: -
- Depends on: -
- Blocks: -
- Related: LISS-0006 (Grok agent entry point, full-mirror precedent),
  LISS-0010 (Cursor agent entry point, same precedent and live-research
  method).

## Referee Decision Points

- `.github/copilot-instructions.md`: resolved 2026-07-16 — keep full mirror,
  since the impact of weaker adherence would be confined to Copilot itself
  and GitHub's own docs flag that risk.
- `.cursor/rules/*.mdc`: resolved 2026-07-16 — attempt the shrink-to-reference
  trial, conditional on live verification that Cursor reliably inlines the
  `@AGENTS.md` reference every session.
- Refinement 2026-07-16 (live Cursor session + Referee "optimize"):
  verification showed root `AGENTS.md` is auto-applied independently of
  `.mdc`, so `@AGENTS.md` inside `.mdc` is redundant. Drop the trial
  references; keep Cursor-complementary content only; rely on native
  `AGENTS.md` loading for shared sections.
- Referee approval 2026-07-16: grounded revision approved ("根拠を付けて
  修正して。承認します。").
- `CLAUDE.md`: resolved 2026-07-16 — consolidate via `@AGENTS.md` import,
  per Anthropic's own documented recommendation.
- `.grok/rules/*.md`: not revisited — keep full mirror, per LISS-0006's
  empirical grounding.

## Context

- Included: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/*.md`, `.cursor/rules/*.mdc`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/collaboration/adoption-guide.md`,
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`,
  LISS-0006 and LISS-0010 and their traces (direct precedent for method and
  the blanket full-mirror decision this issue now supersedes with a
  per-vendor policy).
- Omitted: application source; the adopter feedback's item 3 (safety rules)
  and item 1 (issue/document sync, already resolved by LISS-0014).
- Assumptions: vendor conventions for Copilot/Claude Code/Cursor are
  fast-moving and must be re-verified live rather than assumed from LISS-0010's
  2026-07-14 findings; Grok's conventions were not re-verified this round and
  rely on LISS-0006/LISS-0010's existing findings.

## AI Planning Records

### AIP-0015-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-16
- Planning size: M
- Intended execution route: strong reasoning agent for research synthesis and
  cross-file consistency work; live WebSearch/WebFetch to verify current
  vendor conventions rather than training knowledge; deterministic checks
  (required-file lists, CI reproduction) for verification.
- Intended scope: vendor capability research; conditional Copilot file split;
  contract-file-list and adoption-guide updates; README/CI updates.
- Estimated token range: 8,000-16,000
- Estimated token midpoint: 12,000
- Token metric: approximate total model tokens for research plus
  implementation
- Estimation basis: closely follows the established LISS-0010 pattern (same
  kind of vendor-capability research plus contract-file updates), scoped down
  by excluding the safety-rule work the Referee split out.
- Assumptions: no application code changes; no new ADR needed unless research
  reveals a decision the existing ADR 0006 does not cover.
- Confidence: medium (depends on what the live research finds for Copilot;
  outcome could be "no structural change needed", per Acceptance Note 7).
- Revises:
- Revision reason:
- Superseded by:

## References

- Referee feedback relay, 2026-07-16 (chat): mt4-orchestration project
  feedback document, item 2 ("ルールのモジュール化").
- Referee direction, 2026-07-16 (chat, first round): scope this issue to
  rule-file organization only (excluding item 3).
- Referee direction, 2026-07-16 (chat, second round): the full-mirror pattern
  itself needs current grounds, not inherited precedent; reconsider it.
- Referee decision, 2026-07-16 (chat, in response to AskUserQuestion):
  Copilot keeps full mirror; Cursor gets the shrink-to-reference trial.
- `docs/issues/LISS-0006-grok-agent-entry-point.md` and
  `docs/issues/LISS-0010-cursor-agent-entry-point-and-multi-agent-refresh.md`
  (direct precedent for the investigation method; their blanket full-mirror
  decision is superseded by this issue's per-vendor policy).
- [Adding repository custom instructions for GitHub Copilot in your IDE](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide)
  — path-scoped `applyTo` instructions, fetched 2026-07-16.
- [Copilot code review: Path-scoped custom instruction file support](https://github.blog/changelog/2025-09-03-copilot-code-review-path-scoped-custom-instruction-file-support/)
  — fetched 2026-07-16.
- [Copilot coding agent now supports AGENTS.md custom instructions](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)
  and [Copilot code review: AGENTS.md support and UI improvements](https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements/)
  — native `AGENTS.md` reading and its documented adherence caveat, fetched
  2026-07-16.
- [How Claude remembers your project — Claude Code Docs](https://code.claude.com/docs/en/memory)
  — `@import` mechanism, the explicit `@AGENTS.md` deduplication
  recommendation, and `.claude/rules/*.md` `paths:` scoping, fetched
  2026-07-16.
- [Rules | Cursor Docs](https://cursor.com/docs/rules.md) — four Rules types
  including `AGENTS.md`; nested `AGENTS.md`; FAQ `@filename` in rules;
  fetched 2026-07-16.
- [Help: Rules](https://cursor.com/help/customization/rules.md) — "Cursor
  picks it up automatically" for root `AGENTS.md`; `CLAUDE.md` always
  applied; fetched 2026-07-16.
- Cursor community best-practice sources on referencing vs. embedding in
  `.mdc` rules (search results, 2026-07-16) — lower-confidence than the
  primary-source findings above; treated as directional, not authoritative
  for the final Cursor policy (superseded by primary docs + live session).

## Work Notes

- Implemented 2026-07-16 on branch `process/agent-rule-file-parity`:
  - `CLAUDE.md`: added `@AGENTS.md` import; removed Session Entry, Clean
    Architecture Dependency Rule, External Resources Must Be Ports, and
    Referee Interaction (all verbatim-identical to `AGENTS.md`, confirmed by
    manual comparison before removal). Kept Operating Role, Required First
    Output, Phase Discipline, Project Boundaries, Implementation Entry Point
    (kept as-is: it has real deltas from `AGENTS.md`'s Expected Workflow —
    an EARS/Gherkin-file-reading step and 3 doc references
    (`ai-failure-recovery.md`, `runner-cli-contract.md`,
    `external-resource-adoption-contract.md`) that `AGENTS.md`'s own list is
    missing), Selected Stack, Current Non-Decisions.
  - `AGENTS.md`: removed a now-stale parenthetical pointing at `CLAUDE.md`
    "for the same list kept in sync" (no longer true once `CLAUDE.md` stopped
    keeping its own copy).
  - `.cursor/rules/*.mdc`: replaced only the sections confirmed
    verbatim-identical to `AGENTS.md` (Clean Architecture Dependency Rule,
    External Resources Must Be Ports, Referee Interaction's design-intake
    paragraphs, Session Entry, Expected Workflow, the doc list) with
    `@AGENTS.md` references, marked with an inline HTML comment noting the
    trial and pointing at git history for the original full-mirror text if a
    revert is needed. Deliberately kept Anti-Hallucination Rules, Phase Gate
    detail, Mandatory Thought Output, Decision Gates, and the
    Handoff-and-Completion additions intact, since none of those exist in
    `AGENTS.md` and a blanket "replace everything with `@AGENTS.md`" would
    have silently dropped them.
  - `docs/architecture/adr/0006-prompt-instruction-change-control.md`:
    extended in place with the research findings and per-vendor decision.
  - `docs/collaboration/prompt-instruction-change-control.md`: updated the
    consistency-check wording to "equivalent effective content" rather than
    literal match, and to include `.cursor/rules/*.mdc` (which the existing
    wording had omitted even before this issue — a pre-existing gap fixed in
    passing since it's directly adjacent to this change).
  - `docs/collaboration/adoption-guide.md`: updated the Cursor/Claude Code
    paragraphs and added a new "Adding Stack-Specific Scoped Rules" section
    (Cursor `globs`, Claude Code `.claude/rules/*.md` `paths:`, Copilot
    `applyTo` instructions files).
  - Checked `.github/workflows/ci.yml`: it checks required-file existence and
    that contract changes ship with a trace; it does not byte-diff
    `.cursor/rules/*.mdc` against `AGENTS.md`. No CI changes were needed
    (Acceptance Note 9 turned out to be a non-issue).
  - `.github/copilot-instructions.md` and `.grok/rules/*.md`: left unchanged
    (full mirror kept, per Referee decision).
  - Full research findings, sources, and the per-vendor decision are recorded
    above and in ADR 0006.
- Follow-up 2026-07-16 (Cursor agent, same branch): after live verification,
  removed `@AGENTS.md` references from `.cursor/rules/*.mdc`; replaced with
  short notes that shared content comes from native `AGENTS.md` auto-apply;
  updated ADR 0006, `prompt-instruction-change-control.md`,
  `adoption-guide.md`, and this issue; Status moved `blocked` → `review`.
- Not done in the first implementation pass: live verification that
  `@AGENTS.md` inside a Cursor `.mdc` rule actually loads on every
  application of the rule (Status was `blocked`).
- Done 2026-07-16 in a live Cursor session: observed root `AGENTS.md` fully
  injected as its own always-applied Rules entry alongside `.mdc` files;
  `@AGENTS.md` text inside `.mdc` bodies was not expanded inline. Causation
  (`@` vs native load) is indistinguishable; outcome (shared rules present)
  held. Referee directed optimization: remove redundant `@AGENTS.md`
  references from `.mdc` and document reliance on native `AGENTS.md`
  auto-apply (see follow-up work notes and new trace).

## Verification

- Manual line-by-line comparison of `AGENTS.md` and the pre-edit `CLAUDE.md`
  before removing any section, to confirm only verbatim-identical content was
  removed (see Work Notes for the exact list).
- Re-read of the edited `CLAUDE.md` after editing to confirm the document
  still reads coherently and no heading was left dangling.
- `grep` over `.github/workflows/ci.yml` confirming no CI check depends on
  literal byte-for-byte matching between `.cursor/rules/*.mdc` and
  `AGENTS.md`.
- Live Cursor session 2026-07-16: confirmed independent auto-apply of root
  `AGENTS.md`; removed `@AGENTS.md` from `.mdc`; `grep` confirms no remaining
  `@AGENTS.md` under `.cursor/rules/`.
- AI work traces:
  `docs/collaboration/traces/2026-07-16-agent-rule-file-parity.md`,
  `docs/collaboration/traces/2026-07-16-cursor-mdc-drop-agents-ref.md`.
