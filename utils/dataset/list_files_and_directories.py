#### 1 ディレクトリ構造とファイルのリスト作成
def list_files_and_directories(start_path, output_file):
    # ディレクトリとファイルの構造を格納する辞書
    directory_structure = {}

    # ファイルに書き込むためのファイルオープン
    with open(output_file, 'w') as f:
        # os.walkを使用してディレクトリを探索
        for root, dirs, files in os.walk(start_path):
            # 現在のディレクトリパスを出力
            f.write(f"ディレクトリ: {root}\n")
            print(f"ディレクトリ: {root}")

            # 各ファイルについての情報をファイルに書き込み
            file_list = []
            for file in files:
                file_path = os.path.join(root, file)
                f.write(f"  ファイル: {file_path}\n")
                print(f"  ファイル: {file_path}")
                file_list.append(file_path)

            # 現在のディレクトリを辞書に追加
            directory_structure[root] = file_list