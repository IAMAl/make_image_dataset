import os

#### 6 ファイル名にプリフィックスを付与
def add_prefix_to_files(directory, prefix):
    # 指定されたディレクトリのすべてのサブディレクトリを含めて走査
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 元のファイルパス
            old_file_path = os.path.join(root, file)
            # 新しいファイル名（プリフィックスを追加）
            new_file_name = prefix + file
            # 新しいファイルパス
            new_file_path = os.path.join(root, new_file_name)

            # ファイル名を変更
            os.rename(old_file_path, new_file_path)
            print(f"ファイル名が変更されました: {old_file_path} -> {new_file_path}")