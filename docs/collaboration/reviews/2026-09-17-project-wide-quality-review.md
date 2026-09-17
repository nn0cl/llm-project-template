# P0–P3 統合検討・プロジェクト全体レビュー

Historical assessment: 以下は修正前のレビュー。
現在のdispositionは[実装レビュー](2026-09-17-quality-implementation.md)を参照。

- Date: 2026-09-17
- Reviewed revision: `384f2fed613e0650c020cae0b714c543f97113e7`
- Branch: `codex/feedback-verification-and-review-policy`
- Phase: Architecture Path / phase-0-design
- Scope approval: ユーザーによる P0/P1/P2/P3 の一括検討と全体レビュー。
- Implementation allowed: no。今回の成果物は調査・設計・修正候補。
- Isolation: `same_context`。live runtime-routing は存在せず既定を適用。
  独立コンテキストレビューより弱い。人間の承認を代替しない。
- Agreement / planning: [LISS-0027](../../issues/LISS-0027-integrated-quality-review.md)
- Evidence: [Trace](../traces/2026-09-17-integrated-quality-review.md)
- Canonical Register: live register は存在しない。以下の現行文書を直接参照。

## 結論

フィードバックの5論点を採用候補とする。加えて配布・更新・設定・承認検証で
7件を再現し、静的確認から5件の追加修正候補を抽出した。計17件。
既存CIのローカル実行可能な7チェックが成功しても、再現した7件は検出されない。
この事実から、ルール追記と同時に異常系の回帰検証を整備する必要がある。

優先度は実施順を示す。P0というラベルを、稼働中システムの重大障害が確認された
という意味では使わない。外部フィードバックのファイル行数、ImportError、
64.22%という値は申告情報であり、導入先コードがないため独立検証していない。

## 確認範囲・根拠文書

現行の `AGENTS.md`、`CLAUDE.md`、quickstart、AT-TDD、implementation-readiness、
ai-human-scheme、source-code-quality、definition-of-done、testing-strategy、
project-structure、runtime-routing、document-lifecycle、prompt-instruction-change-control、
branch-commit-pr-discipline、process-review、process-lessons、privacy-context-budget-policy、
model-tool-capability-matrix、local-issue-planning、adoption-guide を確認。
ADR 0004 / 0015、template-rollout仕様、レビュー・設定・PRテンプレートを再読。
Copilot/Grok/Cursorの共有ルールも検索・比較したが、全段落の形式的同値性の証明はしていない。

実行コードは `scripts/` の配布・更新・設定・初期化・2検証器と共有パス一覧、
`.github/workflows/ci.yml` を対象とした。研究記事は現行規則の根拠にしない。
未追跡の `NotebookLM_llm-project-template/`、導入先アプリ、外部アカウント、
GitHub保護設定、外部Actionの実体は対象外。全体レビューは全条件の網羅証明ではない。

## 指摘一覧

全件の disposition は **apply（修正候補として計画へ反映、未修正）**。
F01–F05はフィードバックの評価、F06–F12は再現済み、F13–F17は静的確認。

