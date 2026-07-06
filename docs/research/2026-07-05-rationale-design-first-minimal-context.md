# 設計先行とコンテキスト

2026-07-05。非規範。関連: ADR 0001。

---

「賢いプロンプト」を競う文化は、本質を見落としている。問題は言い回しではなく、
何を渡すか、何を渡さないか、どの道具に任せるかである。自由に動く coding agent を
誘導する手段の一つが payload 設計であり、include/omit はサンドボックスへ何を見せ、
何を推測するなと伝える統合層の一部だ（
[エージェントはサンドボックスである](2026-07-07-rationale-saas-agent-as-sandbox.md)）。
私は、コンテキスト選択を個人技からレビュー可能な設計成果物へ移す。すべての依頼は
設計ステップから始まり、テストと実装はそのあとに来る。

設計インテークでは、対象挙動、VO/DTO 候補、ports/adapters、含める文脈と外す文脈、
モデル/ツールの振り分け、推測禁止境界を先に決める（ADR 0001）。設計は儀式ではない。
意思決定の記録である。

## リポジトリ全体を送るな

より小さいペイロードで足りるなら、リポジトリ全体を送ってはならない。理由は
コストだけではない。無関係な文脈は性能を落とす。
Shi et al.（[arXiv:2302.00093](https://arxiv.org/abs/2302.00093)、取得 2026-07-07、
ICML 2023 採録・GSM-IC ベンチマークを確認）は、無関係情報を問題文に加えるだけで
LLM の推論精度が大きく低下することを示した。payload は選んで送る。これは
推奨ではなく、実証に基づく制約に近い。

コンテキストは希少資源として扱う。
[Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
（取得 2026-07-07、ページ存在確認）は "informative, yet tight" な構成を勧める。
include/omit の台帳を設計の必須項目にするのは、その実装形態である。

## 能力の階段

機械的な作業は決定的ツール、小さいモデル、補完へ。境界判断、曖昧なドメイン、
プライバシーが絡む判断は強い推論へ。最下段の原則は単純だ。決定的ツールで済む
ことに LLM を使うな。

モデル振り分けの経済性は Chen, Zaharia, Zou の FrugalGPT
（[arXiv:2305.05176](https://arxiv.org/abs/2305.05176)、取得 2026-07-07、
抄録に「最大 98% のコスト削減」を確認）が裏づける。安価なモデルで足りるなら
強いモデルを呼ばない。`docs/collaboration/llm-cost-reduction.md` は同じ構造を
運用へ落とす。

## 未決は空白ではない

`Current Non-Decisions` に載る事項は、エージェントが推測してよい領域ではない。
ADR の話題である。Must not guess は設計ノートの必須欄だ。入力の曖昧性抑制には
EARS（[Mavin et al., IEEE RE'09](https://ieeexplore.ieee.org/document/5328509)、
取得 2026-07-07）も使える。

## 不確実性を閉じ込める

決定的ツール優先は、LLM の不確実性を意図的に狭い場所へ閉じ込める設計である。
不確実性を扱う場面を減らすこと自体が規律の一部だ。
[エビデンスと規則](2026-07-06-rationale-evidence-based-process-design.md) と
対をなす考え方である。

## 参考文献

1. 内部: `docs/architecture/adr/0001-design-first-ai-request-routing.md`、
   `CLAUDE.md`、`docs/collaboration/privacy-context-budget-policy.md`、
   `docs/collaboration/llm-cost-reduction.md`
2. Shi, F. et al. "Large Language Models Can Be Easily Distracted by Irrelevant Context."
   arXiv:2302.00093. https://arxiv.org/abs/2302.00093 （取得 2026-07-07）
3. Anthropic. *Effective context engineering for AI agents*.
   https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
   （取得 2026-07-07）
4. Chen, L., Zaharia, M., Zou, J. "FrugalGPT." arXiv:2305.05176.
   https://arxiv.org/abs/2305.05176 （取得 2026-07-07）
5. Mavin, A. et al. EARS. IEEE RE'09.
   https://ieeexplore.ieee.org/document/5328509 （取得 2026-07-07）