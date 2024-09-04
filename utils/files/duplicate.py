import os
from collections import defaultdict

def find_duplicate_files(directory):
    file_dict = defaultdict(list)

    # 再帰的にファイルを検索
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_dict[file].append(file_path)

    # 同じファイル名のファイルをリスト化
    duplicate_files = {file: paths for file, paths in file_dict.items() if len(paths) > 1}

    return duplicate_files

def write_duplicates_to_file(duplicates, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("ファイル名,拡張子,ディレクトリ\n")
        for file, paths in duplicates.items():
            for path in paths:
                directory, file_name = os.path.split(path)
                name, ext = os.path.splitext(file_name)
                f.write(f"{name},{ext},{directory}\n")

def main():
    # 特定のディレクトリR
    directory_r = "path"

    # 重複ファイルを見つける
    duplicates = find_duplicate_files(directory_r)

    # 結果をファイルに書き込む
    output_file = "./duplicate_files_list.csv"
    write_duplicates_to_file(duplicates, output_file)
    print(f"重複ファイルのリストが{output_file}に出力されました。")

if __name__ == "__main__":
    main()
