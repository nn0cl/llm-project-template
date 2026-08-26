# AI Work Trace

## Request

- Date: 2026-08-26
- User request: select existing features and move them into Skills.
- Current phase: process-only, Architecture Path implementation.
- Canonical issue or work plan:
  `docs/issues/LISS-0025-agent-skills-procedures.md`.
- AI planning record: AIP-0025-001 in the issue above.

## Context Ledger

- Included: contract files, four existing procedures, copy/CI, adoption and
  lifecycle pointers, Agent Skills spec.
- Omitted: application source, vendor hooks, custom agent profiles, Grok
  workflows, MCP, duplicate skill trees under `.claude/skills` or
  `.cursor/skills`.
- Assumptions: hosts that do not auto-discover `.agents/skills/` follow the
  path in the contract files. Canonical policy documents remain the source
  of truth.
- Open decisions: none. Session-start document lists stay in the contract
  files except for the moved scaffolds.

## Routing

- Model/assistant/tool: Grok Build for documentation; copy smoke, ripgrep,
  and repository CI for deterministic verification.
- Reason: process/docs alignment with no application runtime.
- Privacy constraints: no secrets, private exports, or adopter data.

## AI Execution Records

### Attempt 1

- Agent: Grok Build
- Environment: Grok Build
- Model as displayed: Grok 4.6
- Reasoning setting as displayed: N/A; not exposed.
- Actual tokens: N/A; not exposed.
- Scope: four skills under `.agents/skills/`; ADR 0018; contract pointers;
  copy path; CI required files and trace glob; adoption and lifecycle
  notes. Standing rules (Prime Directive, Session Entry, Approval Model)
  stay in contract files.
- Result: completed; verification recorded below.

## Adjudicator Decisions

- 2026-08-26: move selected existing procedures into Skills.

## Verification

- Commands/checks:
  - no `[DESIGN CHECK]` fenced scaffold in AGENTS.md or CLAUDE.md
  - four `SKILL.md` files present
  - copy smoke includes skills and excludes LISS/traces
  - `git diff --check`
  - repository CI
- Result: recorded with the implementing PR.

## Changed Files

- `.agents/skills/design-intake/SKILL.md`
- `.agents/skills/process-review/SKILL.md`
- `.agents/skills/same-context-review/SKILL.md`
- `.agents/skills/agent-handoff/SKILL.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.grok/rules/01-quickstart.md`
- `.grok/rules/03-collaboration-and-completion.md`
- `.cursor/rules/01-quickstart.mdc`
- `.cursor/rules/03-collaboration-and-completion.mdc`
- `docs/architecture/adr/0018-agent-skills-for-on-demand-procedures.md`
- `docs/issues/LISS-0025-agent-skills-procedures.md`
- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/collaboration/adoption-guide.md`
- `docs/collaboration/document-lifecycle.md`
- `docs/collaboration/session-start-and-resume.md`
- `docs/collaboration/runtime-routing.md`
- `docs/collaboration/definition-of-done.md`
- `docs/architecture/agent-quickstart.md`
- `docs/architecture/README.md`
- `docs/at-tdd/process.md`
- `scripts/lib/collaboration-template-paths.sh`
- `.github/workflows/ci.yml`
- `docs/collaboration/traces/2026-08-26-agent-skills-procedures.md`

## Next Safe Action

Adjudicator review and merge of `process/liss-0025-agent-skills`. After
merge, mark LISS-0025 `done` and run the process-review skill.
