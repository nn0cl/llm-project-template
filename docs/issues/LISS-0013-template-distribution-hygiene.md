# LISS-0013: Template distribution hygiene

## Metadata

- Local issue ID: LISS-0013
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/docs (bug, template tooling)
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason:
- Owner/agent: Claude Code CLI (Claude Sonnet 5)
- Related branch: process/2026-07-14-token-variance-and-distribution-hygiene

## Summary

- Adapts a proposal originally drafted on branch
  `codex/process/token-variance-reasons` (Codex desktop, 2026-07-10, never
  merged, no PR) as `LISS-0009: Template distribution hygiene`. That
  branch's `LISS-0009` ID now collides with this session's own (different,
  already merged) `LISS-0009: External resource adoption contract`, so this
  issue re-numbers the content and re-verifies it against current `main`
  instead of reusing the original branch as-is.
- **Confirmed live bug, still present on current `main`**:
  `scripts/copy-ai-collaboration-files.sh` copies `docs/issues/` and
  `docs/collaboration/` (including `docs/collaboration/traces/`) as whole
  directories via `collaboration_template_paths` in
  `scripts/lib/collaboration-template-paths.sh`. Every project adopting this
  template today receives this template repository's own maintenance
  history verbatim: all of `LISS-0001` through `LISS-0011` (soon
  `LISS-0013`), every trace file under `docs/collaboration/traces/`, and
  `docs/specs/template-rollout.md` (a spec describing *this repository's*
  own rollout, not the adopter's product). None of this is relevant to an
  adopting project and all of it is presented as if it were the adopter's
  own planning history.
- Fix: exclude the template's own maintenance-history files from
  copy/update, while still creating the empty `.gitkeep`-carrying
  directories so adopters can start their own issue/trace/spec ledgers.
- Also adds CI checks (script syntax, unresolved conflict markers, a live
  copy/init smoke test) that would have caught this category of defect
  automatically — including the kind of bug found manually during this
  session's own PR #6 work (the `*.mdc` placeholder-substitution glob gap,
  LISS-0010).
