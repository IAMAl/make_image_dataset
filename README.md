# Dataset Utilities

データセット処理のための総合的なユーティリティツール群です。

## 目次

- [インストール](#インストール)
- [使用方法](#使用方法)
  - [データセット関連コマンド](#データセット関連コマンド)
  - [ファイル関連コマンド](#ファイル関連コマンド)
  - [画像関連コマンド](#画像関連コマンド)
  - [テキスト関連コマンド](#テキスト関連コマンド)

## インストール

必要なPythonパッケージをインストールします：

```bash
pip install pillow tqdm
```

## 使用方法

### データセット関連コマンド

#### 1. ファイル内容の置換 (dataset_replace)
```bash
python make_image_dataset.py dataset_replace \
  --src_dir SOURCE_DIR \
  --dest_dir DEST_DIR \
  --replacements "old,new" "old2,new2" \
  --report REPORT_PATH \
  --list_file LIST_FILE
```
- `src_dir`: 元のディレクトリ
- `dest_dir`: 出力先ディレクトリ
- `replacements`: 置換ペアのリスト
- `report`: レポートファイルのパス
- `list_file`: 置換ルールリストファイル

#### 2. ディレクトリのコピー (dataset_copy)
```bash
python make_image_dataset.py dataset_copy \
  --src_dir SOURCE_DIR \
  --dest_dir DEST_DIR
```
- `src_dir`: コピー元ディレクトリ
- `dest_dir`: コピー先ディレクトリ

#### 3. プレフィックス追加 (dataset_prefix)
```bash
python make_image_dataset.py dataset_prefix \
  --directory DIR \
  --prefix PREFIX
```
- `directory`: 対象ディレクトリ
- `prefix`: 追加するプレフィックス

### ファイル関連コマンド

#### 1. ファイル検索 (file_find)
```bash
python make_image_dataset.py file_find \
  --directory DIR \
  --tokens_file TOKENS \
  --ext EXTENSION
```
- `directory`: 検索対象ディレクトリ
- `tokens_file`: 検索キーワードファイル
- `ext`: 対象ファイルの拡張子

#### 2. 重複ファイルの削除 (file_rm_dup)
```bash
python make_image_dataset.py file_rm_dup \
  --text_dir TEXT_DIR \
  --image_dir IMAGE_DIR
```
- `text_dir`: テキストファイルディレクトリ
- `image_dir`: 画像ファイルディレクトリ

### 画像関連コマンド

#### 1. 画像のリサイズ (image_resize)
```bash
python make_image_dataset.py image_resize \
  --src_dir SOURCE_DIR \
  --dest_dir DEST_DIR \
  --size SIZE
```
- `src_dir`: 元画像ディレクトリ
- `dest_dir`: 出力先ディレクトリ
- `size`: 目標サイズ（ピクセル）

#### 2. 画像の反転 (image_flip)
```bash
python make_image_dataset.py image_flip \
  --src_dir SOURCE_DIR \
  --dest_dir DEST_DIR \
  --replacements "left,right" "right,left"
```
- `src_dir`: 元画像ディレクトリ
- `dest_dir`: 出力先ディレクトリ
- `replacements`: ファイル名の置換ルール

### テキスト関連コマンド

#### 1. テキスト追加 (text_add)
```bash
python make_image_dataset.py text_add \
  --directory DIR \
  --text_file TEXT_FILE \
  --ext EXTENSION \
  --append BOOL
```
- `directory`: 対象ディレクトリ
- `text_file`: 追加するテキストファイル
- `ext`: 対象ファイルの拡張子
- `append`: 先頭に追加する場合はTrue

#### 2. スペース削除 (text_rm_space)
```bash
python make_image_dataset.py text_rm_space \
  --directory DIR \
  --ext EXTENSION
```
- `directory`: 対象ディレクトリ
- `ext`: 対象ファイルの拡張子

#### 3. 単語の削除 (text_rm_word)
```bash
python make_image_dataset.py text_rm_word \
  --src_dir SOURCE_DIR \
  --dest_dir DEST_DIR \
  --words_file WORDS_FILE \
  --ext EXTENSION
```
- `src_dir`: 元ディレクトリ
- `dest_dir`: 出力先ディレクトリ
- `words_file`: 削除する単語リストファイル
- `ext`: 対象ファイルの拡張子

## 注意事項

- バックアップを取ってから実行することを推奨します
- 大量のファイルを処理する場合は、十分なディスク容量を確保してください
- ファイルパスに日本語が含まれる場合は、適切なエンコーディングを使用してください

## ログ

実行ログは `utils_execution.log` に保存されます。エラーが発生した場合は、このログファイルを確認してください。
