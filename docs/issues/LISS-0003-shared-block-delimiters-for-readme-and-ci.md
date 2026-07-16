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

- `.github/workflows/ci.yml` is tracked as a shared template path (see
  `scripts/lib/collaboration-template-paths.sh`). Once an adopting project
  customizes it, a later 3-way sync's merge conflict can span nearly the
  entire file, because there is no structural marker separating
  "template-owned section" from "project-owned section" within the same
  file. (`README.md` originally had the same problem as a shared path; as
  of 2026-07-16 it is no longer distributed at all — see Work Notes — so
  the remaining scope is `ci.yml` only.)
- Reported by an external adopter (voice-to-dic) as the single most
  time-consuming conflict class to resolve by hand.

## Acceptance Notes (proposed, not yet accepted)

- Identify which parts of `README.md`/`ci.yml` are genuinely meant to
  propagate (e.g. required-files list, ADR-count check, onboarding links)
  versus free-form project prose.
- Consider delimiting the propagating parts (HTML comment markers, or a
  separate generated snippet the project includes) so future syncs only
  ever conflict on that narrow, intentionally-shared block.
- This changes the shape of two files every adopter touches; needs Referee
  design review before implementation, not a mechanical fix.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0002, ADR 0008

## Referee Decision Points

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

- 2026-07-16: The README half of this issue is resolved by a different
  route than delimiters: `README.md` / `README.ja.md` were removed from
  `collaboration_template_paths` (and from `ci.yml`'s `required_files`)
  entirely, on the grounds that the template README carries no
  placeholders, describes the template repository itself, and was the
  documented worst conflict class for adopters. Projects now own their
  README with no template sync against it. The remaining scope of this
  issue is the `ci.yml` shared-block question only.

## Verification

- N/A until accepted and scoped.
