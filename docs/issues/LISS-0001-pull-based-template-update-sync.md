# LISS-0001: Pull-based template update propagation

## Metadata

- Local issue ID: LISS-0001
- GitHub issue:
- Status: review
- Phase: docs-only
- Type: process/tooling
- Priority: medium
- Owner/agent: Claude Sonnet 5
- Related branch: feature/template-update-propagation

## Summary

- Design and implement a pull-based mechanism so repositories that already
  adopted this template can safely bring in later template updates, without
  silently overwriting or resurrecting files the adopting project has
  intentionally customized or deleted.

## Acceptance Notes

- A version marker records which template commit an adopted project last
  synced against.
- An explicit ignore list lets an adopting project exclude paths from future
  syncs.
- Updates use a 3-way merge (base = marker commit, ours = target's current
  file, theirs = template's current file); unresolved conflicts are left with
  conflict markers for human resolution, never silently overwritten.
- The update script never commits directly to the target's trunk branch: it
  creates a dedicated branch and opens a PR, per
  `docs/collaboration/branch-commit-pr-discipline.md` and ADR 0007.
- Files the target deleted since the marker commit, where the template also
  changed the file, are flagged for manual decision rather than silently
  restored.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: ADR 0005, ADR 0007

## Adjudicator Decision Points

- Confirmed: pull model (not push/registry-based) is the desired mechanism.
- Confirmed: 3-way merge with explicit ignore list, no silent overwrite.
- Confirmed: the sync mechanism itself must follow branch + PR discipline
  rather than committing to trunk directly.

## Context

- Included: `scripts/copy-ai-collaboration-files.sh`,
  `docs/collaboration/adoption-guide.md`,
  `docs/collaboration/branch-commit-pr-discipline.md`, ADR 0005, ADR 0007.
- Omitted: target-project-specific customizations, private data, concrete CI
  provider choice for running the sync on a schedule.
- Assumptions: adopting projects run this script locally (or in their own CI)
  against a local checkout of this template; the script does not clone or
  register remote repositories itself.

## References

- `docs/collaboration/branch-commit-pr-discipline.md` (this repository)
- `docs/architecture/adr/0007-trunk-oriented-branching.md` (this repository)

## Work Notes

- Implemented `scripts/lib/collaboration-template-paths.sh` shared by both
  the copy and update scripts to avoid path-list drift.
- Implemented `scripts/update-ai-collaboration-files.sh` performing the 3-way
  merge and branch/PR creation in the target repository.
- Added ADR 0008 recording the pull-model decision.

## Verification

- `bash -n` syntax check on both scripts.
- Dry-run against a temporary target repository fixture.
