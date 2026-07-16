# Quickstart 日本語ガイド：導入とアンインストール

[English version](QUICKSTART.md)

これは `QUICKSTART.md` の逐語訳ではありません（`README.ja.md` と同じ方針）。
何かをコピーする前に確認してほしい 3 点——このテンプレートをどこに
checkout するか、エージェントに導入作業を任せるときの安全な進め方、そして
やめたくなったときにどう取り除くか——を短くまとめた入口です。テンプレート
が何を提供し、なぜそうなっているかは [README.ja.md](README.ja.md) を見て
ください。ここでは思想は繰り返しません。

## 1. 導入先プロジェクトの外に checkout する

このテンプレートは、導入先プロジェクトの**兄弟ディレクトリ**として clone
してください。導入先リポジトリのサブフォルダや、その内部にネストした
git リポジトリとしては置きません。

```text
~/dev/
├── my-target-project/      # 導入先プロジェクト（自分の git 履歴を持つ）
└── llm-project-template/   # このテンプレート（別に clone する）
```

```bash
cd ~/dev
git clone <このリポジトリの URL> llm-project-template
```

理由は次のとおりです。

- `scripts/copy-ai-collaboration-files.sh` と
  `scripts/update-ai-collaboration-files.sh` は、**このテンプレートの
  checkout 側から** `--target /path/to/my-target-project` を指定して実行
  します。導入先リポジトリの内部に置く必要は一切ありません。
