# LISS-0017: Document and trace lifecycle management

## Metadata

- Local issue ID: LISS-0017
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/documentation
- Priority: medium
- Initial planning size: L
- Current planning size: L
- Reclassification reason:
- Owner/agent: Codex
- Related branch: main

## Summary

Adopt a reusable lifecycle for collaboration documents and AI work traces so
current guidance is easy to find without losing historical evidence. Keep
template-owned rules separate from target-owned specifications and decisions.

## Acceptance Notes

1. Document lifecycle rules define `Entry`, `Canonical`, `Evidence`, and
   `Archive`, plus `Current` and `Historical` status.
2. The lifecycle rules define one Canonical document per topic, source
   references, consolidation/archive conditions, and a reversible consolidation
   ledger.
3. Adoption and session-start guidance records Template-owned/Target-owned
   separation and the standard read order.
4. Trace guidance defines representative traces, compression conditions, and a
   Review Summary entry point.
5. A Canonical Register template and Review Summary template are provided.
6. A deterministic check validates register keys, paths, statuses, source
   references, and prevents Archive paths from being declared as Entry or
   Canonical.
7. CI runs the deterministic check without requiring target-specific domain
   documents.
8. No mandatory retention duration, automatic deletion, or target-specific
   deprecated-term catalog is introduced.
9. The Canonical Register and Review Summary are explicitly derived aids and
   do not replace or widen the existing Issue, specification, ADR, Work Plan,
   or Adjudicator approval unit.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: ADR 0008, `docs/collaboration/ai-work-trace-log.md`

## Adjudicator Decision Points

- Architecture approval received 2026-08-19 for the scoped adoption plan.
- Retention periods, deletion automation, and deprecated-term catalogs remain
  target-owned decisions.

## Context

- Included: collaboration lifecycle, adoption, session start, Trace, review,
  Definition of Done, and deterministic repository checks.
- Omitted: application source, target domain specifications, and provider or
  datastore choices.
- Assumptions: adopting projects may place their register at
  `docs/collaboration/canonical-document-register.md` by copying the supplied
  template.

## AI Planning Records

### AIP-0017-001

- Status: accepted
- Created by:
  - Agent/environment: Codex desktop
  - Model as displayed: GPT-5
  - Reasoning setting as displayed: N/A
  - N/A reason: not exposed by this environment
- Created at: 2026-08-19
- Planning size: L
- Intended execution route: documentation and deterministic Python check
- Intended scope: lifecycle policy, register/review templates, Trace and
  session guidance, CI wiring, and verification
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: process-only change with cross-document contract checks
- Assumptions: no target-specific canonical register is populated in this
  template repository
- Confidence: medium
- Revises:
- Revision reason:
- Superseded by:

## Work Notes

- Implementation follows the approved Architecture Path design from
  2026-08-19.
- Final Adjudicator approval received 2026-08-19. Implementation and
  deterministic verification are complete.

## Verification

- `python3 scripts/check-document-lifecycle.py`.
- `bash -n` on changed shell scripts.
- CI required-file and copy smoke checks.
