import os
from PIL import Image

def remove_metadata_from_jpeg_files(directory, new_metadata=None):
    # 指定されたディレクトリ以下のすべてのファイルとディレクトリを取得する
    for root, dirs, files in os.walk(directory):
        for file in files:
            # JPEGファイルの場合のみ処理を行う
            if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
                # JPEGファイルのパスを取得する
                file_path = os.path.join(root, file)
                # メタデータを削除する
                replace_metadata(file_path, new_metadata)

def replace_metadata(image_path, new_metadata=None):
    # 画像を開く
    img = Image.open(image_path)
    
    # 新しいExif情報が指定されている場合は、それを適用する
    if new_metadata:
        # 元のExif情報を削除する
        img.info['exif'] = None
        
        # 新しいExif情報を画像に適用する
        img.save(image_path, exif=new_metadata)
    else:
        # 新しいExif情報が指定されていない場合は、元のExif情報を削除する
        img.info.pop('exif', None)
        
        # 画像を保存する（元のファイルを上書きするので注意）
        img.save(image_path)



# 指定されたディレクトリ以下のすべてのJPEGファイルからメタデータを削除する
remove_metadata_from_jpeg_files(directory_path, new_metadata)
