# LISS-0025: Move selected procedures into Agent Skills

## Metadata

- Local issue ID: LISS-0025
- GitHub issue:
- Status: in_progress
- Phase: process-only
- Type: process/docs
- Priority: high
- Initial planning size: M
- Current planning size: M
- Owner/agent: Grok
- Related branch: process/liss-0025-agent-skills

## Summary

Move four existing on-demand procedures out of always-loaded contract files
into Agent Skills under `.agents/skills/`. Keep Canonical policy documents
and standing rules in place. Contract files keep the obligation and a path.

## Acceptance Notes

1. Skills exist at `.agents/skills/{design-intake,process-review,same-context-review,agent-handoff}/SKILL.md` using the Agent Skills `name` and `description` frontmatter only.
2. The `[DESIGN CHECK]` scaffold lives in the design-intake skill, not in `AGENTS.md` / `CLAUDE.md` / Copilot / Grok / Cursor rule bodies.
3. Contract files still require design intake, process review, same-context review, and handoff, and name the skill path so hosts that do not auto-discover `.agents/skills/` still load it.
4. Canonical policy remains `docs/collaboration/process-review.md` and the existing templates. Skills point at those files; they do not become a second source of truth.
5. Standing rules stay in the contract files: Prime Directive, Session Entry, Approval Model, ports, phase gates.
6. Copy and update treat `.agents/skills/` as template-authoritative. CI requires the four `SKILL.md` files. The files are on the operating-contract list.
7. No vendor-specific skill copies (`.claude/skills`, `.cursor/skills`, `.github/skills`).

## Dependencies

- Related: ADR 0006, ADR 0015, ADR 0016, ADR 0018

## Adjudicator Decision Points

- Implementation requested 2026-08-26: select existing procedures and move them into Skills.

## Context

- Included: contract files, copy/CI, adoption and lifecycle pointers.
- Omitted: application code, vendor hooks, custom agent profiles, Grok workflows, MCP.
- Assumptions: hosts that auto-load `.agents/skills/` get progressive disclosure; others follow the path in the contract files.

## AI Planning Records

### AIP-0025-001

- Status: accepted
- Created by:
  - Agent/environment: Grok Build
  - Model as displayed: Grok 4.6
  - Reasoning setting as displayed: N/A; not exposed
  - N/A reason: environment does not expose the setting
- Created at: 2026-08-26
- Planning size: M
- Intended execution route: process-only
- Intended scope: four skills, contract pointers, copy/CI/adoption
- Estimated token range: N/A
- Token metric: N/A
- Estimation basis: document and path-list alignment
- Confidence: high

## References

- `docs/architecture/adr/0018-agent-skills-for-on-demand-procedures.md`

## Verification

- Copy smoke includes the four skills and excludes LISS/WP traces.
- CI required-files and ADR 0018 existence.
- `rg` shows no `[DESIGN CHECK]` fenced scaffold in AGENTS.md or CLAUDE.md.
- `git diff --check`.
