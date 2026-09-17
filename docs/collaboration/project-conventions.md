# Project Conventions

Target-owned for this repository (the collaboration template itself).
Adopting projects get their own copy from `docs/templates/project-conventions.md`.
Template sync must not overwrite an adopting project's live file.

## Project

- Name: llm-project-template
- Domain: reusable AI-human collaboration process template
- Stack: Markdown process docs, Bash adoption scripts, Python standard-library
  verification/routing tools, GitHub Actions

## External resources (ports)

- Git and GitHub CLI for branch, PR, and sync operations
- No application datastore
- No LLM provider SDK in this repository

## Runtime and trust boundaries

- The project is local-first documentation and scripts.
- No production application runtime.

## Current non-decisions

- Adopter application stack, datastore, and LLM provider

## Stack-specific architecture documents

- none beyond the shipped process architecture documents

## Additional project rules

- Implementation: `scripts/`; shared pure policy and Git adapters: `scripts/lib/`.
- Regression tests: `scripts/tests/`, Python 3.11+ standard library unittest.
- Blocking checks: all run steps in `.github/workflows/ci.yml`, including
  `python3 scripts/run-regression-tests.py`, shell syntax, record validators,
  required documents/ADRs, conflict markers, copy smoke, and PR traceability
  when validating a pull request. Local runs without PR context must report
  that gap rather than claim hosted CI success.
- Environment: Bash 3.2+ and Git/Perl for adoption scripts; Python 3.11+ for
  verification/routing tools. No approved test exclusions.

- This repository maintains the reusable template. Target product facts do
  not belong in template context files.
