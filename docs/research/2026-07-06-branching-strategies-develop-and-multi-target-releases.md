# develop と複数リリース先

2026-07-06 調査。非規範。関連: LISS-0005 項目4。
方針の記録: [ブランチと統合](2026-07-06-rationale-branching-and-release-strategy.md)。

---

第2アダプターは `develop` を作り、マージ戦略を実行しなかった。feature ブランチに
スタックが溜まり、統合は先送りされた。Referee は、テンプレートが develop を禁止すべきか、
複数リリース先を持つ大型プロダクトをどう支えるべきかを問った。本稿はその調査稿である。
結論を先に述べる。研究が責めるのは長命ブランチの存在ではなく統合遅延であり、
マルチターゲットを健康に保つのは上流優先の伝播と設計レベルの分岐である。

## develop は許容しうるか

DORA は 3 万人超・7 年以上の調査から trunk-based development をエリート性能の
予測因子として同定するが、その操作的定義は「長命ブランチゼロ」ではない。
アクティブブランチを 3 本以下に保ち、1 日少なくとも 1 回トランクへマージする——
これが要求である
（[DORA Capabilities](https://dora.dev/capabilities/trunk-based-development/)、
取得 2026-07-07）。害は integration latency として現れる。日次で統合し短周期で
main へ出す develop は trunk に近い。週単位で乖離を溜める develop は、測定された
アンチパターンそのものだ。

Driessen の 2020 年追記は、継続デリバリの Web には GitHub flow のような単純な
フローを勧め、明示的バージョン付けや複数バージョンの野外サポートには GitFlow が
依然適合しうると述べる
（[nvie.com](http://nvie.com/posts/a-successful-git-branching-model/)、取得 2026-07-07）。
develop の正当な領域は、2010 年代に流行したときよりずっと狭い。

## 複数リリース先はどう流れるか

よくある誤解は、複数ターゲットへ feature を cherry-pick で組み立てるというものだ。
調査した実践ではそうではない。main が単一の真実源であり、未完成機能は feature flag
の背後にある。リリースは main のある時点のスナップショット——GitLab の release ブランチ、
Microsoft Release Flow の sprint ブランチ、Kubernetes の `release-X.Y`、Chromium の
リリースチャネル——がこの形をとる。cherry-pick は切り出し後の修正バックポート用であり、
機能セットを diverge したブランチ間で cherry-pick し続けることは、コンフリクトと
リグレッションのリスクからアンチパターンとして扱われる。

### upstream-first

「共通変更を早く波及させる」を検査可能にする規律は upstream-first である。
GitLab Flow は修正をまず main に入れ release へ cherry-pick する——Google と Red Hat も
同様と明記する
（[GitLab Flow best practices](https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/)、
取得 2026-07-07）。Microsoft Azure DevOps チームは mainline で変更し release へポートする
（[Microsoft branching guidance](https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops)、
取得 2026-07-07）。Kubernetes は cherry-pick が main に存在することを前提とし、
新しい release から古い release へ、該当する全アクティブブランチへ適用することを
求める
（[cherry-pick policy](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-release/cherry-picks.md)、
取得 2026-07-07）。

### 分岐は設計で

ターゲット間の差は feature flag、設定、ビルド変化、モジュール境界——ports/adapters——で
作る
（[Fowler: Feature Toggles](https://martinfowler.com/articles/feature-toggles.html)、
取得 2026-07-07）。恒久の per-target ブランチは DORA の長命ブランチ警告を二重に受ける。

これらの組織が「1 PR = 1 自己完結した論理変更、flag で守る」規律を課すのは、
バックポートと revert を安全にするためである。粒度規律は upstream-first の前提であり、
リリース組み立ての手段ではない。

## GitFlow の develop と下流 release ライン

GitFlow は develop を main の上流に置く。Release Flow と GitLab Flow は main を
唯一の統合トランクとし、release / 環境ブランチを下流に置く。共通変更の早期波及は
下流モデルのほうが構造的に保証しやすい。`develop` という名を残すプロジェクトは、
実質を main 下流のステージング/環境ブランチとして定義し直す余地がある。

## LISS-0005 項目4 への提案

「develop には ADR が要る」という準禁止を、「統合契約のもとで長命ブランチを許容する」
へ置き換える根拠は、上記のエビデンスが支持する。既定は trunk 指向——main と短命
ブランチ。長命の統合・release・環境ブランチは、マルチバージョン/マルチターゲット
向けに正当化しうるが、採用プロジェクトの ADR が契約を定義すべきである。

- 上流の真実源（共有変更は upstream-first）
- 数値の統合頻度（統合ラインへ日次、main へ 1〜2 週以内など。超過は違反として可視化）
- 伝播規則（全アクティブターゲットへ新→旧、単一 issue で追跡）
- 分岐の階層（flag → 設定 → port/adapter → 恒久 per-target ブランチは最終手段＋別 ADR）
- 各 release ブランチの EOL とロック方針

## 参考文献

1. 内部: LISS-0005、`docs/collaboration/branch-commit-pr-discipline.md`
2. DORA. *Trunk-based development*.
   https://dora.dev/capabilities/trunk-based-development/ （取得 2026-07-07）
3. Driessen, V. *A successful Git branching model* (reflection 2020).
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
8. Runway. "Cherry-picks vs backmerges."
   https://www.runway.team/blog/cherry-picks-vs-backmerges-whats-the-right-way-to-get-fixes-into-your-release-branch
   （取得 2026-07-07、記事存在確認）
9. Squires, J. "Comparing release branch strategies." 2022.
   https://www.jessesquires.com/blog/2022/03/27/comparing-release-branch-strategies/
   （取得 2026-07-07、記事存在確認）
10. Chromium. "Merging to release branches."
    https://www.chromium.org/developers/how-tos/drover/ （取得 2026-07-07、ページ存在確認）