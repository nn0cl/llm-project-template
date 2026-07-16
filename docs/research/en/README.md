# About docs/research (English entry point)

This folder holds the research and rationale essays behind the
`llm-project-template` — the design philosophy of AI-human collaborative
software development: why the template puts a human Adjudicator at decision
points, why work is phase-gated, why plans and decisions live in the
repository, and why agent context is deliberately minimized.

**The Japanese originals in [`docs/research/`](../README.md) are
authoritative.** This file is the English entry point: it summarizes each
essay so English-speaking readers can decide what to have translated or
read with machine assistance. If full translations are added later, they
live in this `en/` directory under the same filenames as the originals,
each opening with a note stating which commit of the original it was
translated from.

These documents are non-normative reading material for humans:

- Agents never read this folder. Operating paths in
  `docs/architecture/agent-quickstart.md` enumerate agent inputs as an
  allowlist, and `docs/research/` is outside it.
- This folder is not distributed to adopting projects.
  `scripts/lib/collaboration-template-paths.sh` excludes it.
- Nothing here defines rules. Conclusions get promoted to ADRs or
  `docs/collaboration/` documents through Adjudicator review; the essays
  remain as background reading.

Citation conventions (retrieval-dated sources, explicit "unverified"
markers, evidence-grade annotations, ACM-style quotations) are defined in
the Japanese [README](../README.md).

## The essays

Read the first one before the rest; it is the entry point.

### [The target end state: why AI collaboration needs structure](2026-07-05-rationale-target-end-state.md)

Fast code generation that leaves nothing behind — no approvals, no design
rationale, no resumable context — is not software engineering. The
template's goal is scaffolding for sustained AI-human collaboration:
an explicit operating contract (`AGENTS.md`, `CLAUDE.md`), Docs-as-Code
for every decision, three questions every diff must answer (what
requirement, where is the truth recorded, where does the next person
resume), and human checkpoints designed against Bainbridge's "Ironies of
Automation". Deliberately leaves domain, stack, and datastore decisions
to the adopting project.

### [The agent is a sandbox: an architecture of freedom and control](2026-07-07-rationale-saas-agent-as-sandbox.md)

Vendor sandboxes (GitHub Copilot, Cursor) provide OS-level safety —
isolated, ephemeral execution — but never semantic safety: they cannot
stop an architecture violation or a spec misunderstanding. The team must
supply the integration layer itself: operating-path allowlists, a shared
constitution in the repository, design intake, Adjudicator approval gates,
and PR review. Covers tiered agent teams (LLM cascades, learned routing,
orchestrator-worker patterns) and why hierarchy does not dissolve the
human's distinct responsibility.

### [The Adjudicator and phases: automation's ironies and the design of responsibility](2026-07-05-rationale-adjudicator-centered-collaboration.md)

Instead of making the human a full-time reviewer of every generated
token, the Adjudicator owns decision points: phase transitions, ADR
acceptance, test review, ambiguity resolution. The AT-TDD cycle
(Red / Green / Refactor) is externalized from personal discipline into
physical approval gates, connecting TDD, Continuous Delivery pipelines,
Specification by Example, BDD, and EARS requirements syntax. Argues that
escalating to a stronger model and requesting human approval are
semantically different acts, and that stronger models make gates more
important, not less.

### [Design first and controlling the context boundary](2026-07-05-rationale-design-first-minimal-context.md)

Context is a scarce resource. Irrelevant context measurably degrades LLM
reasoning (Shi et al.), long contexts have U-shaped recall (Lost in the
Middle), so include/omit decisions are reviewable design artifacts, not
prompt-engineering folklore. Omission is an active boundary against
guessing. The "capability ladder" routes work to deterministic tools,
small models, or strong reasoning models (FrugalGPT, RouteLLM), and
undecided items are managed as explicit non-decisions that agents must
not fill in.

### [Output contracts and the boundary of verifiability](2026-07-05-rationale-ai-output-contracts.md)

Fluent prose is not a correctness guarantee (hallucination and
faithfulness research), so AI output crossing a trust boundary must be
structured, validatable, and traceable to sources — Design by Contract
(Meyer) applied to model output, with Torvalds' "we do not break
userspace" as the interface-stability parallel. Reasoning is recorded as
auditable evidence (sources, assumptions, confidence, review status),
not chain-of-thought dumps; persisting an output is treated as adopting
it.

### [Reviewable code and managing cognitive load](2026-07-05-rationale-code-for-human-review.md)

When generation is cheap, verification becomes the bottleneck. Generated
code is optimized for minimal human cognitive load, not minimal lines:
understanding is the main challenge of code review (Bacchelli & Bird),
programs are theories the team must be able to rebuild (Naur), and
dependency rules localize what a reviewer must hold in their head at
once. Tests are written as readable Given/When/Then specifications, for
future agents as much as for humans.

### [Keeping plans in the repository: repository-native planning and change control](2026-07-05-rationale-repository-native-planning-and-change-control.md)

Chat windows are not artifacts. Plans, local issues with dependency
graphs, work traces, and handoffs are versioned files, so agents can
resume from the repository alone. ADRs function as legislation for
context-free agents ("law dictates code", inverting Lessig), prompts and
agent instructions are treated as code with review and CI-enforced
traces, and the two-tier local-first design (Kleppmann et al.) keeps the
planning ledger in the repository with GitHub as a projection.

### [The pull-based upstream: sovereignty in template distribution](2026-07-06-rationale-template-as-pull-based-upstream.md)

Template updates propagate by downstream pull, never upstream push. A
3-way merge protects adopter sovereignty — including respecting
deletions — in the spirit of cruft/Copier and Renovate-style PR-based
sync; a clean merge is still not a substitute for semantic review.
Improvements flow back upstream as issues. Draws on the push-to-pull
shift in manufacturing (Kanban) and networked organizations
(Team of Teams), annotated as practitioner accounts rather than
controlled studies.

### [Branching strategy for AI collaboration: the economics of integration latency](2026-07-06-branching-strategies-develop-and-multi-target-releases.md)

DORA's trunk-based development capability condemns integration latency,
not branch names: three or fewer active branches, daily merges to trunk.
GitFlow's own author narrowed its niche in 2020. Multi-target releases
work as immutable snapshots off a single main (GitLab, Microsoft Release
Flow, Kubernetes cherry-pick policy), with divergence handled by feature
toggles and module boundaries rather than long-lived per-target
branches. Proposes the topics an adopting project's ADR should settle
before keeping any long-lived integration branch.

### [Normative versus reading documents: an architecture for documentation](2026-07-06-rationale-normative-vs-reading-documents.md)

Humans skip irrelevant documents; agents cannot — everything in context
influences generation. So agent inputs are an explicit allowlist
(stronger than any denylist), and reading material is structurally
outside it. Maps the split onto Diátaxis (reference/how-to vs
explanation) and the RFC 2119 normative/informative tradition. Promotion
from research to rules is one-way, via Adjudicator review.

### [Evidence and rules: EBSE and respect for context](2026-07-06-rationale-evidence-based-process-design.md)

Process rules are set by evidence, not fashion: formulate the question,
search the evidence, appraise it critically, integrate it into the
project's own context — Evidence-Based Software Engineering (Kitchenham
et al.) scaled down to daily operations. Adopter feedback flows into a
process-gap register and revises the norms. Persuasiveness is not
evidence: sources carry retrieval dates, unverified URLs are marked, and
nothing is promoted to a rule without Adjudicator review.
