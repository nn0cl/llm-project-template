# リポジトリに計画を置く

2026-07-05。非規範。関連: ADR 0005、ADR 0006。

---

チャットは成果物ではない。セッションで決めたこと、計画したこと、文脈として渡した
こと——放っておけばログに埋もれて消える。エージェントはサンドボックス内では自由に
動けるが、プロジェクトとして統合する配線は外側——リポジトリ、CI、承認——に置く
（[エージェントはサンドボックスである](2026-07-07-rationale-saas-agent-as-sandbox.md)）。
私は、計画・指示・来歴をすべてリポジトリ内のファイルとし、コードと同じレビュー、
CI、差分管理の対象に載せる。挙動を変えるものは、理由とレビューと痕跡を伴ってだけ
変わる。

## 計画はファイルである

local issue（LISS）と work plan は `docs/issues/` と `docs/work-plans/` に置く。
GitHub へのネットワークアクセスなしに計画が成立する（ADR 0005）。エージェントが
設計インテーク中に読めるリポジトリローカルな成果物が必要だからだ。計画の読者に
エージェントを一級として想定している。

計画は ToDo リストではない。depends_on / blocks / parent で表される依存グラフ
である。未解決の depends_on がある issue に着手してはならない。

決定の記録をリポジトリに置く発想の原典は Nygard の ADR 提言
（[Documenting Architecture Decisions, 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)、
取得 2026-07-07、本文に「決定を版管理下の短いテキストで残す」方針を確認）である。
本テンプレートは ADR を計画（issue）・指示（契約ファイル）・来歴（trace）へ拡張する。

## プロンプトは設定ではなくコード

`AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md` は近接して重複した
操作契約である。放置すれば無言でドリフトする（ADR 0006）。変更には理由、Referee
レビュー、ファイル間整合、trace を要求し、CI が trace 欠落を拒否する。

これは docs-as-code の延長だ
（[Write the Docs: Docs as Code](https://www.writethedocs.org/guide/docs-as-code/)、
取得 2026-07-07）。ただし対象は説明書ではなく、エージェントの挙動そのものである。

## local-first の計画

Ink & Switch の local-first
（[2019](https://www.inkandswitch.com/local-first/)、取得 2026-07-07、
エッセイページ存在確認）は、所有権と可用性をローカルに置く原則を述べる。
GitHub は有用だが、計画の一次台帳はリポジトリ内——この二層構造は、計画における
local-first と読める。

## 観測が規範を更新する

ADR 0005 の Negative（local と GitHub メタデータのドリフト、status 更新の規律依存）は、
第2アダプターレビューで親 issue の陳腐化として顕在化した。その観測は LISS-0005 へ
還流している。規範は机上の理念で終わらせない。
[エビデンスと規則](2026-07-06-rationale-evidence-based-process-design.md) が述べる
フィードバックループの実例である。

## 参考文献

1. 内部: ADR 0005、ADR 0006、`docs/collaboration/local-issue-planning.md`、
   `docs/collaboration/prompt-instruction-change-control.md`、
   `docs/collaboration/ai-work-trace-log.md`
2. Nygard, M. "Documenting Architecture Decisions." 2011.
   https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
   （取得 2026-07-07）
3. Kleppmann, M. et al. "Local-first software." Ink & Switch, 2019.
   https://www.inkandswitch.com/local-first/ （取得 2026-07-07）
4. Write the Docs. *Docs as Code*.
   https://www.writethedocs.org/guide/docs-as-code/ （取得 2026-07-07）