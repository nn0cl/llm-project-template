# LLM Project Template

[日本語ガイド](README.ja.md)

This repository is a starter template for a **Clean Architecture + AT-TDD**
development workflow where a human architect (the "Referee") and one or more
AI coding agents (Claude, Copilot, Codex, Grok, etc.) collaborate under a
shared, written operating contract.

In this repository, **AT-TDD** is a local shorthand for an **ATDD + TDD hybrid
workflow**: acceptance specifications drive failing tests, reviewed tests drive
minimal implementation, and refactoring happens only after verified Green. It
is not used here as a claim that "AT-TDD" is a separate industry-standard
method name.

Everything here is process and collaboration scaffolding. It contains no
application domain logic, stack decision, datastore decision, provider choice,
or product specification. Those belong to the repository where this template is
installed.

## What this template gives you

- A **phase-gated workflow** (Design Intake -> Red -> Green -> Refactor) that
  every agent must follow, with explicit stop points for human review.
- A **Referee-centered collaboration scheme**: the human approves phase
  transitions, ADRs, and ambiguous decisions; agents produce reviewable,
  minimal, phase-correct artifacts.
- **Agent operating contract files** (`AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/`) kept in sync by a
  documented change-control rule and a CI check. Codex reads `AGENTS.md`
  directly and needs no dedicated file.
- **Local issue and work-plan planning** under `docs/issues/` and
  `docs/work-plans/`, usable before or alongside GitHub Issues.
- **AI work traces** under `docs/collaboration/traces/` for auditability.
- **Reusable templates** for design intake, Referee review, agent handoff,
  work traces, local issues, work plans, Gherkin features, and ADRs.
- A **CI skeleton** that checks the contract files exist, checks that
  ADRs are numbered, and enforces that contract-file changes come with a
  trace.
- A **copy script** for rolling the collaboration files into a new or existing
  repository without overwriting existing target files by default.
- An **LLM setup prompt script** that prepares a compact first message for a
  new AI session after installation.
- A **target-local adoption guide** that can be copied without replacing an
  existing product README.
- A **project start and development guide** for moving from template adoption
  to target-owned specifications, domain modeling, and phase-gated work.
- A **lightweight cost/reasoning control ledger** for checking whether strong
  LLM reasoning was actually needed.

## Why use it?

Use this template when you want AI-assisted development to be reviewable,
phase-correct, and cheaper to reason about.

It helps reduce:

- guessed implementation before accepted specs.
- AI agents skipping from vague requests to production code.
- hidden business logic in adapters, UI, provider clients, or persistence.
- oversized prompts and unnecessary strong-model reasoning.
- dependency choices made without security, version, troubleshooting, test, or
  POC evidence.
- handoff gaps when another human or agent continues the work.

The benefits depend on using the process consistently; the template is not an
automatic productivity guarantee. See
`docs/collaboration/template-benefits.md` for the detailed rationale.

## Install into another repository

From this template repository:

```bash
scripts/copy-ai-collaboration-files.sh --target /path/to/target-repo
```

The copy script skips existing files by default. This is intentional: when the
template is introduced into an existing project, the target project's
architecture documents, specifications, README, and application files remain
owned by that project.

Optional placeholder replacement:

```bash
scripts/copy-ai-collaboration-files.sh \
  --target /path/to/target-repo \
  --project-name "Example Product" \
  --domain-summary "one-line target project summary" \
  --stack "backend language, frontend framework, package manager"
```

Use `--dry-run` to preview actions. Use `--force` only when you intentionally
want to replace files that are part of this template.

## Initialize an LLM session

After copying the template into the target repository, run:

```bash
cd /path/to/target-repo
scripts/init-llm-context.sh .
```

Paste the generated prompt into the first LLM session for that repository. The
prompt tells the agent which operating documents to read, which phase gates to
respect, how to choose Fast Path / Feature Path / Architecture Path, and when
to stop for Referee approval. It does not select the target project's stack,
datastore, LLM provider, external APIs, or domain behavior.

Target-local onboarding lives in
`docs/collaboration/adoption-guide.md` after the template is copied.

