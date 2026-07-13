# Work Plan: External feedback intake (2026-07-13)

## Goal

- Evaluate the 2026-07-13 external feedback document (real-world template
  usage: Studio integration, long-running AI image generation, human review
  of generated artifacts) and incorporate the parts that fit this template's
  intent — stack-neutral, provider-neutral, Referee-gated collaboration
  process — without making any generation-specific dependency a required
  part of the template.

## Scope

- In: closing Gap Register #7 (AI failure and recovery); adding a
  verified/inferred/unknown compatibility concept to the model/tool
  capability matrix; turning existing cost-reduction guidance into a concrete
  optional runner CLI contract; adding an optional generated-artifact
  lifecycle and output-shape contract for projects that produce AI-generated
  media.
- Out: any Studio-specific, image-model-specific, or adult-content-specific
  terminology becoming a named template concept; new mandatory phase gates;
  application code changes (this plan is docs/process only).

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0008 | review | L | L | AIP-0008-001 | - | - | process/ai-failure-recovery-and-runner-cli-contract |
| LISS-0009 | proposed | L | L | AIP-0009-001 | - | - | (not yet created) |

## Recommended Order

1. LISS-0008 (AI failure and recovery procedure) — resolves an already
   tracked Gap Register item, has fewer open design questions.
2. LISS-0009 (generated artifact lifecycle and output contract) — net-new
   optional extension point; benefits from LISS-0008's failure-taxonomy
   vocabulary (e.g. "output retrieval failure") being settled first, though
   it is not a hard dependency.

## Current Next Issue

- Issue: LISS-0009
- Reason it is unblocked: no dependencies; LISS-0008 is implemented and in
  `review` (branch `process/ai-failure-recovery-and-runner-cli-contract`,
  not yet committed/merged).
- Referee approval needed: commit/merge decision for LISS-0008's branch;
  LISS-0009 was rescoped mid-plan (media-artifact-specific ->
  general external resource adoption contract, per Referee correction on
  2026-07-13) and needs its own ADR/issue rewrite before implementation
  starts.

## Risks

- Scope creep back toward Studio/image-generation-specific language if the
  source feedback's examples are copied instead of generalized.
- LISS-0009 fragmenting into too many small documents, raising cognitive
  load contrary to `docs/collaboration/definition-of-done.md`.

## Verification Plan

- Doc-only changes: verify with `git diff --check`, existing CI required-file
  and ADR checks (per the pattern used for LISS-0007), and a manual
  cross-reference check that every new/edited document is reachable from
  CLAUDE.md's Implementation Entry Point list.
