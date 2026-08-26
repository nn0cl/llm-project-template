# AI Work Trace

## Request

- Date: 2026-08-26
- User request: at template adoption, run an interactive setup shell that
  records review/implementation isolation and optional host-displayed model
  identifiers, keeping documents consistent.
- Current phase: process-only, Architecture Path implementation after
  approval of the recommended defaults.
- Canonical issue or work plan:
  `docs/issues/LISS-0020-runtime-routing-setup.md`.
- AI planning record: AIP-0020-001 in the issue above.

## Context Ledger

- Included: adoption scripts, agent contracts, review templates, capability
  matrix, ADR 0006/0008/0014, QUICKSTART/README/CI required-file lists.
- Omitted: application source, provider SDKs, credentials, live subagent
  execution, loop-template human-absent policy.
- Assumptions: the host or a human launches any actual subagent; empty model
  fields mean capability-class routing.
- Open decisions: none remaining from the approved defaults.

## Routing

- Model/assistant/tool: Grok Build for design and documentation; Bash and
  throwaway Git repositories for deterministic verification.
- Reason: process/tooling change with contract-file alignment.
- Privacy constraints: no secrets, private exports, or adopter data.

## AI Execution Records

### Attempt 1

- Agent: Grok Build
- Environment: Grok Build
- Model as displayed: Grok 4.6
- Reasoning setting as displayed: N/A; not exposed.
- Actual tokens: N/A; not exposed.
- Scope: configure script, runtime-routing policy and form, same-context
  review template, ADR 0015, LISS-0020, contract hooks, adoption/CI
  consistency, stale ADR-count correction (0001-0015), copy-path inclusion
  of `scripts/check-document-lifecycle.py`, and CLAUDE.md full-mirror
  wording in the adoption guide.
- Result: completed; verification recorded below.

## Adjudicator Decisions

- 2026-08-26: recommended defaults accepted; document consistency in scope.
- Human Adjudicator remains the approval authority.
- Provider-specific subagent invocation remains out of scope.
- ADR 0014 template-sync `--subagent` remains a separate concern.

## Verification

- Commands/checks:
  - `bash -n` on configure/copy/update/init scripts
  - throwaway copy + configure `--non-interactive` + `--force` override
  - live toml absent after copy, present after configure
  - refuse overwrite without `--force`
  - `git diff --check`
- Result: recorded in the issue work notes after the local smoke run.

## Changed Files

- `scripts/configure-ai-collaboration.sh`
- `scripts/copy-ai-collaboration-files.sh`
- `scripts/init-llm-context.sh`
- `scripts/update-ai-collaboration-files.sh`
- `scripts/lib/collaboration-template-paths.sh`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.grok/rules/01-quickstart.md`
- `.grok/rules/03-collaboration-and-completion.md`
- `.cursor/rules/03-collaboration-and-completion.mdc`
- `.github/workflows/ci.yml`
- `docs/architecture/agent-quickstart.md`
- `docs/architecture/ai-request-routing.md`
- `docs/architecture/README.md`
- `docs/architecture/adr/0015-runtime-routing-setup.md`
- `docs/collaboration/runtime-routing.md`
- `docs/collaboration/adoption-guide.md`
- `docs/collaboration/session-start-and-resume.md`
- `docs/collaboration/model-tool-capability-matrix.md`
- `docs/collaboration/ai-human-scheme.md`
- `docs/collaboration/definition-of-done.md`
- `docs/collaboration/document-lifecycle.md`
- `docs/collaboration/process-gap-register.md`
- `docs/collaboration/llm-cost-reduction.md`
- `docs/templates/runtime-routing.toml`
- `docs/templates/same-context-review.md`
- `docs/templates/agent-handoff.md`
- `docs/templates/examples/adoption-prompts.md`
- `docs/specs/template-rollout.md`
- `docs/issues/LISS-0020-runtime-routing-setup.md`
- `QUICKSTART.md`
- `QUICKSTART.ja.md`
- `README.md`
- `README.ja.md`
- `docs/collaboration/traces/2026-08-26-runtime-routing-setup.md`

## Next Safe Action

Run the deterministic smoke tests and review the branch before merge.

## Notes

- Historical traces and closed issues that still say ADRs 0001-0011 were
  left unchanged; current Canonical docs and CI now say 0001-0015.
- LISS-0017 number collision is unchanged and out of this issue's scope.
