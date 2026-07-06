# Referee とフェーズ

2026-07-05。非規範。関連: ADR 0003、`docs/at-tdd/process.md`。

---

human-in-the-loop は必要だ、という合意だけでは足りない。どこに人間を置くかが
設計されていなければ、結局は全出力の監視か、全出力の放置のどちらかになる。
前者は持続不可能で、後者は責任が宙に浮く。私は第三の形を採る。人間は決定点を
所有し、それ以外はエージェントに委ねる。

Referee はフェーズ遷移の承認、ADR の受理、Phase 1 テストのレビュー、曖昧な選択の
決定を所有する。エージェントは設計インテーク、コンテキストの選択、フェーズに
適合した成果物の生成、仮定の可視化、決定的検証、handoff を所有する。境界が
文書化されていること自体が、協働の前提である（ADR 0003）。

## AT-TDD

開発サイクルは ATDD と TDD のハイブリッドとして定義する。受入仕様が失敗する
テストを駆動し、レビュー済みのテストが最小実装を駆動し、リファクタリングは
Green のあとにだけ行う。Red / Green / Refactor は
[Martin Fowler の TDD 説明](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
（取得 2026-07-07。「Write a test → make it pass → refactor」の三手順を確認）
に連なるが、本テンプレートの独自性は、この規律を人間の自制ではなくエージェントへの
承認ゲートとして外部化した点にある。

「AT-TDD」という語を業界標準の別名として売り込むつもりはない。README にその
注記があるのは、誠実さのためだ。呼び名より、ゲートの実在が重要である。

## フェーズスキップを止める

曖昧な依頼から本番コードへ直行する——これはエージェント特有の失敗様式である。
フェーズスキップの禁止が第一の防壁になる。Red のあとに Green を、Green のあとに
Refactor を。Phase 1 のテストがレビューされないまま Phase 2 に入ることを、
プロセスとして許さない。

受入仕様駆動の系譜は [Gojko Adzic: Specification by Example](https://gojko.net/books/specification-by-example/)
（取得 2026-07-07、書籍紹介ページ存在確認）や
[Cucumber の BDD 文書](https://cucumber.io/docs/bdd/)（取得 2026-07-07、ページ存在確認）
に連なる。実装前に具体例で合意する原則は、AI 協働では推測余地を塞ぐ手段になる。
入力側の曖昧性抑制には EARS 記法
（[Mavin et al., IEEE RE'09](https://ieeexplore.ieee.org/document/5328509)、
取得 2026-07-07、IEEE Xplore 上の論文ページ存在確認）も有効である。

## 注意力は希少資源

人間のレビューは全トークンに向けるべきではない。ADR 0003 は "Human review is
focused on decision points instead of every token of output" と述べる。注意力は
希少資源として設計に組み込む。ゲートの数を増やすことが目的ではない。決定点の
質を保つことが目的である。テンプレートを書類仕事にしてしまうリスク——ADR 0003
が Negative として挙げるもの——は、常に意識しなければならない。

## 能力向上はゲート撤廃の理由にならない

モデルが強くなっても Referee の所有権は変わらない。ゲートは能力不足の一時しのぎ
ではなく、責任と監査可能性のための構造である。エージェントがより多くを生成できる
ほど、決定点の設計はむしろ重要になる。

## 参考文献

1. 内部: `docs/architecture/adr/0003-ai-human-collaboration-governance.md`、
   `docs/at-tdd/process.md`、`README.md`、`docs/collaboration/template-benefits.md`
2. Fowler, M. *Test Driven Development*.
   https://martinfowler.com/bliki/TestDrivenDevelopment.html （取得 2026-07-07）
3. Adzic, G. *Specification by Example*.
   https://gojko.net/books/specification-by-example/ （取得 2026-07-07）
4. Cucumber. *Behaviour-Driven Development*.
   https://cucumber.io/docs/bdd/ （取得 2026-07-07）
5. Mavin, A. et al. "Easy Approach to Requirements Syntax (EARS)." IEEE RE'09.
   https://ieeexplore.ieee.org/document/5328509 （取得 2026-07-07）
6. Anthropic. *Building effective agents*.
   https://www.anthropic.com/research/building-effective-agents （取得 2026-07-07）