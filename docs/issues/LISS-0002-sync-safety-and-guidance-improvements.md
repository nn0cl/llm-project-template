# LISS-0002: Template update sync safety and guidance improvements

## Metadata

- Local issue ID: LISS-0002
- GitHub issue:
- Status: in_progress
- Phase: docs-only
- Type: process/tooling
- Priority: high
- Owner/agent: Claude Sonnet 5
- Related branch: process/template-sync-feedback-fixes

## Summary

- An external adopter (voice-to-dic) ran `scripts/update-ai-collaboration-files.sh`
  for the first time against an already-substantially-customized,
  pre-existing repository and reported concrete gaps in ADR 0008's pull-sync
  mechanism. This issue tracks the subset of that feedback judged realistic
  and beneficial to fix now.
- Deferred items from the same feedback are tracked separately in LISS-0003
  and LISS-0004 rather than folded into this issue, since they require
  structural or content decisions this repository cannot make unilaterally.

## Acceptance Notes

- `scripts/update-ai-collaboration-files.sh` detects when a newly-added
  upstream file under `docs/architecture/adr/NNNN-*` or
  `docs/issues/LISS-NNNN-*` shares a number with an existing target file of a
  different slug, and reports it as a distinct "NUMBER COLLISIONS" category
  (not folded into Added/Updated/Merged/Conflicts/Needs Decision) with a
  suggested next-free number in the target's own sequence.
- The "needs decision (deleted locally, changed upstream)" output includes a
  one-line hint to check for a same-content file under a different name
  elsewhere in the target repository before assuming a real deletion.
- `docs/collaboration/adoption-guide.md` documents a recovery recipe for
  repositories that predate the `.collaboration-template-version` marker
  mechanism (manual/copy-paste adopters, or adopters older than this
  template's own git history).
- `docs/collaboration/adoption-guide.md` calls out checking whether the
  target's `CLAUDE.md`/`AGENTS.md` needs a matching update after a sync
  introduces new cross-cutting process vocabulary.
- ADR 0008 records the collision-detection behavior as part of its Decision
  section and notes, in Consequences, that a clean merge is not the same
  guarantee as "nothing needs review."

## Dependencies

- Parent:
- Depends on: ADR 0008 (already accepted)
- Blocks:
- Related: LISS-0001, LISS-0003, LISS-0004

## Adjudicator Decision Points

- Confirmed: fix silent numbering collisions and add missing recovery/
  guidance documentation; do not restructure README.md/ci.yml or fabricate
  unverified stack-specific CI content as part of this issue.

## Context

- Included: `scripts/update-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`,
  `docs/architecture/adr/0008-template-update-propagation.md`,
  `docs/collaboration/adoption-guide.md`.
- Omitted: voice-to-dic's actual repository content; any concrete Tauri/Rust
  CI job content (unverified by this repository, see LISS-0004).
- Assumptions: the reported gaps are representative of what most adopters
  with pre-existing repositories will hit, not specific to voice-to-dic.

## References

- External feedback report from voice-to-dic's first pull-sync
  (template commit `85052ab` -> `869fca6`).
- `docs/architecture/adr/0008-template-update-propagation.md`

## Work Notes

- Added number-collision detection to `process_file`/reporting logic in
  `scripts/update-ai-collaboration-files.sh`.
- Added a rename-check hint line to the needs-decision summary output.
- Extended `docs/collaboration/adoption-guide.md` with a manual-adoption
  recovery recipe and a CLAUDE.md/AGENTS.md vocabulary-drift callout.
- Extended ADR 0008 Decision and Consequences sections.

## Verification

- `bash -n` syntax check on the updated script.
- Dry-run against temporary fixture repositories reproducing a number
  collision and a renamed-file false-deletion.
