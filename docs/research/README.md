# docs/research について

[English entry point](en/README.md)

このフォルダは、Referee と AI の相談のなかで生まれた調査と論考を置く場所である。
AI と人間が協調して開発を進めるための設計思想——なぜそういう仕組みを置くのか——を
人間向けに残す。ここにある文章は、エージェントへの指示でもなく、ADR でもない。
規範は `AGENTS.md` や `docs/collaboration/` にあり、research はその背後の理由である。

規則は別の場所に住む。設計図書は `docs/architecture/` に、運用制約は
`docs/collaboration/` に、決定は ADR に、計画は local issue に置かれる。
research は、その背後にある理由を残すための層である。結論が規範へ昇格するとき、
昇格先だけが拘束力を持ち、本稿はそのまま読み物として残る。逆方向——規範文書が
research を normative に参照する——は作らない。

エージェントはこのフォルダを読む必要がない。`agent-quickstart.md` が列挙する
文書だけが作業の入力であり、research はその列挙の外にある。人間は読まなくても
よい文書を無視できるが、エージェントはコンテキストに入った文をすべて影響源と
する。だから読み物は、構造的に読む対象から外す。

テンプレートを他リポジトリへ展開するとき、research はコピーされない。
`scripts/lib/collaboration-template-paths.sh` の同期対象に含まれない。下流へ
配るのは規範だけであり、世界観の叙述は上流にとどめる。

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
- 日本語の直接引用（Referee の発言など）は鉤括弧 `「...」` で囲む。
- 間接引用や筆者の論述には引用符を付けない。
- 参考文献リストの文献・作品名は斜体のままとする（例: *Docs as Code*）。

関連する ADR や local issue があるときは、昇格経路をたどれるようリンクする。

## 多言語

日本語の原本が正である。英語の入口は [en/README.md](en/README.md) に置き、
各エッセイの要旨を英語で提供する。全文翻訳を追加する場合は `en/` 配下に
原本と同じファイル名で置き、冒頭に「どのコミット時点の原本を訳したか」を
明記する。翻訳が原本の推敲に追随できていない場合、その翻訳は陳腐化して
いるものとして扱い、原本を参照する。`docs/research` はディレクトリ単位で
同期対象外なので、`en/` を含めて配布されない。

## 収録

総論から読み始める。

- [完成形](2026-07-05-rationale-target-end-state.md)
- [エージェントはサンドボックスである](2026-07-07-rationale-saas-agent-as-sandbox.md)
- [Referee とフェーズ](2026-07-05-rationale-referee-centered-collaboration.md)
- [設計先行とコンテキスト](2026-07-05-rationale-design-first-minimal-context.md)
- [出力の契約](2026-07-05-rationale-ai-output-contracts.md)
- [レビュー可能なコード](2026-07-05-rationale-code-for-human-review.md)
- [リポジトリに計画を置く](2026-07-05-rationale-repository-native-planning-and-change-control.md)
- [pull 型の上流](2026-07-06-rationale-template-as-pull-based-upstream.md)
- [AI協働におけるブランチ戦略](2026-07-06-branching-strategies-develop-and-multi-target-releases.md)
- [規範と読み物](2026-07-06-rationale-normative-vs-reading-documents.md)
- [エビデンスと規則](2026-07-06-rationale-evidence-based-process-design.md)