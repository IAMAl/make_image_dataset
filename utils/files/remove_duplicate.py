import os
from collections import defaultdict

def find_files(directory):
    file_map = defaultdict(list)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_name_without_ext = os.path.splitext(file)[0]
            file_map[file_name_without_ext].append(os.path.join(root, file))
    
    return file_map

def remove_duplicates(file_map):
    files_to_keep = {}
    files_to_delete = defaultdict(list)
    
    for file_name, file_list in file_map.items():
        if len(file_list) > 1:
            # 最初のファイルを残し、それ以外を削除対象に追加
            files_to_keep[file_name] = file_list[0]
            files_to_delete[file_name] = file_list[1:]
        else:
            files_to_keep[file_name] = file_list[0]
    
    return files_to_keep, files_to_delete

def synchronize_directories(text_directory, image_directory):
    # テキストディレクトリ内のファイルを検索
    text_files_map = find_files(text_directory)
    # 画像ディレクトリ内のファイルを検索
    image_files_map = find_files(image_directory)
    
    # テキストファイルで重複を削除
    text_files_to_keep, text_files_to_delete = remove_duplicates(text_files_map)
    
    # 削除するテキストファイルに対応する画像ファイルも削除
    for file_name, file_paths in text_files_to_delete.items():
        for file_path in file_paths:
            os.remove(file_path)
            print(f"Deleted text file: {file_path}")
            # 対応する画像ファイルの削除
            image_file_path = os.path.join(image_directory, os.path.relpath(file_path, text_directory))
            image_file_path = os.path.splitext(image_file_path)[0] + ".jpg"  # 画像の拡張子を適宜変更
            if os.path.exists(image_file_path):
                os.remove(image_file_path)
                print(f"Deleted corresponding image file: {image_file_path}")

text_directory_path = "caption_path"
image_directory_path = "image_path"

synchronize_directories(text_directory_path, image_directory_path)