- テンプレートの checkout を手元に残しておけば、あとで `git pull` して
  `scripts/update-ai-collaboration-files.sh` を実行するだけで、再 clone
  せずにテンプレートの改善を取り込めます。詳しくは
  [Receiving Later Template Updates](docs/collaboration/adoption-guide.md#receiving-later-template-updates)
  を参照してください。
- 導入先プロジェクトの作業ツリーの中に別の `.git` をネストすると、
  submodule の混乱や意図しない commit の混入を招きがちです。兄弟
  ディレクトリにすれば、この種の事故はそもそも起こりません。
- このテンプレート自身の保守用 local issue や trace、sample rollout spec
  は、導入先リポジトリには入りません。copy script 自体がすでにそれらを
  除外していますが、兄弟ディレクトリとして checkout しておけば、2つの
  作業ツリーを見比べたときに分離が一目でわかります。

## 2. エージェントに導入作業を任せる

以下の shell コマンドを自分で実行しても構いませんが、このテンプレートは
Referee の監督下でエージェントが安全に導入作業を代行できるように設計され
ています。そのまま貼り付けられる prompt は
[`docs/templates/examples/adoption-prompts.md`](docs/templates/examples/adoption-prompts.md)
にあります。要点は次のとおりです。

1. **導入先リポジトリを working directory にして** agent session を開きます
   （テンプレートの checkout 側ではありません）。
2. テンプレートの checkout パスと、やるべきタスクを伝えます。copy script
   を実行すること、何をコピーし何をスキップしたかを報告すること、そして
   Referee が承認していない導入先固有の事実（スタック、データストア、
   provider、ドメインモデル）は推測せずに止まること。
3. エージェントが placeholder を埋めたり Feature Path の作業を始めたりする
   前に、diff を必ず自分でレビューします。エージェントは `AGENTS.md` の
   Prime Directive に従い、推測せず止まって確認を求めるべきです。

これは、このテンプレートが他のあらゆるタスクに課している通常の Fast Path /
Architecture Path の規律をそのまま踏襲したものです。導入作業だからといって
Referee レビューを省略してよい特例にはなりません。

## 3. 導入する

テンプレートの checkout 側で実行します。

```bash
scripts/copy-ai-collaboration-files.sh --target ~/dev/my-target-project
```

導入先に既存のファイルがある場合、デフォルトではスキップされます。まず
`--dry-run` で確認し、`--force` は「このテンプレートに属するファイルを意図
的に上書きしたいとき」だけに使ってください。導入先プロジェクト自身の
README、仕様、architecture document を上書きする目的では絶対に使いません。

続けて、導入先リポジトリ側で実行します。

```bash
cd ~/dev/my-target-project
scripts/init-llm-context.sh .
```

出力された prompt を、そのリポジトリの最初の AI session に貼り付けます。

どの placeholder をどの順番で埋めるかを含む詳しい導入手順は、
[README.md § Install into another repository](README.md#install-into-another-repository)
と [`docs/collaboration/adoption-guide.md`](docs/collaboration/adoption-guide.md)
にあります。

## 4. アンインストールする

このテンプレートを取り除くことは、機械的なスクリプト一発では終わりません。
scaffolding として導入されたファイルの中には、その後プロジェクトが書き込ん
だ仕様・ADR・issue・trace など、テンプレート自体とは無関係な資産が積み重
なっている可能性があるからです。アンインストールは Architecture Path の
作業として扱い、削除する前に「なぜ削除するのか」を ADR か commit message
に記録してください。これは、他のあらゆる process 変更をこのテンプレート
自身のルールに沿って記録するのと同じ作法です。

以下のリストは
[`scripts/lib/collaboration-template-paths.sh`](scripts/lib/collaboration-template-paths.sh)
——copy/update script が使っているのと同じリスト——を、削除の安全度で分類
したものです。

### そのまま削除してよい（純粋なテンプレートのツール類）

- `scripts/copy-ai-collaboration-files.sh`
- `scripts/update-ai-collaboration-files.sh`
- `scripts/init-llm-context.sh`
- `scripts/lib/collaboration-template-paths.sh`
- `.collaboration-template-version`（導入先リポジトリ直下の同期マーカー）
- `.collaboration-template-ignore`（作成していれば）
- `docs/templates/`（design-intake、handoff、trace、issue、work-plan、ADR、
  Gherkin の各テンプレート）
- `docs/at-tdd/process.md`

### 先に確認する——これらは運用契約そのもの

これらを削除すると、このテンプレート固有の文言が消えるだけでなく、
エージェントが phase-gated workflow に従うこと自体が止まります。「1つの
ルールを緩めたい」程度の話であれば削除ではなく編集で対応できないか、先に
確認してください。

- `AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md`
- `.grok/rules/`、`.cursor/rules/`

### 選別が必要——テンプレートとプロジェクトの内容が混在するフォルダ

これらは `rm -rf` しないでください。フォルダ内のテンプレート由来ファイル
だけを取り除き、プロジェクトが追加したものは残します。

- `docs/architecture/adr/0001-*.md` から `0011-*.md` までは、このテンプレー
  トが同梱する process ADR です。この 11 件だけを削除し、プロジェクトが
  その後採番した ADR（0012 以降）は残します。
- `docs/architecture/` はそれ以外にも、テンプレート提供ファイル
  （`agent-quickstart.md`、`implementation-readiness.md`、
  `ai-request-routing.md`、`io-reasoning-contracts.md`、
  `dependency-policy.md`、`project-structure.md`、`testing-strategy.md`、
  `README.md`）と、同じフォルダ内にプロジェクトが書いた stack 固有の
  architecture document が混在します。テンプレート提供ファイルだけを個別
  に削除し、残りは保持します。
- `docs/collaboration/` はほぼ全体がテンプレート提供の process 文書です
  が、`docs/collaboration/traces/` や、実際の決定を記録するために
  プロジェクトが編集したファイルは、プロジェクト自身の監査履歴です。
  あとで参照したくなる可能性があるなら、削除ではなく archive を検討して
  ください。
- `docs/issues/`、`docs/work-plans/`、`docs/specs/`、`docs/evaluation/` は
  テンプレートが空（`.gitkeep` のみ）の状態で配る scaffolding 用ディレクト
  リです。アンインストールを検討する頃には、ほぼ確実に実際のプロジェクト
  内容が入っています。プロジェクトが書き込んだ時点で「テンプレートのも
  の」ではなくなっているので、これらは削除しないでください。

### 削除ではなく編集が必要

- `.github/workflows/ci.yml` ——「Check required project documents」と
  「Check architecture decision records」の step は、上記の契約ファイルが
  存在することを前提にしています。`AGENTS.md` や ADR を削除してこの
  workflow を編集しなければ、次の push で CI が落ちます。実際に残した
  内容に合わせて step を書き換えるか削除してください。
- `README.md` / `README.ja.md` ——導入後は、これらはテンプレートのもので
  はなく導入先プロジェクト自身の README です。ファイルごと削除するので
  はなく、テンプレート固有の記述（この Quickstart へのリンク、導入手順
  など）だけを編集で取り除いてください。

### テンプレートの一部ではないもの

`.github/dependabot.yml`、`.github/pull_request_template.md`、
`.github/ISSUE_TEMPLATE/` は、このテンプレートが妥当な既定値として同梱して
いるだけの、一般的な GitHub 設定です。AI 協働プロセスを続けるかどうかに
関わらず、これらはそれ自体として有用なので残すことをおすすめします。

## このファイルがエージェントの context を浪費しない理由

このテンプレートの契約下で動くエージェントは、
`docs/architecture/agent-quickstart.md` が Fast Path / Feature Path /
Architecture Path それぞれで明示的に列挙した文書だけを読みます
（`AGENTS.md` 参照）。このファイルは、その3つのリストのいずれにも意図的
に含めていません。また `scripts/lib/collaboration-template-paths.sh` にも
含めていないため、導入先プロジェクトにコピーされることも、エージェントの
通常の読み込み対象になることもありません。`docs/research/` が受けているの
と同じ扱いを、同じ理由で適用しています。

ただし、この保証はアーキテクチャ設計上の期待値であって、物理的なアクセス
禁止ではありません。このテンプレートの allowlist と無関係にリポジトリ全体
を context へ読み込んでしまうツールの harness や、このファイルを手動で
prompt に貼り付ける人間がいれば、それでも context には入り得ます。ファイル
の置き場所だけでそれを完全に防ぐことはできません。このテンプレートが
制御できるすべてのリスト（読了リストと配布リスト）からこのファイルを
確実に外しておくことが、ここで実際に担保できる範囲です。
