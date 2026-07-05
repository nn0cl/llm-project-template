# LLM Project Template 日本語ガイド

[English README](README.md)

これは `README.md` の逐語訳ではありません。日本語話者がこのテンプレートを
導入・運用するときに、判断を迷いやすい点を短く確認するための入口です。
正式な運用契約は `AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md`
と `docs/` 配下の各文書を参照してください。

## これは何か

このリポジトリは、Clean Architecture と AT-TDD を前提に、人間の Referee と
複数の AI coding agent が協調するためのテンプレートです。

アプリケーションの仕様、技術スタック、DB、外部 API、LLM provider、ドメイン
モデルは決めません。それらは導入先リポジトリの仕様・ADR・アーキテクチャ文書
で決めます。

## 大事な考え方

- 仕様なしで実装しない。
- Phase を飛ばさない。
- 人間の Referee が phase transition、ADR、曖昧な判断を承認する。
- AI に渡す context は最小限にする。
- AI output は信頼済みデータとして扱わず、構造・根拠・review status を確認する。
- 導入先の README、仕様、アーキテクチャをテンプレートで上書きしない。

## 作業 path の使い分け

このテンプレートは、毎回 AI に重い reasoning をさせないために 3 つの path を
使い分けます。

### Fast Path

機械的で局所的な作業に使います。

例:

- typo 修正。
- README の短い補足。
- shell script の構文確認。
- ファイルコピーの dry-run。
- formatter、linter、search、test など deterministic tool で確認できる作業。

Fast Path では full `[THOUGHT]` は不要です。compact design note で、scope、
読んだ context、省いた context、実行する deterministic check を示します。

### Feature Path

AT-TDD の Phase 1/2/3 に使います。

- Phase 1: Red。失敗する test だけを書く。
- Phase 2: Green。review 済み test を通す最小実装だけを書く。
- Phase 3: Refactor。挙動を変えずに読みやすさと境界を整える。

Feature Path では target spec、phase rule、関連 architecture document を読み、
full `[THOUGHT]` を出します。

### Architecture Path

ADR、prompt/instruction 変更、privacy-sensitive routing、境界判断、process 変更に
使います。プロジェクト方針を変える場合は Referee approval が必要です。

## 新規リポジトリへ導入する

テンプレート側で実行します。

```bash
scripts/copy-ai-collaboration-files.sh --target /path/to/target-repo
```

placeholder を少し埋める場合:

```bash
scripts/copy-ai-collaboration-files.sh \
  --target /path/to/target-repo \
  --project-name "Example Product" \
  --domain-summary "one-line target project summary" \
  --stack "backend language, frontend framework, package manager"
```

導入後、target repo で初回 LLM session 用 prompt を作ります。

```bash
cd /path/to/target-repo
scripts/init-llm-context.sh .
```

出力された prompt を、そのリポジトリの最初の AI session に貼ります。

## 既存リポジトリへ途中導入する

まず dry-run します。

```bash
scripts/copy-ai-collaboration-files.sh --target /path/to/existing-repo --dry-run
```

問題なければ `--force` なしで実行します。デフォルトでは既存ファイルを
上書きしません。既存の product README や architecture document は導入先が
所有する文書として保持します。

導入先でのオンボーディングは `docs/collaboration/adoption-guide.md` を見ます。

## 導入後に最初に埋めるもの

1. `AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md` の project 名や
   stack placeholder。
2. `docs/architecture/README.md` の project-specific な説明。
3. `docs/specs/` 配下の最初の EARS/Gherkin specification。
4. 必要になった architecture document。必要になるまで作りすぎない。
5. 外部 resource 一覧。DB、settings、secret storage、外部 API、LLM provider など。

## やってはいけないこと

- このテンプレートで導入先の domain model を決める。
- placeholder 例を、そのまま技術選定として扱う。
- Feature Path で review 前に Phase 2 へ進む。
- Fast Path で仕様変更、architecture 変更、agent instruction 変更をする。
- `--force` で既存文書をまとめて上書きする。
- private data、secret、`.env` 全文を AI prompt に入れる。

## 迷ったら

- ただの局所作業なら Fast Path。
- accepted spec に対する実装作業なら Feature Path。
- 方針や境界を変えるなら Architecture Path。
- path が曖昧なら Architecture Path に寄せて、Referee に判断を求めます。
