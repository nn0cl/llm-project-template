# LISS-0010: Cursor agent entry point, Grok/Codex convention refresh

## Metadata

- Local issue ID: LISS-0010
- GitHub issue:
- Status: done
- Phase: docs-only
- Type: process/docs
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason:
- Owner/agent: Claude Code CLI (Claude Sonnet 5)
- Related branch: process/cursor-agent-entry-point

## Summary

- Referee asked to research the current (2026-07-14) state of Grok, Cursor,
  and Codex project-configuration conventions and make the template work
  with all three, following the precedent set by LISS-0006 (2026-07-08),
  which added `.grok/rules/` and confirmed Codex needs no dedicated file.
- Live research (WebSearch/WebFetch against current vendor documentation)
  found:
  - **Codex**: unchanged since LISS-0006. Reads `AGENTS.override.md` then
    `AGENTS.md` (then configurable fallback names) at global and per-
    directory project scope; `project_doc_max_bytes` defaults to 32 KiB.
    Still needs no dedicated template file.
  - **Grok Build**: behavior has broadened since LISS-0006's investigation.
    In addition to the `.grok/rules/*.md` discovery surface confirmed via a
    live adopter's `grok inspect` output on 2026-07-08, current xAI
    documentation states Grok Build now also reads `AGENTS.md` natively at
    three levels (`~/.grok/AGENTS.md`, `<repo-root>/AGENTS.md`,
    `<cwd>/AGENTS.md`, deeper files taking precedence) and reads `CLAUDE.md`
    "for compatibility." This is additive, not a replacement — the template
    keeps `.grok/rules/*.md` as the primary, stronger-binding surface.
  - **Cursor**: no prior template support existed. Current Cursor
    documentation confirms two mechanisms: `AGENTS.md` as a "simple
    alternative" (root or subdirectories), and `.cursor/rules/*.mdc` as the
    primary, more powerful mechanism — files must use the `.mdc` extension
    with YAML frontmatter (`description`, `globs`, `alwaysApply`); a plain
    `.md` file in `.cursor/rules/` is ignored because it has no frontmatter.
    Setting `alwaysApply: true` makes a rule apply to every request
    regardless of file globs.
  - Cross-tool note found during research: AGENTS.md's format was moved to
    the Agentic AI Foundation (a Linux Foundation directed fund) for neutral
    stewardship, with Cursor, Cline, Windsurf, Codex, and Gemini CLI all
    aligning on it — explaining why Cursor and Grok Build both added native
    `AGENTS.md` fallback support since LISS-0006's investigation.
- Decision: add a full-mirror `.cursor/rules/*.mdc` file set (three files,
  matching the existing `.grok/rules/*.md` pattern exactly in content, with
  a Cursor-specific persona header and `.mdc` frontmatter), rather than
  relying on Cursor's native `AGENTS.md` fallback — consistent with the
  Referee's LISS-0006 decision to keep full per-vendor mirrors instead of a
  thin pointer, even though this is now a fifth file set to keep in sync.
- Found and fixed a related pre-existing bug while implementing: the
  placeholder-substitution glob in `scripts/copy-ai-collaboration-files.sh`
  (`*.md|*.yml|*.yaml`) did not include `*.mdc`, which would have silently
  left `<PROJECT_NAME...>`/stack placeholders unfilled in any adopted
  project's `.cursor/rules/*.mdc` files.

## Acceptance Notes

1. Add `.cursor/rules/01-quickstart.mdc`,
   `.cursor/rules/02-architecture-boundaries.mdc`, and
   `.cursor/rules/03-collaboration-and-completion.mdc`, mirroring the full
   content of `.grok/rules/*.md` (which itself mirrors `AGENTS.md`) with a
   Cursor-specific persona header and `.mdc` YAML frontmatter
   (`description`, empty `globs`, `alwaysApply: true`).
2. Add `.cursor/rules` to `scripts/lib/collaboration-template-paths.sh` so
   distribution/sync scripts pick it up like `.grok/rules`.
3. Fix `scripts/copy-ai-collaboration-files.sh`'s `replace_placeholders`
   file-extension case pattern to include `*.mdc` alongside
   `*.md|*.yml|*.yaml`, so placeholder substitution actually runs on the new
   Cursor rule files.
4. Add the three new files to the CI `repository-sanity` required-files
   check, and add `.cursor/rules/*.mdc` to the contract-traceability case
   pattern, in `.github/workflows/ci.yml`.
5. Add `.cursor/rules/*.mdc` to the Agent Operating Contract Files list in
   `docs/collaboration/prompt-instruction-change-control.md`.
6. Extend ADR 0006 in place (Context/Consequences/Enforcement) to name
   `.cursor/rules/*.mdc` and record the 2026-07-14 finding that Cursor and
   Grok Build now also read `AGENTS.md` (Grok Build: `CLAUDE.md` too)
   natively as a fallback, without changing the full-mirror decision.
7. Update `README.md` and `README.ja.md`: mention Cursor alongside
   Claude/Copilot/Codex/Grok in the agent list, explain why dedicated files
   are kept despite native `AGENTS.md` fallback support, add
   `.cursor/rules/` to the Directory Guide tree, and add `.grok/rules/*.md`
   plus `.cursor/rules/*.mdc` to the placeholder-fill instructions (the
   English README's list had not been updated with `.grok/rules/*.md` when
   LISS-0006 shipped; fixed here as a small, directly-related correction).
8. Update `docs/collaboration/adoption-guide.md`: add `.cursor/rules/*.mdc`
   to the placeholder-fill step, and add a note in the LLM Session Setup
   section explaining Cursor's `.mdc`-extension requirement, `alwaysApply`
   behavior, and native `AGENTS.md` fallback; extend the existing Grok note
   with the new `AGENTS.md`/`CLAUDE.md` fallback finding.

