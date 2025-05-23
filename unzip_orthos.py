import configparser
import os
import zipfile
import shutil

# INIファイル読み込み
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

zip_dir = config['paths']['input_zip_dir']
output_dir = config['paths']['output_extract_dir']
overwrite = config['options'].getboolean('overwrite', fallback=False)

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(zip_dir):
    if filename.endswith('.zip'):
        zip_path = os.path.join(zip_dir, filename)
        print(f"処理中: {filename}")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for member in zip_ref.namelist():
                # ファイル名だけ抽出（サブフォルダが含まれていた場合対応）
                base_name = os.path.basename(member)
                if not base_name:
                    continue  # フォルダはスキップ

                dest_path = os.path.join(output_dir, base_name)

                if os.path.exists(dest_path) and not overwrite:
                    print(f"スキップ: {base_name}（既に存在）")
                    continue

                with zip_ref.open(member) as source, open(dest_path, "wb") as target:
                    shutil.copyfileobj(source, target)
                    print(f"展開 → {base_name}")

print("✅ 全ファイルをまとめて解凍・整理しました！")
