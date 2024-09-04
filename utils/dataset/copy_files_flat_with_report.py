import os
import shutil

#### 2 サブディレクトリを含むディレクトリ下のファイルをフラットにコピー
def copy_files_flat_with_report(source_directory, destination_directory, report_file):

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    # すでにコピーされたファイル名を記録するセット
    copied_files = set()
    # スキップされたファイルのリスト
    skipped_files = []

    # ソースディレクトリからファイルを探索
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_file_path = os.path.join(root, file)

            # ファイルがすでにコピーされているか確認
            if file in copied_files:
                # スキップされたファイルの記録
                skipped_files.append(file)
                continue  # 次のファイルへ

            # デスティネーションファイルのパスを生成
            destination_file_path = os.path.join(destination_directory, file)
            # ファイルをコピー
            shutil.copy2(source_file_path, destination_file_path)
            # コピーされたファイルを記録
            copied_files.add(file)
            print(f"コピーされたファイル: {destination_file_path}")

    # レポートをファイルに書き込み
    with open(report_file, 'w') as f:
        if skipped_files:
            f.write("スキップされたファイル:\n")
            for skipped_file in skipped_files:
                f.write(f"{skipped_file}\n")
        else:
            f.write("スキップされたファイルはありません。\n")