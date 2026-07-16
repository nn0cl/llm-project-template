# 規範と読み物：ドキュメントのアーキテクチャ

2026-07-06。非規範。関連: `docs/research/README.md`、`agent-quickstart.md`。

---

ドキュメントが増えるほど、「従う規則」と「背景の読み物」の境界が曖昧になる。人間は不要な文書をスキップできるが、エージェントはコンテキストに入った文をすべて影響源とする。だから作業入力は allowlist で列挙し、読み物は構造的に外す（方針の定義は [README](README.md) の「エージェントと research」。完成形・sandbox の総論とも同旨）。

文書の三層は、設計図書（Architecture）、運用制約（Collaboration）、読み物（Research）である。エージェントの通常入力は上位二つの規範に限る。調査と哲学は Sources 付きで人間向けに残し、合意した結論だけが ADR / collaboration / issue へ **一方向に昇格**する。`docs/research/` の編集だけでは規範は変わらない。

## Diátaxis との対応：情報アーキテクチャ

[Diátaxis](https://diataxis.fr/) は、ソフトウェアドキュメントを目的別に四象限（tutorials / how-to / reference / explanation）に分類し、「これらを混ぜ合わせるとドキュメントの品質が致命的に落ちる」と喝破した。本テンプレートの設計図書と運用制約は、Diátaxis における `reference` と `how-to` に強く対応する。対して `research` は純粋な `explanation` に対応する。エージェントは `explanation` を読む必要がない——これはまさに、Diátaxis の「reference の中に explanation を混ぜるな」という鉄則の、AI エージェント時代における実装版である。

Diátaxis の最も重要な教訓は、文書間に優劣があるのではなく、「目的の違い」があるという点だ。reference は正確さと検索性を至上命題とする。how-to は手順の機械的な完遂を優先する。explanation は読者の深い理解と思索を助ける。私たちが research を充実した explanation として書けるのは、エージェントが従うべき reference と how-to が別のフォルダに隔離されているからだ。逆に、もし research の中に直接的な指示（規則）を混ぜてしまえば、explanation は単なる説教くさいルールブックに堕ち、reference は情報過多で曖昧なものになる。

## RFC の伝統：Normative と Informative

インターネットの基盤を築いてきた [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) 以来、技術標準の世界において "normative"（規範的・義務的）なテキストと "informative"（参考・非規範的）なテキストの厳密な区別は、標準化作業の絶対的な基本である。本稿における「読み物」とは、システムの準拠（コンプライアンス）——すなわちエージェントの正しいコード生成やツールの動作——には直接影響を与えない、informative な文書のことだ。

RFC の世界では、同じひとつの文書の中にも normative text と informative examples が共存することがある。しかし本テンプレートでは、それをさらに強く、物理的な「フォルダ」とスクリプトによる「参照経路」で物理的に分割する。理由は再三述べる通り、エージェントのコンテキスト管理である。人間のエンジニアは「ここからここは背景説明のコラムだな」と視覚的に読み分けられるが、エージェントに渡された長い文書は、しばしばその全テキストが「行動の根拠（プロンプト）」としてフラットに解釈されてしまう。だからこそ、絶対に混在させず、読み物は読み物として別の隔離された場所に置くのだ。

## Allowlist は Denylist より強い：セキュリティと予算

`privacy-context-budget-policy.md` がコンテキストの payload 最小化を規範化している。この制約を満たすため、読み物をエージェントの読む対象から確実に外す最も堅牢な実装手段は、除外リスト（Denylist）ではなく「列挙制（Allowlist）」である。参照されない文書は、システム上に存在しないのと同じ保証を与える。

Denylist は、エントロピーが増大し続けるファイルシステムに対して脆い。新しい読み物や一時ファイルが追加されたとき、それを除外リストへ明示的に書き入れ忘れるだけで、たちまち agent payload にノイズとして混ざり込む。Allowlist なら完全に逆である。作業経路（Operating Path）が読むべき文書をホワイトリストで列挙し、新しい文書は、アーキテクチャ上の合意を経て明示的に追加されない限り、決して入力コンテキストにはならない。この堅牢な性質は、プライバシー（機密情報の保護）とリーズニングバジェット（推論精度の維持）の両方に強力に機能する。

## 昇格は一方向である

`research` から（Adjudicator の判断を経て）ADR / collaboration / issue への「昇格」は推奨される。しかし、その逆の経路は絶対に作らない。規範文書が `research` の内容を normative に（従うべきルールとして）参照してしまえば、せっかくの構造的分離は崩壊する。同期対象外であることの技術的担保は、`collaboration-template-paths.sh` の列挙リストに `docs/research` が一切含まれないことによって物理的に強制される。

昇格の経路が一方向であることは、決して research を軽んじているからではない。むしろ、research という知的な活動を真に自由にするためである。ここでは大胆な仮説、歴史的な背景、採用されなかった反論、他社の文献の読み比べを、文字数を気にすることなく豊かに書ける。まだ確定した規則ではない柔らかい考えを、無理に短く硬い命令文（プロンプト）の形に押し込める必要はない。人間が深く思考し、哲学を熟成させる場所を確保するために、あえてエージェントが従う冷徹な場所とは分けるのである。

## 参考文献

1. **プロジェクト内部規定**
   - `docs/research/README.md`
   - `docs/collaboration/privacy-context-budget-policy.md`
   - `docs/architecture/agent-quickstart.md`
   - `scripts/lib/collaboration-template-paths.sh`
2. **ドキュメンテーション・アーキテクチャ**
   - Diátaxis. https://diataxis.fr/ （取得 2026-07-07）
   - Canonical. "Diátaxis, a new foundation for Canonical documentation." https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation （取得 2026-07-07）
3. **技術標準化の原則**
   - RFC 2119. *Key words for use in RFCs to Indicate Requirement Levels*. https://www.rfc-editor.org/rfc/rfc2119
   - RFC 8174. *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*. https://www.rfc-editor.org/rfc/rfc8174 （取得 2026-07-16）
