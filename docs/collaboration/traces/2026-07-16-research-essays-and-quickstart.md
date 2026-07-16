# AI Work Trace

## Request

- Date: 2026-07-16 (covering the research-essay refinement sessions of
  2026-07-05 through 2026-07-16 on branch `docs/research-rationale-essays`)
- User request: Referee asked for (1) advanced editing of the
  `docs/research/` rationale essays — fact-checking against academic
  sources, link liveness verification, pruning of weak analogies, and
  normative/reading separation; (2) a new `QUICKSTART.md`/`QUICKSTART.ja.md`
  adoption-and-uninstall guide recommending a sibling-directory checkout
  and agent-assisted introduction; (3) a critical self-review and fixes for
  its findings.
- Current phase: non-normative documentation (research essays) plus new
  template-repo-local guide files; no operating-contract files changed.
- Canonical issue or work plan: none — the Referee explicitly ran this as
  issue-less documentation work in session. Per
  `docs/collaboration/local-issue-planning.md`'s waiver expectation, that
  waiver is recorded here rather than left verbal.
- AI planning record: per-task compact design notes in session.

## Context Ledger

- Included: all `docs/research/*.md`; `docs/research/README.md`'s own
  citation conventions; `AGENTS.md`/`CLAUDE.md`/`agent-quickstart.md` (to
  verify the essays' claims about read paths);
  `scripts/lib/collaboration-template-paths.sh` and
  `.github/workflows/ci.yml` (to verify distribution/CI isolation claims);
  external sources fetched live for verification (see essay reference
  lists; every cited URL carries a 取得日 and unverifiable ones are marked
  未検証).
- Omitted: application/stack documents (none exist in this template);
  adopter repositories.
- Assumptions: fetched page content reflects the cited sources as of the
  retrieval dates recorded in each essay.
- Open decisions: none blocking.

## Routing

- Model/assistant/tool: Claude (Fable 5) for prose analysis and rewriting;
  WebFetch for live verification of every questioned citation (Cursor and
  GitHub sandbox docs, Anthropic engineering/docs pages, arXiv abstracts,
  Ink & Switch, Chromium, kernel archives); bash/grep for link-set
  comparisons, cross-reference checks, and stash content audits.
- Reason: citation verification must not rely on training memory; the
  folder's own rule requires retrieval-dated sources.
- Privacy constraints: none (public sources and repository-local files).

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: local CLI session(s)
- Model as displayed: claude-fable-5 (parts of one session on
  claude-sonnet-5 by Referee's model switch)
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
- Scope: see Changed Files.
- Result: success; verification below.
- Attempt boundary: multiple sessions on one branch, treated as one logical
  unit of documentation work.
- Notes: substantive corrections included removing an unsourced
  "Fintech/MT4" claim that contradicted both the folder's citation policy
  and the essays' own Referee-responsibility argument; regrounding the
  model-tier pattern in cascade/routing literature (Yue et al. ICLR 2024,
  RouteLLM) plus a grade-annotated vendor self-report; author and URL
  corrections (Hodgson not Fowler for Feature Toggles; Tyree, J.;
  Ink & Switch and platform.claude.com URL moves); restoration of
  LISS-0005 from a stash so essay references resolve.

## Cost / Reasoning Control

- Operating path: documentation editing with live-source verification;
  Architecture Path-adjacent only where essays' claims about template
  mechanics were checked against scripts/CI.
- Files read: Context Ledger "Included" list.
- Context intentionally omitted: see Context Ledger.
- Deterministic checks used: grep-based cross-link resolution over
  `docs/research/`; URL-set comparison between stash and working tree;
  conflict-marker scan; QUICKSTART link-target existence checks; grep
  assertions that QUICKSTART/research appear in no read-path list, no
  distribution list, and no CI required-files list.
- Escalation reason: n/a.
- Avoided LLM work: link/list integrity checked with grep/diff, not
  generation.
- Rework caused by AI output: two essays briefly carried near-duplicate
  escalation-vs-approval passages introduced during rewriting; deduplicated
  by keeping the full argument in the Referee essay and referencing it from
  the sandbox essay.

## Referee Decisions

- Issue-less execution of this documentation work (waiver recorded here).
- Deletion of the superseded
  `2026-07-06-rationale-branching-and-release-strategy.md` in favor of the
  merged branching-strategies essay.
- Stash `wip-before-session-docs` audited and dropped after extracting
  LISS-0005 and three superior citations (Referee direction, 2026-07-16).
- QUICKSTART stays out of every agent read path and out of the template
  distribution (Referee, 2026-07-16).

## Verification

- Commands/checks: all `docs/research/` relative links resolve; README
  収録 list matches the file set and the target-end-state 各論 ordering;
  every flagged external URL fetched live (dead/redirected ones fixed:
  Ink & Switch, docs.claude.com; deprecated one annotated: Chromium
  drover; blocked archives marked 未検証: LKML); no research/QUICKSTART
  path appears in `agent-quickstart.md` read lists,
  `collaboration-template-paths.sh`, `init-llm-context.sh`, or `ci.yml`
  `required_files`.
- Result: all checks passed.

## Changed Files

- `docs/research/*.md` (ten essays + README refined; one superseded essay
  deleted)
- `docs/issues/LISS-0005-adopter-feedback-process-hygiene-improvements.md`
  (restored from stash, unmodified)
- `QUICKSTART.md`, `QUICKSTART.ja.md` (new)
- `README.md`, `README.ja.md` (QUICKSTART links; template-repo-local)
- `docs/collaboration/traces/2026-07-16-research-essays-and-quickstart.md`
  (this trace)

## Next Safe Action

- Land as two docs PRs (research essays; QUICKSTART) separate from the
  README-distribution process PR, replacing the original mixed PR #12.

## Notes

- `docs/research/` remains outside agent read paths and outside the
  distribution; nothing in this work changes normative template behavior.
