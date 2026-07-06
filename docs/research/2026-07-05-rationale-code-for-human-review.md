# レビュー可能なコード

2026-07-05。非規範。関連: ADR 0004。

---

生成コストがほぼゼロになったとき、ボトルネックは書く速度から検証する速度へ移る。
かつて「書く手間」が自然に抑えていた複雑性は、もはど自動的には生まれない。
だから規範として復元する。生成コードの最適化目標は「動く最小」ではなく、
人間の認知負荷の最小である（CLAUDE.md、ADR 0004）。

テストを通すためだけの dense な Green は、acceptable Green ではない。
賢い圧縮より読める冗長を選ぶ。"Do not compress implementation into dense code
just to be minimal"——この釘は、AI 時代だからこそ必要になる。

## 理解がレビューの主戦場

Bacchelli & Bird の大規模調査
（[ICSE 2013](https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/)、
取得 2026-07-07、Microsoft Research 上の論文ページ存在確認）は、コードレビューの
最大の課題が変更の理解にあることを示した。欠陥発見より先に、読めるかどうかが
問われる。レビューしやすさは理解しやすさと同義だ。

Ousterhout は複雑性を、システムを理解・変更しにくくするものと定義する
（[*A Philosophy of Software Design*](https://web.stanford.edu/~ouster/cgi-bin/book.php)、
取得 2026-07-07、書籍紹介ページ存在確認）。浅いモジュールと不要な間接化を戒める
立場は、ADR 0004 の「まとめておくべき兆候」と一致する。分割は善ではない。
読者が同時に保持すべき業務判断が一つを超えるとき、分ける。責務を減らさない
間接化のためだけに分けてはならない。

## 依存方向は認知負荷の規律

domain がフレームワーク知識なしに読めること、business policy が adapter に
漏れ出さないこと——Clean Architecture の依存規律は、レビュー対象を局所化する
手段でもある（[Martin: The Clean Architecture (2012)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)、
取得 2026-07-07、ブログ記事存在確認）。

## 未来のエージェントも読者

可読性は人間だけのためではない。セッションをまたぐ AI 協働の前提条件でもある。
"Future agents can resume work without rediscovering hidden intent"（ADR 0004）。
モデルが文脈外の暗黙知にだけ正しいコードは、許容しない。コードは自己完結すべきだ。
この点で本稿は
[設計先行とコンテキスト](2026-07-05-rationale-design-first-minimal-context.md) と
接続する。

## 参考文献

1. 内部: `docs/architecture/adr/0004-human-readable-source-code-quality.md`、
   `docs/collaboration/source-code-quality.md`、`CLAUDE.md`、
   `docs/collaboration/template-benefits.md`
2. Bacchelli, A., Bird, C. "Expectations, Outcomes, and Challenges of Modern Code Review."
   ICSE 2013. https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/
   （取得 2026-07-07）
3. Ousterhout, J. *A Philosophy of Software Design*.
   https://web.stanford.edu/~ouster/cgi-bin/book.php （取得 2026-07-07）
4. zakirullin. *Cognitive Load is what matters*.
   https://github.com/zakirullin/cognitive-load （取得 2026-07-07、README 存在確認）
5. Martin, R. C. "The Clean Architecture." 2012.
   https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
   （取得 2026-07-07）