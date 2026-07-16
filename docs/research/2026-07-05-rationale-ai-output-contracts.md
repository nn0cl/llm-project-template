# 出力の契約と検証可能性の境界

2026-07-05。非規範。関連: ADR 0002。

---

ソフトウェアエンジニアリングにおいて「契約（Contract）」という概念は、単なるインターフェースの定義を超えた深い哲学を持っている。Bertrand Meyer が提唱した「契約による設計（Design by Contract）」（[Meyer, 1992](https://doi.org/10.1109/2.161279)）は、呼び出し元と呼び出し先の間に事前条件、事後条件、不変条件を厳密に定義することで、ソフトウェアの信頼性を担保しようとした。この哲学は、AI時代において新たな次元の重要性を帯びている。

流暢な散文は、正しさの保証ではない。これは LLM に対する不信の表明というより、ソフトウェア境界の設計原則である。人間も誤る。検索結果も古くなる。データベースにも欠損がある。システムを構築する際、私たちは常に不完全なコンポーネントを組み合わせる。違いは、LLM の出力がしばしば「完成した説明」の形をとるため、検証されていない推測まで完成品に見えてしまう点にある。だからこそ、AI 出力の信用を「もっと賢いモデル」に委ねず、Meyer の言うような検証可能な契約へと移さなければならない。

## 提供側の自由と利用側契約：インターフェースの安定

契約による設計を、AI 協働のコード変更に写すとき、Semantic Versioning（[semver.org](https://semver.org/)）が求める「公開 API を明確に宣言し、後方互換でない変更は major version として扱う」という考え方は **分かりやすい類推**になる。提供側（実装）をどれほど綺麗にしても、利用側が依存する公開契約を黙って壊せば、システム全体の信頼が崩れる——という教訓として読む。

AI エージェントはコードベースを広く書き換えられるため、「内部を直すついでに引数や戻り値の型まで変える」誘惑に弱い。内部（例: Clean Architecture の Adapter）の最適化は許容しうるが、**利用側との Interface や外部呼び出し規約を勝手に変えない**、というのがここでの実務ルールである（ADR 0002 の精神とも整合する）。契約は JSON スキーマの型チェックだけではない。提供側と利用側の信頼境界であり、生成の自由度を閉じ込めるための設計である。パッケージのバージョニング制度と同一の運用を求めているわけではない。**類推は理解の補助であり、移植可能な法則ではない。**

## 散文の流暢さと事実性の分離

Ji et al. のハルシネーション調査（[arXiv:2202.03629](https://arxiv.org/abs/2202.03629)）は、生成の流暢さと事実性が独立しうることを体系的に整理している。また、Maynez et al. の要約研究（[ACL Anthology](https://aclanthology.org/2020.acl-main.173/)）は、抽象要約が入力に忠実でない内容を生成しうることを、faithfulness（忠実性）と factuality（事実性）の観点から分析した。

これらの研究が与える教訓は共通している。AI 出力の根本的な問題は「たまに嘘をつく」ことではない。出力されたテキストの表面を見るだけでは、それが何に基づいているか、どこまで確かか、業務のドメイン事実として採用してよいかが原理的に判定不能だということである。

ADR 0002 が拒否するのは、検証も出典追跡も人間レビューも、信頼できるストアへの安全な書き戻しもできない散文である——"useful-looking prose that cannot be validated, traced to source evidence, reviewed by a human, or safely written back into any trusted store"。出力は最初から、拒否・レビュー・永続化が可能な形で受け取られなければならない。

## 散文を悪者にしない：情報隠蔽と境界の設計

誤解してはいけない。散文は不要ではない。説明、要約、探索、設計案の提示といった、人間のインスピレーションや判断を助ける領域においては、散文が圧倒的に向いている。問題は、David Parnas が「情報隠蔽（Information Hiding）」で説いたようなモジュール境界を無視して、散文をそのまま信頼境界の内側（システムの状態として永続化される領域）に入れてしまうことである。レビュー画面に表示される説明文と、ドメインが信頼する事実レコードは別物でなければならない。

この区別は、型やスキーマが大事だという平凡な話に見えるかもしれない。しかし LLM を組み込むと、この平凡な境界が急に破られやすくなる。SDK の戻り値にもっともらしい `message.content` が入っている。デモではそれを画面に出すだけで価値が出る。次に、その文字列を DB に保存したくなる。最後に、保存された文字列が「確認済みの知識」として別の use case に読まれる。事故は、この滑り台の上で起こる。

出力契約は、その滑り台に段差を作る。これは「AI を信用するな」という感情論ではなく、「信用する場所を明示せよ」というアーキテクチャ上の要請である。自由記述の説明は説明として扱う。信頼できる知識は、出典、確信度、レビュー状態、採用範囲を持つ構造化データとして扱う。

## 推論は証拠として残す：監査可能性の担保

推論を、LLM の隠れた思考プロセスとしてブラックボックス化してはならない。それは監査可能な証拠として扱うべきである。ユーザー可視の内容や永続状態に影響するなら、根拠、引用、出典スパン、仮定、棄却した代替案、確信度、レビュー状態を記録する（ADR 0002）。ただし記録するのは chain-of-thought の生ダンプではない。構造化された証拠である。私的な思考過程を露出させず、差分としてレビューできる形だけを残す。

この「証拠としての推論」は、人間のレビュー時間を短くするための設計でもある。レビュアーが知りたいのは、モデルが内心どのような文章をたどったかではない。どの入力断片を根拠にしたか、何を仮定したか、どこが不確かか、この出力を採用するとどの保存先や UI に影響するかである。AI の説明責任を chain-of-thought の露出へ短絡させる必要はない。業務で必要な説明責任は、ソース参照とレビュー状態の適切なデータ設計でかなりの部分を満たせる。

Amershi et al. の Human-AI Interaction guidelines（CHI 2019）は、AI システムが不確実性を適切に示し、ユーザーのフィードバックや修正を支えることの重要性を整理している。出力契約は、この UI レベルの原則をアプリケーションのデータ境界まで下げたものだ。不確実性を UI に表示するには、まずシステム内部に「不確実性」が構造化されたデータとして存在しなければならない。

## レビューで拒否できる規則に落とす

理念で終わらせてはならない。自由記述の AI 散文を、なんら検証せず信頼できるドメインデータとして扱う use case は明確に reject する。出典証拠もレビュー状態も伴わず永続化された AI 由来の知識も reject する（ADR 0002 Enforcement）。散文を業務事実として DB に書き込む設計は、最初からアーキテクチャのレベルで許容しない。

スキーマで検証可能な出力は、主要プロバイダが一級機能として提供し始めている。OpenAI の Structured Outputs や Anthropic の Structured outputs はその例である。だが重要なのは、プロバイダの機能そのものではない。プロバイダが JSON Schema に近い形を返せるとしても、その構造をアプリケーションの信頼境界にどう接続するかはプロジェクト側の責任である。

Clean Architecture の観点では、provider SDK の便利機能は adapter の内側に留まるべきである。use case が受け取るのは SDK 固有の応答ではなく、プロジェクトが定義した DTO（Data Transfer Object）と validation result である。モデルが構造化出力を返すことは、契約の実装を助ける。しかし契約そのものではない。契約は、何を必須とし、何が欠けたら reject し、どの状態なら human review required とするかを決めるプロジェクト側にある。

## 永続化は採用の宣言である

AI 出力を一時的に画面に表示することと、信頼できるストアへ保存することは重みが決定的に違う。保存は、将来の use case がその情報を再利用してよいという宣言になりやすい。たとえ UI 上で「未確認」と表示していても、DB の別テーブルへコピーされた瞬間にレビュー状態が失われる設計なら、未確認性は実質的に消滅し、システム内に汚染が広がる。

したがって、出力契約は保存先まで含めて考える必要がある。`review_status`、`source_refs`、`confidence`、`warnings`、`scope` のような情報は、画面表示の装飾ではない。後続処理がそのデータをどう扱ってよいかを決める制御情報である。

`docs/architecture/external-resource-adoption-contract.md` が外部 resource に採用ライフサイクルを置くのも、同じ発想である。検査の結果は `accepted | rejected | needs_recheck` であり、**検査に通った（accepted）だけでは信頼利用中ではない**。常用・信頼境界への投入は別遷移の `accepted -> adopted` である（用語は [README](README.md) の accepted / adopted）。由来が AI か人間かにかかわらず、外部由来のものをプロジェクトの信頼境界へ入れるには、厳密な採用の記録が要る。

## このフォルダ自身の作法

`research` の出典に取得日を付し、未検証 URL を明記する運用は、同じ契約の概念を人間向け文書へ適用したものである。推測で文献を補わない。ハルシネーションをコードや API だけの問題と見なさない。ドキュメントも、システムを構成する重要な要素である以上、同じ防壁が要る。

ただし `docs/research/` は、運用テンプレートの規則を一方的に変更する場所ではない。ここにある文章は、人間がソフトウェア開発の哲学を読み解くための explanation であり、AI エージェントに機械的に読ませる契約ではない。ある主張がプロジェクトの規範へ進むなら、ADR、collaboration 文書、issue など、別の reviewable artifact へ昇格しなければならない。この分離そのものが、出力契約の思想と通じている。説明は説明として豊かに書く。採用する規則は、別の境界で明示的に採用する。

## 参考文献

1. **プロジェクト内部規定**
   - `docs/architecture/adr/0002-input-output-reasoning-contracts.md`
   - `docs/architecture/io-reasoning-contracts.md`
   - `docs/architecture/external-resource-adoption-contract.md`
   - `docs/research/README.md`
2. **ソフトウェア工学・哲学**
   - Meyer, B. "Applying 'Design by Contract'". IEEE Computer, 1992. https://doi.org/10.1109/2.161279 （取得 2026-07-17）
   - Parnas, D. L. "On the Criteria To Be Used in Decomposing Systems into Modules". CACM, 1972. https://doi.org/10.1145/361598.361623 （取得 2026-07-17）
   - Preston-Werner, T. *Semantic Versioning 2.0.0*. https://semver.org/ （公開 API の宣言、および互換性のない API 変更における major version increment の規則を参照。取得 2026-07-17）
3. **AI研究・ヒューマンコンピューターインタラクション**
   - Ji, Z. et al. "Survey of Hallucination in Natural Language Generation." *ACM Computing Surveys* / arXiv:2202.03629. https://arxiv.org/abs/2202.03629 （取得 2026-07-16）
   - Maynez, J. et al. "On Faithfulness and Factuality in Abstractive Summarization." ACL 2020. https://aclanthology.org/2020.acl-main.173/ （取得 2026-07-16）
   - Amershi, S. et al. "Guidelines for Human-AI Interaction." CHI 2019. https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ （取得 2026-07-16）
4. **公式ドキュメント**
   - OpenAI. *Structured Outputs*. https://platform.openai.com/docs/guides/structured-outputs （取得 2026-07-16）
   - Anthropic. *Structured outputs*. https://platform.claude.com/docs/en/build-with-claude/structured-outputs （取得 2026-07-16）
   - Anthropic. *Increase output consistency*. https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency （取得 2026-07-16。旧 docs.claude.com URL はここへリダイレクトされる）
