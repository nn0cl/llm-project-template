# Dependency Policy

Dependency relationships must be checked by tools as the implementation grows.

Pick and configure the tools that match your stack. See
`docs/templates/examples/` for two worked examples (`cargo-deny` for Rust,
`dependency-cruiser` for a TypeScript front-end) — copy the pattern for
whatever language and package ecosystem this project actually uses.

## Package-Level Dependency Checks

Use a package-dependency auditing tool (e.g. `cargo-deny`, `npm audit` /
`pip-audit` / `osv-scanner`) once the corresponding project manifest exists.

Initial responsibilities:

- detect vulnerable dependencies.
- enforce license policy.
- detect duplicate or banned packages when configured.
- make dependency decisions visible in CI.

These tools do not replace Clean Architecture review. They check package-level
dependency policy, not whether a module imported the wrong local module.

## Import-Boundary Checks

Use an import-boundary tool (e.g. `dependency-cruiser` for TypeScript,
`import-linter` for Python) once the corresponding front-end or backend
project exists.

Initial responsibilities:

- prevent UI components from importing backend transport/provider SDKs
  directly.
- keep feature, entity, and shared boundaries visible.
- detect circular imports.

## CI Rule

Dependency policy checks should be conditional until the relevant
implementation exists — gate each job on the presence of the corresponding
manifest or config file (see the commented-out example jobs in
`.github/workflows/ci.yml`).

## Not a Substitute

These tools do not decide architecture. ADRs and AT-TDD specifications remain
the source of design decisions.
