# LISS-0011: `update-ai-collaboration-files.sh` does not substitute placeholders in newly added files

## Metadata

- Local issue ID: LISS-0011
- GitHub issue:
- Status: proposed
- Phase: phase-0-design
- Type: process/docs (bug, template tooling)
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason:
- Owner/agent:
- Related branch:

## Summary

- Found during a review audit of PR #6 (2026-07-14):
  `scripts/copy-ai-collaboration-files.sh`'s `replace_placeholders` function
  substitutes `<PROJECT_NAME...>` and stack placeholders in every copied
  file matching `*.md|*.mdc|*.yml|*.yaml`, but
  `scripts/update-ai-collaboration-files.sh` — used by already-adopted
  projects to pull in later template updates — never calls an equivalent
  substitution step. Its `process_file` function, when it finds a file that
  exists in the template but not yet in the target
  (`docs/collaboration/adoption-guide.md` calls this the "added" case,
  `scripts/update-ai-collaboration-files.sh:283-289`), simply `cp`s the
  template's file verbatim into the target.
- Consequence: any already-adopted project that runs
  `update-ai-collaboration-files.sh` to pick up a template change that adds
  a brand-new contract file (for example, this session's
  `.cursor/rules/*.mdc`, or the earlier `.grok/rules/*.md` from LISS-0006)
  will receive that file with the literal `<PROJECT_NAME: one-line
  description...>` and `<FILL IN: e.g. backend language...>` placeholders
  still in it, unless the adopter notices and fills them in by hand. The
  initial-copy path (`copy-ai-collaboration-files.sh`) does not have this
  problem; only the update path does.
- This is a pre-existing gap (it applied to `.grok/rules/*.md` since
  LISS-0006 shipped it, 2026-07-08) whose blast radius grew with this
  session's addition of three more such files, which is what surfaced it
  during review.

## Acceptance Notes

- `update-ai-collaboration-files.sh`'s "added" (new-upstream-file) path
  substitutes the same `<PROJECT_NAME...>` and stack placeholders that
  `copy-ai-collaboration-files.sh` does, using the target's already-recorded
  project name/stack values rather than asking the Referee to re-supply
  them (the target's own already-filled contract files, e.g. `AGENTS.md`,
  are the natural source — the design must state exactly how the value is
  recovered without re-parsing free text unreliably).
- Files the target has customized are never touched by this substitution
  step; it applies only to genuinely new files being introduced for the
  first time (the existing `added` case), not to the 3-way-merge `updated`/
  `merged` cases, which already preserve target customization.
- The fix must not regress `--dry-run` (planned actions are reported, no
  files change) or `--no-pr` behavior.
- Add a regression check: a small fixture-based test or a documented manual
  verification step (matching how LISS-0006's trace verified the initial-copy
  path with a live dry-run/real-run against a throwaway directory) that
  simulates a target with a recorded project name/stack and confirms a
  newly-added contract file has no leftover placeholders after update.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0006 (introduced `.grok/rules/*.md`, where this gap first
  applied), LISS-0010 (introduced `.cursor/rules/*.mdc`, tripling the
  affected file count and surfacing this issue).

## Referee Decision Points

- Open: where does the update script recover the target's project-name/
  stack values from? Candidates: re-derive from the target's own `AGENTS.md`
  (fragile — free text, no guaranteed anchor), read
  `.collaboration-template-version` or a similar marker file (would need a
  new field), or require the Referee to pass `--project-name`/`--stack`
  flags to the update script explicitly (matching the initial-copy script's
  own interface, but adds a manual step to every update run). Needs Referee
  input before Phase 1.
- Open: should this be scoped narrowly (fix only the placeholder gap) or
  combined with a broader look at `update-ai-collaboration-files.sh`'s
  new-file handling in general? Default assumption: narrow fix only, to
  keep this issue's planning size at `M` rather than growing it.

## Context

- Included: `scripts/update-ai-collaboration-files.sh`,
  `scripts/copy-ai-collaboration-files.sh` (source of the working pattern
  to port over), `docs/collaboration/adoption-guide.md`.
- Omitted: unrelated parts of the update script (3-way merge logic for
  already-existing files, which is out of scope and already working).
- Assumptions: the fix is scoped to newly-added files only; the existing
  3-way-merge behavior for already-tracked files is correct and untouched.

## References

- Found during review audit of PR #6, 2026-07-14 (Referee-requested "logic
  error" review of `llm_project_template`).
- `scripts/copy-ai-collaboration-files.sh` lines around `replace_placeholders`
  (the pattern to reuse).
- `scripts/update-ai-collaboration-files.sh` lines around `process_file`'s
  `added+=("$rel")` branch (the gap).

## Work Notes

- Not implemented in this issue — recorded as a proposed issue only, per
  the Referee's decision during the PR #6 review to scope the immediate fix
  branch to the drift/consistency findings (F1, F2, F3, F5, F6) and defer
  this structural gap (F4) to its own issue.

## Verification

- Not yet started.
