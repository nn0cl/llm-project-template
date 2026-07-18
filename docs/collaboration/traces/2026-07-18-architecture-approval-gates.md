# Architecture approval and reassessment gates

## Request

- Date: 2026-07-18
- User request: Incorporate common feedback about scope approval, architecture
  reassessment, bounded multi-Issue execution, and CI-only validation.
- Current phase: process-only / Architecture Path
- Canonical issue or work plan: LISS-0017 / WP-0002
- AI planning record: AIP-0017-001

## Context Ledger

- Included: `AGENTS.md`, `CLAUDE.md`, Copilot/Grok/Cursor entry points,
  `docs/architecture/agent-quickstart.md`, `docs/at-tdd/process.md`, review
  and design templates, `docs/collaboration/ai-human-scheme.md`, Definition of
  Done, current CI workflow, and the execution-batch proposal.
- Omitted: Hooks, application code, target-project ADRs and private session
  logs, and any provider-specific enforcement.
- Assumptions: `AGENTS.md` is the common contract source; CI validates records
  but does not authenticate human approval; Hook changes remain out of scope.
- Open decisions: whether the execution-batch JSON shape should later be
  extended, and which low-risk categories adopters select in their own records.

## Routing

- Model/assistant/tool: Codex with deterministic repository inspection and
  standard-library Python validation
- Reason: cross-agent contract alignment and a stack-neutral CI check
- Privacy constraints: no secrets, private exports, or target-project source
  used

## Adjudicator Decisions

- Use `AGENTS.md` as the shared approval and design-check source.
- Rename `[THOUGHT]` to `[DESIGN CHECK]` across common agent surfaces.
- Add typed approval and bounded execution-batch guidance.
- Introduce CI-only review-record validation; do not add Hooks.
- Permit post-review status only as a human review transition in the contract;
  CI checks record consistency but does not manufacture approval.

## Execution

- Updated common agent entry points and process/templates with the design-check
  and approval vocabulary.
- Added `docs/templates/execution-batch-review.md`.
- Added `scripts/check-execution-batch-reviews.py` using only the Python
  standard library.
- Added the validator to `.github/workflows/ci.yml` and the template path list;
  matching `batch/<batch-id>` branches are checked from their approval commit
  against the declared allowed paths.
- Synchronized LISS-0017 and WP-0002 to the in-progress branch.

## Verification

- `git diff --check`: passed.
- Validator against the current repository with no execution-batch records:
  passed.
- Shell syntax checks: passed.
- Template copy smoke and `init-llm-context.sh` checks: passed.
- Exact legacy `[THOUGHT]` label check across normative surfaces: passed.
- Batch branch/path binding: implemented; no live batch record exists in this
  repository, so the validator's empty-record path was exercised locally.
- Full repository CI-equivalent checks: local checks passed; hosted CI remains
  pending the pull request.

## Changed Files

- Common agent entry points and process documents listed in the branch diff.
- `.github/workflows/ci.yml`
- `scripts/check-execution-batch-reviews.py`
- `docs/templates/execution-batch-review.md`
- `scripts/lib/collaboration-template-paths.sh`
- `docs/issues/LISS-0017-architecture-approval-and-reassessment-gates.md`
- `docs/work-plans/WP-0002-architecture-approval-and-reassessment.md`

## Next Safe Action

- Run the full deterministic validation suite, inspect the cross-agent diff,
  and request Adjudicator review before merge.
