import os

def remove_spaces_around_commas(directory, ext):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("."+ext):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # コンマ前後の空白を削除
                new_content = ','.join([part.strip() for part in content.split(',')])

                # テキストファイルを更新
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Processed file: {file_path}")