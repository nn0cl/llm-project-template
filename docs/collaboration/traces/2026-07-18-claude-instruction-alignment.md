# Claude instruction alignment

## Request

- Date: 2026-07-18
- User request: Adjust only the Claude-specific response contract and reading sequence because other agents are operating correctly.
- Current phase: Architecture Path / instruction change
- Canonical issue or work plan: N/A; explicit Adjudicator scope
- AI planning record: This trace

## Context Ledger

- Included: `CLAUDE.md`, `AGENTS.md`, `docs/architecture/agent-quickstart.md`, `docs/architecture/io-reasoning-contracts.md`, `docs/collaboration/prompt-instruction-change-control.md`
- Omitted: Hooks, CI enforcement, phase-state files, and all non-Claude agent entry points
- Assumptions: Claude Code continues to import `AGENTS.md`; the change is limited to Claude-specific presentation and reading order
- Open decisions: Whether later evidence warrants Claude-specific hooks or deterministic gates

## Routing

- Model/assistant/tool: Codex with deterministic repository inspection
- Reason: Instruction-contract review and narrow documentation edit
- Privacy constraints: No private data, secrets, or external project context used

## Execution

- Result: Updated the Claude-only design-check wording and fixed Claude Code reading sequence. Shared `AGENTS.md` and other agent entry points were not changed.

## Cost / Reasoning Control

- Operating path: Architecture Path
- Files read: Listed in Context Ledger
- Context intentionally omitted: Application source, feature specifications, hooks, and CI implementation
- Deterministic checks used: Repository search, diff inspection, and `git diff --check`
- Escalation reason: None
- Avoided LLM work: No implementation or hook design was attempted

## Adjudicator Decisions

- Apply candidate 1: replace `[THOUGHT]` / reasoning wording with auditable design-check wording.
- Apply candidate 2: make the Claude Code reading sequence explicit.
- Do not change shared agent contracts or add enforcement machinery.

## Verification

- Commands/checks: `rg`, `git diff --check`, inspection of `CLAUDE.md` and changed-file diff
- Result: `git diff --check` passed; old `[THOUGHT]` and `reasoning evidence` labels are absent from `CLAUDE.md`; `AGENTS.md` and other agent entry points remain unchanged.

## Changed Files

- `CLAUDE.md`
- `docs/collaboration/traces/2026-07-18-claude-instruction-alignment.md`

## Next Safe Action

- Review the Claude-only diff and run the deterministic checks recorded above.
