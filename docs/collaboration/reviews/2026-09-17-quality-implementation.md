# Integrated quality implementation review

- Date: 2026-09-17
- Agreement: [LISS-0027](../../issues/LISS-0027-integrated-quality-review.md)
- Acceptance: [quality-and-review](../../specs/quality-and-review.md)
- Architecture: [ADR 0019](../../architecture/adr/0019-verification-structure-and-review.md)
- Initial evidence: [17 findings](2026-09-17-project-wide-quality-review.md)
- Trace: [execution record](../traces/2026-09-17-integrated-quality-review.md)
- Approved scope: 統合計画による修正開始。実装済み、最終人間reviewは未完了。
- Review isolation: same_context（live設定なし）。独立reviewではない。
- Current phase: phase-3-refactor / final verification and review。
- Next approval type: final human review of contract/implementation; no merge authorization.

## Disposition and verification mapping

| Findings | Disposition | Artifacts / evidence |
| --- | --- | --- |
| F01 | implemented | verification-policy、verification-record、DoD、AT-TDD、PR、SHA/count付きregression runner。全blockingはCI各run blockと区別。 |
| F02/F03 | implemented as process contracts | consumer/private import棚卸し、smoke/隣接回帰、意味/テスト/除外差分とspec対応を各review入口へ追加。導入先の全言語依存解析は実装していない。 |
| F04 | implemented | TOML structure予算、Git base/head計測、Python syntax counts/imports、責務/循環の未評価表示、例外disposition。 |
| F05 | implemented | opt-in OR判定、strict thresholds、unknown→ask、model/budget、後方互換。routing7tests、Git計測6tests。 |
| F06/F07/F13 | implemented | branch事前検査、適用前branch作成、既存marker保持、配布対象dirty source拒否。distribution tests。 |
| F08/F09 | implemented | 期限切れactive拒否、statusに依存せず当該batch branchのpath制限。historical正常系と拒否経路を検証。 |
| F10/F11 | implemented | Perl/awkへ文字列を環境経由で渡して再解釈を防止。特殊文字/TOML往復を検証。 |
| F12 | implemented | Current registerのplaceholder source拒否、未記入フォームは保持。validator test。 |
| F14/F15 | implemented | ghにbase/body-fileを渡す。番号衝突時はlocal commit後に停止しpush/PR/mergeしない。local bare remoteとCLI stubで検証。 |
| F16 | implemented | CIにregression runnerを追加。既存正常系と拒否系、値保存、Git計測を一括実行。 |
| F17 | implemented | layout/testing文書の固有placeholderを廃止。実値をtarget-owned conventionsに集約。旧導入先の移行手順をadoption-guideへ追加。 |

## Evidence and limits

- Baseline SHA: `384f2fed613e0650c020cae0b714c543f97113e7`。
- Environment: Darwin arm64、Bash 3.2.57、Python 3.14.6、Python外部依存なし。
- Initial regression Red: 14件中11失敗、3成功。対象の不具合が原因、collection errorなし。
- 修正後の同14件は成功。新規routing7件は7 Redから7 Green。
- 27件時点のregression: 27成功、0失敗/エラー/skip。
- 追加4件: rejected状態のpath検査、dirty sourceでのupdate拒否、新設定フォーム/上書き拒否、
  model改行の拒否。最終31件の結果は最終commit後のregression JSONとCI run logsを参照。
- 全CI run blockはlocal shellで実行。snapshot段階では8成功、PR-contextの1件は未実行。
  最終commit後はbase/headを指定して9件を再実行する。GitHub hosted CIの成功とは区別する。
- 最終SHAの証拠はrepo外に保存して最終応答へリンクする。今後のcommitで再検証が必要。

## Review notes

- Re-read: 配布/設定/update、source-clean、validator、review_policy/change_metrics/CLI、
  全回帰テスト、CI、verification/source-quality/runtime policyとagent共有追記を確認。
- 正常系だけでなくbranch衝突、文字列変質、承認失効、許可外変更、未知情報を検査した。
- P2/P3の自動判定は数量と設定だけを扱う。責務の数/意味、動的import、解決済み依存graph/
  循環はreviewまたは導入先ツールで確認する。未評価を0件や問題なしとして扱わない。
- update中のI/O失敗は専用review branchに部分差分を残す場合がある。
  transactional rollbackは今回追加せず、成功として扱わず復旧対象とする。
- 既存update/configure CLIは300行を超える。今回は互換性修正を優先し既存の
  CLI制御フローを維持する理由付きdisposition。source整合性検査は共通helperへ分離。
  薄いfacade化を分割完了とは主張しない。新規policy/Git adapter/CLIはそれぞれ別責務。
- Exclusions: テスト除外なし。導入先固有実装、Linux実行、実GitHub送信、独立reviewは未実施。
- 全agent入口の追加契約は同じ内容。process reviewと独立product reviewの役割を整理。
- Lessons: 正常系Greenと検証網羅性の違いを恒久テストへ反映。

## Remaining human review

契約変更とADR、large-changeの既定値/unknown挙動、source dirty拒否による運用変更、
長大な既存CLIを維持する理由を確認する。Issueはreviewで保持し、done/mergeは主張しない。
