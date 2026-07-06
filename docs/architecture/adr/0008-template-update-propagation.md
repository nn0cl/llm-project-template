# ADR 0008: Pull-Based Template Update Propagation

## Status

Accepted

## Context

`scripts/copy-ai-collaboration-files.sh` only supports a one-time copy into a
new or existing repository. Once a project has adopted the template, it has
no repeatable way to bring in later template improvements (for example, ADR
0007's branching practices) without a human manually diffing every file.

A push model, where this template repository knows about every adopting
repository and opens PRs against them, would require a registry of adopting
repositories and write credentials to each one -- both are template-scope
assumptions this project avoids (see `docs/collaboration/adoption-guide.md`'s
adoption safety rules). A pull model, where each adopting repository chooses
when to sync and runs the sync locally or in its own CI, does not require the
template to know who adopted it.

The Referee also raised a specific risk: a naive "copy the newest version
over the old one" update would silently overwrite or resurrect files an
adopting project intentionally customized or deleted after adoption. Any
update mechanism must preserve those local decisions by default and never
apply an unreviewed change to `main`/trunk (per ADR 0007).

## Dependency Adoption Evidence

Not applicable. The mechanism uses `git merge-file`, `git show`, and `gh`,
which the repository (or its adopters) already depends on; no new library or
service is introduced.

## Decision

1. Adoption records a version marker, `.collaboration-template-version`, at
   the target repository root, containing the source template location and
   the commit SHA the project last synced against. Both
   `scripts/copy-ai-collaboration-files.sh` (initial adoption) and
   `scripts/update-ai-collaboration-files.sh` (later syncs) write this file.
2. An adopting project may list paths in `.collaboration-template-ignore`
   (simple glob patterns, one per line) that the update script must never
   touch, regardless of upstream changes.
3. `scripts/update-ai-collaboration-files.sh` updates a target repository
   using a per-file 3-way merge: base = the file at the recorded marker
   commit, ours = the target's current file, theirs = the template's current
   file (via `git merge-file`).
   - If only the template changed the file since the marker commit, the
     target is updated automatically.
   - If only the target changed the file, the target's version is kept.
   - If both changed it, the two changes are merged; a clean merge is applied
     automatically, and an unresolved merge is written with conflict markers
     and reported, never silently resolved in either direction.
   - If the target deleted a file since the marker commit and the template
     has not changed it since, the deletion is respected silently. If the
     template *has* changed a file the target deleted, the situation is
     reported as needing a manual decision; the file is not auto-restored.
     This also fires when the target renamed the file (for example, to its
     own sequential ADR/local-issue number) rather than deleting it, since
     the script diffs by path; the reported guidance tells reviewers to
     check for a same-content match under a different filename before
     assuming a real deletion.
   - Numbered ADR (`docs/architecture/adr/NNNN-*`) and local issue
     (`docs/issues/LISS-NNNN-*`) files are a distinct class: when the
     template adds a new one, the script checks whether the target already
     has a different file under the same number. A match is reported as a
     `NUMBER COLLISION` requiring manual renumbering (with the next free
     number in the target's own sequence suggested), separate from the
     Added/Updated/Merged/Conflicts/Needs-decision categories, since a plain
     path diff cannot otherwise tell two unrelated documents "at the same
     number" apart.
4. The update script never commits to the target's trunk branch. It creates
   a dedicated branch (`process/update-collab-template-<date>-<short-sha>`),
   commits the merge result and the updated marker there, and opens a pull
   request with `gh` when available and the target has a remote, per
   `docs/collaboration/branch-commit-pr-discipline.md` and ADR 0007. A PR
   with unresolved conflicts or flagged deletions must not be merged until a
   human resolves them.
5. The template repository does not maintain a registry of adopting
   repositories and does not push updates to them.

## Consequences

Positive:

- Adopting projects can pull in template improvements repeatedly instead of
  only at initial adoption.
- Local customizations and intentional deletions are preserved by default;
  nothing is silently overwritten or resurrected.
- The template repository carries no list of, or credentials to, adopting
  repositories.
- The sync always goes through the same branch/PR/CI gate as any other
  change, so a bad merge cannot land without review.

Negative:

- Adopting projects must keep a local checkout of the template repository
  with enough history to reach the marker commit; a shallow clone missing
  that commit will fail the sync with an explicit error rather than guessing.
- Three-way text merging on Markdown/YAML files can produce conflicts on
  reformatting-only changes (e.g., a paragraph rewrap) even when the
  semantic content does not truly conflict; this trades a few avoidable
  manual resolutions for never silently overwriting target customizations.
- Nothing runs this automatically; an adopting project that never re-runs the
  script simply never updates. Scheduling it (e.g., via a periodic CI job) is
  left to the adopting project.
- A clean merge (no conflict markers) is not the same guarantee as "nothing
  needs review": a hunk can merge cleanly purely because of where the
  target's own edits fell relative to line boundaries, even immediately next
  to a hunk that did conflict, and it can introduce a forward reference (for
  example, to a file also being added by the same sync, or skipped via
  `.collaboration-template-ignore`) with no visible signal. Reviewers should
  diff the whole changed file against its pre-sync version, not only search
  for conflict markers.

## Enforcement

Code review should reject:

- any change to `scripts/update-ai-collaboration-files.sh` that commits
  directly to the target's trunk branch instead of a dedicated branch.
- a sync PR merged while it still contains conflict markers or unresolved
  "needs decision" items in its description.
- removing the `.collaboration-template-ignore` honoring logic, or making the
  update script overwrite ignored paths.
- adding a registry of adopting repositories or push-based delivery to this
  template repository without superseding this ADR.
