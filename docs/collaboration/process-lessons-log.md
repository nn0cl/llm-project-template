# Process Lessons Log

Target-owned. Created from `docs/templates/process-lesson.md`. Do not store
secrets. Policy: `docs/collaboration/process-lessons.md`.

Record meta-level patterns only. No session transcripts.

## Lesson

- Date: 2026-08-26
- Class: status-drift
- Pattern: ISSUE and work-plan status stayed `review` or `in_progress` after
  the work had already merged to `main`. Later agents treating the ledger as
  current work would resume closed process changes.
- What later design or implementation must do: when a process PR merges,
  update the issue and work-plan status in the same context or immediately
  after. Leftover `review` / `in_progress` after merge is ledger drift, not
  open work.
- Source issue or work plan (adopter's own ID, if any): LISS-0024
- Status: applied

## Lesson

- Date: 2026-09-17
- Class: verification-coverage
- Pattern: validatorやsmokeの成功だけでは、不正な承認記録の拒否、特殊文字の保存、
  失敗時の状態保全を確認できない。検証対象0件や空フォームの成功も網羅性を示さない。
- What later design or implementation must do: 正常系に加え、期限切れ・許可外差分・
  部分失敗・入力往復の受入例を定義し、基準SHA/環境/検証対象件数を示す。
  focused成功と全体検証、診断での不具合再現と修正後Greenを分けて報告する。
- Source issue or work plan: LISS-0027
- Status: applied（拒否経路と文字列往復の恒久回帰テスト、SHA付き検証出力を追加。
  focused結果と全CI実行の記録は分離）

## Lesson

- Date: 2026-08-26
- Class: other
- Pattern: two local issues shared one LISS ID. Filename uniqueness is not
  the same as ID uniqueness; skipped numbers must stay unused.
- What later design or implementation must do: assign the next free ID only
  after listing existing `docs/issues/LISS-*` files and their metadata IDs.
  Do not reuse a skipped or colliding number. If a collision is found, keep
  the earlier claim on the ID and renumber the later file.
- Source issue or work plan (adopter's own ID, if any): LISS-0024
- Status: applied
