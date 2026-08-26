# AI Work Trace

## Request

- Date: 2026-08-26
- User request: project-specific conventions in a separate file that agents
  must read, so template context files can be overwritten on template update.
- Current phase: process-only.
- Canonical issue or work plan:
  `docs/issues/LISS-0022-project-conventions.md`.
- AI planning record: AIP-0022-001.

## Context Ledger

- Included: persona files, copy/update scripts, adoption-guide.
- Omitted: application code, provider SDKs.
- Assumptions: first overwrite after migration is reviewed in the sync PR.

## Routing

- Model/assistant/tool: Grok Build; bash throwaway copy.
- Privacy constraints: no secrets.

## AI Execution Records

### Attempt 1

- Agent: Grok Build
- Model as displayed: Grok 4.6
- Scope: project-conventions file, retire Tier 2 persona merge, copy creates
  the live file, context files point at it.
- Result: completed pending smoke.

## Adjudicator Decisions

- Implementation requested 2026-08-26.

## Changed Files

- See the commit on `process/liss-0022-project-conventions`.

## Next Safe Action

Review the branch and CI.
