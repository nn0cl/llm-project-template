# LISS-0003: Shared-block delimiters for README.md and ci.yml template syncs

## Metadata

- Local issue ID: LISS-0003
- GitHub issue:
- Status: proposed
- Phase: phase-0-design
- Type: process/tooling
- Priority: low
- Owner/agent:
- Related branch:

## Summary

- `README.md` and `.github/workflows/ci.yml` are tracked as shared template
  paths (see `scripts/lib/collaboration-template-paths.sh`). Once an
  adopting project replaces the template's own explainer prose with its own
  product content (which `copy-ai-collaboration-files.sh`'s default
  skip-existing behavior encourages), a later 3-way sync's merge conflict on
  these files can span nearly the entire file, because there is no
  structural marker separating "template-owned section" from
  "project-owned section" within the same file.
- Reported by an external adopter (voice-to-dic) as the single most
  time-consuming conflict class to resolve by hand.

## Acceptance Notes (proposed, not yet accepted)

- Identify which parts of `README.md`/`ci.yml` are genuinely meant to
  propagate (e.g. required-files list, ADR-count check, onboarding links)
  versus free-form project prose.
- Consider delimiting the propagating parts (HTML comment markers, or a
  separate generated snippet the project includes) so future syncs only
  ever conflict on that narrow, intentionally-shared block.
- This changes the shape of two files every adopter touches; needs Adjudicator
  design review before implementation, not a mechanical fix.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0002, ADR 0008

## Adjudicator Decision Points

- Not yet reviewed. Deliberately left at `proposed` status instead of being
  implemented alongside LISS-0002, since it changes file structure every
  adopter depends on and deserves its own design pass.

## Context

- Included: `README.md`, `.github/workflows/ci.yml`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/update-ai-collaboration-files.sh`.
- Omitted: any concrete delimiter syntax decision (left open).

## References

- External feedback report from voice-to-dic's first pull-sync, finding 4.

## Work Notes

- None yet; this is a backlog placeholder.

## Verification

- N/A until accepted and scoped.
