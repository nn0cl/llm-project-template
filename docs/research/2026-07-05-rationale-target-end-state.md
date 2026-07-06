# 完成形

2026-07-05。非規範。各論の入口。

---

AI にコードを書かせること自体は、もはや驚きではない。驚くべきは、その速度のあとに
何も残らないことだ。チャットの断片と、いきなり増えた diff。誰が何を承認したか、
なぜその形になったか、次の担当者がどこから読めばよいか——これらが消える。
私は、そういう開発を工学的ワークフローとは呼ばない。

コーディングエージェントはサンドボックスのなかで驚くほど自由に動く。だが自由だけでは
プロジェクトにはならない。AI と人間が協調するには、Operating Path、操作契約、
Referee の承認ループ、永続成果物という**チーム側の仕組み**が要る——この前提は
[エージェントはサンドボックスである](2026-07-07-rationale-saas-agent-as-sandbox.md)
で展開する。

このテンプレートがめざすのは、AI と人間が**協調して**開発を進めるための足場である。
アドホックな会話を、レビュー可能な協働へ移す。速度を落として統制を後付けするのでは
ない。Referee・Agent・Deterministic Tool の三役と、契約・成果物・承認点を先に置く。
統制は速度の対価ではなく、協働の構造そのものである。

## 契約のもとで働く

人間の設計者（Referee）と AI エージェントは、書かれた運用契約のもとでだけ
協働すべきである。承認と裁定は人間が、生成と検証はエージェントが担う。
この分担は個人の気分ではなく、`AGENTS.md` や `CLAUDE.md` に固定される。
README はこれを "a shared, written operating contract" と呼んでいるが、
要するに「口約束で済ませない」という宣言である。

## 判断は消えてはならない

仕様、決定、計画、作業記録、引き継ぎ——すべてがリポジトリ内の成果物で
なければならない。EARS/Gherkin の受入仕様、ADR、local issue と work plan、
trace、handoff。チャットログは成果物ではない。将来の保守者が来歴をたどれる
ことは、機能の付属品ではなく、プロダクトの一部である。

プロセスをコードと同様にリポジトリで管理する docs-as-code の延長として、
このテンプレートはエージェントの挙動を定義する契約ファイルまでを版管理の
対象にする。[Write the Docs: Docs as Code](https://www.writethedocs.org/guide/docs-as-code/)
（取得 2026-07-07、ページ存在確認）がドキュメントにレビューと CI を適用するなら、
挙動を変える文書にも同じ規律を適用するのは自然な帰結である。

## テンプレートはドメインを決めない

スタック、データストア、プロバイダ、ドメインロジック——ここには何も入れない。
提供するのはプロセスと協働の足場だけである。未決のことは推測してよい空白ではなく、
`Current Non-Decisions` として明示的に未決とマークされる。エージェントに
「適当に埋めよ」とは言わない。ADR を書け、と言う。

## 完成形は静的ではない

テンプレートはコピーされた瞬間から古くなる。だから上流は push ではなく pull で
同期し、下流の主権を 3-way merge で保護する（ADR 0008）。改善は下流から還流し、
LISS として上流に戻る。エコシステムとして進化し続ける器である。

## 未完成を隠さない

`process-gap-register.md` は、高並列エージェント運用や障害復旧手順が未成熟である
と率直に書いている。完成形に「安全な並列運用」が含まれるなら、今はまだ
到達していない。ADR 0007 の worktree 分離は、その布石にすぎない。到達度を
自己評価の対象にすることも、設計の一部である。

## 人間の承認点

チェックポイントを設け、生成を委ね、レビューで止める——この構造は
[Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
（取得 2026-07-07、ページ存在確認）が推奨するエージェント設計と同じ方向を向く。
ただし本テンプレートの独自性は、承認点を文書とフェーズゲートとして固定した点に
ある。モデルが強くなってもゲートは残る。責任と監査可能性のための設計だからだ。

## 各論へ

以下の論考が、上記を個別のテーマへ展開する。

- [エージェントはサンドボックスである](2026-07-07-rationale-saas-agent-as-sandbox.md)
- [Referee とフェーズ](2026-07-05-rationale-referee-centered-collaboration.md)
- [設計先行とコンテキスト](2026-07-05-rationale-design-first-minimal-context.md)
- [出力の契約](2026-07-05-rationale-ai-output-contracts.md)
- [レビュー可能なコード](2026-07-05-rationale-code-for-human-review.md)
- [リポジトリに計画を置く](2026-07-05-rationale-repository-native-planning-and-change-control.md)
- [pull 型の上流](2026-07-06-rationale-template-as-pull-based-upstream.md)
- [ブランチと統合](2026-07-06-rationale-branching-and-release-strategy.md)
- [規範と読み物](2026-07-06-rationale-normative-vs-reading-documents.md)
- [エビデンスと規則](2026-07-06-rationale-evidence-based-process-design.md)

## 参考文献

1. 内部: `README.md`、`docs/collaboration/template-benefits.md`、
   `docs/collaboration/process-gap-register.md`
2. Write the Docs. *Docs as Code*.
   https://www.writethedocs.org/guide/docs-as-code/ （取得 2026-07-07）
3. Anthropic. *Building effective agents*.
   https://www.anthropic.com/research/building-effective-agents （取得 2026-07-07）