## What you must fill in

This template deliberately avoids naming a stack, a domain, or concrete
architecture layers. Before using it on a real project:

1. Replace every `<PLACEHOLDER>` in `AGENTS.md`, `CLAUDE.md`,
   `.github/copilot-instructions.md`, and `docs/architecture/README.md` with
   your project's name, domain summary, and selected stack.
2. Add one architecture document per architectural area you actually have
   (e.g. `backend-architecture.md`, `frontend-architecture.md`,
   `persistence.md`). Use `docs/architecture/project-structure.md` and
   `docs/architecture/testing-strategy.md` as the starting shape and fill in
   real paths. See `docs/templates/examples/` for two filled-in examples
   (Rust/Tauri core, React front-end) — copy the pattern, not the content.
3. Add project-specific "external resources must be ports" entries to
   `CLAUDE.md` / `AGENTS.md` (e.g. payment provider, LLM provider, message
   queue, external API).
4. Write your first EARS/Gherkin specification under `docs/specs/` using
   `docs/templates/gherkin-feature.md`.
5. Update `.github/workflows/ci.yml`'s `required_files` list and add
   stack-specific jobs (lint, test, dependency policy) once those tools
   exist.
6. Renumber/extend `docs/architecture/adr/` as real architecture decisions are
   made. The eight ADRs included here (0001-0008) describe the collaboration
   process itself and normally do not need to change.

## Introduce into an existing repository

For midway adoption, start with a dry run:

```bash
scripts/copy-ai-collaboration-files.sh --target /path/to/existing-repo --dry-run
```

Then run the copy without `--force`. Review skipped files, decide whether any
existing project documents should manually adopt the collaboration wording, and
only then consider targeted overwrites. Do not use this template to replace the
target project's accepted architecture or feature specifications.

## Read order for a new agent

1. `docs/architecture/agent-quickstart.md`
2. Select the smallest safe path: Fast Path, Feature Path, or Architecture
   Path.
3. Read only the documents required by that path.
4. `docs/architecture/implementation-readiness.md` before Phase 1, 2, or 3
   starts.

## Directory Guide

```text
.
├── AGENTS.md                       # operating contract (tool-agnostic)
├── CLAUDE.md                       # operating contract (Claude-specific entry point)
├── .grok/
│   └── rules/                      # operating contract (Grok-specific entry point)
├── .github/
│   ├── copilot-instructions.md     # operating contract (Copilot-specific entry point)
│   ├── pull_request_template.md
│   ├── ISSUE_TEMPLATE/
│   └── workflows/ci.yml
└── docs/
    ├── at-tdd/process.md           # phase discipline
    ├── collaboration/              # process rules (Referee scheme, DoD, privacy, branching, ...)
    │   └── traces/                 # AI work trace log (per-task audit trail)
    ├── templates/                  # design intake, handoff, trace, issue, work-plan, ADR, Gherkin
    │   └── examples/               # filled-in stack-specific examples, for reference only
    ├── architecture/               # Clean Architecture rules, quickstart, readiness checklist
    │   └── adr/                    # architecture decision records (0001-0008 = process ADRs)
    ├── specs/                      # EARS/Gherkin feature specifications
    ├── issues/                     # local issue files (LISS-0000 style)
    ├── work-plans/                 # multi-issue work plans
    └── evaluation/                 # golden examples and evaluation criteria
└── scripts/
    ├── copy-ai-collaboration-files.sh
    └── init-llm-context.sh
```

## Core rules worth remembering

- No implementation without a reviewed acceptance specification.
- No phase skipping. Only the Referee-selected phase runs.
- No hidden business logic in adapters, UI components, or framework handlers.
- Every external resource is represented as a port before it is used.
- Every task starts with path-appropriate design intake: compact note for Fast
  Path, full `[THOUGHT]` for Feature Path or Architecture Path.
- Changing an agent operating contract file requires a stated reason, Referee
  review, and a trace under `docs/collaboration/traces/` (CI enforced).

## License

[MIT](LICENSE)
