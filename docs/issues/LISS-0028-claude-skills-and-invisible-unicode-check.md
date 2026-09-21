# LISS-0028: Claude Code用skillsの追加と不可視Unicode検出CI

## Metadata

- Local issue ID: LISS-0028
- GitHub issue: none
- Status: review
- Phase: process-only
- Type: process / ci
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: none
- Owner/agent: Claude Code
- Related branch: process/liss-0028-claude-skills-and-unicode-check

## Summary

2026-09のClaude更新調査で、Claude Codeが`.agents/skills/`を読まず、
`.claude/skills/`だけをskillの探索場所とすることを公式ドキュメントで確認した。
Claude Codeがskillを説明文から自動で読み込めるよう、`.claude/skills/`を追加する。
あわせて、エージェントが読む追跡対象テキストに不可視Unicodeが混入していないかを
CIで検出する。

## Acceptance Notes

1. `.claude/skills/<name>/SKILL.md`が`.agents/skills/<name>/SKILL.md`と
   バイト単位で一致する（全文コピー、Adjudicator選択）。
2. CIが両ツリーの差分を拒否する。copy/updateが`.claude/skills/`を配布し、
   `.claude/settings.local.json`は配布しない。
3. `scripts/check-invisible-unicode.py`がGit追跡対象のUTF-8テキスト全体を検査し、
   Cfカテゴリ・異体字セレクタ・ハングルフィラーを位置付きで拒否する。
   バイナリと未追跡ファイルは対象外。CIのブロッキング手順に入れ、配布対象にする。
4. 拒否経路（ゼロ幅、双方向制御、タグ文字、異体字セレクタ、BOM）と、
   通過経路（通常の日本語/英語、バイナリ、未追跡）を回帰テストで示す。
5. ADR 0018の決定5を改訂し、ADR 0006と変更管理文書に新しいCI検査を記録する。

## Dependencies

- Parent: none
- Depends on: none
- Blocks: none
- Related: ADR 0006, ADR 0018

## Adjudicator Decision Points

- [x] `.claude/skills/`を追加する（2026-09-21指示）。
- [x] 形式は全文コピー（薄いラッパー案は不採用、2026-09-21選択）。
- [x] 不可視Unicode検出の範囲はGit追跡対象の全テキスト（2026-09-21選択）。
- [ ] 実装レビューとマージ承認。

## Context

- Included: Claude Code skills/memory公式ドキュメント、ADR 0006/0018、
  配布パス一覧、CI、回帰テスト基盤。
- Omitted: 他ツールのskill探索仕様の再確認（今回変更しない）。
- Assumptions: 許可リストは設けない（導入時点で該当文字0件）。
  シンボリックリンクは配布スクリプトが`find -type f`で扱わないため不採用。

## AI Planning Records

### AIP-0028-001

- Status: accepted（2026-09-21の実施指示と2点の選択により）
- Created by:
  - Agent/environment: Claude Code / desktop app
  - Model as displayed: claude-opus-5
  - Reasoning setting as displayed: N/A
  - N/A reason: ホストが推論設定を表示しない
- Created at: 2026-09-21
- Planning size: M
- Intended execution route: host agent + deterministic checks（unittest、CI手順のローカル再現）
- Intended scope: `.claude/skills/`、検出スクリプトとテスト、CI、配布パス、ADR 0006/0018、変更管理文書、adoption-guide
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: 複数ファイル（CI・配布・文書・テスト）にまたがるためM。
- Assumptions: ネットワーク不要の決定的検証で完結する。
- Confidence: medium
- Revises: none
- Revision reason: none
- Superseded by: none

## References

- https://code.claude.com/docs/en/skills （2026-09-21 fetch確認）
- https://code.claude.com/docs/en/memory （2026-09-21 fetch確認）

## Work Notes

- 導入前に追跡対象全テキストを走査し、該当文字0件を確認した。

## Verification

- `docs/collaboration/traces/2026-09-21-claude-skills-and-unicode-check.md`を参照。

## Process Review

- Outcome: not yet
- Lesson written: not applicable
- Template-feedback path: none
