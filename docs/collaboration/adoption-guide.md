# Collaboration Template Adoption Guide

Use this guide after copying the collaboration template into a new or existing
repository. It is intentionally separate from the target repository README so
midway adoption does not overwrite product documentation.

For the benefits and tradeoffs of using the template, see
`docs/collaboration/template-benefits.md`.

## New Repository Adoption

1. Run `scripts/copy-ai-collaboration-files.sh --target <repo>`.
2. Fill generic placeholders in `AGENTS.md`, `CLAUDE.md`,
   `.github/copilot-instructions.md`, and `docs/architecture/README.md`.
3. Add the first target feature specification under `docs/specs/`.
4. Add only the stack-specific architecture documents that the project already
   needs.
5. Read `docs/collaboration/project-start-guide.md` for the first development
   loop.
6. Run `scripts/init-llm-context.sh <repo>` and paste the generated prompt into
   the first agent session.

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
   conflict markers, and files flagged as "needs decision" (deleted in the
   target but changed upstream since the last sync).
5. Resolve any conflict markers or flagged items before merging the PR the
   script opened. Never merge a sync PR with unresolved conflict markers.

The script never commits to the target's trunk branch; it creates a
dedicated branch and opens a PR, per
`docs/collaboration/branch-commit-pr-discipline.md` and
`docs/architecture/adr/0008-template-update-propagation.md`. It does not
clone or register repositories on its own, and this template repository does
not track which projects have adopted it.

## LLM Session Setup

Use `scripts/init-llm-context.sh <repo>` to print a compact first prompt.
For more detailed, project-neutral prompt examples, see
`docs/templates/examples/adoption-prompts.md`.

The prompt instructs the agent to:

- read `AGENTS.md` and `docs/architecture/agent-quickstart.md`.
- select Fast Path, Feature Path, or Architecture Path.
- avoid introducing target stack, datastore, provider, or domain decisions
  without an accepted specification or ADR.
- stop when the target specification or requested phase is missing.

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