- Also fixes a stale ADR-count reference in `README.md` ("eight ADRs
  (0001-0008)"), found while re-verifying this content against current
  `main`: the count was already stale relative to the original branch's own
  fix (nine, 0001-0009, as of 2026-07-10) and is more stale now (eleven,
  0001-0011, after this session's ADR 0010/0011 work).

## Acceptance Notes

- `scripts/lib/collaboration-template-paths.sh` gains a
  `collaboration_template_exclude_paths` array
  (`docs/collaboration/traces/*.md`, `docs/issues/LISS-*.md`,
  `docs/specs/template-rollout.md`) and an `is_collaboration_template_excluded`
  helper function, reused by both scripts below.
- `scripts/copy-ai-collaboration-files.sh`'s directory-copy path
  (`copy_path`) skips any file matching the exclude patterns, printing
  `skip template-history <path>` (matching the existing `skip existing
  <path>` message style) instead of copying it.
- `scripts/update-ai-collaboration-files.sh`'s `list_files` applies the same
  exclusion so already-adopted projects never receive these files via
  update either.
- Adopting projects still receive the `.gitkeep` files for
  `docs/issues/`, `docs/collaboration/traces/`, and `docs/specs/` (the
  `.gitkeep` files themselves are not matched by the exclude patterns,
  since the patterns target `*.md` content files and the specific
  `template-rollout.md` filename).
- `.github/workflows/ci.yml` gains, in the existing `repository-sanity`
  job:
  - Additional `required_files` entries for files that exist in this repo
    but were not yet checked: `README.ja.md`, `.github/dependabot.yml`,
    `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/
    bug_report.md`, `.github/ISSUE_TEMPLATE/config.yml`,
    `.github/ISSUE_TEMPLATE/feature_request.md`,
    `scripts/copy-ai-collaboration-files.sh`,
    `scripts/update-ai-collaboration-files.sh`, `scripts/init-llm-context.sh`,
    `scripts/lib/collaboration-template-paths.sh`.
  - A "Check script syntax" step (`bash -n` on all four scripts).
  - A "Check unresolved conflict markers" step (`git grep` for
    `<<<<<<<`/`=======`/`>>>>>>>`, excluding `.git`).
  - A "Check template copy smoke test" step: runs
    `copy-ai-collaboration-files.sh` against a throwaway `git init`'d
    target, then `init-llm-context.sh` against it, and asserts the
    `.gitkeep` files exist while no `LISS-*.md`, trace `*.md`, or
    `template-rollout.md` file was copied.
- `README.md` and `README.ja.md`: the Directory Guide tree gains
  `update-ai-collaboration-files.sh` and `lib/collaboration-template-paths.sh`
  (already present as files but missing from the tree), plus a short note
  that template-maintenance history is excluded from adopting projects. The
  stale "eight ADRs (0001-0008)" reference is corrected to the current
  count (eleven, 0001-0011) rather than the source branch's own
  already-outdated "nine" fix.
- `docs/collaboration/adoption-guide.md` gains the same short exclusion
  note near the update-sync instructions.
- `docs/collaboration/local-issue-planning.md` is unaffected by this issue
  (its token-related wording is LISS-0012's concern).

### Addendum (2026-07-14): ported from a third, previously-unpushed commit

A third commit existed only in the Adjudicator's local checkout of
`codex/process/token-variance-reasons` (`358280f`, "Tighten template
adoption guidance"), never pushed to `origin/codex/process/
token-variance-reasons` and therefore not visible when this issue was
first drafted. Discovered when the Adjudicator asked to push/PR/merge that
branch directly; re-implemented here (not pushed as-is, for the same
merge-base-staleness reason as the first two commits) rather than as a new
issue, since it is a direct continuation of this same distribution-hygiene
concern:

- New `.gitignore` at the repository root (`.DS_Store`, `.idea/`,
  `.vscode/`), added to `collaboration_template_paths` so adopting projects
  receive it too.
- CI `required_files` gains `.gitignore`; the smoke test gains `test -f
  "$tmp/target/.gitignore"`.
- CI smoke test gains a placeholder-substitution check: greps the copied
  `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules`, and (extended beyond the source commit, which predates
  this session's Cursor support) `.cursor/rules` for unfilled
  `<PROJECT_NAME: one-line description...>`/`<FILL IN: e.g. backend...>`
  placeholders and fails if any remain.
- `README.md`, `README.ja.md`, and `docs/collaboration/adoption-guide.md`'s
  placeholder-fill instructions are reworded to distinguish what the copy
  script can fill automatically (project name, domain summary, stack, via
  `--project-name`/`--domain-summary`/`--stack`) from what still requires
  Adjudicator-approved target facts (runtime boundaries, datastore, migration
  tool, external resources, stack-specific architecture documents).
- `README.md`'s Directory Guide tree gains the `.gitignore` line.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0012 (same source branch, implemented together in this
  session), LISS-0001/LISS-0002 (original copy/update script design),
  ADR 0008 (template update propagation).

## Adjudicator Decision Points

- Resolved 2026-07-14: adopt the distribution-hygiene proposal, renumbered
  to avoid the LISS-0009 collision with this session's own issue of that
  number.
- Resolved 2026-07-14: fix the ADR-count reference to the current true
  count (eleven) rather than reproducing the source branch's own
  already-stale "nine" fix verbatim.
- Not open, but worth recording: the exclude-pattern list
  (`docs/issues/LISS-*.md`, `docs/collaboration/traces/*.md`,
  `docs/specs/template-rollout.md`) is deliberately narrow and file-specific
  rather than excluding `docs/issues/` or `docs/collaboration/traces/`
  wholesale, so that a future adopter who *does* want to see this
  template's example issue/trace structure by reading this template
  repository directly (not their own copy) is unaffected — only the copy/
  update scripts skip these files.

## Context

- Included: the `codex/process/token-variance-reasons` branch's second
  commit (`6ed7a7d` "Improve template distribution hygiene") diffed against
  its merge-base with `main` (`80edcdd`);
  `scripts/lib/collaboration-template-paths.sh`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/update-ai-collaboration-files.sh`, `.github/workflows/ci.yml`,
  `README.md`, `README.ja.md`, `docs/collaboration/adoption-guide.md`.
- Omitted: the source branch's token-variance changes (tracked separately
  as LISS-0012); application source (none exists in this template repo).
- Assumptions: `docs/specs/template-rollout.md` is genuinely this
  repository's own dogfooding spec (confirmed by reading its content: "This
  specification covers this repository as a reusable AI-human collaboration
  template... It must not define the product architecture... of a target
  repository") and should never be distributed as if it were a target
  project's spec.

## AI Planning Records

### AIP-0013-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-14
- Planning size: M
- Intended execution route: deterministic diff/review of the source branch
  content, direct edits to re-implement against current `main`, live smoke
  test verification (mirroring the source branch's own verification
  approach)
- Intended scope: `collaboration-template-paths.sh`,
  `copy-ai-collaboration-files.sh`, `update-ai-collaboration-files.sh`,
  `.github/workflows/ci.yml`, `README.md`, `README.ja.md`,
  `docs/collaboration/adoption-guide.md`
- Estimated token range: 8,000-16,000
- Token metric: approximate total model tokens for this process task
- Estimation basis: script logic port plus CI job addition plus doc
  updates, verified with a live throwaway-directory smoke test
- Assumptions: no application code changes; no new ADR needed (this is
  tooling/process hygiene, not an architecture boundary decision)
- Confidence: high
- Revises:
- Revision reason:
- Superseded by: AIP-0013-002

### AIP-0013-002

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-14
- Planning size: S
- Intended execution route: deterministic diff/review of a third,
  previously-unpushed source commit (`358280f`), direct edits to
  re-implement against current `main`, live smoke test re-verification
- Intended scope: new `.gitignore`, `collaboration-template-paths.sh`,
  `.github/workflows/ci.yml`, `README.md`, `README.ja.md`,
  `docs/collaboration/adoption-guide.md`
- Estimated token range: 4,000-8,000
- Token metric: approximate total model tokens for this follow-up task
- Estimation basis: one new file plus small additions to five
  already-touched documents/scripts
- Assumptions: no application code changes
- Confidence: high
- Revises: AIP-0013-001
- Revision reason: Adjudicator asked to push/PR/merge the source branch
  directly; a third, previously-unpushed local commit on that branch was
  discovered in the process and is re-implemented here as a continuation
  of the same issue.
- Superseded by:

## References

- `codex/process/token-variance-reasons` (GitHub branch, unmerged, no PR),
  commits `6ed7a7d` and `358280f` (the latter never pushed to
  `origin/codex/process/token-variance-reasons`).
- `docs/specs/template-rollout.md` (confirms the exclusion rationale).
- Adjudicator request, 2026-07-14 (chat): asked to evaluate the branch's
  content and adapt it to current `main` if worthwhile; later asked to
  push/PR/merge the branch, which surfaced the third commit.

## Work Notes

- The original branch's own `docs/issues/LISS-0009-template-distribution-hygiene.md`
  and `docs/collaboration/traces/2026-07-10-template-distribution-hygiene.md`
  remain on the `codex/process/token-variance-reasons` branch as historical
  record of the original proposal; they are not copied into this
  repository's `main` history since this issue supersedes them with a
  collision-free ID.
- 2026-07-14 addendum: the Adjudicator asked to push/PR/merge the
  `codex/process/token-variance-reasons` branch directly. Doing so verbatim
  was rejected — the branch's merge-base predates most of this session's
  own work, so a direct push/PR would have produced extensive conflicts and
  risked reviving the superseded `LISS-0009` filename. The branch's third,
  previously-unpushed local commit (`358280f`) was instead diffed and its
  content re-implemented here (see AIP-0013-002 and the Addendum in
  Acceptance Notes).

## Verification

- Local reproduction of CI's required-files, ADR-existence, and
  conflict-marker checks — pass.
- Live, real smoke test (copy script against a throwaway `mktemp -d` +
  `git init` target, `init-llm-context.sh`, then direct `ls -la`
  inspection) — confirmed only `.gitkeep` files present, no `LISS-*.md`, no
  trace `*.md`, no `template-rollout.md` copied.
- Found and fixed a real defect during this verification: the CI smoke
  test's originally-ported `! compgen -G "..." >/dev/null` assertion
  returns exit code 0 regardless of match, so it would have failed
  unconditionally; replaced with an `ls`-based check, re-verified correct
  in both directions under `bash`.
- `git diff --check` — pass.
- See `docs/collaboration/traces/
  2026-07-14-token-variance-and-distribution-hygiene.md` for the full
  verification record.
