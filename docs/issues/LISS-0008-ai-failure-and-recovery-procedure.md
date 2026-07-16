# LISS-0008: AI failure and recovery procedure

## Metadata

- Local issue ID: LISS-0008
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/docs
- Priority: high
- Initial planning size: L
- Current planning size: L
- Reclassification reason:
- Owner/agent:
- Related branch: process/ai-failure-recovery-and-runner-cli-contract

## Summary

- Resolve Gap Register #7 (AI Failure and Recovery Procedure, currently
  `Status: future`) with a generalized, provider-neutral recovery procedure,
  and extend two existing documents that the same external feedback showed
  are incomplete in practice:
  - `docs/collaboration/model-tool-capability-matrix.md`: add a
    verified/inferred/unknown compatibility state so routing decisions do not
    silently assume an unverified provider/model/tool configuration.
  - new `docs/collaboration/runner-cli-contract.md`: net-new, optional
    guidance (not a refinement of any existing text — `llm-cost-reduction.md`
    currently has no slow-job or detach/resume guidance at all) motivated by
    `llm-cost-reduction.md`'s existing cost-reduction goal, defining a
    concrete runner CLI contract (plan/detach/status/resume/dedupe, plus a
    run-state model covering an `unconfirmed` state for unresolved provider
    idempotency) for any slow external job, not only AI image generation.
    `llm-cost-reduction.md` keeps only a short pointer to it.
- Source: external feedback document supplied by the Adjudicator via chat on
  2026-07-13, based on real usage of this template outside this repository
  (Studio integration, long-running generation jobs). The template's own
  files were not changed by that feedback; this issue is where it gets
  evaluated and, where accepted, incorporated.

## Acceptance Notes

- New `docs/collaboration/ai-failure-recovery.md` classifies failures into at
  least: input contract, provider connection, workflow/tool compatibility,
  output retrieval, and human review — without naming any specific commercial
  provider, model, or generation tool.
- The document defines: last-trusted-artifact concept, a resumable
  experiment/run identifier, what changed between attempts, and resume
  conditions, generalized from (not copied from) the feedback's image-specific
  example.
- Resume/dedupe guidance states that re-running a job adds only unreviewed
  candidates; records that already carry a human verdict (accepted/rejected)
  are never deleted or silently overwritten.
- Resume guidance distinguishes local record-level dedup (candidates are not
  duplicated) from provider-level request idempotency (the same job is not
  resubmitted to the provider a second time). A run whose last submission's
  outcome cannot be confirmed enters an explicit `unconfirmed` state, distinct
  from `completed`/`failed`. Automatic resume from `unconfirmed` is allowed
  only when the provider's idempotency-key or safe-retry support is `verified`
  in the model/tool capability matrix (see the compatibility-state work in
  this same issue); when it is `inferred` or `unknown`, the run pauses for a
  human decision instead of auto-resubmitting.
- Each of the five failure categories includes one short example error
  pattern, and the document states a tie-break rule for the input-contract
  vs. workflow/tool-compatibility boundary: if the caller's input is
  unchanged but the provider/tool's acceptance criteria changed, classify as
  workflow/tool compatibility; if the caller's input violates its own
  declared input contract, classify as input contract violation.
- Gap Register entry #7 in `docs/collaboration/process-gap-register.md` is
  updated from `Status: future` to `Status: resolved` with a resolution
  pointer, consistent with how gaps #1-6, #8-10 are already written.
- `docs/collaboration/model-tool-capability-matrix.md` gains a
  verified/inferred/unknown compatibility concept applied to the existing
  capability classes/routing table, not a parallel new table.
- New `docs/collaboration/runner-cli-contract.md`, explicitly scoped to
  "projects that run slow external AI jobs" so it does not become a mandatory
  requirement for template adopters that have no such workload;
  `llm-cost-reduction.md` links to it instead of absorbing it.
- No new document assumes a specific target stack, image/generation
  dependency, or commercial provider (per `docs/collaboration/
  template-benefits.md`: the template does not choose target stack, datastore,
  provider, or LLM).
- ADR 0010 is the durable record of this decision; the doc work below must
  stay consistent with it.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0009, Gap Register #7, ADR 0010

## Adjudicator Decision Points

- Resolved 2026-07-13: yes, ADR 0010 (`docs/architecture/adr/
  0010-ai-failure-recovery-and-runner-cli-contract.md`) is written and
  accepted, covering the failure taxonomy, the `unconfirmed` run state, the
  capability-matrix compatibility state, and the runner CLI contract split.
