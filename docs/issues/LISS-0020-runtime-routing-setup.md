# LISS-0020: Runtime routing setup for review and implementation

## Metadata

- Local issue ID: LISS-0020
- GitHub issue:
- Status: done
- Phase: process-only
- Type: process/tooling
- Priority: medium
- Initial planning size: L
- Current planning size: L
- Reclassification reason:
- Owner/agent: Grok
- Related branch: process/liss-0020-runtime-routing-setup

## Summary

At template adoption, run an interactive setup shell that records how the
adopting project wants agent-to-agent review and implementation to be routed:
same-context review with a dedicated prompt, a separate-context subagent, or
ask-each-time; and optional host-displayed model identifiers for those roles.
The human Adjudicator remains the approval authority. The script does not
call a model, store secrets, or invoke a subagent.

## Acceptance Notes

1. `scripts/configure-ai-collaboration.sh` writes target-owned
   `docs/collaboration/runtime-routing.toml` from
   `docs/templates/runtime-routing.toml`.
2. A TTY asks for review isolation, review model, implementation isolation,
   and implementation model. Flags cover the same fields non-interactively.
   Without a TTY, safe defaults are written: review `same_context`,
   implementation `host`, empty model identifiers.
3. `--force` is required to replace an existing live file.
4. Missing live file preserves current behavior: capability-class routing on
   the host agent, no invented model names.
5. Agent-to-agent review isolation applies only where the process already
   requires an agent review packet. It is not a new mandatory gate and does
   not replace Adjudicator approval.
6. `separate_context` records that the host must launch a subagent with a
   clean context. The template remains provider-neutral and does not invoke
   one.
7. `same_context` uses `docs/templates/same-context-review.md`.
8. ADR 0014 template-sync `--subagent` remains a separate concern.
9. Copy, update, adoption, QUICKSTART, README, CI, and agent contract files
   stay consistent with the new script, policy, and ADR count.
10. The live toml is never copied or overwritten by template sync.

## Dependencies

- Parent:
- Depends on: ADR 0006, ADR 0008, ADR 0014
- Blocks:
- Related: ADR 0001, LISS-0019

## Adjudicator Decision Points

- Architecture and recommended defaults approved 2026-08-26: live file at
  `docs/collaboration/runtime-routing.toml`; new configure script; review
  default `same_context`; implementation default `host`; no new review gate;
  v1 covers review and implementation only; model identifiers are optional
  free text; same-context review is a first-class template.
- Document consistency across contract files, adoption guides, CI, and ADR
  counts is in scope.

## Context

- Included: adoption scripts, agent contracts, review templates, capability
  matrix, ADR 0006/0008/0014, QUICKSTART/README/CI required-file lists.
- Omitted: application code, provider SDKs, API keys, loop-template
  human-absent policy, documentation-language settings, linter setup prompts.
- Assumptions: the host agent or human launches any actual subagent; empty
  model fields mean capability-class routing.

## AI Planning Records

### AIP-0020-001

- Status: accepted
- Created by:
  - Agent/environment: Grok Build
  - Model as displayed: Grok 4.6
  - Reasoning setting as displayed: N/A; not exposed
  - N/A reason: environment does not expose the setting
- Created at: 2026-08-26
- Planning size: L
- Intended execution route: process-only; bash script, docs, contract
  alignment, throwaway-target smoke tests
- Intended scope: adoption-time runtime routing setup and document
  consistency
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: multiple contract surfaces and adoption scripts must
  stay aligned
- Assumptions: no provider SDK; no new mandatory review gate
- Confidence: medium
- Revises:
- Revision reason:
- Superseded by:

## References

- `docs/architecture/adr/0014-delivery-and-subagent-selection.md`
- `docs/collaboration/model-tool-capability-matrix.md`
- `docs/collaboration/adoption-guide.md`

## Work Notes

- Implementation completed on `process/liss-0020-runtime-routing-setup`.
- Copy smoke: live `runtime-routing.toml` is not copied; configure writes it.
- Configure `--non-interactive` writes review `same_context` / implementation
  `host`. A second run without `--force` exits 1. `--force` with explicit
  isolation and model identifiers overwrites as requested. Invalid isolation
  is rejected. `--dry-run` writes nothing.
- Stale current-doc ADR counts (0001-0011) in README/QUICKSTART/CI were
  updated to 0001-0015. `scripts/check-document-lifecycle.py` is now on the
  copy path list so adopter CI matches the shipped workflow.

## Verification

- `bash -n` on configure/copy/update/init scripts: passed.
- Throwaway target copy + configure smoke tests: passed.
- `git diff --check`: passed.
- `python3 scripts/check-document-lifecycle.py`: passed.

Process review: no operating-contract deviation or operational problem found.
