import os
import re

def clean_text_content(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 連続するコンマを一つにする
                content = re.sub(r',+', ',', content)
                
                # テキストの先頭と後端のコンマを削除
                content = content.strip(',')
                
                # テキストファイルを更新
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Processed file: {file_path}")

directory_path = "path"
clean_text_content(directory_path)