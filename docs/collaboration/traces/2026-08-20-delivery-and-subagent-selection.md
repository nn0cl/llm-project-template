# AI Work Trace

## Request

- Date: 2026-08-20
- User request: let the template deployment/update script choose GitHub PR
  publication or local branch review, and choose whether a subagent is
  requested.
- Current phase: process-only, Architecture Path implementation after approval.
- Canonical issue or work plan:
  `docs/issues/LISS-0019-delivery-and-subagent-selection.md`.
- AI planning record: AIP-0019-001 in the issue above.

## Context Ledger

- Included: `scripts/update-ai-collaboration-files.sh`, ADR 0007/0008,
  branch/PR discipline, and template rollout specification.
- Omitted: application source, provider SDKs, credentials, and live subagent
  execution.
- Assumptions: provider-neutral subagent selection records a request and
  handoff context; the host agent remains responsible for actual creation.

## Routing

- Model/assistant/tool: Codex desktop for design and documentation; Bash and
  throwaway Git repositories for deterministic verification.
- Privacy constraints: no secrets, private exports, or adopter data.

## AI Execution Records

### Attempt 1

- Agent: Codex desktop
- Environment: Codex desktop
- Model as displayed: GPT-5
- Reasoning setting as displayed: N/A; not exposed.
- Actual tokens: N/A; not exposed.
- Scope: add delivery/base/subagent selection, explicit auto-merge route,
  acceptance issue, ADR, and verification.
- Result: completed; verification recorded below.

## Referee Decisions

- 2026-08-20: implementation approved.
- Existing agreement units remain unchanged.
- Provider-specific subagent invocation remains out of scope.

## Verification

- `bash -n scripts/update-ai-collaboration-files.sh`: passed.
- `--help` output checked for the new options: passed.
- Throwaway target smoke tests cover local delivery, selected base branch,
  `--subagent yes`, GitHub dry-run, and invalid delivery/merge combinations:
  passed.

## Changed Files

- `scripts/update-ai-collaboration-files.sh`
- `docs/architecture/README.md`
- `docs/architecture/adr/0014-delivery-and-subagent-selection.md`
- `docs/issues/LISS-0019-delivery-and-subagent-selection.md`
- `docs/collaboration/traces/2026-08-20-delivery-and-subagent-selection.md`

## Next Safe Action

Run the deterministic checks and review the script diff before committing the
process change.
