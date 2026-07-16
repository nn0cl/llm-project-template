# AI Work Trace

## Request

- Date: 2026-07-17
- User request: replace the uniform 3-way merge in
  `scripts/update-ai-collaboration-files.sh` with a tiered policy -- most
  template files fully template-authoritative (hash differs -> overwrite),
  except a named subset (the agent persona/contract files) that should be
  handed to an AI agent to reconcile instead of merged or overwritten.
- Current phase: process-only (tooling + docs), Architecture Path (extends
  ADR 0008; adds a new `docs/templates/*.md` contract file).
- Canonical issue or work plan:
  `docs/issues/LISS-0016-tiered-template-sync-policy.md`.
- AI planning record: AIP-0016-001 (in the issue above).

## Context Ledger

- Included: `scripts/update-ai-collaboration-files.sh`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`,
  `docs/architecture/adr/0008-template-update-propagation.md`,
  `docs/collaboration/adoption-guide.md`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `.github/workflows/ci.yml`.
- Omitted: application source (none exists in this template repository);
  unrelated CI jobs.
- Assumptions: this is a template-repository-only tooling change; verified
  with a throwaway local target repository rather than a real adopter
  repository, since none is available in this session.

## Routing

- Model/assistant/tool: Claude Code CLI, direct shell-script editing plus a
  local throwaway-repo smoke test (deterministic verification, no AI
  reasoning needed for the shell logic itself).
- Reason: Architecture Path work extending ADR 0008 and adding a new
  contract-file template.
- Privacy constraints: none.

## AI Execution Records

### Attempt 1

- Agent: Claude Code CLI
- Environment: Claude Code CLI (claude-sonnet-5)
- Model as displayed: Claude Sonnet 5
- Reasoning setting as displayed: N/A
- Estimated token range: 12,000-20,000 (per AIP-0016-001)
- Estimated token midpoint: 16,000
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not exposed by this environment's output.
- Estimate variance: N/A
- Variance reason: N/A
- Scope: add a Tier 2 persona/contract-file classification; rewrite the sync
  script's merge decision into overwrite (Tier 1) / needs-AI-merge (Tier 2) /
  interactive-default-restore (deletions, either tier); replace the summary
  and PR-body reporting; add `docs/templates/contract-file-sync-prompt.md`;
  extend ADR 0008; update the adoption guide and CI required-files list;
  verify with a throwaway local target repository.
- Result: completed; see Verification for what was and was not exercised.
- Attempt boundary: single cohesive execution across one chat session.
- Notes: two design points were resolved via `AskUserQuestion` before
  implementation: the Tier 2 mechanism (durable prompt template + `git show`
  references, not a generated throwaway prompt file) and Tier 1 deletion
  handling (interactive ask, default restore, explicit per-file outcome
  report).

## Optional Reference Total

- Value:
- Metric:
- Source:
- Compatibility statement:

## Cost / Reasoning Control

- Operating path: Architecture Path (extends ADR 0008; new contract file).
- Files read: `scripts/update-ai-collaboration-files.sh`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`, ADR 0008, adoption-guide.md,
  prompt-instruction-change-control.md, `.github/workflows/ci.yml`.
- Context intentionally omitted: none beyond application source (none exists
  in this repository).
- Deterministic checks used: `bash -n` on the edited script; a throwaway
  local git repository exercising the copy script, a simulated Tier 1
  customization+deletion, a simulated Tier 2 both-sides-changed conflict, and
  a template addition, run through the update script in both
  `--non-interactive` and piped-interactive-input modes.
- Escalation reason: none.
- Avoided LLM work: none.
- Rework caused by AI output: none.

## Referee Decisions

- 2026-07-16/17 (chat): adopt a tiered sync policy; Tier 1 =
  fully-template-authoritative, Tier 2 = the five persona/contract files,
  reconciled via AI assistance instead of merged or overwritten.
- 2026-07-16/17 (via `AskUserQuestion`): Tier 2 mechanism = templated prompt +
  `git show` references; Tier 1 (and, as implemented, either tier's)
  deletion handling = interactive ask with default-restore, plus a final
  per-file outcome report.

## Verification

- Commands/checks: `bash -n scripts/update-ai-collaboration-files.sh`.
- Throwaway-repo smoke test (see Work Notes for the exact scenarios and
  observed output) exercising: Added, Updated, Overwritten (Tier 1
  customization discarded), NEEDS AI-ASSISTED MERGE (Tier 2 both changed),
  Restored / Kept deleted (interactive and `--non-interactive` paths),
  Ignored, and Number Collision.
- Result: recorded in Work Notes in the local issue.

## Changed Files

- `scripts/lib/collaboration-template-paths.sh`
- `scripts/update-ai-collaboration-files.sh`
- `docs/templates/contract-file-sync-prompt.md`
- `docs/architecture/adr/0008-template-update-propagation.md`
- `docs/collaboration/adoption-guide.md`
- `.github/workflows/ci.yml`
- `docs/issues/LISS-0016-tiered-template-sync-policy.md`
- `docs/collaboration/traces/2026-07-17-tiered-template-sync-policy.md` (this
  file)

## Next Safe Action

- Open a PR for branch `process/tiered-template-sync` once the Adjudicator
  confirms the smoke-test results are sufficient (contract file changed; PR
  review cannot be AI self-review alone, per
  `prompt-instruction-change-control.md`).

## Notes

- `copy-ai-collaboration-files.sh` (the initial-adoption script) was not
  changed; only the later-sync script's merge/overwrite/deletion behavior
  changed.
