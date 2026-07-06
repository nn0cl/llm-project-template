# 出力の契約

2026-07-05。非規範。関連: ADR 0002。

---

流暢な散文は、正しさの保証ではない。LLM はそれらしく書けるが、事実性を保証しない。
Ji et al. のハルシネーション調査
（[arXiv:2202.03629](https://arxiv.org/abs/2202.03629)、取得 2026-07-07、
ACM Computing Surveys (2022) 掲載・抄録確認）は、生成の流暢さと事実性が独立しうる
ことを体系的に整理している。だから私は「信用」を「検証可能性」に置き換える。

ADR 0002 が拒否するのは、検証も出典追跡も人間レビューも、信頼できるストアへの
安全な書き戻しもできない散文である——"useful-looking prose that cannot be validated,
traced to source evidence, reviewed by a human, or safely written back into any trusted
store"。出力は最初から、拒否・レビュー・永続化が可能な形で受け取られなければならない。

## 推論は証拠として残す

推論を隠れた思考として扱わない。監査可能な証拠として扱う。ユーザー可視の内容や
永続状態に影響するなら、根拠、引用、出典スパン、仮定、棄却した代替案、確信度、
レビュー状態を記録する（ADR 0002）。ただし記録するのは chain-of-thought の生ダンプ
ではない。構造化された証拠である。私的な思考過程を露出させず、差分としてレビュー
できる形だけを残す。

## レビューで拒否できる規則に落とす

理念で終わらせない。自由記述の AI 散文を信頼できるドメインデータとして扱う
use case は reject する。出典証拠もレビュー状態も伴わず永続化された AI 由来の
知識も reject する（ADR 0002 Enforcement）。散文を業務事実として DB に書き込む設計は、
最初から許容しない。

スキーマで検証可能な出力は、主要プロバイダが一級機能として提供し始めている。
[Anthropic: Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
（取得 2026-07-07、ドキュメントページ存在確認）はその一例である。出力契約を先に
定め、SDK の応答を domain に直接返さない adapter 規律は、この機能を Clean
Architecture の境界に合わせる形だ。

## このフォルダ自身の作法

research の出典に取得日を付し、未検証 URL を明記する運用は、同じ契約を人間向け
文書へ適用したものである。推測で文献を補わない。ハルシネーションをコードだけの
問題と見なさない。文書も同じ防壁が要る。

## 参考文献

1. 内部: `docs/architecture/adr/0002-input-output-reasoning-contracts.md`、
   `docs/architecture/io-reasoning-contracts.md`、`docs/research/README.md`
2. Ji, Z. et al. "Survey of Hallucination in Natural Language Generation."
   arXiv:2202.03629. https://arxiv.org/abs/2202.03629 （取得 2026-07-07）
3. Anthropic. *Structured outputs*.
   https://platform.claude.com/docs/en/build-with-claude/structured-outputs
   （取得 2026-07-07）