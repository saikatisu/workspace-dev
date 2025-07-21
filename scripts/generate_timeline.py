import os
import re
from datetime import datetime, timedelta

# 属性とフォルダ対応
attribute_map = {
    "バグ調査": "bugs",
    "仕様確認": "specs",
    "技術検証": "research",
    "運用作業": "ops",
    "資料作成": "documents",
    "会議": "meetings",
    "その他": "etc"
}

dashboard_path = "dashboard/タスクダッシュボード.md"

# ダッシュボードを読み込む
with open(dashboard_path, encoding="utf-8") as f:
    content = f.read()

# 個人スケジュール表の取得
match = re.search(r"(## 👤 個人スケジュール\n\n((\|.+\n)+))", content)
if not match:
    raise ValueError("個人スケジュール表が見つかりません。")

full_table = match.group(1)
table_lines = full_table.strip().split("\n")
columns = table_lines[2]
task_lines = table_lines[3:]

tasks = []

# 日付抽出とタスク情報収集
for row in task_lines:
    cells = [cell.strip() for cell in row.split("|")[1:-1]]
    if len(cells) < 7:
        continue

    task_title = cells[1]
    start_str = cells[2]
    end_str = cells[3]

    # 無効な日付行をスキップ
    if not re.match(r"\d{4}/\d{2}/\d{2}", start_str) or not re.match(r"\d{4}/\d{2}/\d{2}", end_str):
        print(f"⚠ 無効な日付スキップ: {task_title}")
        continue

    start_date = datetime.strptime(start_str, "%Y/%m/%d")
    end_date = datetime.strptime(end_str, "%Y/%m/%d")

    tasks.append((task_title, start_date, end_date))

# 日付範囲の決定
if not tasks:
    raise ValueError("有効なタスクが見つかりません。")

min_date = min(t[1] for t in tasks)
max_date = max(t[2] for t in tasks)
date_range = [(min_date + timedelta(days=i)).strftime("%m/%d") for i in range((max_date - min_date).days + 1)]

# タイムラインテーブル生成
timeline_lines = []
header_line = "| タスク | " + " | ".join(date_range) + " |"
separator_line = "|--------|" + "|".join(["------"] * len(date_range)) + "|"
timeline_lines.append(header_line)
timeline_lines.append(separator_line)

for task_title, start, end in tasks:
    row = [task_title]
    for day in (min_date + timedelta(days=i) for i in range((max_date - min_date).days + 1)):
        row.append("→" if start <= day <= end else " ")
    timeline_lines.append("| " + " | ".join(row) + " |")

# タイムライン全体ブロックを生成
timeline_block = "\n".join([
    "## 🗓 スケジュールタイムライン（自動生成）",
    "<!-- TIMELINE_START -->",
    *timeline_lines,
    "<!-- TIMELINE_END -->"
])

# 既存のタイムラインを削除して差し替え
if "<!-- TIMELINE_START -->" in content and "<!-- TIMELINE_END -->" in content:
    content = re.sub(r"<!-- TIMELINE_START -->(.|\n)+?<!-- TIMELINE_END -->", timeline_block, content)
else:
    content = content.replace(full_table, full_table + "\n\n" + timeline_block)

# 上書き保存
with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ タイムラインを挿入・更新しました。")
