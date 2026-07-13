# Shared path list for the AI-human collaboration template.
#
# Sourced by scripts/copy-ai-collaboration-files.sh and
# scripts/update-ai-collaboration-files.sh so both scripts stay in sync about
# which paths belong to the reusable template.

collaboration_template_paths=(
  "AGENTS.md"
  "CLAUDE.md"
  "README.md"
  "README.ja.md"
  ".github/copilot-instructions.md"
  ".grok/rules"
  ".cursor/rules"
  ".github/dependabot.yml"
  ".github/pull_request_template.md"
  ".github/ISSUE_TEMPLATE"
  ".github/workflows/ci.yml"
  "docs/architecture"
  "docs/at-tdd"
  "docs/collaboration"
  "docs/evaluation"
  "docs/issues"
  "docs/specs"
  "docs/templates"
  "docs/work-plans"
  "scripts/copy-ai-collaboration-files.sh"
  "scripts/update-ai-collaboration-files.sh"
  "scripts/init-llm-context.sh"
  "scripts/lib/collaboration-template-paths.sh"
)
