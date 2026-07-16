# AI Work Trace

## Request

- Date: 2026-07-16
- User request: The Referee asked whether `README.md` needs to be part of
  the template distribution at all ("READMEも配布が必要ですか？"), after
  directing that `QUICKSTART.md` stay out of the distribution. Investigation
  concluded distribution was unnecessary and harmful; the Referee's question
  and the follow-up direction authorized the removal.
- Current phase: Architecture Path (template distribution behavior change).
- Canonical issue or work plan: LISS-0003 (its README half; annotated in
  that issue's Work Notes and Summary). No new issue was opened; the change
  is small, Referee-directed, and recorded here per the trace policy.
- AI planning record: inline analysis in session (no separate planning doc).

## Context Ledger

- Included: `scripts/lib/collaboration-template-paths.sh`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/update-ai-collaboration-files.sh`, `.github/workflows/ci.yml`,
  `README.md`, `README.ja.md`, `docs/collaboration/adoption-guide.md`,
  `docs/issues/LISS-0003-shared-block-delimiters-for-readme-and-ci.md`.
- Omitted: `docs/research/` essays (non-normative, unrelated to the
  mechanism), adopter repositories (not accessible; their reported pain is
  taken from LISS-0003's reference).
- Assumptions: adopting projects that previously synced README keep their
  local copy untouched (the update script only iterates the current paths
  list; verified by reading the script, not by running against a real
  adopter).
- Open decisions: none. Whether `ci.yml` itself gets shared-block delimiters
  remains LISS-0003's open scope.

## Routing

- Model/assistant/tool: Claude (Fable 5) for analysis and edits;
  deterministic verification via bash (`bash -n`, real copy run, grep).
- Reason: the decision needed repository archaeology (LISS-0003 adopter
  report, script behavior) plus Referee judgment; the edits themselves are
  mechanical.
- Privacy constraints: none (all inputs are repository-local).

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: local CLI session
- Model as displayed: claude-fable-5
- Reasoning setting as displayed: default
- Estimated token range: not estimated
- Estimated token midpoint: not estimated
- Actual tokens: unavailable
- Token metric: n/a
- Token source: n/a
- Token attribution boundary: n/a
- Actual token unavailable reason: session-level accounting not exposed to
  the agent
- Estimate variance: n/a
- Variance reason: n/a
- Scope: remove `README.md`/`README.ja.md` from
  `collaboration_template_paths` and from `ci.yml` `required_files`; update
  LISS-0003; update `QUICKSTART.md`/`QUICKSTART.ja.md` uninstall wording to
  match.
- Result: success; verification below.
- Attempt boundary: single session, single attempt.
- Notes: none.

## Cost / Reasoning Control

- Operating path: Architecture Path (distribution behavior), executed after
  explicit Referee direction in session.
- Files read: the Context Ledger "Included" list.
- Context intentionally omitted: see Context Ledger.
- Deterministic checks used: `bash -n` on all touched scripts; a real
  `copy-ai-collaboration-files.sh` run into a scratch git repository
  asserting README/QUICKSTART absence, distributed `ci.yml` README-entry
  absence, core artifact presence, and the CI smoke test's own placeholder
  grep; `scripts/init-llm-context.sh` run against the scratch target.
- Escalation reason: n/a.
- Avoided LLM work: no generation was used for the mechanical list edits.
- Rework caused by AI output: an earlier commit in the same branch added a
  `QUICKSTART.md` link to the then-distributed `README.md`, creating a
  dangling link in adopting projects; this change dissolves that defect.

## Referee Decisions

- QUICKSTART.md / QUICKSTART.ja.md stay out of the distribution (Referee,
  2026-07-16, in session).
- README.md / README.ja.md are removed from the distribution and from
  `ci.yml` `required_files` (Referee direction via the question and
  follow-up in session, 2026-07-16).
- Grounds: the template README has no placeholders and describes the
  template repository itself, so new-repo adoption shipped wrong content;
  LISS-0003 records a real adopter (voice-to-dic) reporting README sync
  conflicts as the most time-consuming conflict class.

## Verification

- Commands/checks: `bash -n` on copy/update/paths scripts; real copy into a
  scratch repo (`git init` temp dir) with `--project-name/--domain-summary/
  --stack`; asserted no `README*`/`QUICKSTART*` in target, zero `"README`
  entries in the target's `ci.yml`, presence of `AGENTS.md`, `CLAUDE.md`,
  `.gitignore`, `docs/architecture/agent-quickstart.md`,
  `.collaboration-template-version`; ran the CI smoke test's placeholder
  grep against the target contract files; ran `init-llm-context.sh` against
  the target.
- Result: all checks passed.

## Changed Files

- `scripts/lib/collaboration-template-paths.sh`
- `.github/workflows/ci.yml`
- `docs/issues/LISS-0003-shared-block-delimiters-for-readme-and-ci.md`
- `QUICKSTART.md`, `QUICKSTART.ja.md` (uninstall wording alignment)
- `docs/collaboration/traces/2026-07-16-stop-readme-distribution.md` (this
  trace)

## Next Safe Action

- Land this as its own process PR, separate from the research-essay and
  QUICKSTART docs PRs. LISS-0003's remaining `ci.yml` shared-block question
  stays open for a future design pass.

## Notes

- Existing adopters are unaffected on disk: the update script simply stops
  syncing README; their local README remains as-is.
