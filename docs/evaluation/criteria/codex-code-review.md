# Codex Code Review Evaluation Criteria

This rubric evaluates whether advisory Code Review findings apply existing
repository policy. It does not grant approval or replace CI, Adjudicator
review, or the canonical policies linked below.

## Rule 1: Specification and phase boundaries

- Canonical policy: `docs/architecture/implementation-readiness.md`,
  `docs/collaboration/ai-human-scheme.md`, and the current reviewed issue or
  specification.
- Trigger: an implementation diff introduces behavior outside the accepted
  specification or proceeds beyond the approved phase without recorded
  approval.
- Expected finding: identify the concrete out-of-scope change or phase
  transition, cite the missing acceptance/approval evidence, and request
  removal or an explicit spec-based disposition. Do not claim the review itself
  grants approval.
- Safe counterexample: an implementation changes only behavior explicitly
  covered by the accepted specification and stays within the approved phase.
- Expected result for counterexample: no finding under this rule.

## Rule 2: Verification claim integrity

- Canonical policy: `docs/collaboration/verification-policy.md`.
- Trigger: a change or PR description claims full Green while showing only a
  focused test, omitting a declared blocking suite, or recording evidence for
  a different commit than the final commit under review.
- Expected finding: name the missing or mismatched suite/SHA and ask for the
  required run or a narrower, accurate claim. Do not infer that unrun checks
  passed.
- Safe counterexample: the report distinguishes focused from all-blocking
  checks, names the tested final SHA and environment, and explicitly records
  any unassessed or blocked suite.
- Expected result for counterexample: no finding under this rule.

## Scoring

For each trigger, pass only when the finding is specific, policy-grounded, and
asks for a safe disposition without claiming authority. For each counterexample,
pass only when no finding is raised under that rule. Record false positives,
misses, and unavailable Code Review execution as unassessed rather than pass.
