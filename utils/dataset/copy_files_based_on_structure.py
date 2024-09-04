import os
import shutil

#### 3 １で作ったディレクトリ構造を基に指定したディレクトリのファイルを構造を作成してコピー
def copy_files_based_on_structure(source_directory, destination_directory, structure_file, extensions, report_file):
    # レポートデータを格納するための辞書
    report_data = {
        'files_not_in_list': [],
        'files_missing': []
    }

    # ファイルリストを読み込む
    with open(structure_file, 'r') as file:
        listed_files = file.read().splitlines()

    # リストファイルに基づいてディレクトリを作成
    for line in listed_files:
        if line.startswith('ディレクトリ: '):
            rel_dir = os.path.relpath(line[len('ディレクトリ: '):], start=source_directory)
            os.makedirs(os.path.join(destination_directory, rel_dir), exist_ok=True)
        elif line.startswith('  ファイル: '):
            rel_file = os.path.relpath(line[len('  ファイル: '):], start=source_directory)
            if not rel_file.endswith(tuple(extensions)):
                continue  # 拡張子が指定されたものと異なる場合はスキップ
            source_path = os.path.join(source_directory, rel_file)
            destination_path = os.path.join(destination_directory, rel_file)
            if os.path.exists(source_path):
                shutil.copy2(source_path, destination_path)
            else:
                report_data['files_missing'].append(source_path)

    # ディレクトリ内の全ファイルを検査し、リストにないファイルを報告
    for root, _, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path not in listed_files and file.endswith(tuple(extensions)):
                report_data['files_not_in_list'].append(file_path)

    # レポートをファイルに書き込む
    with open(report_file, 'w') as f:
        if report_data['files_not_in_list']:
            f.write("リストにないファイル:\n")
            for file in report_data['files_not_in_list']:
                f.write(f"{file}\n")
        if report_data['files_missing']:
            f.write("リストに記載されているが存在しないファイル:\n")
            for file in report_data['files_missing']:
                f.write(f"{file}\n")