| ID | 優先度 | 修正点 | 根拠・影響・確認方法 |
| --- | --- | --- | --- |
| F01 | P0 | focused成功と全体Green、検証証拠の鮮度を分離 | `definition-of-done.md` Phase 2/3 と `at-tdd/process.md` は available な deterministic verification の実施に留まり、blocking suite一覧・対象SHA・環境・失敗差分を要求しない。PRテンプレートもCIチェックボックスのみ。関連テストだけで完了と読める。 |
| F02 | P1 | 分割時の実利用者の互換性を検証 | `source-code-quality.md` Splitting Rules と `testing-strategy.md` に利用者棚卸し、内部シンボル、import smoke、隣接回帰の契約がない。公開APIの形だけの検査では既存の非公開シンボル利用が漏れる。 |
| F03 | P1 | 仕様への対応・意味変更・テスト弱体化をレビュー項目にする | Phase 2の最小実装・テスト不変ルールは既にある。追加すべきは実行証拠であり、spec→変更→テスト対応、除外差分、エラー境界・順序・シリアライズの影響をreview-summary/same-context-review/PRで確認する。 |
| F04 | P2 | 実装本体を含む構造予算と例外処理 | ADR 0004 と source-code-quality は定性的。行数閾値、実装移設、例外の扱いは未定義。`update-ai-collaboration-files.sh`自身も682行、configureは330行。行数超過だけでは欠陥と断定しない。 |
| F05 | P3 | 規模判定とレビュー方式の設定を追加 | runtime-routing と ADR 0015 は固定の isolation/model のみ。same-context-reviewのL以上・契約変更時のエスカレーション、process-reviewのsame-context既定との優先関係を一緒に定義する必要がある。 |
| F06 | P1 | ブランチ作成失敗前の書換えを防ぐ | `scripts/update-ai-collaboration-files.sh:554` はprocess_fileで書換え済み。ブランチ存在検査は604行、作成は609行。生成予定ブランチを先に作ったfixtureでexit 1となり、mainのAGENTS.mdがversion twoに変わったまま。事前検査→隔離→適用の順へ。 |
| F07 | P1 | copy再実行で同期マーカーを誤更新しない | `scripts/copy-ai-collaboration-files.sh:178` は既存ファイルのskipに関係なくHEADを記録。古いAGENTSを残してcopyすると旧markerだけが最新になる。続くupdateはalready syncedで終了でき、未適用変更を失う。既存marker保持・初回部分採用の扱いを定義する。 |
| F08 | P1 | 有効期限切れの実行承認を拒否 | `scripts/check-execution-batch-reviews.py:127` はexpires_at > approved_atだけを検査。2020年に期限切れのin_progressを当該batch branchで検証しても成功。活動中の承認には現在時刻との比較が必要。過去の完了記録を一律に失敗させない。 |
| F09 | P1 | post_reviewedでallowed_paths検査が消えないようにする | 同検証器171行の対象statusにpost_reviewedがない。許可外outside.txtをコミット後、review済みフィールドを揃えると当該batch branchで検証成功。承認した差分の終端SHAを固定し、完了後の追記も捕捉する。レビュー者認証とは別の整合性検査。 |
| F10 | P2 | 導入時の文字列をデータとして置換 | `scripts/copy-ai-collaboration-files.sh:141` は `/` と `&` のみescapeし、Perl replacementへ展開する。project-name `Price $5 @home` が `Price  ` になる。ドル・アット・バックスラッシュ等を含む入力の往復検証が必要。 |
| F11 | P2 | TOMLモデル名の多重escapeを修正 | `scripts/configure-ai-collaboration.sh:289` のawk -vがTOML用escapeを再解釈。文字列 `host\name` はTOMLで読み戻すと改行を含む別値になった。構文grepでなくparse後の値一致で検証する。 |
| F12 | P2 | Current registerの根拠placeholderを拒否 | `scripts/check-document-lifecycle.py:85` はsource_pathsが非空なら通し、88行はplaceholderをskip。Current行にsource_paths=`<missing>`だけを入れても成功。空のフォームと記入済みCurrent行を区別する。 |
| F13 | P1 | 配布内容と記録SHAを一致させる | copyは182行、updateは285行付近でHEADを記録する一方、配布内容は作業ツリーのcp/find。source側dirtyを検査しない。未コミット/未追跡ファイルが配布されても同じSHAが記録される。コミットsnapshotから列挙・コピーするか、dirty sourceを明示拒否する。 |
| F14 | P2 | 選択したbase branchをPRへ渡す | updateのselect_base_branchとPR本文はbaseを選ぶが、末尾の`gh pr create`に`--base`がない。選択branchがremote defaultと異なる場合、PR比較先が意図とずれる可能性。CLI呼出しをstubで確認する回帰テストを追加。実GitHub送信は未実施。 |
| F15 | P1 | 番号衝突中のauto-merge要求を拒否 | updateはcollisionsを警告するだけで、末尾の`--merge-pr`経路へ進む。CIにもADR番号一意性チェックがない。文書上の「衝突解消前にmerge禁止」を自動経路でも守る。GitHub実動作は未実施。 |
| F16 | P1 | 更新・失敗系・値保存を既存CIへ追加 | `.github/workflows/ci.yml` のsmokeはcopyと通常設定を中心に検証。update実行、期限切れ、許可外差分、特殊文字の往復がない。batch検査はこのrepoで0件、lifecycleの1件は空フォームであり、実データ網羅を意味しない。 |
| F17 | P2 | 導入先固有の構造・テスト定義の所有権を統一 | `project-structure.md`は導入先の実layoutへの置換を要求し、testing-strategyにも導入先用placeholderがある。一方共有pathsは`docs/architecture`全体をtemplate-authoritativeとして配布する。双方変更時に導入先の設定を上書きし得る。具体layout/テストcommandはtarget-owned側へ寄せ、共通規則から参照する。 |

