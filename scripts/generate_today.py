import os
from datetime import datetime
from pathlib import Path

# 日付を取得
today_str = datetime.today().strftime("%Y%m%d")

# ファイルパス
dashboard_path = Path(__file__).parent.parent / "dashboard/タスクダッシュボード.md"
today_dir = Path(__file__).parent.parent / "today"
today_file = today_dir / f"{today_str}.md"

# 今日やることの抽出と生成
if dashboard_path.exists():
    lines = dashboard_path.read_text(encoding="utf-8").splitlines()
    extracting = False
    today_lines = ["# 今日のタスクリスト\n"]
    for line in lines:
        if line.strip() == "## 🕒 今日やること":
            extracting = True
            continue
        if line.startswith("## ") and extracting:
            break
        if extracting:
            today_lines.append(line)
    today_dir.mkdir(parents=True, exist_ok=True)
    today_file.write_text("\n".join(today_lines), encoding="utf-8")
    print(f"✅ {today_file.name} を生成しました")
else:
    print("⚠️ タスクダッシュボードが見つかりません")
