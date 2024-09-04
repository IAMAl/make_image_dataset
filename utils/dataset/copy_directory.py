import os
import shutil

#### 5 ディレクトリ丸ごとコピー
def copy_directory(source_directory, destination_directory):
    # ソースディレクトリが存在するか確認
    if not os.path.exists(source_directory):
        print(f"エラー: ソースディレクトリ '{source_directory}' が存在しません。")
        return

    # 目的ディレクトリが既に存在する場合、エラーを出力
    if os.path.exists(destination_directory):
        print(f"エラー: 目的ディレクトリ '{destination_directory}' は既に存在します。")
        return

    # ディレクトリをコピー
    try:
        shutil.copytree(source_directory, destination_directory)
        print(f"{source_directory} から {destination_directory} へのコピーが完了しました。")
    except Exception as e:
        print(f"ディレクトリのコピー中にエラーが発生しました: {e}")