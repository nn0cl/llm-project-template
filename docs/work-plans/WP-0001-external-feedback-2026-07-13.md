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
  optional runner CLI contract; adding an optional external resource
  adoption contract (AI-generated artifacts and human-sourced external
  content/data resources) covering the intake-check-adopt lifecycle.
- Out: any Studio-specific, image-model-specific, or adult-content-specific
  terminology becoming a named template concept; new mandatory phase gates;
  application code changes (this plan is docs/process only); software
  dependency adoption (already covered by `dependency-policy.md`).

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0008 | review | L | L | AIP-0008-001 | - | - | process/ai-failure-recovery-and-runner-cli-contract |
| LISS-0009 | review | L | L | AIP-0009-002 (revises AIP-0009-001) | - | - | process/external-resource-adoption-contract |

## Recommended Order

1. LISS-0008 (AI failure and recovery procedure) — resolves an already
   tracked Gap Register item, has fewer open design questions. Implemented
   and committed to its branch 2026-07-13.
2. LISS-0009 (external resource adoption contract) — net-new optional
   extension point; was rescoped mid-plan from a media-artifact-specific
   contract to a general adoption-check principle after Referee review
   rejected technology-specific vocabulary. Implemented 2026-07-13.

## Current Next Issue

- Issue: none — both issues implemented and in `review` on their own
  branches, neither committed changes merged to `main` yet.
- Referee approval needed: commit/merge decision for both branches. Note
  that `CLAUDE.md`, `docs/architecture/README.md`'s Accepted Decisions list,
  and `.github/workflows/ci.yml`'s ADR-existence loop were each edited
  independently on both branches (Part 1 added its lines/ADR 0010; Part 2
  added its lines/ADR 0011); expect a small, easily-resolved conflict on
  `ci.yml`'s single-line loop, and a possible `WP-0001` "both added"
  conflict for this file itself, when merging the two branches into `main`
  in sequence.

## Risks

- Scope creep back toward Studio/image-generation-specific language if the
  source feedback's examples are copied instead of generalized. Caught once
  already mid-plan (LISS-0009's original media-specific draft) and
  corrected.
- LISS-0009 fragmenting into too many small documents, raising cognitive
  load contrary to `docs/collaboration/definition-of-done.md`. Avoided by
  keeping the adoption lifecycle and check-record shape in one document.

## Verification Plan

- Doc-only changes: verify with `git diff --check`, local reproduction of
  CI's required-file, ADR-existence, and contract-traceability checks (run
  for both branches, see each issue's Verification section), and a manual
  cross-reference check that every new document is reachable from
  CLAUDE.md's Implementation Entry Point list.
- Confirmed both branches' new documents contain no leftover
  technology-specific vocabulary presented as a template requirement.
