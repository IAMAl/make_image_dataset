import os

def append_text_to_files(directory, text_file_path, append=True):
    # ファイルBの内容を読み込む
    with open(text_file_path, 'r', encoding='utf-8') as file_b:
        appended_text = ','.join(line.strip() for line in file_b)
        print(appended_text)

    # ディレクトリ内のテキストファイルに追加する
    for filename in os.listdir(directory):
        print(filename)
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.endswith('.caption'):
            if append:
                # ファイルを読み込んで既存の内容を取得
                with open(file_path, 'r', encoding='utf-8') as file:
                    existing_text = file.read()
                # 既存の内容の先頭に追加する
                with open(file_path, 'w', encoding='utf-8') as file_to_write:
                    file_to_write.write(appended_text + ',' + existing_text)
                    print(file_to_write)
            else:
                with open(file_path, 'r', encoding='utf-8') as file:
                    existing_text = file.read()
                # ファイルの末尾に追加する
                with open(file_path, 'a', encoding='utf-8') as file_to_append:
                    file_to_append.write(existing_text + ',' + appended_text)

# ディレクトリとファイルBのパスを指定する
directory_path = 'path'
text_file_b_path = 'add_list.txt'
append=True

# テキストをファイルに追加する
append_text_to_files(directory_path, text_file_b_path, append)
