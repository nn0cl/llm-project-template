# LISS-0016: Tiered template-authoritative sync policy

## Metadata

- Local issue ID: LISS-0016
- GitHub issue:
- Status: in_progress
- Phase: process-only
- Type: process/tooling
- Priority: medium
- Initial planning size: L
- Current planning size: L
- Reclassification reason:
- Owner/agent: Claude Code CLI (Claude Sonnet 5)
- Parent: -
- Depends on: -
- Blocks: -
- Related branch: process/tiered-template-sync

## Summary

- `scripts/update-ai-collaboration-files.sh` (ADR 0008) treats every template
  file the same way: a per-file 3-way merge (`git merge-file`), with
  conflicts left as markers for manual resolution. This protects adopter
  customizations everywhere, but most template files are pure process
  documentation (`docs/collaboration/*.md` other than the persona files,
  `docs/templates/*.md`, `docs/at-tdd/process.md`, shipped ADRs) that
  adopters are never supposed to hand-edit in the first place. Running a
  text-level 3-way merge on those produces avoidable false conflicts (ADR
  0008 already names this as an accepted downside) for files where there is
  nothing legitimate to protect.
- Adjudicator proposal (2026-07-16, chat): split template files into two
  tiers. Tier 1 (no adopter-fillable placeholders): the template is fully
  authoritative — on a hash difference, overwrite the target's copy, no
  merge. Tier 2 (the five agent persona/contract files that carry
  adopter-filled placeholders: `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`,
  `.cursor/rules/*.mdc`): do not auto-merge or auto-overwrite when both sides
  changed; flag the file for AI-assisted reconciliation instead.
- Two open design points were resolved via `AskUserQuestion`:
  - Tier 2 mechanism: a templated prompt (`docs/templates/contract-file-sync-prompt.md`)
    that tells an agent to read the old and new template content via `git
    show` (no throwaway prompt files), not a per-run generated prompt file.
  - Tier 1 deletions (target intentionally deleted a file the template later
    changed again): ask interactively when a TTY is available, default to
    restoring if not answered or non-interactive, and report the actual
    per-file outcome (overwritten / restored / kept-deleted / needs-AI-merge /
    unchanged / ignored / added / number-collision) at the end of the run
    rather than only reporting conflict/needs-decision counts.

## Acceptance Notes

1. Add a `collaboration_template_contract_paths` classification (or
   equivalent function `is_contract_persona_file`) to
   `scripts/lib/collaboration-template-paths.sh`, naming exactly: `AGENTS.md`,
   `CLAUDE.md`, `.github/copilot-instructions.md`, everything under
   `.grok/rules/`, everything under `.cursor/rules/`.
2. Rewrite `process_file()` in `scripts/update-ai-collaboration-files.sh`:
   - Tier 1, both sides changed since the marker commit: overwrite with the
     template's version unconditionally (no `git merge-file`, no conflict
     markers). Log as "overwritten" if the target had actually diverged from
     the base, or "updated" if the target had not customized it.
   - Tier 2, both sides changed: do not touch the target file. Log as "needs
     AI-assisted merge", naming the file, the old ref, and the new ref, and
     pointing at `docs/templates/contract-file-sync-prompt.md`.
   - Any tier, file missing on target but present at the marker commit
     (target deleted it) and the template changed it since: if stdin/stdout
     are a TTY, prompt `Restore '<path>'? [Y/n]` (default: restore on empty
     input); otherwise default to restoring without prompting. Add a
     `--non-interactive` flag that forces the default without prompting even
     under a TTY. Log the actual outcome ("restored" or "kept deleted") per
     file.
   - Keep the existing Added / Number Collision / Ignored / Unchanged logic
     as-is; these are orthogonal to the tier split.
3. Replace the current summary print (`Updated` / `Merged` / `CONFLICTS` /
   `NEEDS DECISION`) with the new outcome categories: Added, Overwritten
   (Tier 1, target had diverged), Updated (Tier 1, target had not diverged),
   Needs AI-assisted merge (Tier 2), Restored (was deleted locally), Kept
   deleted (Adjudicator/operator decision), Number Collisions, Ignored,
   Unchanged. Update the PR body template to match.
4. Add `docs/templates/contract-file-sync-prompt.md`: instructions for an
   agent to reconcile one Tier 2 file, given the target repo, the file path,
   the old ref, and the new ref — read the target's current (adopter-filled)
   content, the template's content at the old ref, and the template's content
   at the new ref (all via `git show`/`cat`), identify what the target
   customized relative to the old ref, and re-apply those specific
   customizations onto the new ref's structure, then present the result for
   Adjudicator review rather than committing it unreviewed.
