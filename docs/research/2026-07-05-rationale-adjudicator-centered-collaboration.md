# Adjudicator とフェーズ：自動化の皮肉と責任の設計

2026-07-05。非規範。関連: ADR 0003、`docs/at-tdd/process.md`。

---

「Human-in-the-loop は必要だ」という総論の合意だけでは、実際のプロジェクトを運用するには全く不十分である。どこに、どのような形で人間を配置するかがアーキテクチャとして設計されていなければ、結局は「エージェントの全出力を血眼になって監視する」か、「エージェントの全出力を放置して無責任にマージする」かのどちらかに必ず堕ちる。前者は人間の認知限界を超えており持続不可能であり、後者はソフトウェアエンジニアリングとしての責任の放棄である。

私は第三の道、すなわち構造的な協働の形を採る。人間（Adjudicator）はシステムにおける「決定点（Decision Points）」を明示的に所有し、それ以外の生成と検証のプロセスはエージェントに委ねる。

Adjudicator はフェーズ遷移の承認、ADR（アーキテクチャ決定記録）の受理、Phase 1 テストのドメインレビュー、そして曖昧な選択に対する最終決定権を所有する。対してエージェントは、設計インテークの策定、コンテキストの選択、フェーズに適合したコードやドキュメントの生成、仮定の可視化、決定的ツールによる検証、そして人間への handoff（引き継ぎ）を所有する。この責任境界が文書化され、システムに組み込まれていること自体が、持続可能な協働の前提である（ADR 0003）。

## 人間を「常時監視者」にしない：自動化の皮肉を越えて

AIとの協働プロジェクトで最もよくある失敗は、人間を「最後の責任者」という名誉ある監視職に就かせ、実際にはAIが生成した巨大な差分（diff）を事後に全量検査させることだ。これでは、人間は創造的な設計者ではなく、疲弊しただけのライン工になる。

Lisanne Bainbridge は1983年の古典的論文 "Ironies of Automation" （[ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0005109883900468)）において、自動化が進めば進むほど人間の役割がなくなるどころか、逆に「人間には自動化システムが処理できない最も難しく複雑な仕事だけが残される」という皮肉を指摘した。さらに、単調な監視だけを任された人間は、いざ異常事態が発生した際に状況を正確に把握して介入することが極めて困難になる。

AIコーディングにおいても、全く同じ皮肉が成立する。コード生成を大量に自動化すると、人間には「AIが書いた文脈不明のコードを全部読んで安全性を保証する」という、もっとも認知負荷が高く、エラーを起こしやすい仕事だけが残される。

Adjudicator-centered collaboration（レフェリー中心の協働）は、この自動化の皮肉に対するアーキテクチャレベルでの対抗策である。人間を常時監視者にするのではなく、意味のある決定点の所有者にする。Phase 1 のテストを承認する。Phase 2 の実装方針を確認する。ADR の採否を決める。曖昧な provider、DB、privacy、schema の選択で処理を一旦止める。この構造によって、人間の希少な注意力はすべての生成トークンに向かうのではなく、プロジェクトの意味が非可逆的に変わる地点（フェーズゲート）へと集中的に向けられる。

## 多エージェント時代の Adjudicator：エスカレーションと承認は違う

