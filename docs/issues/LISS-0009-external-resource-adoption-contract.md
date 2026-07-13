# LISS-0009: External resource adoption contract

## Metadata

- Local issue ID: LISS-0009
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/docs
- Priority: medium
- Initial planning size: L
- Current planning size: L
- Reclassification reason: scope generalized 2026-07-13 from a media-artifact-
  specific contract to a general external resource adoption contract, per
  Referee correction; size unchanged (still L) since the document count and
  cross-reference work are comparable, but the design is now more novel
  (no longer reusing a media-specific worked example).
- Owner/agent:
- Related branch: process/external-resource-adoption-contract

## Summary

- Add a standalone, optional architecture document,
  `docs/architecture/external-resource-adoption-contract.md`, covering
  AI-generated artifacts and human-sourced external content/data resources
  (explicitly not software packages/libraries/SDKs, which remain covered by
  `docs/architecture/dependency-policy.md`). It defines:
  - a generic adoption lifecycle so "resource obtained" is never conflated
    with "approved for use"
    (`intake -> checked -> accepted | rejected | needs_recheck`,
    `accepted -> adopted`), with the rule that skipping the check step is
    never acceptable, whether the resource is AI-generated or human-sourced,
    and whether the check is automated or human.
  - a check-record shape (source, what was checked, method, verdict,
    timestamp) as a concrete instance of the existing Output Contract in
    `docs/architecture/io-reasoning-contracts.md`.
  - a statement that concrete check criteria are project-specific, with
    illustrative (not prescriptive) examples across resource types.
  - a tool-vs-human steer (mechanically verifiable -> prefer deterministic
    tool; subjective/intent judgment -> requires human) stated as a general
    rule, not a fixed per-property table.
  - an optional generic "scope" field (e.g. environment/tier/dataset scope)
    so a resource adopted for one scope cannot leak into a production/
    trusted scope for another purpose, without naming any specific content
    category as a template concept.
- Source: same external feedback document as LISS-0008 (2026-07-13).
- **Rescope note (2026-07-13):** this issue originally covered only
  AI-generated binary/media artifacts (images/audio/video), matching the
  feedback's own examples. The Referee reviewed the resulting draft ADR
  0011 and rejected its image-specific vocabulary (orientation, resolution,
  crop, alpha channel) and its deterministic-vs-human table naming those
  same properties. The Referee's stated principle was broader: adoption
  without a recorded check is unacceptable whether the resource is
  AI-generated or human-sourced, and regardless of who performs the check.
  This issue and ADR 0011 were rewritten (and both renamed) to state that
  general principle instead of a media-specific one. See Work Notes for the
  full history.

## Acceptance Notes

- The new document is fully separated from `io-reasoning-contracts.md`,
  `dependency-policy.md`, and `ai-work-trace-log.md` — those documents gain,
  at most, a one-line pointer each. No resource-type-specific vocabulary
  (image, audio, dataset field names, etc.) is added inline to any of them.
  This is deliberate cognitive-load protection for adopters with no
  external/AI-generated-resource workload, not a document-count
  minimization goal.
- The new document lives flat under `docs/architecture/`
  (`docs/architecture/external-resource-adoption-contract.md`), sibling to
  `dependency-policy.md`, matching the template's existing convention for
  optional, domain-specific architecture documents. No new subdirectory.
- The document states its boundary with `dependency-policy.md` explicitly:
  software packages/libraries/SDKs/CLI/test helpers go through
  `dependency-policy.md`; other externally-sourced content/data resources go
  through this document.
- The adoption lifecycle and check-record shape are presented together in
  one document, since they describe the same adopted-resource record from
  two angles (state vs. what was recorded about it).
- The tool-vs-human steer is stated as a general rule (mechanically
  verifiable -> prefer deterministic tool; subjective/intent judgment ->
  requires human; re-verify per project), not a table naming specific
  properties or tools. It points to the verified/inferred/unknown
  compatibility state from ADR 0010/LISS-0008 for whether a given
  deterministic check can actually be trusted.
