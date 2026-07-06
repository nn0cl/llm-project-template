# 規範と読み物

2026-07-06。非規範。関連: `docs/research/README.md`、`agent-quickstart.md`。

---

ドキュメントが増えるほど、どれが従うべき規則でどれが読み物かが曖昧になる。
人間は「読まなくてよい文書」を無視できる。エージェントはできない。コンテキストに
入った文はすべて挙動に影響する。だから私は、エージェントが読む文書を列挙制で
定義し、読み物を構造的にその外へ置く。

「調査結果は Sources 付きのレポートとして、設計図書や運営用制約ドキュメントとは
別のもの——エージェントは読む必要がない読み物——として管理したい。research フォルダは
他リポジトリへテンプレート展開するときにはコピーされない。」

文書には三つの階級がある。設計図書（architecture）、運用制約（collaboration）、
読み物（research）。エージェントのコンテキストは規範だけで構成される。調査結果は
捨てない。Sources 付きで人間向けに蓄積する。規則になった結論だけが ADR や
collaboration 文書、issue へ昇格する。

## Diátaxis との対応

[Diátaxis](https://diataxis.fr/)（取得 2026-07-07、tutorials / how-to / reference /
explanation の四象限を確認）は、ドキュメントを目的別に分け、混ぜると品質が落ちる
と述べる。設計図書と運用制約は reference / how-to に、research は explanation に
対応する。エージェントは explanation を読む必要がない——Diátaxis の「reference に
explanation を混ぜるな」の、エージェント版だ。

## RFC の伝統

[RFC 2119](https://www.rfc-editor.org/rfc/rfc2119)（内容は安定した標準文書）以来、
normative と informative の区別は標準化の基本である。読み物とは、準拠——すなわち
エージェントの正しい動作——に影響しない文書のことだ。

## allowlist は denylist より強い

`privacy-context-budget-policy.md` が payload 最小化を規範化するなら、読み物を
読む対象から外す実装手段は列挙制である。参照されない文書は、存在しないのと同じ
保証を与える。除外リストでは足りない。

## 昇格は一方向

research →（Referee 判断）→ ADR / collaboration / issue は許す。逆は作らない。
規範文書が research を normative に参照すれば、分離は壊れる。同期対象外であることの
担保は、`collaboration-template-paths.sh` の列挙に `docs/research` が含まれない
ことによる（2026-07-07 に copy / update 両スクリプトが同一リストを参照することを
確認）。

## 参考文献

1. 内部: `docs/research/README.md`、`docs/collaboration/privacy-context-budget-policy.md`、
   `docs/architecture/agent-quickstart.md`、`scripts/lib/collaboration-template-paths.sh`
2. Diátaxis. https://diataxis.fr/ （取得 2026-07-07）
3. RFC 2119. *Key words for use in RFCs to Indicate Requirement Levels*.
   https://www.rfc-editor.org/rfc/rfc2119
4. Canonical. "Diátaxis, a new foundation for Canonical documentation."
   https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation
   （取得 2026-07-07、ブログ存在確認）