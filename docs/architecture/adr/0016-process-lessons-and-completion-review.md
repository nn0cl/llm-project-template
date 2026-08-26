# ADR 0016: Process Lessons, Completion Review, and Adopter-Safe Identifiers

## Status

Accepted

## Context

Adopting repositories receive process ADRs and collaboration rules, not this
template's planning ledger. Citations of this template's `LISS-NNNN` or
`WP-NNNN` identifiers in shipped Canonical files point at files that copy
excludes, so agents in the target search for missing issues.

Unfilled angle-bracket placeholders are easy to treat as domain or technology
facts. Review write-ups that replay a single incident do not transfer to the
next task. Completing an issue or work plan without checking operating-contract
deviations hides process debt until the next adoption round.

`CLAUDE.md` is a full effective-content mirror. Canonical contract-change
text that still describes an `@AGENTS.md` import contradicts that decision.

## Decision

1. Shipped Canonical process documents must not cite this template's local
   issue or work-plan identifiers. They cite ADRs, policy paths, or dated
   decision rounds. Naming-format examples (`LISS-0000`, `LISS-0001-short-title.md`)
   remain. Copy and update exclude `docs/work-plans/WP-*.md` and
   `docs/collaboration/reviews/*.md` in addition to existing issue, trace,
   and rollout-spec exclusions.
2. If a relied-on contract or architecture file still contains an unfilled
   `<...>` placeholder, agents stop after design intake and ask the
   Adjudicator to set the value. Placeholder text is not a fact.
3. `CLAUDE.md` remains a full mirror. It does not import `@AGENTS.md`.
   Contract-change checks compare effective content across the five agent
   surfaces as already decided in ADR 0006.
4. Review outcomes that should change later work are recorded as meta-level
   lessons: recurring process risks, contract-deviation classes, and
   operating-path failures. Do not record a blow-by-blow of a specific
   session. Read the lessons log at the next design intake and before
   implementation. Policy: `docs/collaboration/process-lessons.md`.
5. When a local issue or work plan is marked `done`, the same context runs a
   development-process review against the operating contract. If no
   deviation or operational problem is found, record that. If one is found,
   agree the disposition with the Adjudicator and write a template-feedback
   record from `docs/templates/template-feedback.md` under
   `docs/collaboration/template-feedback/` so it can be sent upstream.
   Policy: `docs/collaboration/process-review.md`.

## Consequences

Positive:

- Adopters are not sent looking for this template's issue files.
- Placeholders cannot silently become stack or domain choices.
- Later design and implementation can reuse process patterns.
- Template feedback is captured in the adopting repo with Adjudicator
  agreement, not only in chat.

Negative:

- Completion takes an extra same-context review step.
- Meta lessons still need human judgment to stay non-anecdotal.
- Historical traces in this template repository keep issue IDs; they are
  not copied.

## References

- `docs/collaboration/process-lessons.md`
- `docs/collaboration/process-review.md`
- `docs/collaboration/prompt-instruction-change-control.md`
- `scripts/lib/collaboration-template-paths.sh`
