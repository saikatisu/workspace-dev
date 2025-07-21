import pandas as pd
import os
import argparse

INPUT_DIR = "scripts/input"
OUTPUT_DIR = "scripts/output"

def excel_to_markdown(excel_path, sheet_name=None):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    df.fillna("", inplace=True)
    return df.to_markdown(index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ExcelファイルをMarkdown形式に変換して出力します")
    parser.add_argument("filename", help="scripts/input 内のExcelファイル名（例：タスク一覧.xlsx）")
    parser.add_argument("--sheet", help="対象のシート名（省略時は先頭シート）", default=None)

    args = parser.parse_args()
    input_path = os.path.join(INPUT_DIR, args.filename)

    if not os.path.exists(input_path):
        print(f"ファイルが存在しません: {input_path}")
        exit(1)

    md_output = excel_to_markdown(input_path, args.sheet)

    # 拡張子を .md に変換して出力パスを生成
    base_name = os.path.splitext(args.filename)[0]
    output_path = os.path.join(OUTPUT_DIR, f"{base_name}.md")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_output)

    print(f"✅ Markdown形式で出力しました → {output_path}")
