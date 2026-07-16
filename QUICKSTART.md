# Quickstart: Adopting This Template

Read this before you copy anything. It answers three practical questions:
where to check this template out, how to let an agent do the introduction
safely, and how to remove it later if you change your mind.

For what the template provides and why, see [README.md](README.md). This
file is the step-by-step companion; it does not repeat the rationale.

## 1. Check this template out next to your project, not inside it

Clone this template as a **sibling directory** of the project you want to
adopt it into, not as a subfolder or nested git repository inside that
project:

```text
~/dev/
├── my-target-project/      # your project, its own git history
└── llm-project-template/   # this template, cloned separately
```

```bash
cd ~/dev
git clone <this-repository-url> llm-project-template
```

Reasons this matters:

- `scripts/copy-ai-collaboration-files.sh` and
  `scripts/update-ai-collaboration-files.sh` are run **from this template's
  checkout**, with `--target /path/to/my-target-project`. They never need to
  live inside the target repository.
- Keeping the template checkout around lets you `git pull` it later and run
  `scripts/update-ai-collaboration-files.sh` to receive template
  improvements without re-cloning — see
  [Receiving Later Template Updates](docs/collaboration/adoption-guide.md#receiving-later-template-updates).
- Nesting a second `.git` inside your project's working tree is a common
  source of accidental submodule confusion and stray commits; a sibling
  checkout avoids that class of mistake entirely.
- This template's own maintenance history (local issues, traces, sample
  rollout spec) stays out of your project's repository. The copy script
  already excludes those paths, but a sibling checkout makes the separation
  obvious to anyone looking at the two working trees side by side.

## 2. Let an agent do the introduction

You can run the shell commands below yourself, but this template is built so
an AI coding agent can safely perform the introduction under Referee
supervision. Ready-to-paste prompts are in
[`docs/templates/examples/adoption-prompts.md`](docs/templates/examples/adoption-prompts.md).
The short version:

1. Open an agent session **with the target repository as the working
   directory**, not the template checkout.
2. Tell the agent the path to the template checkout and the task: run the
   copy script, report what it skipped versus copied, and stop before
   filling in any target-specific fact (stack, datastore, provider, domain
   model) that has not been Referee-approved.
3. Review the diff yourself before the agent fills placeholders or starts any
   Feature Path work. The agent should stop and ask, per `AGENTS.md`'s Prime
   Directive, rather than guess.

This mirrors the ordinary Fast Path / Architecture Path discipline the
template applies to every other task. Adoption is not a special case that
skips Referee review.

## 3. Install

From the template checkout:

```bash
scripts/copy-ai-collaboration-files.sh --target ~/dev/my-target-project
```

Existing files in the target are skipped by default. Add `--dry-run` first if
you want to preview without writing anything, and only use `--force` when you
intend to overwrite files that belong to this template — never to overwrite
your project's own README, specs, or architecture docs.

Then, from the target repository:

```bash
cd ~/dev/my-target-project
scripts/init-llm-context.sh .
```

Paste the generated prompt into the first AI session for that repository.

Full install steps, including which placeholders to fill and in what order,
are in
[README.md § Install into another repository](README.md#install-into-another-repository)
and [`docs/collaboration/adoption-guide.md`](docs/collaboration/adoption-guide.md).

## 4. Uninstalling

Removing this template is a project decision, not a mechanical script. Files
installed as scaffolding may now hold project-owned content (specs, ADRs,
issues, traces) that has nothing to do with the template itself. Treat
uninstall as Architecture Path work: record why in an ADR or a commit message
before deleting anything, the same way any other process change gets
recorded under this template's own rules.

The list below follows
[`scripts/lib/collaboration-template-paths.sh`](scripts/lib/collaboration-template-paths.sh) —
the same list the copy/update scripts use — split by how safe each item is to
delete outright.

### Safe to delete outright (template tooling only)

- `scripts/copy-ai-collaboration-files.sh`
- `scripts/update-ai-collaboration-files.sh`
- `scripts/init-llm-context.sh`
- `scripts/lib/collaboration-template-paths.sh`
- `.collaboration-template-version` (the sync marker at your repo root)
- `.collaboration-template-ignore`, if you created one
- `docs/templates/` (design-intake, handoff, trace, issue, work-plan, ADR,
  Gherkin templates)
- `docs/at-tdd/process.md`

### Review first — these are the operating contract itself

Deleting these stops agents from following the phase-gated workflow at all,
not just this template's specific wording. Confirm that is actually what you
want — versus, say, relaxing one rule — before removing:

- `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`
- `.grok/rules/`, `.cursor/rules/`

### Selective — these folders mix template scaffolding with your content

Do not `rm -rf` these. Remove only the template-authored files inside them
and keep anything your project added:

- `docs/architecture/adr/0001-*.md` through `0011-*.md` are the process ADRs
  this template ships with; remove only those eleven, and keep any ADR your
  project numbered afterward (0012 and up).
- `docs/architecture/` otherwise holds a mix of template-provided files
  (`agent-quickstart.md`, `implementation-readiness.md`,
  `ai-request-routing.md`, `io-reasoning-contracts.md`,
  `dependency-policy.md`, `project-structure.md`, `testing-strategy.md`,
  `README.md`) and the stack-specific documents your project wrote inside the
  same folder. Remove the template files individually; keep the rest.
- `docs/collaboration/` is almost entirely template-provided process docs,
  but `docs/collaboration/traces/` and any file your project edited to
  record real decisions are your project's audit history. Consider archiving
  instead of deleting if you might want that history later.
- `docs/issues/`, `docs/work-plans/`, `docs/specs/`, `docs/evaluation/` are
  scaffolding directories the template ships empty (`.gitkeep` only). By the
  time you are uninstalling, they almost certainly hold real project
  content. Do not delete these — they stopped being "the template's" the
  moment your project wrote into them.

### Must edit, not delete

- `.github/workflows/ci.yml` — the "Check required project documents" and
  "Check architecture decision records" steps assert that the contract files
  above exist. If you delete `AGENTS.md` or the ADRs without editing this
  workflow, CI starts failing on the next push. Rewrite or remove those
  steps to match what you actually kept.
- `README.md` / `README.ja.md` — once adopted, these are your project's own
  README, not the template's. Edit out the template-specific sections (this
  Quickstart link, the install instructions) rather than deleting the file.

### Not part of the template

`.github/dependabot.yml`, `.github/pull_request_template.md`, and
`.github/ISSUE_TEMPLATE/` are generic GitHub configuration this template
happens to ship with sensible defaults. Keep them regardless of whether you
keep the AI-collaboration process — they are useful on their own.

## Why this file will not bloat agent context

Agents operating under this template's contract only read what
`docs/architecture/agent-quickstart.md`'s Fast Path / Feature Path /
Architecture Path lists name explicitly (see `AGENTS.md`). This file is
deliberately absent from all three lists, and from
`scripts/lib/collaboration-template-paths.sh`, so it is never copied into an
adopting project and never becomes part of an agent's ordinary read path —
the same treatment `docs/research/` gets, for the same reason.

That guarantee is architectural, not physical. A tool whose own harness loads
an entire repository tree into context regardless of this template's
allowlist, or a human who manually pastes this file into a prompt, can still
put it in front of a model. No file placement can prevent that; keeping this
file out of every list this template controls is the extent of what is
actually enforceable here.
