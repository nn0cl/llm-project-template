# AI Work Trace

## Request

- Date: 2026-07-06
- User request: Design and implement pull-based propagation of template
  updates to repositories that already adopted this template, addressing the
  Referee's concern that ignored/customized/deleted target files must not be
  silently merged over, and requiring the mechanism itself to follow the
  repository's branch/PR discipline.
- Current phase: Feature Path (LISS-0001), implemented directly given the
  small, script-level scope; verified with a fixture instead of a formal
  Red/Green split since this is repository tooling, not target-project
  behavior under Gherkin/EARS.

## Context Ledger

- Included: `scripts/copy-ai-collaboration-files.sh`,
  `docs/collaboration/adoption-guide.md`,
  `docs/collaboration/branch-commit-pr-discipline.md`, ADR 0005, ADR 0007,
  `.github/workflows/ci.yml`.
- Omitted: concrete CI scheduling for automatic syncs (left to adopting
  projects), private data, any specific merge-queue/PR-bot vendor.
- Assumptions: adopting projects run the sync against a local checkout of
  this template with enough history to reach the recorded marker commit;
  network cloning of the template is out of scope for the script itself.
- Open decisions: none within this issue's scope.

## Routing

- Model/assistant/tool: direct implementation (bash scripts, docs, ADR); a
  local git fixture (three throwaway repos under the scratch directory) was
  used to exercise merge/conflict/deletion/ignore paths before trusting the
  script.
- Reason: this is deterministic tooling logic, well suited to direct
  implementation plus fixture-based verification rather than delegation.
- Privacy constraints: no private data used; fixture repos were synthetic and
  discarded.

## Referee Decisions

- Pull model confirmed over push/registry model.
- 3-way merge with explicit ignore list and no silent overwrite confirmed.
- The sync mechanism itself must follow branch + PR discipline (no direct
  commits to target's trunk) -- implemented and documented in ADR 0008.

## Verification

- Commands/checks:
  - `bash -n` on both scripts.
  - Fixture test covering: new file added upstream, non-conflicting merge,
    conflicting merge (labeled conflict markers), local deletion respected
    when upstream unchanged, local deletion flagged as "needs decision" when
    upstream changed the same file, ignored path never touched even when
    both sides changed it, and an idempotent re-run reporting "already
    synced".
  - Verified `copy-ai-collaboration-files.sh` still runs end-to-end and now
    writes `.collaboration-template-version`.
- Result: passed.

## Changed Files

- `scripts/lib/collaboration-template-paths.sh` (new)
- `scripts/update-ai-collaboration-files.sh` (new)
- `scripts/copy-ai-collaboration-files.sh`
- `docs/architecture/adr/0008-template-update-propagation.md` (new)
- `docs/collaboration/adoption-guide.md`
- `docs/collaboration/branch-commit-pr-discipline.md`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/issues/LISS-0001-pull-based-template-update-sync.md` (new)
- `docs/collaboration/traces/2026-07-06-template-update-propagation.md`

## Next Safe Action

- Open a PR from `feature/template-update-propagation` into `main`, per this
  repository's own branch-commit-pr-discipline, and merge after CI passes.

## Notes

- The first draft of the merge routine had a bug: it rebuilt the "base" file
  from a shell-captured variable, which silently dropped the file's trailing
  newline and produced spurious conflicts on otherwise non-overlapping edits.
  Fixed by writing `git show <ref>:<path>` straight to a temp file instead of
  round-tripping through a variable.