- Concrete check criteria (e.g. "a project generating images might check
  dimensions and licensing; a project importing datasets might check schema
  and provenance") appear only as clearly-labeled illustrative examples, not
  as required template fields.
- The "scope" field is generic (no domain-specific terms in the template
  itself); an example row may illustrate the concept without making it a
  named first-class category.
- ADR 0011 is the durable record of this decision; the doc work below must
  stay consistent with it.
- Add a line for the new document to CLAUDE.md's Implementation Entry Point
  list, matching the existing per-document reference pattern.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0008, ADR 0002 (input/output/reasoning contracts), ADR 0011,
  `docs/architecture/dependency-policy.md`

## Referee Decision Points

- Resolved 2026-07-13: standalone document at
  `docs/architecture/external-resource-adoption-contract.md`, not an
  extension of `io-reasoning-contracts.md`, `dependency-policy.md`, or
  `ai-work-trace-log.md`. Reason: those documents are read by every adopter
  regardless of whether the project adopts external/AI-generated resources,
  and resource-type-specific vocabulary would be pure noise otherwise.
- Resolved 2026-07-13: ADR 0011
  (`docs/architecture/adr/0011-external-resource-adoption-contract.md`) is
  written and accepted. It explicitly states that it extends ADR 0002 for
  the resources it covers and does not modify ADR 0002 or
  `dependency-policy.md` for anything else.
- Resolved 2026-07-13 (superseding the prior "Open" item): the "scope"
  field is included, generic and optional/illustrative — not a required
  template field, and not tied to any named content category.
- Resolved 2026-07-13: scope generalized from "AI-generated binary/media
  artifacts only" to "AI-generated artifacts and human-sourced external
  content/data resources," explicitly excluding software dependencies
  (already covered by `dependency-policy.md`). See Rescope note above.

## Context

- Included: `docs/architecture/io-reasoning-contracts.md`,
  `docs/architecture/dependency-policy.md`,
  `docs/collaboration/model-tool-capability-matrix.md`,
  `docs/collaboration/evaluation-and-golden-examples.md`,
  `docs/collaboration/ai-work-trace-log.md`,
  `docs/collaboration/definition-of-done.md`, the Referee-supplied external
  feedback document (2026-07-13), the Referee's 2026-07-13 rescope
  correction (chat).
- Omitted: the feedback source repository's game-specific safe-area
  dimensions, adult-content experiment details, and any Studio/provider-
  specific API shapes.
- Assumptions: this extension point must remain entirely optional at the
  template level; a project with no external/AI-generated-resource workload
  should be able to ignore this issue's output entirely.

## AI Planning Records

### AIP-0009-001

- Status: superseded
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-13
- Planning size: L
- Intended execution route: strong reasoning agent for the architecture-
  boundary and scope decisions (new extension point vs. existing-doc
  extension), deterministic search/diff for consistency verification
- Intended scope: extension to `io-reasoning-contracts.md` and/or a new
  linked document, possible short ADR, possible worked-example addition to
  `definition-of-done.md`
- Estimated token range: 12,000-25,000
- Token metric: approximate total model tokens for design intake plus doc
  drafting
- Estimation basis: five feedback items to generalize and consolidate into
  a coherent, optional contract without duplicating ADR 0002's existing
  scope; real uncertainty about final document boundaries
- Assumptions: no application code changes; final size may be reclassified
  to XL if the Referee decides this needs a full new ADR plus a new
  standalone document rather than an extension of existing docs
- Confidence: medium
- Revises:
- Revision reason:
- Superseded by: AIP-0009-002

### AIP-0009-002

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-13
- Planning size: L
- Intended execution route: strong reasoning agent for rewriting ADR 0011
  and this issue to a technology-neutral general adoption-check contract;
  deterministic search/diff for consistency verification and rename
  tracking
- Intended scope: rename and rewrite ADR 0011 and LISS-0009; write
  `external-resource-adoption-contract.md`; add pointers from
  `io-reasoning-contracts.md`, `dependency-policy.md`, and
  `ai-work-trace-log.md`; update CLAUDE.md, architecture README, and CI
  ADR-existence loop
- Estimated token range: 10,000-20,000
- Token metric: approximate total model tokens for the rescope and
  implementation
- Estimation basis: content rewrite of two already-drafted documents plus
  one new document and three pointer edits; lower uncertainty than the
  original estimate since the general principle is now settled
- Assumptions: no application code changes
- Confidence: high
- Revises: AIP-0009-001
- Revision reason: Referee rejected the media-specific draft and specified
  the general adoption-check principle; scope narrowed in novelty even
  though file count is similar
- Superseded by:

## References

- Referee-supplied external feedback document, 2026-07-13 (transcribed in
  chat; not stored as a separate file in this repository).
- `docs/architecture/adr/0002-input-output-reasoning-contracts.md`.
- `docs/architecture/adr/0011-external-resource-adoption-contract.md`.
- `docs/architecture/dependency-policy.md`.

## Work Notes

- Referee agreed on 2026-07-13 to split the feedback into two local issues
  (LISS-0008 and this one) rather than adopting the feedback document
  verbatim.
- Referee ran a second adversarial self-review on 2026-07-13 and surfaced
  three gaps in the (then media-specific) draft: (1) inline extension of
  existing core contract docs would raise cognitive load for non-media
  adopters; (2) a static deterministic-vs-human boundary table naming
  specific tools would go stale; (3) risk of rule conflict with ADR 0002
  without an explicit topology statement. All three were accepted at the
  time.
- Referee then rejected the resulting draft's technology-specific
  vocabulary entirely (2026-07-13) and specified the general principle:
  adoption of any AI-generated or human-sourced external resource requires
  an explicit, recorded check (automated and/or human) before use;
  skipping the check is never acceptable regardless of who is adopting.
  This issue and ADR 0011 were renamed and rewritten accordingly — see the
  Rescope note in Summary and AIP-0009-002.
- Implementation completed 2026-07-13 on branch
  `process/external-resource-adoption-contract`.

## Verification

- New document section-structure sanity check (`grep -n "^## "`) passed for
  `external-resource-adoption-contract.md`.
- Re-read `external-resource-adoption-contract.md` and ADR 0011 for
  leftover technology-specific vocabulary (image/audio/dataset field names
  as required rather than illustrative); none found.
- Local reproduction of CI's "Check required project documents" step
  passed.
- Local reproduction of CI's "Check architecture decision records" step
  passed (0011 resolves).
- Local reproduction of CI's "Check agent operating contract change
  traceability" step passed.
- `git diff --check` passed (no whitespace errors).
- Manually confirmed the new document is reachable from `CLAUDE.md`,
  `docs/architecture/README.md`, `io-reasoning-contracts.md`, and
  `dependency-policy.md`.
