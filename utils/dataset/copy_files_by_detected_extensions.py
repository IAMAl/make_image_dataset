import os
import shutil

def copy_files_by_detected_extensions(source_directory, destination_base):
    # すべてのファイル拡張子を検出して保存
    extensions = set()
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            ext = os.path.splitext(file)[1][1:]  # 拡張子を抽出
            if ext:  # 拡張子が空でない場合のみ追加
                extensions.add(ext)

    # 検出された拡張子ごとにディレクトリを作成し、ファイルをコピー
    for ext in extensions:
        ext_directory = f"{destination_base}_{ext}"
        if not os.path.exists(ext_directory):
            os.makedirs(ext_directory)

        for root, dirs, files in os.walk(source_directory):
            for file in files:
                if file.endswith(f".{ext}"):
                    source_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(root, source_directory)
                    destination_path = os.path.join(ext_directory, relative_path)
                    if not os.path.exists(destination_path):
                        os.makedirs(destination_path)
                    destination_file_path = os.path.join(destination_path, file)
                    # ファイルをコピー
                    shutil.copy2(source_file_path, destination_file_path)
                    print(f"ファイルがコピーされました: {destination_file_path}")