## Dependencies

- Parent:
- Depends on:
- Blocks:
- Related: LISS-0006 (Grok agent entry point, same precedent and pattern).

## Referee Decision Points

- Full-mirror vs. thin-pointer for `.cursor/rules/*.mdc`: resolved by
  following the Referee's existing LISS-0006 precedent (full mirror), not
  re-litigated here since the same reasoning applies (keep the pattern
  consistent across vendors, explicit stronger-binding entry point per
  tool).
- Whether to remove or shrink `.grok/rules/*.md` now that Grok Build reads
  `AGENTS.md`/`CLAUDE.md` natively: declined. `.grok/rules/*.md` was
  confirmed via live `grok inspect` testing (LISS-0006, 2026-07-08) as a
  stronger-binding discovery surface than generic context loading; native
  `AGENTS.md` reading is additive, not a replacement signal.

## Context

- Included: `AGENTS.md`, `.grok/rules/*.md` (as the mirror source),
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`,
  `scripts/copy-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`, `.github/workflows/ci.yml`,
  `README.md`, `README.ja.md`, `docs/collaboration/adoption-guide.md`,
  `docs/issues/LISS-0006-grok-agent-entry-point.md` and its trace (direct
  precedent).
- Omitted: full vendor documentation pages beyond what was needed to answer
  the specific discovery-order and file-format questions; no private or
  adopter-specific data was involved in this round (unlike LISS-0006, which
  was triggered by a specific adopter's feedback).
- Assumptions: Cursor's `.mdc` frontmatter requirements and Grok Build's
  `AGENTS.md`/`CLAUDE.md` native-reading behavior, both confirmed via live
  web search this session, are accurate as of 2026-07-14. These are
  fast-moving products (Grok Build itself launched in beta May 2026); if
  either vendor changes its convention again, the fix is confined to this
  file set, matching the same isolation property LISS-0006 relied on.

## AI Planning Records

### AIP-0010-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: no reasoning-effort label is exposed to this agent in this
    environment's output
- Created at: 2026-07-14
- Planning size: M
- Intended execution route: strong reasoning agent for the research
  synthesis and cross-file consistency work; live WebSearch/WebFetch to
  verify vendor documentation rather than relying on training knowledge
  (explicitly required by this template's anti-hallucination rules for
  external tool conventions); deterministic checks for verification
- Intended scope: three new `.cursor/rules/*.mdc` files, script fix, CI
  updates, ADR 0006 extension, README/README.ja/adoption-guide updates
- Estimated token range: 8,000-16,000
- Token metric: approximate total model tokens for research plus
  implementation
- Estimation basis: closely follows an already-established pattern
  (LISS-0006) with one new tool to onboard and two to re-verify; lower
  uncertainty than LISS-0006 since the mirror content already exists
- Assumptions: no application code changes; reuses `docs/templates/adr.md`
  (no new ADR needed — extending ADR 0006 in place, matching LISS-0006's own
  precedent for the same reason)
- Confidence: high
- Revises:
- Revision reason:
- Superseded by:

## References

- Referee request, 2026-07-14 (chat): "grok/cursor/codexの最新の情報を調べて
  テンプレートが働くように対応して."
- `docs/issues/LISS-0006-grok-agent-entry-point.md` and
  `docs/collaboration/traces/2026-07-08-grok-agent-entry-point.md` (direct
  precedent for both the investigation method and the full-mirror decision).
- Cursor Rules documentation (https://cursor.com/docs/rules), fetched
  2026-07-14: confirms `AGENTS.md` native support as a "simple alternative",
  `.cursor/rules/*.mdc` as the primary mechanism, `.mdc` extension/frontmatter
  requirement, and `alwaysApply` behavior.
- xAI Grok Build documentation and community references (search results
  2026-07-14, https://docs.x.ai/build/overview and related pages): confirm
  `AGENTS.md` read at three levels and `CLAUDE.md` read "for compatibility";
  could not fetch a page explicitly documenting `.grok/rules/` status
  directly (404 on a guessed URL), so this issue relies on LISS-0006's
  primary-source `grok inspect` confirmation for that surface, and the new
  search-result text for the `AGENTS.md`/`CLAUDE.md` fallback finding.
- OpenAI Codex documentation
  (https://developers.openai.com/codex/guides/agents-md,
  https://developers.openai.com/codex/config-reference), fetched via search
  2026-07-14: confirms discovery order and byte-limit configuration,
  consistent with LISS-0006's 2026-07-08 finding.

## Work Notes

- Implemented 2026-07-14 on branch `process/cursor-agent-entry-point`,
  created from `main` after the LISS-0008/LISS-0009 merge.
- Unlike LISS-0006, this round was not triggered by a specific adopter's
  feedback — the Referee asked directly for a research-and-refresh pass.

## Verification

- Docs-only except for the two shell-script edits
  (`copy-ai-collaboration-files.sh`, `collaboration-template-paths.sh`).
- `bash -n` on both touched shell scripts.
- CI required-files check reproduced locally with the three new
  `.cursor/rules/*.mdc` paths added.
- CI contract-traceability check reproduced locally.
- A live dry-run and non-dry-run execution of
  `copy-ai-collaboration-files.sh` against a throwaway target directory,
  confirming `.cursor/rules/*.mdc` is copied and both `<PROJECT_NAME...>`
  and stack placeholders are substituted (verifying the `*.mdc` glob fix).
- A trace under `docs/collaboration/traces/` accompanies this issue, per
  `prompt-instruction-change-control.md` (contract files touched).
