# LISS-0022: Project conventions file and overwritable context files

## Metadata

- Local issue ID: LISS-0022
- GitHub issue:
- Status: in_progress
- Phase: process-only
- Type: process/tooling
- Priority: high
- Initial planning size: L
- Current planning size: L
- Owner/agent: Grok
- Related branch: process/liss-0022-project-conventions

## Summary

Keep project-specific facts and extra rules in a target-owned conventions
file. Make template context files overwriteable on template update. Instruct
every agent to read the conventions file.

## Acceptance Notes

1. Live file `docs/collaboration/project-conventions.md` is created from
   `docs/templates/project-conventions.md` on copy when missing, and is never
   overwritten by copy or update.
2. Template context files no longer hold project name, stack, ports,
   boundaries, or extra project rules. They tell agents to read the
   conventions file.
3. Update treats those context files as template-authoritative overwrite.
   Tier 2 AI-assisted merge for persona files is retired.
4. Unfilled placeholders that a task relies on, including in the conventions
   file, still stop the agent.
5. Adoption and sync docs tell existing adopters to move facts out of
   context files before merging an overwrite.

## Dependencies

- Related: ADR 0008, ADR 0017

## Adjudicator Decision Points

- Implementation requested 2026-08-26.

## Context

- Included: persona files, copy/update scripts, adoption-guide, architecture
  README placeholders.
- Omitted: application code, provider SDKs.
- Assumptions: a sync PR remains the review gate for the first overwrite
  after migration.

## AI Planning Records

### AIP-0022-001

- Status: accepted
- Created by:
  - Agent/environment: Grok Build
  - Model as displayed: Grok 4.6
  - Reasoning setting as displayed: N/A; not exposed
  - N/A reason: environment does not expose the setting
- Created at: 2026-08-26
- Planning size: L
- Intended execution route: process-only
- Intended scope: conventions file, overwriteable context files, copy/update
- Estimated token range: N/A
- Token metric: N/A
- Estimation basis: contract surfaces and sync script
- Confidence: medium

## References

- `docs/architecture/adr/0017-project-conventions-file.md`

## Verification

- Throwaway copy creates `project-conventions.md` and fills name/stack flags:
  passed.
- Copy does not leave PROJECT_NAME placeholders in template context files:
  passed.
- Second copy does not overwrite an existing conventions file: passed.
- `bash -n` and `git diff --check`: passed.