## P0–P3を一括で扱う統合設計案

以下は採用前の提案。現行規則・承認済みADRを置き換えるものではない。

### 検証契約（P0/P1）

1. 導入先のblocking suite一覧・コマンド・必要環境・許可された除外をtarget-ownedな
   定義に置く。focused、隣接回帰、import smoke、全blockingを別の結果として残す。
2. 結果は `passed / failed / not_run / environment_blocked / excluded` を区別。
   部分実行や既知失敗をGreenと呼ばない。全blockingが成功した場合だけ全体Green。
   承認済み除外があればその限定を明示し、失敗をIssue化しただけでは除外にしない。
3. commit SHA、tree/dirty状態、base SHA、コマンド、作業dir、OS/runtime/依存版、
   開始終了時刻、exit code、総数/失敗/skip/collection error、ログ所在を保存。
   テスト数を取得できない検査はunknown/N/Aとし、0件成功と偽らない。
4. baselineと候補の失敗ID集合を同等環境で比較。失敗原因数と影響テスト/スイート数を分離。
   import/collectionで未実行になったケースは失敗件数に無理に変換せず、未評価範囲を記録。
   baseline再現不能なら新規失敗0件とは報告しない。
5. 最終コミット後のSHAで全blockingを実行し、結果はそのSHAに紐づくCI成果物等に保存。
   証拠ファイルを追ってコミットする場合は新HEADを未検証と扱い、再実行する。
   文書だけの変更という暗黙免除は設けない。merge後のSHAの保証はbranch検証と区別する。
6. 分割前後にimport元と使用シンボル、非公開参照、re-export、CLI入口、動的import、
   plugin/registration、循環依存を調査。静的検索の限界を残し、実利用者のsmokeで補う。
7. Phase 1の期待RedはGreenとは別の状態として記録。今回新たにActive-Red管理の実装まで
   引き受けるものではなく、導入先固有の管理がある場合に誤ったGreenへ統合しない。

### 構造予算（P2）

- target-ownedの設定を持ち、300行は初期提案値・分割検討トリガーとする。
  ファサードと移設先、private/legacy/helperも含める。generated/vendor除外を明示する。
- ソースfileの物理行数と変更行数は異なる指標。全source上限とimplementation上限を
  両方置く場合は分類・優先順位を定義する。変更量はbaseとの差分の追加+削除と定義。
- 超過時は責務分割、理由付き維持、期限/owner付き後続Issue、明示例外のいずれかを記録。
  自動分割はしない。後続Issueはblocking failureを免除する仕組みにはしない。
- 機械計測できる行数/関数/クラス/import graphと、人間・agentによる責務の評価を分離。
  未対応言語はunknown、責務数は判断根拠付き。見かけ上のファイル短縮を完了証拠にしない。

### 規模に応じたレビュー（P3）

- `[review.large_change]`はopt-in。設定なし/disabledでは既存`[review]`を適用する。
  disabledは、通常のreviewやAdjudicator承認の免除を意味しない。
- 提案: 有効な条件のORで発動。変更対象の実装fileが300行超、追加+削除500行超、
  変更file数5超、または複数の論理module境界をまたぐ場合。等号・削除・rename・binary・
  generated除外・diff基準を受入例に固定する。閾値は設定可能。
- `cross_module_required`は「発動条件」か「他条件とのAND」か曖昧なので、
  明確な名前とtruth tableを仕様に置く。moduleはディレクトリ数で代用しない。
- 巨大fileから小fileへ抽出する変更を取りこぼさないよう、base/候補双方の行数を見る。
  不完全な差分/計測不能をsmall changeと推測しない。
- isolationと任意modelをoverride可能とする。予算は入力コンテキストとreview範囲を
  絞る設計に使い、上限超過時に黙ってsame_contextへ弱めない。利用不能/予算不足は
  未完了として人間へ返す。推定tokenと実測tokenは区別する。
- ADR 0015の「既に要求されるreviewのrouting」と、新しくgateを発動する設計は別。
  提案はまず既存reviewの強度を選ぶ方式。規模だけで新規gateを追加する場合は明示決定する。