5. Extend ADR 0008 in place: record the tiered policy, its rationale (most
   template files are never meant to be locally customized; 3-way merge on
   them is pure overhead), and the two Adjudicator decisions from
   `AskUserQuestion` (prompt-template mechanism for Tier 2; interactive
   default-restore for deletions across both tiers).
6. Update `docs/collaboration/adoption-guide.md`'s description of the sync
   script's behavior to match (it currently describes a uniform 3-way merge).
7. Update `scripts/update-ai-collaboration-files.sh`'s `usage()` help text.
8. `docs/templates/contract-file-sync-prompt.md` is itself a contract file
   (`docs/templates/*.md`) per `prompt-instruction-change-control.md`; this
   PR needs an accompanying trace under `docs/collaboration/traces/`.
9. Verification: since this cannot be tested against a real separate adopter
   repository in this session, build a throwaway local target repo (temp dir,
   `git init`, run `copy-ai-collaboration-files.sh` once, hand-edit a few
   files to simulate adopter customization/deletion, advance the template
   with a new commit) and run `update-ai-collaboration-files.sh
   --non-interactive` (and once with a piped `Y`/`n` to exercise the
   interactive path) against it, confirming each new outcome category fires
   as expected. Record the exact scenarios exercised in Work Notes.

## Dependencies

- Parent: -
- Depends on: -
- Blocks: -
- Related: LISS-0001 (original pull-based sync), ADR 0008 (the decision this
  extends).

## Referee Decision Points

- Tier 2 mechanism: resolved via `AskUserQuestion` (2026-07-16) — templated
  prompt + `git show` references, not generated throwaway prompt files.
- Tier 1 deletion handling: resolved via `AskUserQuestion` (2026-07-16) —
  interactive ask with default-restore, plus a final per-file outcome report.
- Whether numbered ADR/local-issue files the template ships (e.g. this
  template's own `docs/architecture/adr/000N-*.md`) count as Tier 1: yes,
  they carry no adopter placeholders — an adopter who wants their own
  decision creates a new ADR at their own next number rather than editing a
  shipped one.

## Context

- Included: `scripts/update-ai-collaboration-files.sh`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`,
  `docs/architecture/adr/0008-template-update-propagation.md`,
  `docs/collaboration/adoption-guide.md`,
  `docs/collaboration/prompt-instruction-change-control.md` (for the existing
  "Agent Operating Contract Files" list, reused as the Tier 2 classification).
- Omitted: application source; unrelated CI jobs.
- Assumptions: this is a template-repository-only tooling change; no adopting
  project's actual repository is touched by this session.

## AI Planning Records

### AIP-0016-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-16
- Planning size: L
- Intended execution route: careful shell-script rewrite plus a throwaway
  local repo for verification (no real adopter repository is available this
  session); deterministic checks (`bash -n`, the throwaway-repo smoke test)
  over AI reasoning for the script logic itself.
- Intended scope: tier classification, rewritten merge/overwrite/deletion
  logic, new outcome reporting, new prompt template, ADR 0008 extension,
  adoption-guide update, usage text update, trace.
- Estimated token range: 12,000-20,000
- Estimated token midpoint: 16,000
- Token metric: approximate total model tokens for the rewrite plus
  verification
- Estimation basis: `update-ai-collaboration-files.sh` is a 484-line script
  with several interacting code paths (added/updated/merged/conflicts/needs
  decision/number collisions); reworking the core merge decision and adding
  interactive prompting plus a new report format touches most of those paths.
- Assumptions: no change to `copy-ai-collaboration-files.sh`'s initial-copy
  behavior (only the later-sync script changes); the Tier 2 classification
  reuses the existing "Agent Operating Contract Files" persona subset rather
  than inventing a new list.
- Confidence: medium (the throwaway-repo verification should catch scripting
  mistakes, but there is no way to test against a real, organically-drifted
  adopter repository in this session).
- Revises:
- Revision reason:
- Superseded by:

## References

- Adjudicator proposal, 2026-07-16 (chat): hash-compare-and-overwrite for
  "most files", template as source of truth.
- Adjudicator clarification, 2026-07-16 (chat): AI-agent-assisted
  reconciliation for placeholder-bearing files, via a shown prompt or the
  files themselves.
- `AskUserQuestion` responses, 2026-07-16: templated prompt + git reference
  for Tier 2; interactive ask with default-restore plus final per-file report
  for Tier 1 deletions.
- `docs/architecture/adr/0008-template-update-propagation.md` (the decision
  this extends) and `docs/issues/LISS-0001-pull-based-template-update-sync.md`
  (original implementation).

## Work Notes

- 

## Verification

- 
