import os

#### 4 ディレクトリ名を置換し、その置換と同じ規則でテキストファイル内も置換する
def load_replacements(replacement_file):
    # リストファイルから置換ルールを読み込む
    replacements = {}
    with open(replacement_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                replacements[parts[0]] = parts[1]
                print(f"add: {parts[1]} to {parts[0]} replacements")
            elif len(parts) > 2:
                list_text = parts[1]
                for part in parts[2:]:
                    if not part in list_text:
                        list_text = list_text+","+part

                replacements[parts[0]] = list_text
                print(f"add: {list_text} to {parts[0]} replacements")

    return replacements


def remove_duplicate(texts):
    texts = texts.split(',')
    count = 0
    result = []
    for index1, text1 in enumerate(texts):
        find = False
        for index2, text2 in enumerate(texts):
            if text2 == text1 and index1 != index2:
                find = True
                break
        if not find:
            result.append(text1)
            count += 1

    if count > 0:
        return ','.join(result)
    else:
        return ','.join(texts)


def replace_in_files_and_directories(source_directory, destination_directory, replacements, report_file, list_file):
    # 置換ルールを辞書に変換
    #replacement_dict = load_replacements(list_file)

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # 置換が行われなかったファイルを記録するリスト
    no_replacement_files = []

    # 置換ルールの辞書作成
    replacement_dict_ = {r[0]: r[1] for r in replacements}

    # ソースディレクトリを再帰的に走査
    for root, dirs, files in os.walk(source_directory):
        original_dir_name = root.split("/")[-1].split("_")[0]
        #print(f"original_dir_name : {original_dir_name}")
        # ディレクトリ作成
        for dir_name in dirs:
            # ディレクトリ名の置換
            new_dir_name = dir_name
            for old, new in replacement_dict_.items():
                if old in dir_name:
                    new_dir_name = dir_name.replace(old, new)
                    break

            # 新しいディレクトリパスの作成
            new_dir_path = os.path.join(destination_directory, new_dir_name)
            os.makedirs(new_dir_path, exist_ok=True)

        for file_name in (files):
            original_dir_name = root.split('/')[-1]
            new_dir_name = original_dir_name
            for old, new in replacement_dict_.items():
                #print(f"DIR CHANGE {old} ->{new}")
                if old in original_dir_name:
                    new_dir_name = original_dir_name.replace(old, new)
                    break

            #print(f"DIR {original_dir_name} -> {new_dir_name}")
            # ファイルパスの計算
            file_path = os.path.join(root, file_name)
            # ファイルの内容を読み、必要に応じて置換
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 置換
            new_dir_path = os.path.join(destination_directory, new_dir_name)
            new_file_path = os.path.join(new_dir_path, file_name)
            replaced = False
            content = remove_duplicate(content)
            if old in content:
                content = content.replace(old, new)
                #print(f"{file_path} -> {new_file_path} : {old} -> {new} : {content}")
                replaced = True

            # 置換された内容で新しいファイルを作成
            os.makedirs(new_dir_path, exist_ok=True)
            with open(new_file_path, 'w', encoding='utf-8') as file:
                file.write(content)

            # 置換が行われなかった場合、リストに追加
            if not replaced:
                no_replacement_files.append(file_path)

    # 置換が行われなかったファイルのレポートを作成
    with open(report_file, 'w', encoding='utf-8') as file:
        if no_replacement_files:
            file.write("置換対象の文字列が見つからなかったファイル:\n")
            for no_file in no_replacement_files:
                file.write(f"{no_file}\n")
        else:
            file.write("すべてのファイルで置換が成功しました。\n")