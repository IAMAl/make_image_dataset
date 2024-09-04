import utils.dataset.replace_in_files_and_directories as replace_in_files_and_directories
import utils.dataset.copy_directory as copy_directory
import utils.dataset.add_prefix_to_files as add_prefix_to_files
import utils.dataset.resize_and_copy_images as resize_and_copy_images
import utils.dataset.flip_and_rename_images as flip_and_rename_images
import utils.dataset.copy_files_flat_with_report as copy_files_flat_with_report

######## Parameters: 作業工程
# 0 キャプションファイル生成後にキャプションファイルと画像ファイルを分別する
#source_dir = "../root_dir_caption_generated"
#destination_base = source_dir
#copy_files_by_detected_extensions(source_dir, destination_base)

# 1 ディレクトリ構造とファイルのリスト作成
dir_images_br = "image_path"

# 2 キャプションファイルのコピー
dir_copied_caption = "caption_path"

# 3 ディレクトリ名とキャプションファイル内容の置換
dir_replace_texts = "replace_text_path"

# 4 キャプションファイル名変更前にコピー
dir_replace_texts_copied_1 = "copied_caption_path_lr1"

# 5 キャプションファイル名置換前にコピー
dir_replace_texts_copied_2 = "copied_caption_path_lr2"

# 6 置換とプリフィックス付与

# 7 リサイズ
dir_source_images = dir_images_br
dir_resized_images = "images_resized_path"

# 8 プリフィックス付与前にコピー
dir_replace_images_copied_1 = "image_resized_original_path"

# 9 プリフィックス付与前に左右反転してコピー（dir名置換付き
dir_replace_images_copied_2 = "image_lr_flipped_path"

# 10 ファイルのマージ：学習用データディレクトリの作成
dir_final_place = "image_and_caption_merged_path"



######## Make Directory Structure and File List
#### 1 ディレクトリ構造とファイルのリスト作成
# start_directoryディレクトリ下にサブディレクトリで画像ファイルが配置されているとする
#start_directory = dir_images_br
#output_path = "../dir_images_structure.txt"
#directory_data = list_files_and_directories(start_directory, output_path)

#### 2 サブディレクトリを含むディレクトリ下のファイルをフラットにコピー
#copy_files_flat_with_report(source_directory, destination_directory, report_file):

######## Make Caption Files and LR-Flipped Copies, and prefix
#### 3 １で作ったディレクトリ構造を基に指定したディレクトリのファイルを構造を作成してコピー
#source_dir = dir_images_br
#destination_dir = dir_copied_caption
#structure_file = "../dir_images_structure.txt"
#report_path = "../report_1_copy_files_dir.txt"
#extensions = ['.txt', '.jpg']  # 対象とする拡張子
#copy_files_based_on_structure(source_dir, destination_dir, structure_file, extensions, report_path)

#### 4 ディレクトリ名を置換し、その置換と同じ規則でテキストファイル内も置換する
source_dir = dir_copied_caption
destination_dir = dir_replace_texts
replacements = [('left', 'right'),('right', 'left')]
report_path = "./report_2_file_replace_texts.txt"
list_file = "./replace_dir_text.txt"
replace_in_files_and_directories(source_dir, destination_dir, replacements, report_path, list_file)

#### 5 ディレクトリ丸ごとコピー
source_dir = dir_replace_texts
destination_dir = dir_replace_texts_copied_1
copy_directory(source_dir, destination_dir)

#### 6 ファイル名にプリフィックスを付与
directory_path = dir_replace_texts_copied_1
file_prefix = "1_"
add_prefix_to_files(directory_path, file_prefix)

#### 7 ディレクトリ丸ごとコピー
source_dir = dir_copied_caption
destination_dir = dir_replace_texts_copied_2
copy_directory(source_dir, destination_dir)

#### 8 ファイル名にプリフィックスを付与
directory_path = dir_replace_texts_copied_2
file_prefix = "2_"
add_prefix_to_files(directory_path, file_prefix)



######## Make Rescaled Images and LR-Flipped Copies, add prefix
#### 8 画像をリサイズしてディレクトリ構造維持してコピー
source_dir = dir_source_images
destination_dir = dir_resized_images
image_target_size = 1024  # 新しいサイズ
resize_and_copy_images(source_dir, destination_dir, image_target_size)

#### 9 ディレクトリ丸ごとコピー
source_dir = dir_resized_images
destination_dir = dir_replace_images_copied_1
copy_directory(source_dir, destination_dir)

#### 10 ファイル名にプリフィックスを付与
directory_path = dir_replace_images_copied_1
file_prefix = "2_"
add_prefix_to_files(directory_path, file_prefix)

#### 11 画像を左右反転してディレクトリ構造持してコピー
source_dir = dir_resized_images
destination_base = dir_replace_images_copied_2
#replacements = [('old_text', 'new_text')]
replacements = [('right', 'left'),('left', 'right')]
flip_and_rename_images(source_dir, destination_base, replacements)

#### 12 ファイル名にプリフィックスを付与
directory_path = dir_replace_images_copied_2
file_prefix = "1_"
add_prefix_to_files(directory_path, file_prefix)



######## Make Training Dataset
#### 13 サブディレクトリを含むディレクトリ下のファイルをフラットにコピー
# キャプションファイルを指定したディレクトリにフラットにコピー
source_dir = dir_replace_texts_copied_1
destination_dir = dir_final_place
report_path = "./report_3_copy_files_flat_captions.txt"
copy_files_flat_with_report(source_dir, destination_dir, report_path)

# キャプションファイルを指定したディレクトリにフラットにコピー
source_dir = dir_replace_texts_copied_2
destination_dir = dir_final_place
report_path = "./report_4_copy_files_flat_captions.txt"
copy_files_flat_with_report(source_dir, destination_dir, report_path)

#### 14 サブディレクトリを含むディレクトリ下のファイルをフラットにコピー
# 画像ファイルを指定したディレクトリにフラットにコピー
source_dir = dir_replace_images_copied_1
destination_dir = dir_final_place
report_path = "./report_5_copy_files_flat_images.txt"
copy_files_flat_with_report(source_dir, destination_dir, report_path)

# 画像ファイルを指定したディレクトリにフラットにコピー
source_dir = dir_replace_images_copied_2
destination_dir = dir_final_place
report_path = "./report_6_copy_files_flat_images.txt"
copy_files_flat_with_report(source_dir, destination_dir, report_path)