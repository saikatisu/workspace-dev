# 📁 仕事用ワークスペース構成ガイド

このリポジトリは、ローカルMarkdownベースでナレッジ管理・タスク進行・報告書作成を一元管理するためのワークスペースです。  
以下は各ディレクトリの構成と役割です。

---

## 🛠 導入手順（初回セットアップ）

1. このリポジトリをローカルにクローン：

   ```bash
   git clone https://github.com/saikatisu/workspace-dev.git
   cd workspace-dev
   ```

2. Python 3 が動作する環境があればすぐに利用可能（追加ライブラリ不要）

3. 推奨エディタ：VSCode（拡張機能：Markdown All in One、Python など）

> フォルダ構成・テンプレート・スクリプトはすべてリポジトリに含まれています。

---

## 🔰 ワークの始め方

1. **タスクを追加する**

   - `dashboard/タスクダッシュボード.md` の `## 👤 個人スケジュール` 表に新しいタスク行を追加
   - 「タスク行テンプレート」を下部からコピーして編集

2. **タスクファイルを生成する**

   - ターミナルで以下を実行：

     ```bash
     python scripts/generate_tasks_from_dashboard.py
     ```

   - `task/` 以下にタスク属性ごとの `.md` ファイルが自動で生成される
   - `ダッシュボード.md` の「備考」欄にリンクが自動挿入される

3. **タスクファイルに詳細を記録する**

   - 各タスクファイル（例：`task/specs/製品A_CSV出力仕様.md`）に進捗やメモ、調査内容を随時追記
   - 完了したら `ダッシュボード.md` 側で終了日・状態を更新

---

## 📂 ディレクトリ構成

```
workspace-dev/
├─ dashboard/
│  └─ タスクダッシュボード.md   ← 全体のタスク・WBS・スケジュールを集約
├─ task/
│  ├─ bugs/         ← バグ調査・不具合対応
│  ├─ specs/        ← 仕様確認・設計作業
│  ├─ research/     ← 技術検証・調査・PoC
│  ├─ ops/          ← 運用手順・定型作業
│  ├─ documents/    ← 資料作成・まとめ
│  ├─ meetings/     ← 会議準備・議事録
│  └─ etc/          ← その他分類が難しいタスク
├─ reports/
│  └─ 月次報告_2025_07.md         ← 成果物レポート（Markdown/PDF）
├─ knowledge/
│  ├─ テクサポ問い合わせ管理.md   ← ナレッジベース（FAQ・対応履歴など）
│  └─ ChatGpt学習用.md            ← AI活用ログ・学習メモ
├─ scripts/
│  ├─ generate_tasks_from_dashboard.py  ← ダッシュボードからタスクを自動生成
│  └─ Excel→Markdown変換.py             ← 表の整形・貼り付け支援
└─ README.md                     ← この構成ガイド
```

---

## ✅ 主な使い方

- `dashboard/タスクダッシュボード.md` に全体のスケジュールとタスクを集約管理
- `task/` に各タスクの記録・調査・進行状況を属性ごとに整理
- `reports/` に成果物（週報・月報など）をMarkdown形式で保管
- `knowledge/` に業務知識や技術サポート記録を蓄積
- `scripts/` にMarkdownワークフロー支援のPythonツールを配置

---

## 🚀 自動化スクリプト例（scripts/）

- `generate_tasks_from_dashboard.py`  
  → ダッシュボードの「個人スケジュール」からタスクを属性ごとに自動生成＆リンク挿入

- `Excel→Markdown変換.py`  
  → Excelの表をコピーしてMarkdown形式に整形

---

## 📌 備考

- 本ワークスペースは**ローカル環境（クラウド非依存）前提**
- Markdown × Python × VSCode による軽量・自律的な情報管理基盤
- Gitでの履歴管理・成果物差分比較にも適しています

---

## 🆕 Excelからダッシュボード生成

プロジェクトスケジュールがExcelファイルで共有される場合、個人スケジュールを `タスクダッシュボード.md` に自動変換することができます。

### 📄 対応フォーマット（Excel）

- ファイル： `dashboard/タスクスケジュールテンプレート.xlsx`
- シート名： `個人スケジュール`
- 列構成： `No / タスク / 開始日 / 終了日 / タスク属性 / 担当者 / 備考`

### 🛠 使用スクリプト

```bash
python scripts/excel_to_dashboard.py
```

- `dashboard/タスクダッシュボード.md` に Markdown形式の個人スケジュール表が自動出力されます。
- テンプレートファイルは `scripts/` フォルダ内の `excel_to_dashboard.py` です。


---

## 📤 Excel表をMarkdownに変換

Excelで作成された表をそのままMarkdown形式のテーブルとして出力できます。  
議事録、仕様書、タスクリストのMarkdown化に便利です。

### 🛠 使用スクリプト

```bash
python scripts/excel_to_markdown_table.py ファイル名.xlsx --sheet シート名
```

- 入力ファイルは `scripts/input/` に配置してください。
- 出力ファイルは `scripts/output/` に Markdown形式で生成されます。
- `--sheet` は省略可能（先頭のシートを使用）

### 📁 ディレクトリ構成（一部）

```
scripts/
├─ input/                      ← Excelファイルを置く場所
├─ output/                     ← Markdownファイルが出力される
└─ excel_to_markdown_table.py ← 変換スクリプト本体
```
