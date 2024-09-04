from PIL import Image
import os

#### 8 画像を左右反転してディレクトリ構造維持してコピー
def flip_and_rename_images(source_directory, destination_base, replacements, extensions=('.jpg', '.jpeg', '.png')):
    # 置換ルールを辞書に変換
    replace_dict = dict(replacements)

    # ソースディレクトリを再帰的に走査
    for root, dirs, files in os.walk(source_directory, topdown=False):
        for file in files:
            if file.lower().endswith(extensions):
                # ファイル名の一時的置換
                temp_file_name = file.replace('right', 'right_temp')

                # 次に'left'を'right'に置換
                new_file_name = temp_file_name.replace('left', 'right')

                # 最後に'temp_right'を'left'に置換
                new_file_name = new_file_name.replace('right_temp', 'left')

                # 元の画像ファイルパス
                source_file_path = os.path.join(root, file)
                # 画像を開く
                with Image.open(source_file_path) as img:
                    # 画像を左右反転
                    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

                    # ディレクトリの一時的置換
                    relative_path = os.path.relpath(root, source_directory)
                    temp_relative_path = relative_path.replace('right', 'right_temp')
                    new_relative_path = temp_relative_path.replace('left', 'right').replace('right_temp', 'left')

                    destination_path = os.path.join(destination_base, new_relative_path)
                    if not os.path.exists(destination_path):
                        os.makedirs(destination_path)

                    # 新しいファイルパス
                    destination_file_path = os.path.join(destination_path, new_file_name)
                    # 画像を保存
                    flipped_img.save(destination_file_path)
                    print(f"画像が左右反転され、保存されました: {destination_file_path}")