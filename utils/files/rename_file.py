import os

def rename_files_in_directory(directory_path, append, old_string, new_string):
    try:
        # 指定したディレクトリ内のすべてのファイルとサブディレクトリを取得
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                if append:
                    new_file_name = new_string+file_name
                    old_path = os.path.join(root, file_name)
                    new_path = os.path.join(root, new_file_name)
                    os.rename(old_path, new_path)
                    print(f"ファイル名を変更しました: {old_path} → {new_path}")      
                elif old_string in file_name:
                    # ファイル名に指定した文字列が含まれている場合に変更
                    new_file_name = file_name.replace(old_string, new_string)
                    old_path = os.path.join(root, file_name)
                    new_path = os.path.join(root, new_file_name)
                    os.rename(old_path, new_path)
                    print(f"ファイル名を変更しました: {old_path} → {new_path}")

        print("すべてのファイル名を変更しました。")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

# ディレクトリのパス、置換前文字列、置換後文字列を指定
directory_path = 'path'
old_string = '1_'
new_string = ''
append = False

rename_files_in_directory(directory_path, append, old_string, new_string)
