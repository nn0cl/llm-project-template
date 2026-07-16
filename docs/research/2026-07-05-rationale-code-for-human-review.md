# レビュー可能なコードと認知負荷の管理

2026-07-05。非規範。関連: ADR 0004。

---

コード生成コストがほぼゼロに近づいたとき、ソフトウェア開発における最大のボトルネックは「書く速度」から「検証する速度」へと不可逆的に移動する。かつて「コードを書くこと自体の物理的・認知的摩擦」が自然に抑えていたシステムの複雑性は、もはや自動的には抑制されない。

AI は、躊躇なく 800 行のファイルを生成する。少しずつ異なるヘルパー関数を三つ作る。責務の境界を曖昧にしたまま、テストを通す局所的な正解を組み合わせる。これらに悪意はない。単に生成の摩擦が低く、かつ長期的な保守性を評価するフィードバックループが即座には働かないからそうなるのだ。Frederick Brooks は「銀の弾丸などない」で、ソフトウェアの複雑性には「偶発的複雑性（Accidental Complexity）」と「本質的複雑性（Essential Complexity）」があると述べた。AI は、私たちが偶発的複雑性を大量に生み出す手助けをいとも簡単にやってのける。

だからこそ、私たちは規範として「読むことの価値」を復元する。生成コードの最適化目標は「テストが通る動く最小構成」ではなく、人間の認知負荷の最小化である（CLAUDE.md、ADR 0004）。テストを通すためだけの密度の高い（dense な）Green は、私たちが受け入れる Green ではない。賢い圧縮より読める冗長を選ぶ。"Do not compress implementation into dense code just to be minimal"——この釘は、プログラミングが書き込み偏重の時代（AI 時代）に突入したからこそ、最も重要になる。

## 理解がレビューの主戦場である

Bacchelli & Bird による大規模調査（[Microsoft Research](https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/)）は、現代的コードレビューの期待・成果・課題を詳細に調べ、「変更の理解」がレビューにおける最大の障害であることを示した。コードレビューは単なる静的な欠陥検出器ではない。それはチーム内での知識共有、代替案の検討、設計の健全性確認、そして将来保守の準備という複合的な社会的プロセスである。そのすべての前提に、「まず人間が読めること」がある。

John Ousterhout は著書 *A Philosophy of Software Design* の中で、複雑性を「システムを理解し、変更しにくくするあらゆるもの」と定義する。浅いモジュール（インターフェースに比べて実装が少ないもの）と不要な間接化を強く戒める立場は、ADR 0004 の「まとめておくべき兆候」と完全に一致する。モジュール分割は絶対的な善ではない。読者が同時に頭に保持しなければならない業務判断が一つを超えるとき、初めて分ける。責務を減らさず、単にファイルを細切れにするような間接化のためだけにコードを分けてはならない。

この観点に立てば、「短いコード」は必ずしも読みやすいコードではない。短さはしばしば、コードが担うべきコンテキストを読者の脳内へ負荷として移し替える。名前が短すぎる、条件式が圧縮されすぎる、副作用が隠れている、抽象化が premature（早すぎる）である。AI がよく生成する「一見きれいな helper 群」は、一つ一つは小さくても、読む側に「なぜこの分割なのか」「どこに業務判断が隠れているのか」を推測させるなら、それは明確に複雑性の増大である。

## プログラムは理論である

