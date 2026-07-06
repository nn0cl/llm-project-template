# エージェントはサンドボックスである

2026-07-07。非規範。
関連: [完成形](2026-07-05-rationale-target-end-state.md)、
[Referee とフェーズ](2026-07-05-rationale-referee-centered-collaboration.md)、
[リポジトリに計画を置く](2026-07-05-rationale-repository-native-planning-and-change-control.md)、
[設計先行とコンテキスト](2026-07-05-rationale-design-first-minimal-context.md)。

---

私は、AI と人間が**協調して**開発を進める仕組みを作ろうとしている。エージェントに
仕事を奪わせるのではない。人間が設計と承認を担い、エージェントが探索と生成を担い、
その境界を文書と成果物とレビューで接続する——そういう工学的協働だ。

その前提として、コーディングエージェントは驚くほど自由に動く。ファイルを読み、
コマンドを打ち、複数ファイルを書き換え、失敗してやり直す。SaaS 製品はこの自由を
"isolated" / "ephemeral" な実行空間——サンドボックス——のなかで与える
（GitHub Copilot: [cloud and local sandboxes](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes)、
取得 2026-07-07。Cursor: [agent sandboxing](https://cursor.com/blog/agent-sandboxing)、
取得 2026-07-07）。自由はベンダー側の実行境界で確保される。

だが自由だけではプロジェクトにならない。統合の仕組みはベンダーが売るものではなく、
**チームがリポジトリに書くもの**である。本テンプレートは、その仕組みの設計図だ。

## 協働の三役

`docs/collaboration/ai-human-scheme.md` は、役割を三つに分ける。

**Referee**——人間の設計者。フェーズ遷移の承認、ADR の受理、Phase 1 テストのレビュー、
曖昧な判断の決定を所有する。

**Agent**——AI コーディング補助。設計インテークから始め、依頼されたフェーズだけを
実行し、仮定と境界を可視化し、Referee の決定が要るところで止まる。

**Deterministic Tool**——formatter、linter、test runner など。モデルの判断に依存
すべきでない事実を、再現可能に検証する。

協働は、この三役がループのなかで回ることで成立する。エージェント単体の性能ではない。

```text
依頼
  -> Phase 0 設計インテーク
  -> Referee のレビューまたは承認
  -> Phase 1 Red
  -> Referee がテストをレビュー
  -> Phase 2 Green
  -> 決定的検証
  -> Phase 3 Refactor
  -> レビュー者共感サマリ
  -> Referee の最終レビュー
```

（`ai-human-scheme.md` の Collaboration Loop を要約）

## 本リポジトリが置く制御——実行強制ではなく、協調の規範

ここで誤解しやすい。`CLAUDE.md` と `AGENTS.md` は、エージェントのシェルコマンドを
プログラムで遮断する仕組みではない。サンドボックスの権限モデルを書き換えるものでも
ない。**行動憲法**である。セッション全体を通じて、何をしてよいか、いつ止まるか、
何を推測してはならないかを述べる。

制御は次の層で接続されている。層は上から順に、エージェントの最初の一歩に近い。

### 第一関門——Operating Path の列挙制

`docs/architecture/agent-quickstart.md` は、依頼の性質に応じて Fast / Feature /
Architecture の三経路を選ばせる。各経路は**読む文書を列挙する**。読まない文書は、
そのタスクの規範に入らない。これは research をエージェントの読む対象から外すのと
同じ論理であり、コンテキスト予算の実装でもある
（[規範と読み物](2026-07-06-rationale-normative-vs-reading-documents.md)）。

`scripts/init-llm-context.sh` は、セッション開始時にこの順序を最初のプロンプトへ
焼き込む。仕様もフェーズもまだなければ、実装に入らず設計インテークのあとで止まれ、
と指示する。協働はいきなり生成から始まらない。

### 憲法——同期した操作契約

`AGENTS.md`（ツール非依存）、`CLAUDE.md`（Claude 入口）、
`.github/copilot-instructions.md`（Copilot 入口）は、同じフェーズ規律と依存境界を
複数エージェント向けに同期した**操作契約**である。Claude Code on the web は
リポジトリの `CLAUDE.md` をセッションに持ち込むが、ユーザーホームだけの設定は
持ち込まない（[Use Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)、
取得 2026-07-07）。だから憲法はリポジトリに置く。サンドボックスはそれをクローンして
読む側にすぎない。

契約の変更自体も統制の対象だ。`prompt-instruction-change-control.md` は Referee
レビューと trace を要求し、CI が契約変更に trace が無い PR を拒否する。協働のルールを
変える行為も、協働のルールに従う。

### 誘導——設計インテークと Prime Directive

`AGENTS.md` の Prime Directive は三つだ。レビュー済み受入仕様なしに実装しない。
フェーズをスキップしない。adapter に隠れた業務ロジックを置かない。

毎依頼は設計から始まる。Feature / Architecture Path では `[THOUGHT]` が、
対象挙動、include/omit、ports/adapters、Must not guess、モデル/ツール振り分けを
先に固定する。Fast Path では compact design note で同趣旨を短く述べる。これは
セッション前のブリーフィングではなく、**作業中ずっと効く誘導**である。

### ライブ制御——Referee の承認ループ

規範文書だけでは協働は完結しない。人間がループの中に入る。Referee は決定点を
「所有」するだけでなく、各フェーズで**止めて承認させる**能動的制御である。
Phase 2 はレビュー済み Phase 1 のあとにだけ始まる。フェーズ遷移は Referee の
明示的な依頼が要る（`agent-quickstart.md` の Phase Rule）。

ここが本テンプレートの統合の心臓だ。サンドボックス内の自由な生成は、Referee の
承認点を通過するとき初めてプロジェクトの前進になる。

### 配線——永続成果物とアーキテクチャ境界

issue、ADR、trace、handoff、EARS/Gherkin 仕様は、セッションをまたぐ配線である。
Clean Architecture の依存規則と Ports は、生成物をリポジトリが受け入れられる形に
寄せる。エージェントの自由な diff が、のちのレビューと引き継ぎで読めるようにする。

### 出口——PR、人間レビュー、薄い CI

サンドボックスから出た変更は PR と人間レビューへ載る。CI は補助的関所である。
本テンプレートの CI は、契約ファイルの存在、ADR 番号、契約変更時の trace などを
見る骨格にすぎない。フェーズ遵守を毎コミットで機械判定する層ではない。統合の最終
責任は Referee とレビュアーにある。正直なフェーズ報告（"Report Red, Green, Refactor,
or Fast Path status honestly"）は、規範が誠実さを要求する部分だ。

## 二つの世界を混ぜない

整理のために、次の二つを分けておく。

**ベンダーのサンドボックス**——実行の自由と安全境界（ファイル、シェル、ネットワーク）。
製品が与える。

**チームの協働規範**——`CLAUDE.md` / `AGENTS.md`、Operating Path、Referee ループ、
成果物、PR。リポジトリが与える。

私が「内側は自由、外側は明示的」と言うとき、外側の主役は CI ではなく、**規範文書と
人間の承認ループと永続成果物**である。サンドボックスがあるから内側を任せられる。
協働規範があるから外側で一貫性を保てる。どちらか一方では足りない。

## このテンプレートは何か、何でないか

本リポジトリはアプリケーションではない。プロセスと協働の足場である。ここにある
`CLAUDE.md` / `AGENTS.md` は、**アダプター先のターゲットプロジェクトへコピーされ、
そこで憲法として機能する**設計図だ（`copy-ai-collaboration-files.sh`）。

やろうとしていることは明確だ。**自由に動くエージェントを、人間と一緒に使える
工学的ワークフローへ接続する。** エージェントを信じて仕組みを省くのでも、
エージェントを疑って自由を潰すのでもない。三役の協働ループと、リポジトリに書かれた
規範と、Referee の承認で、統合された開発を作る。

`docs/research/` の各論——Referee、設計先行、出力契約、レビュー可能なコード、
リポジトリ計画——は、この一枚の骨格の上に載る詳細である。

## 並列するとき

複数エージェントが並ぶとき、各セッションは別のサンドボックスで自由に動く。衝突は
サンドボックス同士ではなく、git と worktree（ADR 0007）で吸収する。並列の成熟は
`process-gap-register.md` が未完成と認めているが、方向は同じだ。永続境界でマージし、
Referee が統合を見る。

## 参考文献

1. 内部: `AGENTS.md`、`CLAUDE.md`、`docs/architecture/agent-quickstart.md`、
   `docs/collaboration/ai-human-scheme.md`、`docs/collaboration/prompt-instruction-change-control.md`、
   `scripts/init-llm-context.sh`、ADR 0007
2. GitHub Docs. *About cloud and local sandboxes for GitHub Copilot*.
   https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes
   （取得 2026-07-07）
3. Cursor. *Implementing a secure sandbox for local agents*.
   https://cursor.com/blog/agent-sandboxing （取得 2026-07-07）
4. Anthropic. *Use Claude Code on the web*.
   https://code.claude.com/docs/en/claude-code-on-the-web （取得 2026-07-07）
5. Anthropic. *Building effective agents*.
   https://www.anthropic.com/research/building-effective-agents （取得 2026-07-07）
6. Shi, F. et al. arXiv:2302.00093.
   https://arxiv.org/abs/2302.00093 （取得 2026-07-07）