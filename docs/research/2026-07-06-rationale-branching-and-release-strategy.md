# ブランチと統合

2026-07-06。非規範。関連: LISS-0005 項目4。
詳細調査: [develop と複数リリース先](2026-07-06-branching-strategies-develop-and-multi-target-releases.md)。

---

GitFlow か trunk-based か——この二項対立で議論を終わらせたくない。規制の対象は
ブランチの存在ではなく、統合の遅延である。develop が存在することは十分あり得る。
大型プロダクトではリリース先ごとにブランチが錯綜することもある。それを支持する。
ただし、ラインを保持してよいのは、短周期で main へ統合する契約を付けたときだけだ。

「develop としてのラインは保持して良いが、できるだけ短い期間で main へリリース
すること。リリース先が複数あるサービスでは共通仕様をできるだけ早く波及させること。
リリース先専用の機能には厳密な設計が必要である。」

これが私の立場の核である。悪いのはラインの名前ではなく、その運用だ。

## 研究が測るのは統合遅延

DORA の trunk-based development
（[Capabilities ページ](https://dora.dev/capabilities/trunk-based-development/)、
取得 2026-07-07）は、操作的定義として「アクティブブランチ3本以下」「少なくとも
1日1回トランクへマージ」を挙げる。長命ブランチの存在禁止ではない。害は
integration latency——肥大したマージ、コードフリーズ、欠陥——として現れる。
「短周期で main へ」は、この測定対象を運用要件へ翻訳したものだ。

Vincent Driessen 自身が 2020 年の追記で述べるように、継続デリバリの Web 向けには
より単純なフローを勧め、明示的にバージョン付けされたソフトウェアや複数バージョンの
同時サポートには GitFlow（= develop あり）が依然適合しうる
（[A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)、
取得 2026-07-07、「Note of reflection · March 5, 2020」を確認）。

## 共通変更は上流から

共通仕様の早期波及を検査可能にする規律は upstream-first である。
[GitLab Flow](https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/)
（取得 2026-07-07）は修正をまず main に入れ release へ cherry-pick する。
[Microsoft の branching guidance](https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops)
（取得 2026-07-07、mainline への変更と release へのポートを確認）も同型だ。
[Kubernetes cherry-pick policy](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-release/cherry-picks.md)
（取得 2026-07-07、main 先行・新→旧の順を確認）は、古い方だけへの適用が
アップグレードでリグレッションを生むと明記する。

## 機能差分は VCS ではなく設計で

リリース先ごとの差は、feature flag、設定、ビルド構成、モジュール境界——本テンプレートの
語彙では ports/adapters——で作る
（[Fowler: Feature Toggles](https://martinfowler.com/articles/feature-toggles.html)、
取得 2026-07-07、記事存在確認）。機能セットの異なるブランチを cherry-pick で
並行維持することはアンチパターンとして扱われる。専用機能には厳密な設計が必要、
という私の言葉は、分岐をまず設計で扱いブランチ分岐を最終手段とする、という
業界実践と同型だ。

## develop の位置づけ

GitFlow の develop は main の上流にある。Release Flow や GitLab Flow は main を
唯一のトランクとし、release / 環境ブランチを下流に置く。共通仕様の早期波及は
下流モデルのほうが構造的に保証しやすい。develop という名を残すなら、その実質を
main 下流のステージング/環境ブランチとして定義し直す価値がある。

統合契約付きの許可モデルへの規範化は、LISS-0005 項目4の Referee 判断として
保留中である。本稿は方針の記録にとどめ、数値目標や伝播規則の条文化は規範側の仕事だ。

## 参考文献

1. 内部: LISS-0005、`docs/collaboration/branch-commit-pr-discipline.md`
2. DORA. *Trunk-based development*.
   https://dora.dev/capabilities/trunk-based-development/ （取得 2026-07-07）
3. Driessen, V. "A successful Git branching model." 2010, reflection 2020.
   http://nvie.com/posts/a-successful-git-branching-model/ （取得 2026-07-07）
4. GitLab. *GitLab Flow best practices*.
   https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/
   （取得 2026-07-07）
5. Microsoft. *Git branching guidance*.
   https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops
   （取得 2026-07-07）
6. Kubernetes SIG Release. *Cherry-pick policy*.
   https://github.com/kubernetes/community/blob/main/contributors/devel/sig-release/cherry-picks.md
   （取得 2026-07-07）
7. Fowler, M. "Feature Toggles."
   https://martinfowler.com/articles/feature-toggles.html （取得 2026-07-07）