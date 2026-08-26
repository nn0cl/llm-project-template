# LISS-0019: Delivery route and subagent selection

## Metadata

- Local issue ID: LISS-0019
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/tooling
- Priority: medium
- Initial planning size: L
- Current planning size: L
- Reclassification reason:
- Owner/agent: Codex
- Related branch: process/update-delivery-and-subagent-selection

## Summary

Extend `scripts/update-ai-collaboration-files.sh` so an operator can choose a
GitHub PR route or local branch-review route, choose the local base branch, and
choose whether a provider-neutral subagent handoff is requested.

## Acceptance Notes

1. `--delivery github|local` is supported; omitted values are selected
   interactively in a TTY and default to local without a TTY.
2. `--base-branch BRANCH` selects the local branch from which the sync branch
   is created; an interactive selection is available when omitted.
3. `--no-pr` remains a compatibility alias for local delivery.
4. `--merge-pr` is opt-in, only valid for GitHub delivery, and requests
   auto-merge after required checks pass.
5. `--subagent ask|yes|no` is supported. The script records a provider-neutral
   handoff request but does not select or invoke an LLM provider.
6. Local delivery creates and commits a branch without pushing it or opening a
   PR.
7. GitHub delivery pushes and opens a PR; the PR body records delivery,
   base-branch, and subagent choices.
8. Existing Issue / Spec / ADR / Work Plan / Adjudicator approval units remain
   unchanged.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: ADR 0007, ADR 0008

## Adjudicator Decision Points

- Implementation approved 2026-08-20.
- Provider-specific subagent invocation remains out of scope.

## Context

- Included: `scripts/update-ai-collaboration-files.sh`, branch/PR discipline,
  ADR 0007/0008, and template rollout behavior.
- Omitted: application code, provider SDKs, and automatic subagent execution.
- Assumptions: local branch review means the script commits locally and leaves
  branch selection/review/merge to the operator.

## AI Planning Records

### AIP-0019-001

- Status: accepted
- Created by:
  - Agent/environment: Codex desktop
  - Model as displayed: GPT-5
  - Reasoning setting as displayed: N/A; not exposed
  - N/A reason: environment does not expose the setting
- Created at: 2026-08-20
- Planning size: L
- Intended execution route: shell-script change, docs, and throwaway-target smoke tests
- Intended scope: delivery/base/subagent selection and explicit auto-merge route
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: existing sync script has branching, commit, push, and PR paths
- Assumptions: no provider-specific subagent command is introduced
- Confidence: medium
- Revises:
- Revision reason:
- Superseded by:

## Work Notes

- Implementation completed on the approved process branch.
- Local delivery smoke test passed with `--delivery local --base-branch main
  --subagent yes --non-interactive`.
- GitHub delivery dry-run and invalid `--delivery local --merge-pr` validation
  passed without external publication.
- 2026-08-26: Status synchronized to `done` during LISS-0024 ledger hygiene
  after the work had already merged.

Process review: no remaining open acceptance notes in the merged
implementation. Status was stale after merge and was corrected later.

## Verification

- `bash -n scripts/update-ai-collaboration-files.sh`.
- Throwaway target smoke tests for local delivery and option validation.
- `git diff --check` and repository CI checks remain required before merge.