「決定点の所有者」という Adjudicator の定義は、単一のエージェントを人間が見張るという構図に依存しない。生成の実行は複数の LLM に分割でき（AutoGen: Wu et al., [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)）、不確実性の高い問いだけを強い推論役へ委譲するカスケード構成は、精度を保ったままコストを大幅に下げることが実証されている（Yue et al., [arXiv:2310.03094](https://arxiv.org/abs/2310.03094)）。Anthropic 自身も、強いモデルをリードに、軽いモデルを並列ワーカーに置くオーケストレーター・ワーカー構成を実運用し、単体構成を上回る成果を報告した（[How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)。ベンダー内部評価の自己報告）。この構図が一般化すると、魅力的な誘惑がひとつ生まれる。「Adjudicator もまた、この階層の最上位に置かれた、いちばん賢い推論リソースにすぎないのではないか」という再解釈である。

この再解釈は、情報の流れとしてはエレガントだが、責任の設計としては誤りである。強いモデルへの相談と、人間への承認要求は、どちらも「上位へのエスカレーション」に見えても意味が全く違う。前者は答えの質を上げるための手段であり、何度でもやり直せる。後者はプロジェクトの責任と監査可能性を確定させる行為であり、承認の記録が残り、その決定に人間が拘束される。エージェントチームがどれほど階層化されても、Adjudicator は「最も賢いアドバイザー」として階層に溶け込むのではなく、「決定と責任の所有者」として階層の外側からゲートを握り続ける。協働が「推論リソースのルーティング」だけに還元された瞬間、責任の所在は再び曖昧に戻ってしまうからだ。

## AT-TDD：振る舞いの言語化と承認パイプライン

開発サイクルは ATDD（受入テスト駆動開発）と TDD（テスト駆動開発）のハイブリッドとして定義する。受入仕様が失敗するテストを駆動し、レビュー済みのテストが最小実装を駆動し、リファクタリングは Green のあとにだけ行う。Red / Green / Refactor は Martin Fowler が解説する TDD の基本リズム（[martinfowler.com](https://martinfowler.com/bliki/TestDrivenDevelopment.html)）に連なるが、本テンプレートの独自性は、この規律を「プログラマー個人の内面的な自制」としてではなく、「エージェントから人間への物理的な承認ゲート」として外部化した点にある。

Jez Humble と David Farley の名著 *Continuous Delivery* は、ソフトウェアのリリースプロセスを「デプロイメント・パイプライン」という一連のテスト（検証）ゲートとして捉え、各ゲートを通過するごとに変更への信頼度が高まるモデルを提示した。本テンプレートの「フェーズゲート」は、このパイプラインの思想をデプロイ時だけでなく、**「AIによるコード生成の推論中」**という開発の最も上流へと前倒し（シフトレフト）したものである。

「AT-TDD」という語を業界標準の新しいバズワードとして売り込むつもりはない。README にその注記があるのは、単なる誠実さのためだ。呼び名よりも、ゲートが実在することが重要である。受入仕様を先に置くという発想は、Specification by Example（実例による仕様）や BDD（振る舞い駆動開発）の哲学と深く共鳴する。Gojko Adzic の *Specification by Example*（[公式サイト](https://gojko.net/books/specification-by-example/)）や、Dan North の BDD 紹介（[dannorth.net](https://dannorth.net/introducing-bdd/)）は、システムがどう作られるべきかよりも、システムが「どう振る舞うべきか」を具体例を通じて言語化し、関係者間の共有理解を作ることを重視している。

AI 協働では、この「振る舞いの言語化」と「共有理解」が人対人の開発以上に重要になる。AI エージェントは、仕様の空白を悪びれずに推測で埋めるからだ。だからこそ、空白の少ない受入仕様が先に要る。EARS（[IEEE Xplore](https://ieeexplore.ieee.org/document/5328509)）のような要求構文は、入力側の曖昧性を物理的に減らす道具として極めて有効である。

## フェーズスキップを止める：責任の順序

「曖昧な依頼から、一気に本番コードへ直行する」——これはエージェント特有の、そして最も危険な失敗様式である。この暴走を防ぐためには、フェーズスキップの絶対的な禁止が第一の防壁になる。Red のあとに Green を、Green のあとに Refactor を。Phase 1 のテストが Adjudicator によってレビューされないまま Phase 2 の実装に入ることを、プロセスとして物理的に許さない。

ここで重要なのは、フェーズが単なる「作業の順序」ではなく「責任の順序」でもあることだ。Phase 1 では、エージェントは期待される振る舞いをテストコードへ翻訳するが、本番実装の責任はまだ持たない。Adjudicator は、その翻訳がドメインの要求と一致しているかを確認する。Phase 2 では、エージェントはレビュー済みテストを通すための最小実装を書く責任を負うが、逆に「テストを変える権限」を剥奪される。Phase 3 では、振る舞いを変えずに読みやすさを改善する。各フェーズで権限と責任を明確に分離するからこそ、人間は一度のレビューでひとつのコンテキストに集中できる。

フェーズスキップは、しばしば AI の「善意」から起こる。「ついでにここも直しておきました」「テストも実装に合わせて少し調整しました」「リファクタもしておきました」。AI はこの「ついで」を高速かつシームレスに実行する。だからこそ、その「ついで」を禁止する。仕事を小さく区切ることは、AI の生産性を落とす敵ではない。人間のレビュー可能な単位を守り、プロジェクト全体の速度を維持するための安全装置である。

## 注意力は希少資源

人間のレビューを全トークンに向けるべきではない。ADR 0003 は "Human review is focused on decision points instead of every token of output" と明確に述べる。注意力はソフトウェア開発における最も希少な資源として、設計に組み込まれなければならない。ゲートの数を無闇に増やすことが目的ではない。決定点の質と重みを保つことが目的である。プロセスを単なる煩雑な書類仕事にしてしまうリスク——ADR 0003 が Negative として挙げるもの——は、運用の中で常に警戒しなければならない。

Amershi et al. の Human-AI Interaction guidelines（[Microsoft Research](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)）は、AI システムがユーザーに適切なタイミングで情報を示し、修正や介入を可能にすることを重視する。本テンプレートの Adjudicator ループは、開発プロセス全体を巨大な Human-AI Interaction システムと見たときのアーキテクチャ設計である。人間が介入すべき地点を、phase transition、ADR acceptance、test review、ambiguity decision として明確に名前付けし、それ以外を自動化する。

## 能力向上はゲート撤廃の理由にならない

AI モデルの基礎能力が向上し、より「賢く」なったとしても、Adjudicator の所有権やフェーズゲートは撤廃されない。ゲートは能力不足の一時しのぎ（ワークアラウンド）ではなく、ソフトウェアにおける責任と監査可能性のための不変の構造である。エージェントがより多くを自律的に生成できるようになればなるほど、暴走時の被害は大きくなり、決定点の設計はむしろ重要性を増す。

強いモデルは、より説得的な説明と、より広範な変更を一度に生成できる。これは極めて便利だが、誤った前提をコードベース全体へ一瞬で広く浸透させる破壊力でもある。モデルが弱い時代の最大の危険は「AIにできないこと」だった。モデルが強い時代の最大の危険は「AIが（誤ったまま）できてしまうこと」である。Adjudicator の役割は、AI の能力を疑って盲目的に止めることではなく、AIの強大な能力がプロジェクトの責任構造の境界を越えないようにコントロールすることだ。

この文章自体は、運用テンプレートに新しいゲートを追加するものではない。ここで述べた哲学が具体的な規則へ進む必要があるなら、ADR や collaboration 文書へ別途昇格する（[規範と読み物](2026-07-06-rationale-normative-vs-reading-documents.md)）。その一線を守ることも、Adjudicator-centered collaboration の重要な一部である。

## 参考文献

1. **プロジェクト内部規定**
   - `docs/architecture/adr/0003-ai-human-collaboration-governance.md`
   - `docs/at-tdd/process.md`
   - `README.md`
   - `docs/collaboration/template-benefits.md`
2. **自動化と人間工学**
   - Bainbridge, L. "Ironies of Automation." *Automatica*, 1983. https://www.sciencedirect.com/science/article/abs/pii/0005109883900468 （取得 2026-07-16）
   - Amershi, S. et al. "Guidelines for Human-AI Interaction." CHI 2019. https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ （取得 2026-07-16）
3. **テスト・継続的デリバリー・振る舞い駆動開発**
   - Fowler, M. *Test Driven Development*. https://martinfowler.com/bliki/TestDrivenDevelopment.html （取得 2026-07-16）
   - Humble, J., Farley, D. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*. Addison-Wesley, 2010.
   - Adzic, G. *Specification by Example*. https://gojko.net/books/specification-by-example/ （取得 2026-07-16）
   - Cucumber. *Behaviour-Driven Development*. https://cucumber.io/docs/bdd/ （取得 2026-07-16）
   - North, D. "Introducing BDD." https://dannorth.net/introducing-bdd/ （取得 2026-07-16）
4. **要求工学とエージェント設計**
   - Mavin, A. et al. "Easy Approach to Requirements Syntax (EARS)." IEEE RE'09. https://ieeexplore.ieee.org/document/5328509 （取得 2026-07-16）
   - Anthropic. *Building effective agents*. https://www.anthropic.com/research/building-effective-agents （取得 2026-07-16）
   - Wu, Q. et al. "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." arXiv:2308.08155. https://arxiv.org/abs/2308.08155 （取得 2026-07-16）
   - Yue, M. et al. "Large Language Model Cascades with Mixture of Thoughts Representations for Cost-efficient Reasoning." ICLR 2024 / arXiv:2310.03094. https://arxiv.org/abs/2310.03094 （取得 2026-07-16）
   - Anthropic. *How we built our multi-agent research system*. https://www.anthropic.com/engineering/built-multi-agent-research-system （取得 2026-07-16。ベンダー内部評価の自己報告）
