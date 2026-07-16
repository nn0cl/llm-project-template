# LISS-0005: Process hygiene improvements from second adopter review

## Metadata

- Local issue ID: LISS-0005
- GitHub issue:
- Status: proposed
- Phase: process-only
- Type: process/docs
- Priority: medium
- Owner/agent: Claude Fable 5 (proposal); Referee to assign
- Related branch: (create on acceptance, e.g. process/adopter-feedback-hygiene)

## Summary

- A second adopter (a Laravel/Vue web application with authentication,
  prompt publication, and Ollama/MCP integration work) reported an overall
  positive review of the template: issue/ADR/roadmap/branch-driven decisions
  prevented several dangerous implementation orderings (ad-hoc auth fixes,
  security-heavy work on an outdated framework, public-endpoint/public-data
  conflation).
- The same review surfaced four recurring operational gaps that the template
  documents do not currently address. Each gap is a small, docs-only rule or
  guidance addition. They are bundled here (following the LISS-0002
  precedent for feedback-driven fixes) to keep issue-management overhead
  proportionate — a cost the review itself flags.

## Acceptance Notes

1. ADR-to-issue coupling: `docs/templates/adr.md` gains a "Follow-up work"
   section listing the implementing local issues, and
   `docs/collaboration/local-issue-planning.md` records the rule that
   accepting an ADR which requires implementation creates or updates the
   implementing local issue(s) in the same change, not as a later backfill.
   (Observed: adopter's ADR-0010 was accepted; its implementing issue
   LISS-0015 was added only afterwards.)
2. Parent-issue and roadmap freshness:
   `docs/collaboration/local-issue-planning.md` records the rule that when a
   child issue changes status, the parent issue's status and the relevant
   work plan under `docs/work-plans/` are reviewed in the same change, and
   defines what a long-lived umbrella/governance parent may legitimately
   look like (so `in_progress` parents with completed children are either
   updated or explicitly justified). (Observed: adopter's governance parent
   LISS-0005 stayed `in_progress` while child issues advanced; a roadmap
   went stale until manually corrected.)
3. Adoption commit hygiene: `docs/collaboration/adoption-guide.md` (midway
   adoption section) documents that template adoption should land as its own
   branch/PR containing only template/collaboration documents, separate from
   behavior changes, smoke checks, and generated build artifacts; and adds a
   pre-adoption check that build outputs (e.g. `public/js/*`,
   `public/css/*` style artifacts) are gitignored or otherwise excluded
   before running smoke checks. (Observed: adopter's initial adoption commit
   was heavy and mixed generated assets into a smoke-check diff.)
4. Long-lived integration branches:
   `docs/collaboration/branch-commit-pr-discipline.md` states explicitly
   that the template flow is trunk-oriented; creating a `develop`-style
   long-lived integration branch requires an ADR in the adopting project,
   and stacked branches must be merged down promptly once each reviewable
   unit is accepted rather than accumulating an unexecuted merge strategy.
   (Observed: adopter created `develop` but the real stack accumulated on a
   feature branch with the merge strategy never executed.)

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0002 (first adopter-feedback round, same bundling precedent)

## Referee Decision Points

- Should the `develop`-branch guidance (item 4) be a prohibition or an
  "requires ADR" rule? Proposal: requires ADR, since some adopters have
  organizational reasons for an integration branch.
- Should umbrella/governance parent issues (item 2) be allowed to stay
  `in_progress` long-term with a mandatory child-status ledger, or should a
  distinct status/type be introduced for them?
- Bundle all four items in one PR (proposal) or split per document?
- Out of scope / deferred: a "minimal profile" or staged variant of
  `scripts/copy-ai-collaboration-files.sh` to shrink the initial adoption
  diff. This is a structural script change, not a docs rule; raise as its
  own issue if the heavy-initial-commit complaint recurs.

## Context

- Included: the adopter's review text (translated/summarized above);
  `docs/templates/adr.md`; `docs/collaboration/local-issue-planning.md`;
  `docs/collaboration/adoption-guide.md`;
  `docs/collaboration/branch-commit-pr-discipline.md`.
- Omitted: the adopter repository's actual code, its ADR/issue file
  contents, and its Ollama/Docker environment specifics — the review's
  in-project items (their LISS/ADR numbering, Laravel modernization order)
  are that project's concern, not this template's.
- Assumptions: the four gaps are representative of adopter behavior
  generally, not artifacts of this one project's setup. Items 1, 2, and 4
  were each confirmed by concrete incidents in the review, so the risk of
  fixing a non-problem is low.

## References

- Second adopter review (2026-07-06, provided verbatim by the Referee in
  session; positive on decision-forcing effects, critical on initial diff
  weight, issue-graph maintenance, ADR/issue lag, and unexecuted merge
  strategy).
- `docs/issues/LISS-0002-sync-safety-and-guidance-improvements.md` for the
  bundling precedent.

## Work Notes

- 

## Verification

- Docs-only: markdown lint / CI docs checks pass.
- Each of the four acceptance items maps to a concrete rule text present in
  the named document.
- Prompt/instruction change control applies (contract documents are
  touched): a trace under `docs/collaboration/traces/` accompanies the
  implementing PR.
