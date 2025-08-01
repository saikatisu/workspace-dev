import os
import re

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
task_base_path = "task"

# ダッシュボード全体を読み込む
with open(dashboard_path, encoding="utf-8") as f:
    content = f.read()

# 個人スケジュール表を正規表現で抽出
match = re.search(r"(## 👤 個人スケジュール\n\n((\|.+\n)+))", content)
if not match:
    print("個人スケジュール表が見つかりません。")
    exit()

full_table = match.group(1)
table_lines = full_table.strip().split("\n")
header = table_lines[0]
columns = table_lines[2]
task_lines = table_lines[3:]  # データ行のみ

updated_task_lines = []

for row in task_lines:
    cells = [cell.strip() for cell in row.split("|")[1:-1]]
    if len(cells) < 7:
        updated_task_lines.append(row)
        continue

    task_title = cells[1]
    start_date = cells[2]
    end_date = cells[3]
    attribute = cells[4]
    assignee = cells[5]
    remark = cells[6]

    attribute_folder = attribute_map.get(attribute, "etc")
    file_name = f"{task_title.replace(' ', '_').replace('/', '_')}.md"
    file_path = os.path.join(task_base_path, attribute_folder, file_name)

    # ファイル作成（上書きしない）
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {task_title}\n\n")
            f.write(f"- 属性: {attribute}\n")
            f.write(f"- 開始日: {start_date}\n")
            f.write(f"- 終了日: {end_date}\n")
            f.write(f"- 担当者: {assignee}\n")
            f.write(f"- 備考: \n")
        print(f"作成：{file_path}")
    else:
        print(f"既存：{file_path}")

    # 備考欄に [リンク] が含まれていれば置換
    if remark == "[リンク]":
        relative_path = f"../task/{attribute_folder}/{file_name}"
        remark = f"[リンク]({relative_path})"

    # 更新された行を組み立て直す
    updated_line = f"| {cells[0]} | {task_title} | {start_date} | {end_date} | {attribute} | {assignee} | {remark} |"
    updated_task_lines.append(updated_line)

# スケジュール表全体を書き換えた内容に差し替え
new_table = "\n".join([header, "", columns] + updated_task_lines)
content_updated = content.replace(full_table, new_table)

# 書き戻す
with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content_updated)

print("📝 ダッシュボードのリンクを更新しました。")