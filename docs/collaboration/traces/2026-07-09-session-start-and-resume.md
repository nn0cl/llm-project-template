# AI Work Trace

## Request

- Date: 2026-07-09
- User request: Document session start and resume patterns; add minimal Session
  Entry rules to agent operating contract files; push the change.
- Current phase: Architecture Path / process documentation and contract sync.

## Context Ledger

- Included: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/01-quickstart.md`, `docs/architecture/agent-quickstart.md`,
  `docs/collaboration/adoption-guide.md`, `scripts/init-llm-context.sh`,
  `.github/workflows/ci.yml`, prior discussion on init-llm-context.sh limits
  and new-session context loss.
- Omitted: README changes, `init-llm-context.sh --resume` variant, LISS issue
  creation.
- Assumptions: session continuity should be repository-native (handoff, trace,
  issue, spec, branch) rather than chat-memory-based; human how-to belongs in
  collaboration docs, not README.
- Open decisions: none.

## Routing

- Model/assistant/tool: direct documentation edit on Architecture Path.
- Reason: changes agent session-entry behavior across contract files.

## Adjudicator Decisions

- User requested implementation and push.

## Verification

- Commands/checks: confirmed contract files share the same Session Entry
  bullets; CI `required_files` includes the new collaboration document.
- Result: pass (local review).

## Changed Files

- `docs/collaboration/session-start-and-resume.md` (new)
- `docs/collaboration/adoption-guide.md`
- `docs/architecture/agent-quickstart.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.grok/rules/01-quickstart.md`
- `scripts/init-llm-context.sh`
- `.github/workflows/ci.yml`
- `docs/collaboration/traces/2026-07-09-session-start-and-resume.md`

## Expected Behavior Change

- Agents treat each new session as contextless and recover state from cited
  repository artifacts before acting.
- Agents stop after design intake when path, phase, or authoritative scope is
  missing.
- Adjudicators have a single how-to for first adoption session vs daily resume vs
  new task.
- `init-llm-context.sh` remains a first-adoption bootstrap; later sessions
  point to `session-start-and-resume.md`.