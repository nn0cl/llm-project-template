# docs/research について

[English entry point](en/README.md)

このフォルダは、Adjudicator と AI の相談のなかで生まれた調査と論考を置く場所である。
AI と人間が協調して開発を進めるための設計思想——なぜそういう仕組みを置くのか——を
人間向けに残す。ここにある文章は、エージェントへの指示でもなく、ADR でもない。
規範は `AGENTS.md` や `docs/collaboration/` にあり、research はその背後の理由である。

規則は別の場所に住む。設計図書は `docs/architecture/` に、運用制約は
`docs/collaboration/` に、決定は ADR に、計画は local issue に置かれる。
research は、その背後にある理由を残すための層である。結論が規範へ昇格するとき、
昇格先だけが拘束力を持ち、本稿はそのまま読み物として残る。逆方向——規範文書が
research を normative に参照する——は作らない。

## エージェントと research

**エージェントは、日々の作業入力としてこのフォルダを読む必要がない。**

これは物理的なアクセス禁止ではない。`agent-quickstart.md` が列挙する文書だけが
通常の作業入力（allowlist）であり、research はその列挙の外にある、という
アーキテクチャ上の期待である。人間は読まなくてもよい文書を無視できるが、
エージェントはコンテキストに入った文をすべて影響源とする。だから読み物は、
構造的に通常の読む対象から外す。

英語の要約・翻訳は [en/README.md](en/README.md) に置くが、用語とこの方針の
正は本 README および日本語原本である。英語側は本節を参照して揃える。

テンプレートを他リポジトリへ展開するとき、research はコピーされない。
`scripts/lib/collaboration-template-paths.sh` の同期対象に含まれない。下流へ
配るのは規範だけであり、世界観の叙述は上流にとどめる。

## 用語（本フォルダ内）

誤解を避けるため、research 内では次の語を使い分ける。英語訳の正は
[en/README.md](en/README.md) の Glossary が本節に対応する。

| 用語 | 意味 |
|------|------|
| **Adjudicator** | 意思決定点（フェーズゲート、ADR 採択、曖昧さの裁定）を所有する人間の設計者。AI の役割ではない。 |
| **採用者** | テンプレートを **採用したプロジェクト**側で、同期・運用・フィードバックを担う人またはチーム。Clean Architecture の Adapter ではない。 |
| **Adapter（Clean Architecture）** | ポートを実装する外側レイヤのコンポーネント（DB、SDK、ファイル I/O など）。「採用者」と区別する。 |
| **能力の階段（capability ladder）** | 作業の難易度とリスクに応じ、決定論ツール・小さいモデル・強い推論モデルへ振り分けること。 |
| **非規範（non-normative）** | 読み物。ADR / collaboration へ昇格するまでプロジェクト規則を変えない。 |
| **採用ライフサイクル** | 規範 `docs/architecture/external-resource-adoption-contract.md` が定める外部 resource の状態遷移（下記）。ソフトウェア依存（パッケージ等）は `dependency-policy.md` 側。 |
| **accepted（検査判定）** | 採用ライフサイクル上の **検査の結果（verdict）**。「チェックに通った」ことを意味する。check record の `verdict` に入る。**まだ信頼境界での常用ではない。** |
| **adopted（信頼利用）** | 採用ライフサイクル上の **運用状態**。resource が active な trusted use に入った状態。`accepted` のあとでのみ遷移する。`intake` から直接 `adopted` にはできない。 |
| **rejected / needs_recheck** | いずれも検査判定。失敗、または再検査が必要。ここから直接 `adopted` には進まない。 |

### accepted と adopted を混同しない

規範の図は二段である（`external-resource-adoption-contract.md` / ADR 0011）:

```text
intake -> checked -> accepted | rejected | needs_recheck   ← 検査の結果
accepted -> adopted                                         ← 信頼利用への投入
```

- **accepted ≠ adopted**。検査 OK と、信頼ストア／本番スコープでの常用は別イベントである。
- research や英訳で「Adopted」と書くときは、通常この **lifecycle 終端**を指す。
- ADR 文書の `## Status` / **Accepted**（その ADR をプロジェクトが採択した、という MADR 慣習）は、resource の `accepted` / `adopted` とは **別の名前空間**である。混同しない。

過去に「アダプター（実行者）」「採用アダプター」と書いていた箇所は、
すべて **採用者** に読み替える。

## 命名と引用

ファイル名は `YYYY-MM-DD-short-topic.md` とする。日付は最初に調査を行った日で
あり、のちの推敲で本文や出典が更新されてもファイル名の日付は変えない。本文中の
取得日がファイル名の日付より新しくなることがあるのは、このためである。

外部の主張を借りるときは、出典 URL と取得日を本文または末尾の参考文献に書く。
取得していない URL は「未検証」と明記する。推測で文献を補わない。

参考文献には査読研究・実務報告・回顧録・エッセイが混在する。証拠の等級が主張の
重みに影響する場合は、本文または参考文献の括弧内でその性格を注記する。

直接引用の表記は ACM の run-in quotation に合わせる。

- 英語の直接引用は二重引用符 `"..."` で囲む。斜体は使わない。
- 日本語の直接引用（Adjudicator の発言など）は鉤括弧 `「...」` で囲む。
- 間接引用や筆者の論述には引用符を付けない。
- 参考文献リストの文献・作品名は斜体のままとする（例: *Docs as Code*）。

関連する ADR や local issue があるときは、昇格経路をたどれるようリンクする。

## 多言語

日本語の原本が正である。英語の入口は [en/README.md](en/README.md) に置き、
各エッセイの要旨と全文翻訳を `en/` 配下に提供する。全文翻訳は原本と同じ
ファイル名で置き、冒頭に日本語原本へのリンクと「日本語が権威である」旨を
明記する。用語・「読む必要がない」方針は本 README を参照する。翻訳が原本の
推敲に追随できていない場合、その翻訳は陳腐化しているものとして扱い、原本を
参照する。`docs/research` はディレクトリ単位で同期対象外なので、`en/` を
含めて配布されない。

## 収録

総論から読み始める。

- [完成形](2026-07-05-rationale-target-end-state.md)
- [エージェントはサンドボックスである](2026-07-07-rationale-saas-agent-as-sandbox.md)
- [Adjudicator とフェーズ](2026-07-05-rationale-adjudicator-centered-collaboration.md)
- [設計先行とコンテキスト](2026-07-05-rationale-design-first-minimal-context.md)
- [出力の契約](2026-07-05-rationale-ai-output-contracts.md)
- [レビュー可能なコード](2026-07-05-rationale-code-for-human-review.md)
- [リポジトリに計画を置く](2026-07-05-rationale-repository-native-planning-and-change-control.md)
- [pull 型の上流](2026-07-06-rationale-template-as-pull-based-upstream.md)
- [AI協働におけるブランチ戦略](2026-07-06-branching-strategies-develop-and-multi-target-releases.md)
- [規範と読み物](2026-07-06-rationale-normative-vs-reading-documents.md)
- [エビデンスと規則](2026-07-06-rationale-evidence-based-process-design.md)
