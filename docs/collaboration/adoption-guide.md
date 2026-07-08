# Collaboration Template Adoption Guide

Use this guide after copying the collaboration template into a new or existing
repository. It is intentionally separate from the target repository README so
midway adoption does not overwrite product documentation.

For the benefits and tradeoffs of using the template, see
`docs/collaboration/template-benefits.md`.

## New Repository Adoption

1. Run `scripts/copy-ai-collaboration-files.sh --target <repo>`.
2. Fill generic placeholders in `AGENTS.md`, `CLAUDE.md`,
   `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
   `docs/architecture/README.md`.
3. Add the first target feature specification under `docs/specs/`.
4. Add only the stack-specific architecture documents that the project already
   needs.
5. Read `docs/collaboration/project-start-guide.md` for the first development
   loop.
6. Run `scripts/init-llm-context.sh <repo>` and paste the generated prompt into
   the first agent session.
7. Read `docs/collaboration/session-start-and-resume.md` for ongoing session
   start and resume patterns after adoption.

## Midway Adoption

1. Run `scripts/copy-ai-collaboration-files.sh --target <repo> --dry-run`.
2. Run the copy without `--force` so existing target files remain unchanged.
3. Review skipped files and decide manually whether any target-owned document
   should adopt collaboration wording.
4. Keep accepted target architecture and feature specifications authoritative.
5. Use Fast Path for mechanical adoption cleanup, Feature Path for accepted
   feature work, and Architecture Path for process or boundary decisions.

## Receiving Later Template Updates

Adoption via `scripts/copy-ai-collaboration-files.sh` records a
`.collaboration-template-version` marker at the target repository root. Use
that marker to pull in later template improvements without losing target
customizations:

1. Update your local checkout of this template repository (`git pull` or
   equivalent) so it has the commit you want to sync to.
2. Optionally list paths the target has intentionally diverged from in
   `.collaboration-template-ignore` (simple glob patterns, one per line).
3. Run `scripts/update-ai-collaboration-files.sh --target <repo>`.
4. Review the reported summary: files added, updated, merged, files with
   conflict markers, files flagged as "needs decision" (deleted in the
   target but changed upstream since the last sync), and any "NUMBER
   COLLISIONS" (a newly added ADR or local issue shares a number with an
   existing target file under a different name). A "needs decision" item can
   also mean the target renamed the file (for example, to its own sequential
   ADR/issue number) rather than truly deleting it -- check for a
   same-content match under a different filename before restoring anything.
5. Resolve any conflict markers or flagged items before merging the PR the
   script opened. Never merge a sync PR with unresolved conflict markers,
   unresolved NUMBER COLLISIONS, or unresolved NEEDS DECISION items.
6. If the sync introduces new cross-cutting process vocabulary (for example,
   a new operating-path or phase concept), check whether the target's own
   `CLAUDE.md`/`AGENTS.md` needs a matching, reviewed update so the newly
   imported docs describe a concept the target's agent contract actually
   uses. A project that customized `CLAUDE.md` before that vocabulary
   existed will not get it added automatically, and imported docs that
   reference an unused concept are worse than no docs.

### Recovering When a Repository Predates the Marker

`scripts/update-ai-collaboration-files.sh` requires
`.collaboration-template-version` at the target root, written by
`scripts/copy-ai-collaboration-files.sh`. Some repositories adopted this
template's content before that script existed, or via manual copy/paste, and
have no such marker and no adoption commit to derive one from.

Do not fabricate a `ref:` value without checking it. Instead:

1. Pick a handful of representative shared files that are unlikely to have
   been hand-edited by the target (for example, one ADR under
   `docs/architecture/adr/`, `docs/templates/design-intake.md`).
2. Walk the template's own git history (oldest first) and, for each
   candidate commit, `git show <commit>:<path>` those same files.
3. Find the oldest template commit whose content for those files matches (or
   nearly matches, accounting for placeholder fills) the target's own oldest
   version of the same files. Confirm with `diff`, not by inspection alone.
4. Once confirmed, hand-write `.collaboration-template-version` with that
   commit as `ref:` and commit it on its own (no unrelated changes in the
   same commit), before running the update script for the first time.

If no reasonable match exists (the target's content has diverged too far to
identify a common ancestor), treat the target as a from-scratch adoption
instead: review `docs/collaboration/template-benefits.md` and the current
template content manually rather than running the automated sync.

The script never commits to the target's trunk branch; it creates a
dedicated branch and opens a PR, per
`docs/collaboration/branch-commit-pr-discipline.md` and
`docs/architecture/adr/0008-template-update-propagation.md`. It does not
clone or register repositories on its own, and this template repository does
not track which projects have adopted it.

## LLM Session Setup

Use `scripts/init-llm-context.sh <repo>` once to print a compact first prompt
after adoption. For daily new sessions and resuming work, see
`docs/collaboration/session-start-and-resume.md` instead of rerunning the
script.

For more detailed, project-neutral prompt examples, see
`docs/templates/examples/adoption-prompts.md`.

The first-session prompt instructs the agent to:

- read `AGENTS.md` and `docs/architecture/agent-quickstart.md`.
- select Fast Path, Feature Path, or Architecture Path.
- avoid introducing target stack, datastore, provider, or domain decisions
  without an accepted specification or ADR.
- stop when the target specification or requested phase is missing.

Grok Build discovers `.grok/rules/*.md` as a distinct, stronger-binding rules
surface (visible via `grok inspect`) separate from generic context loading;
keep it in sync with `AGENTS.md`/`CLAUDE.md` like any other contract file.
Codex reads `AGENTS.md` directly (its own `~/.codex/rules/` is a user-home
setting, not a project-distributable one), so it needs no dedicated
template file.

## Cost and Reasoning Control

Use `docs/collaboration/llm-cost-reduction.md` to keep LLM cost control
observable without adding heavy process. For substantial tasks, traces should
record the selected operating path, omitted context, deterministic checks, and
any escalation reason.

## Adoption Safety Rules

- Do not use this template to replace target project architecture.
- Do not ship target-specific domain models as part of the reusable template.
- Do design the target domain model after adoption, through target specs,
  reviewed tests, Referee decisions, and ADRs.
- Do not use `--force` unless the target owner has reviewed each overwrite.
- Do not treat placeholder examples as selected technology.
- Keep target secrets, private data, and full exports out of AI prompts.
- Prefer deterministic checks over AI reasoning for copy verification,
  formatting, parsing, and CI sanity.
