# pull 型の上流

2026-07-06。非規範。関連: ADR 0008、LISS-0001。

---

テンプレートはコピーされた瞬間から古くなる。陳腐化は欠陥ではなく、構造の帰結だ。
問題は古さそのものではなく、上流が下流を知り、下流を書き換えようとすることである。
私は push ではなく pull を採る。いつ同期するかは各アダプターが決め、上流は
レジストリも書き込み資格情報も持たない（ADR 0008）。

## 主権を既定で保護する

3-way merge により、テンプレートだけが変えた箇所は更新し、展開先だけが変えた箇所は
維持し、両方が変えた箇所はコンフリクトとして可視化し、展開先が削除した箇所は
無言で復活させない（ADR 0008 Decision 3）。naive な上書きはカスタマイズを壊す。
このリスクは Referee 自身が ADR に記録している。

[cruft](https://github.com/cruft/cruft)（取得 2026-07-07、リポジトリ存在確認）や
[Copier の update 機能](https://copier.readthedocs.io/en/stable/updating/)
（取得 2026-07-07、ドキュメント存在確認）は、同じ問題——boilerplate drift——に
取り組んできた。本テンプレートは `git merge-file` ベースで、追加ツール依存を
増やさず同型の構造を選んだ。

## 同期も通常の変更である

update script は trunk へ直接コミットしない。専用ブランチ、PR、CI を経る
（ADR 0008 Decision 4、ADR 0007）。テンプレート由来だから特別扱いしない。
[Renovate](https://docs.renovatebot.com/)（取得 2026-07-07、ドキュメント存在確認）が
普及させた「更新は PR として提案され、レビューと CI を通ってのみ取り込まれる」
パターンの、テンプレート版である。

クリーンマージは無審査の口実にならない。"A clean merge is not the same guarantee
as 'nothing needs review'"（ADR 0008 Consequences）。機械的成功と意味的正しさは
別物だ。

## 改善は下流から還流する

アダプターの実運用フィードバックは LISS-0002、LISS-0005 として上流へ戻る。
[GitLab Flow の upstream first](https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/)
（取得 2026-07-07、「修正はまず main へ」を確認）は、共通改善をまず上流へ置く
原則を述べる。本テンプレートの「フィードバックを LISS 化してから配る」運用と
同型である。

## 上流は下流を知らない

この設計はスケーラビリティと信頼を同時に買う。アダプター数に運用コストが
比例しない。資格情報を集中させない。対価は、同期しないアダプターは古いまま
残ること（ADR 0008 Negative）——強制より主権を優先する一貫した選択だ。

research を同期対象から外す判断
（[規範と読み物](2026-07-06-rationale-normative-vs-reading-documents.md)）も、
下流に配るのは規範だけであり、読み物は上流ローカルにとどめる、という同じ
主権方針の現れである。

## 参考文献

1. 内部: ADR 0008、ADR 0007、LISS-0001、LISS-0002
2. cruft. https://github.com/cruft/cruft （取得 2026-07-07）
3. Copier. *Updating a project*.
   https://copier.readthedocs.io/en/stable/updating/ （取得 2026-07-07）
4. Renovate. https://docs.renovatebot.com/ （取得 2026-07-07）
5. GitLab. *GitLab Flow best practices*.
   https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/
   （取得 2026-07-07）