- Resolved 2026-07-13: the five failure category names and the
  input-contract/workflow-compatibility tie-break rule are fixed as written
  in ADR 0010 and in this issue's Acceptance Notes.
- Resolved 2026-07-13: the runner CLI contract is its own document,
  `docs/collaboration/runner-cli-contract.md`, not a subsection of
  `llm-cost-reduction.md`. Reason: the CLI contract (plan/detach/status/
  resume/dedupe, idempotency handling, run-state model) changes for reasons
  unrelated to cost-reduction policy, and coupling the two would make either
  document's edit history noisy for the other concern.
  `llm-cost-reduction.md` keeps only a short pointer to it.

## Context

- Included: `docs/collaboration/process-gap-register.md`,
  `docs/collaboration/model-tool-capability-matrix.md`,
  `docs/collaboration/llm-cost-reduction.md`,
  `docs/collaboration/template-benefits.md`, the Adjudicator-supplied external
  feedback document (2026-07-13).
- Omitted: the feedback source repository's internal experiment data,
  provider-specific (Studio) configuration details, application-internal
  design of the source project.
- Assumptions: the failure-recovery procedure and runner CLI contract must
  stay usable by a project with no AI-generated-media workload at all; both
  are additive/optional guidance, not new mandatory gates.

## AI Planning Records

### AIP-0008-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-13
- Planning size: L
- Intended execution route: strong reasoning agent for the design/boundary
  decisions, deterministic search/diff for verifying doc consistency
- Intended scope: new `ai-failure-recovery.md`, edits to
  `process-gap-register.md`, `model-tool-capability-matrix.md`,
  `llm-cost-reduction.md`, possible new ADR, possible reference line added to
  `CLAUDE.md`'s Implementation Entry Point list
- Estimated token range: 12,000-25,000
- Token metric: approximate total model tokens for design intake plus doc
  drafting
- Estimation basis: four to six documents touched, generalization work to
  strip source-specific (Studio/image) details, plus Gap Register status
  change
- Assumptions: no application code changes; no new ADR template needed
  (existing `docs/templates/adr.md` is reused if an ADR is written)
- Confidence: medium
- Revises:
- Revision reason:
- Superseded by:

## References

- Adjudicator-supplied external feedback document, 2026-07-13 (transcribed in
  chat; not stored as a separate file in this repository).
- `docs/collaboration/process-gap-register.md` gap #7.
- `docs/architecture/adr/0010-ai-failure-recovery-and-runner-cli-contract.md`.

## Work Notes

- Adjudicator agreed on 2026-07-13 to split the feedback into two local issues
  (this one and LISS-0009) rather than adopting the feedback document
  verbatim.
- Adjudicator ran an adversarial self-review on 2026-07-13 and surfaced three
  gaps in the initial design intake: (1) missing provider-level idempotency
  handling on resume, distinct from local record dedup; (2) the runner CLI
  contract outgrowing `llm-cost-reduction.md`'s scope; (3) ambiguity at the
  input-contract/workflow-compatibility failure-category boundary. All three
  were accepted and folded into Acceptance Notes and Adjudicator Decision Points
  above; see the `unconfirmed` run state, the new standalone
  `runner-cli-contract.md`, and the classification tie-break rule.
- Implementation completed 2026-07-13 on branch
  `process/ai-failure-recovery-and-runner-cli-contract`: both new documents
  written, Gap Register #7 resolved, capability matrix and cost-reduction
  docs updated, CLAUDE.md/architecture README/CI updated, trace added. See
  `docs/collaboration/traces/2026-07-13-ai-failure-recovery-and-runner-cli-contract.md`.

## Verification

- New document section-structure sanity check (`grep -n "^## "`) passed for
  `ai-failure-recovery.md` and `runner-cli-contract.md`.
- Local reproduction of CI's "Check required project documents" step
  passed.
- Local reproduction of CI's "Check architecture decision records" step
  passed (0010 resolves).
- Local reproduction of CI's "Check agent operating contract change
  traceability" step passed (`contract_changed=true`, `trace_added=true`).
- `git diff --check` passed (no whitespace errors).
- Manually confirmed `ai-failure-recovery.md` and `runner-cli-contract.md`
  are reachable from `CLAUDE.md`, `docs/architecture/README.md`, and
  `docs/collaboration/process-gap-register.md`/`llm-cost-reduction.md`.
