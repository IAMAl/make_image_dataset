import os

#### 7 画像をリサイズしてディレクトリ構造維持してコピー
def resize_and_copy_images(source_directory, destination_directory, target_size, extensions=('.jpg', '.jpeg', '.png')):
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # ソースディレクトリを再帰的に走査
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith(extensions):
                # 元の画像ファイルパス
                source_file_path = os.path.join(root, file)
                # 画像を開く
                with Image.open(source_file_path) as img:
                    # 元の画像のアスペクト比を維持してリサイズ
                    img.thumbnail((target_size, target_size), Image.ANTIALIAS)

                    # 目的のディレクトリ構造を維持して保存するディレクトリパスを構築
                    relative_path = os.path.relpath(root, source_directory)
                    destination_path = os.path.join(destination_directory, relative_path)
                    if not os.path.exists(destination_path):
                        os.makedirs(destination_path)

                    # 新しいファイルパス
                    destination_file_path = os.path.join(destination_path, file)
                    # 画像を保存
                    img.save(destination_file_path)
                    print(f"画像がリサイズされ保存されました: {destination_file_path}")