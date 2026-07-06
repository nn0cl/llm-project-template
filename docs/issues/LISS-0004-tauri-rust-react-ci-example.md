# LISS-0004: Tauri + Rust + React example CI job

## Metadata

- Local issue ID: LISS-0004
- GitHub issue:
- Status: proposed
- Phase: phase-0-design
- Type: docs/example
- Priority: low
- Owner/agent:
- Related branch:

## Summary

- `docs/templates/examples/` ships stack-neutral placeholders; concrete CI
  jobs are correctly left to each adopting project. An external adopter
  (voice-to-dic) building on Tauri + Rust + React reported that getting a
  green CI job from a fresh Ubuntu runner took five separate debugging
  iterations (missing `libwebkit2gtk`/`libayatana-appindicator3`/
  `librsvg2`/`libxdo`/`libssl` dev packages, missing `libasound2-dev` for
  `cpal`, `actions/setup-node`'s `cache: pnpm` needing `corepack enable`
  first, a GPU-acceleration Cargo feature needing an `cfg(target_os =
  "macos")` gate, and `tauri::generate_context!()` needing `frontend/dist`
  to exist even for a Rust-only `cargo test` job). They offered to
  contribute their now-working job definitions back.

## Acceptance Notes (proposed, not yet accepted)

- Add a tested, working example CI job (or at minimum a troubleshooting
  checklist) for the Tauri + Rust + React stack under
  `docs/templates/examples/`, sourced from a real contributed job
  definition rather than fabricated from general knowledge of the stack.
- Do not merge unverified CI YAML for this stack; this repository has not
  independently verified the specific package/flag list above.

## Dependencies

- Parent:
- Depends on: a contributed, verified job definition (e.g. from
  voice-to-dic) or independent verification by this repository.
- Blocks:
- Related: LISS-0002

## Referee Decision Points

- Not yet reviewed. Left at `proposed` pending either a contributed,
  verified job definition or this repository independently verifying the
  troubleshooting list end to end.

## Context

- Included: `docs/templates/examples/`.
- Omitted: the specific CI YAML content (not yet verified by this
  repository).

## References

- External feedback report from voice-to-dic's first pull-sync, finding 5.

## Work Notes

- None yet; this is a backlog placeholder inviting a contribution.

## Verification

- N/A until a concrete job definition is contributed and verified green on
  a fresh runner.
