import utils.images.remove_metadata_from_jpeg_files as rm_metas

import argparse

open('utils/__init__.py', 'a').close()
open('utils/images/__init__.py', 'a').close()

parser = argparse.ArgumentParser(description="args")

parser.add_argument('--img_dir',    help='target caption file path',    required=True)

args = parser.parse_args()

img_dir = args.img_dir

# 置き換えたいメタデータ
new_metadata = {
    # 例: "Make" (カメラのメーカー)
    271: "New Make",
    # 例: "Model" (カメラのモデル)
    272: "New Model",
    # 他にも必要なExifタグを追加できます
}

directory_path = img_dir
rm_metas.remove_metadata_from_jpeg_files(directory_path, new_metadata)