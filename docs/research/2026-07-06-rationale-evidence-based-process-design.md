# エビデンスと規則

2026-07-06。非規範。関連: LISS-0002、LISS-0005、`process-gap-register.md`。

---

開発プロセスの規則は、流行と声の大きい事例と個人の成功体験で決まりがちだ。
「そのプラクティスは自分たちの文脈で効くのか」を確かめる習慣は、業界に十分
定着しているとは言えない。私は、規則を固定する前に調べ、自プロジェクトの文脈と
突き合わせ、Referee が決める作法を採る。

「先行研究や実証研究、先行サービスの事例、ベストプラクティスなどを調べて
分析して相談に乗って。」

これは develop の扱いを直観で決めない、という要求として出た言葉だ。だが一般則として
三つのパターンに現れる。規則の前に調査する。アダプターのフィードバックを改訂の
一次入力にする。調査と規範を分離して両方残す。

## EBSE の系譜

Kitchenham, Dybå, Jørgensen（[ICSE 2004 PDF](https://web-backend.simula.no/sites/default/files/publications/SE.5.Kitchenham.2004.pdf)、
取得 2026-07-07、PDF 到達確認）は evidence-based practice をソフトウェア工学へ
移植することを提唱した。Dybå et al.（[IEEE Software 2005 PDF](https://web-backend.simula.no/sites/default/files/publications/Dyba.2005.1.pdf)、
取得 2026-07-07、PDF 到達確認）は、客観的エビデンスなしの技術採用が誤判断を
生むと述べる。

EBSE の手順——問いの定式化、エビデンス探索、批判的評価、実務文脈への統合——は、
develop 検討で踏んだ手順と同型である。問い（禁止すべきか）、DORA / GitFlow 原著者 /
Microsoft / GitLab / Kubernetes の調査、「存在ではなく統合遅延が問題」という評価、
統合契約付き許可という規則案。

## データで直観を修正する

[DORA](https://dora.dev/capabilities/trunk-based-development/)（取得 2026-07-07）は、
大規模調査によりプロセス実践とデリバリー性能の相関を測定する。develop 全面禁止という
直観は、データの操作的定義——統合頻度——へ修正できた。規則の背後に実証研究を置く
要求が、実際に機能した事例だ。

## フィードバックが規範を動かす

アダプター報告 → ギャップ分析 → 規範改訂。`process-gap-register.md` は、ギャップを
見つけたら文書を書いて登録簿に記録せよと定める。LISS-0002（第1回）、LISS-0005
（第2回）が実績である。

## 調査したから正しい、ではない

ソフトウェア工学のエビデンスは医学ほど強くない。RCT は稀で文脈依存が大きい。
だから「調査結果 + 自プロジェクトの文脈 + Referee 判断」の三点で決める。
research は非規範のまま残し、規範化は承認後に行う——これは EBSE の「実務文脈へ
統合する」ステップの実装として妥当だ。

出典に取得日を付すのにも意味がある。エビデンスは陳腐化する。規則を見直すとき、
当時の根拠と現在の状況を区別できなければ、トレーサビリティは形だけになる。

## 参考文献

1. 内部: LISS-0002、LISS-0005、`docs/collaboration/process-gap-register.md`
2. Kitchenham, B., Dybå, T., Jørgensen, M. "Evidence-based Software Engineering."
   ICSE 2004. https://web-backend.simula.no/sites/default/files/publications/SE.5.Kitchenham.2004.pdf
   （取得 2026-07-07）
3. Dybå, T., Kitchenham, B., Jørgensen, M. "Evidence-Based Software Engineering for Practitioners."
   IEEE Software 2005. https://web-backend.simula.no/sites/default/files/publications/Dyba.2005.1.pdf
   （取得 2026-07-07）
4. DORA. *Trunk-based development*.
   https://dora.dev/capabilities/trunk-based-development/ （取得 2026-07-07）