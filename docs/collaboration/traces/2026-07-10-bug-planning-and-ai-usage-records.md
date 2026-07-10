# AI Work Trace: Bug Planning and AI Usage Records

## Request

- Date: 2026-07-10
- User request: incorporate project feedback about bug planning, planning
  sizes, and AI planning/execution usage records.
- Current phase: process-only Architecture Path
- Canonical issue or work plan: `docs/issues/LISS-0007-bug-planning-and-ai-usage-records.md`
- AI planning record: `AIP-0007-001`

## Context Ledger

- Included: `AGENTS.md`, agent quickstart, adoption guide, local issue
  planning, work and issue templates, AI work trace policy/template, LLM cost
  policy, Definition of Done, process gap register, bug report template,
  related ADRs, and CI documentation checks.
- Omitted: application source code, stack-specific pricing, provider billing
  exports, and unrelated feature specifications.
- Assumptions: this task is a collaboration-process change, not an application
  behavior change; token usage records are planning evidence, not billing
  records.
- Open decisions: none after Referee approval on 2026-07-10.

## Routing

- Model/assistant/tool: Codex desktop with deterministic repository tools.
- Reason: cross-document process change with architectural contract impact.
- Privacy constraints: no secrets, provider logs, private prompts, or billing
  exports were used.

## AI Execution Records

Use one record per cohesive execution attempt. Do not combine token values
across attempts unless the optional reference total below explicitly states
that the metric, source, and attribution boundary are compatible.

### Attempt 1

- Agent: Codex
- Environment: Codex desktop
- Model as displayed: GPT-5 (agent identity supplied by the environment)
- Reasoning setting as displayed: N/A
- Token usage: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: task-only value unavailable
- N/A reason: this environment does not expose a stable per-task token usage
  value or reasoning-setting label to the agent.
- Scope: bug planning policy, AI planning records, AI execution records, and
  related template/trace/cost/quickstart/DoD documentation.
- Result: completed and verified.
- Attempt boundary: initial execution attempt after Referee approval.
- Notes: deterministic checks will be recorded below.

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: no compatible reference total is available.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: agent contract, quickstart, adoption guide, collaboration
  policies, templates, ADRs, CI workflow, and GitHub bug template.
- Context intentionally omitted: application implementation and unrelated
  feature specs.
- Deterministic checks used: `rg`, `sed`, `git status`, `git diff --check`,
  YAML parsing, CI contract-file check, and documentation consistency search.
- Escalation reason: accepted collaboration rules and templates changed across
  multiple process documents.
- Avoided LLM work: used repository search and local diffs for factual checks.
- Rework caused by AI output: none.

## Referee Decisions

- 2026-07-10: bug fixes may not skip phases; a minor bug can only omit a
  separate planning artifact when it remains one-attempt size `S` and already
  falls within approved scope.
- 2026-07-10: AI planning estimates must be vendor-neutral and readable by
  other AI agents.
- 2026-07-10: AI planning and execution records are required for size `M` or
  larger work, and for second or later attempts.

## Verification

- Commands/checks: `git diff --check`; Ruby YAML parse for
  `.github/workflows/ci.yml` and `.github/ISSUE_TEMPLATE/bug_report.md`; local
  reproduction of CI required-file and ADR checks; local reproduction of the
  contract-change trace check.
- Result: passed.

## Changed Files

- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/workflows/ci.yml`
- `docs/architecture/README.md`
- `docs/architecture/adr/0009-bug-planning-and-ai-usage-records.md`
- `docs/architecture/agent-quickstart.md`
- `docs/collaboration/ai-work-trace-log.md`
- `docs/collaboration/definition-of-done.md`
- `docs/collaboration/llm-cost-reduction.md`
- `docs/collaboration/local-issue-planning.md`
- `docs/collaboration/process-gap-register.md`
- `docs/collaboration/traces/2026-07-10-bug-planning-and-ai-usage-records.md`
- `docs/issues/LISS-0007-bug-planning-and-ai-usage-records.md`
- `docs/templates/ai-work-trace.md`
- `docs/templates/local-issue.md`
- `docs/templates/work-plan.md`

## Next Safe Action

- Referee review, then commit or open a PR from
  `codex/process/bug-ai-planning-records`.

## Notes

- Existing untracked `.idea/` files were treated as user-owned and left
  untouched.