- same-context-reviewの強制エスカレーションとprocess-reviewの役割も整合させる。
  プロダクトレビューと運用手順の振り返りを重複させない。

## 推奨実施順・受入例

一つの統合計画として追跡し、変更の依存順でreviewableな単位に分ける。

| 順序 | 対象 | 受入条件の例 |
| --- | --- | --- |
| 1 | F01–F05の仕様・ADR案、F06–F17の回帰仕様 | 全17件の修正対象と検証方法が対応。新規gate、所有権、例外の意味を人間がreviewできる。 |
| 2 | F06–F15の再現ケース、F16の検証入口 | 既存不具合をRedで確認。branch衝突時のtree/HEAD不変、marker保持、期限/差分拒否、特殊文字往復、Current根拠必須。 |
| 3 | 配布・承認・設定の修正とP0/P1契約 | 通常経路と異常経路の両方が成功。failed/未実行からGreenを生成しない。内部シンボル利用の回帰fixtureを含む。 |
| 4 | P2/P3設定・判定とF17所有権 | 299/300/301行、499/500/501変更行、4/5/6files、disabled/設定なし/不正設定、unknown、レビュー利用不能を検証。導入先設定がsyncで保持される。 |
| 5 | 契約の横断整合・全blocking・最終review | 全agent入口、skill、DoD、PR、設定フォーム、CLI、copy/update、CIが一致。対象SHAを明示した最終検証と必要な人間review。 |

現在は順序1の前段レビュー完了。受入仕様・ADRの正式案、Phase 1/2/3は未実施。

## 検証証拠

- Environment: Darwin arm64、Bash 3.2.57、Python 3.14.6。
- 検証時HEAD: 冒頭のSHA。実装・設定・CIは変更前のまま。
- `bash -n scripts/*.sh scripts/lib/collaboration-template-paths.sh`: 成功。
- `python3 scripts/check-document-lifecycle.py`: 成功、1 register（template）。
- `python3 scripts/check-execution-batch-reviews.py --branch codex/feedback-verification-and-review-policy`:
  成功、0 records。
- `.github/workflows/ci.yml` の7つのrun blockをBashで実行:
  required documents / ADRs / syntax / batch / lifecycle / conflict markers / copy smoke は7成功、0失敗。
  PR base/headを必要とするtraceabilityは未実行。GitHub hosted CI成功とは報告しない。
- 一時fixtureでF06–F12を7件再現。診断は「不具合が存在する」結果であり、修正後Greenではない。
- `git diff --check`: 成功。新規Markdownは別途空白検査。

再現手順（全て一時ディレクトリで実施。実利用者のrepoを使わない）:

1. F06: sourceにAGENTS v1/v2の2commit、targetにv1と旧markerを用意。
   targetに生成予定名`process/update-collab-template-YYYYMMDD-<v2 sha8>`のbranchを事前作成。
   update `--source SOURCE --target TARGET --delivery local --non-interactive`を実行。
   exit 1、branch=main、`git status --porcelain`=` M AGENTS.md`、内容v2を確認。
2. F07: copy済みtargetのmarkerを旧値、AGENTSを旧内容にしてcopyを再実行。
   AGENTSは旧内容のまま、markerのみ現在SHAへ更新される。
3. F08/F09: 検証器の`validate_record`へ一時git repoと有効な形式のrecordを渡す。
   F08はapproved_at=2020-01-01、expires_at=2020-01-02、status=in_progress、
   current_branch=execution_branch。F09はallowed_paths=`docs/**`として
   approval後にoutside.txtをcommitし、status=post_reviewedと必要review項目を埋める。
   両方ともValueErrorを発生させず受理する。
4. F10: copy `--project-name 'Price $5 @home'`。conventionsのName=`Price  `。
5. F11: configure `--review-model 'host\name'`。
   Python `tomllib.loads(...)["review"]["model"]`と入力の比較がFalse。
6. F12: 実在rule.mdをentry/canonicalとするCurrent行でsource_pathsを`<missing>`にする。
   lifecycle `--root FIXTURE`がexit 0。

## 次の決定と残存事項

- 次の作業候補: 統合受入仕様とADR案の具体化、後にPhase 1の回帰テスト。
- 追加の外部送信、PR作成、merge、実装修正は行っていない。
- 独立review、Linuxでの再現、GitHub delivery、動的依存解析は未実施。
- 本レビューの完了と、17件の修正完了を区別する。Issueはreviewのまま。
