# LISS-0014: Synchronize issue documents when work is completed

## Metadata

- Local issue ID: LISS-0014
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/docs
- Priority: high
- Initial planning size: S
- Current planning size: S
- Reclassification reason:
- Owner/agent: Codex
- Parent: -
- Depends on: -
- Blocks: -
- Related branch: process/issue-document-sync

## Summary

Add an explicit template rule that requires issue status, work-plan status, and completion evidence
to be updated when implementation work reaches `done`, `review`, `blocked`, or `wont_do`.

## Acceptance Notes

- Definition of Done requires issue/document synchronization before completion is reported.
- Commit/PR discipline requires status changes and completion evidence in the same reviewable unit.
- Local issue planning documents the allowed lifecycle values used by the synchronization rule.
- The process-gap register records this as a covered collaboration control.

## Verification

- Confirmed the new rule is present in the template's Definition of Done and commit discipline documents.
- Confirmed the issue is marked `done` with process-only scope and completion evidence.

## Referee Review

- Reviewed by: repository Referee (user)
- Review date: 2026-07-16
- Review route: explicit Referee review of the recent agent changes against the repository operating rules.
- Decision: approved after correction and re-commit.
- Review record: `docs/collaboration/reviews/2026-07-16-issue-document-sync-referee-review.md`
- Corrections required by review:
  - combine the split process changes into one reviewable commit.
  - add the required AI work trace for operating-contract changes.
  - make work-plan synchronization conditional when no work plan exists.
  - align the issue acceptance notes with the files actually changed.
