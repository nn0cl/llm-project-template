# LISS-0024: Terminology, bounded-batch parity, and ledger hygiene

## Metadata

- Local issue ID: LISS-0024
- GitHub issue:
- Status: in_progress
- Phase: process-only
- Type: process/docs
- Priority: high
- Initial planning size: M
- Current planning size: M
- Owner/agent: Grok
- Related branch: process/liss-0024-terminology-batch-ledger

## Summary

Align remaining live user-facing and Copilot/Grok contract wording with the
already-accepted Adjudicator, `[DESIGN CHECK]`, and bounded-batch Approval
Model. Repair the local-issue ledger: unique IDs, and `done` for work already
merged. Do not thin session-start document lists.

## Acceptance Notes

1. Live `QUICKSTART.md` and `QUICKSTART.ja.md` use Adjudicator, not Referee,
   for the human decision role. Historical traces and ADR 0012 may keep
   Referee as history.
2. Live `README.md` and `README.ja.md` use `[DESIGN CHECK]`, not `[THOUGHT]`.
3. `.github/copilot-instructions.md` and `.grok/rules/` state typed approvals
   and the bounded-batch rules (`batch/<batch-id>`, CI is not Adjudicator
   approval) with the same effective content as `AGENTS.md` / `CLAUDE.md`.
   Cursor `.mdc` files stay complements; they continue to rely on root
   `AGENTS.md` auto-apply for the full Approval Model.
4. Session-start "must-read" lists, Grok auto-load of AGENTS plus rules plus
   CLAUDE, and Fast Path pointing at runtime-routing are unchanged.
5. Duplicate `LISS-0017` is resolved: architecture-approval keeps `LISS-0017`
   and is `done`; document-lifecycle is `LISS-0023` and remains `done`.
   `LISS-0011` stays unused.
6. Merged issues `LISS-0001`, `0002`, `0006`, `0007`, `0015`, `0016`,
   `0017`, `0018`, and `0019` are `done`. `LISS-0003`, `0004`, and `0005`
   stay `proposed`. WP-0002 records `LISS-0017` as `done`.

## Dependencies

- Related: ADR 0010, ADR 0012, LISS-0017, LISS-0023

## Adjudicator Decision Points

- Implementation requested 2026-08-26, excluding session-start thinning.

## Context

- Included: QUICKSTART, README, Copilot/Grok contract files, local issues,
  WP-0002, document-lifecycle trace path after the ID rename.
- Omitted: application code, provider SDKs, AGENTS/CLAUDE session-start
  document lists, Cursor `.mdc` Approval Model duplication, historical
  traces rewritten as if they used today's terms.
- Assumptions: merged PRs for the stale issues are already on `main`.

## AI Planning Records

### AIP-0024-001

- Status: accepted
- Created by:
  - Agent/environment: Grok Build
  - Model as displayed: Grok 4.6
  - Reasoning setting as displayed: N/A; not exposed
  - N/A reason: environment does not expose the setting
- Created at: 2026-08-26
- Planning size: M
- Intended execution route: process-only
- Intended scope: terminology, Copilot/Grok batch parity, ledger IDs and
  statuses
- Estimated token range: N/A
- Token metric: N/A
- Estimation basis: document alignment and ledger edits
- Confidence: high

## References

- `docs/architecture/adr/0010-architecture-approval-and-reassessment-gates.md`
- `docs/architecture/adr/0012-rename-referee-to-adjudicator.md`

## Verification

- `rg` on live QUICKSTART/README shows no `Referee` and no `[THOUGHT]`.
- Copilot and Grok rules contain `batch/<batch-id>` and
  `CI success is not Adjudicator approval`.
- `ls docs/issues/LISS-0017*` is a single architecture file; lifecycle is
  `LISS-0023`.
- Stale merged issues are `done`; `0003`/`0004`/`0005` remain `proposed`.
- `git diff --check` and repository CI.