Peter Naur の古典的論文 "Programming as Theory Building" （[PDF](https://pages.cs.wisc.edu/~remzi/Naur.pdf)）は、プログラミングを「単に動作するテキスト（コード）を作る行為」ではなく、「開発者がシステムがどのように動くべきかについての理論を形成する行為」として捉える。コードは理論の一部ではあるが、理論そのものではない。なぜその分割なのか、なぜその境界なのか、どの変更には強くどの変更には弱いのか——こうしたシステムへの深い理解がチーム内で共有されていなければ、同じファイルを持っていても同じプログラムを「所有している」とは言いにくい。

AI 生成コードの危うさの核心はここにある。AI はテキストを驚異的な速さで作れるが、チームの共有理論を自動では作らない。むしろ、十分なレビューを経ずにシステムに統合された生成物は、チーム内の理論の断絶を指数関数的に増やす。したがってレビュー可能性とは、単に style guide に従っているかどうかをチェックすることではなく、チームがその変更の背後にある理論を再構築し、システムへの理解を取り戻せるようにすることである。

`docs/collaboration/source-code-quality.md` が小さな関数、明示的な名前、薄い Adapter（Clean Architecture）、読みやすい Given/When/Then を強く求めるのは、審美眼や好みの問題ではない。次にコードを触る人間（あるいはエージェント）が、そのコードの理論を容易に再構築できるようにするための、生存戦略である。

## 依存方向は認知負荷を局所化する規律

ドメインがフレームワークの知識なしに読めること、ビジネスルール（Business Policy）が Clean Architecture の Adapter（ポート実装。採用者ではない。用語は [README](README.md)）に漏れ出さないこと。Clean Architecture に代表される依存規律は、システムを疎結合にするだけでなく、レビュー対象を人間の認知限界に合わせて局所化する極めて実用的な手段である。

Robert C. Martin の "The Clean Architecture"（[Clean Coder Blog](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)）は、依存関係が外側（詳細）から内側（抽象）へ向かうという強力な方針を示す。この方針を AI-TDD のワークフローに持ち込む理由は、アーキテクチャの純粋主義を満たすためではない。一度のレビューで人間が読まなければならない単位を小さくするためだ。

Clean Architecture の Adapter に業務判断が隠れると、レビュアーは provider SDK の仕様、エラーハンドリング戦略、永続化形式、そして業務ルールを「同時に」読解しなければならなくなる。UI component に business policy が混入すれば、表示状態のライフサイクルとドメイン判断が絡み合う。use case が DB schema を直接知ると、変更の理由がデータベースの技術都合なのか、ビジネス側の要求変更なのか分からなくなる。依存方向の違反は、ほとんどの場合、システムの凝集度を下げ、レビュアーの認知負荷を爆発的に増大させる形で表れる。

## テストも読者のためにある

レビュー可能なコードは、レビュー可能なテストを必然的に伴う。AI が作るテストは、ときに大量の mock setup と細かな実装の内部状態検査（ホワイトボックステスト）に寄りがちである。しかし Phase 1 Red の段階でテストが検証すべきものは、実装の先取りではなく、受入仕様としての外部振る舞いである。

Given / When / Then は、単なる BDD（振る舞い駆動開発）の形式的フォーマットではなく、レビュー者の読み順を固定し、コンテキストを提示する強力な手段である。何が前提で、何を起こし、何を観測するのか。テスト名がこの三点を明確に伝えられないなら、テストは仕様の代わりにはならない。Martin Fowler の TDD 解説（[martinfowler.com](https://martinfowler.com/bliki/TestDrivenDevelopment.html)）が示す Red / Green / Refactor のリズムは、AI-TDD においてはさらに「そのテストを人間が読めるか」という厳しいゲートを伴う。

テストが読みやすいと、実装のレビューも劇的に軽くなる。仕様がテストコードに明確に現れていれば、レビュアーは「このコードが何を満たすべきか」を毎回推測しなくてよい。逆にテストが実装詳細に強く依存すると、AI はテストを満たすための局所最適へと進み、結果として Phase 2 Green の実装コードも読みにくく、変更に脆いものになりやすい。

## 未来のエージェントも読者である

可読性は人間だけのためのものではない。セッションをまたぐ AI との継続的な協働の前提条件でもある。"Future agents can resume work without rediscovering hidden intent"（ADR 0004）。モデルが文脈外の暗黙知（チャットの履歴など）に依存して書いたコードは許容しない。コードは自己完結的で、その意図を自ら語るべきだ。この点で本稿の思想は、[設計先行とコンテキスト](2026-07-05-rationale-design-first-minimal-context.md) の議論と深く接続する。

「未来のエージェント」は research を読ませて哲学を学ばせる、という意味ではない（[README](README.md)：日々の作業入力としては読む必要がない）。従う規則は列挙された規範文書にある。本稿は、人間が規則を儀式化せず維持するための読み物である。

## 参考文献

1. **プロジェクト内部規定**
   - `docs/architecture/adr/0004-human-readable-source-code-quality.md`
   - `docs/collaboration/source-code-quality.md`
   - `CLAUDE.md`
   - `docs/collaboration/template-benefits.md`
2. **ソフトウェア工学・哲学**
   - Ousterhout, J. *A Philosophy of Software Design*. https://web.stanford.edu/~ouster/cgi-bin/book.php （取得 2026-07-16）
   - Naur, P. "Programming as Theory Building." 1985. https://pages.cs.wisc.edu/~remzi/Naur.pdf （取得 2026-07-16）
   - Brooks, F. P. *No Silver Bullet - Essence and Accidents of Software Engineering*. 1986.
3. **アーキテクチャ・テスト手法**
   - Martin, R. C. "The Clean Architecture." 2012. https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html （取得 2026-07-16）
   - Fowler, M. *Test Driven Development*. https://martinfowler.com/bliki/TestDrivenDevelopment.html （取得 2026-07-16）
4. **コードレビュー研究**
   - Bacchelli, A., Bird, C. "Expectations, Outcomes, and Challenges of Modern Code Review." ICSE 2013. https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/ （取得 2026-07-16）
5. **その他**
   - zakirullin. *Cognitive Load is what matters*. https://github.com/zakirullin/cognitive-load （取得 2026-07-16、README 存在確認。査読研究ではなく実務者エッセイ。本文では引用していない補足読み物）
