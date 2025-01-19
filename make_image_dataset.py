import argparse
import logging
import os

# Dataset utilities
import utils.dataset.replace_in_files_and_directories as replace_func
import utils.dataset.copy_directory as copy_dir
import utils.dataset.add_prefix_to_files as add_prefix
import utils.dataset.resize_and_copy_images as resize_imgs
import utils.dataset.flip_and_rename_images as flip_imgs
import utils.dataset.copy_files_flat_with_report as copy_flat
import utils.dataset.copy_files_based_on_structure as copy_structure
import utils.dataset.copy_files_by_detected_extensions as copy_by_ext

# File utilities
import utils.files.find_file as find_file
import utils.files.remove_duplicate as rm_dup
import utils.files.rename_file as rename_file
import utils.files.report_duplicate as report_dup

# Image utilities
import utils.images.jpg_metadata_edit as jpg_meta

# Text utilities
import utils.texts.add_word as add_word
import utils.texts.remove_dup_commas as rm_commas
import utils.texts.remove_spaces as rm_spaces
import utils.texts.remove_word as rm_word
import utils.texts.rename_word as rename_word
import utils.texts.statistics as text_stats

def setup_logging(log_file: str = 'utils_execution.log'):
    """ロギングの設定"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file
    )
    return logging.getLogger(__name__)

def setup_dataset_parsers(subparsers):
    """データセット関連のパーサー設定"""
    # replace_in_files
    parser_replace = subparsers.add_parser('dataset_replace', help='Replace content in files')
    parser_replace.add_argument('--src_dir', required=True)
    parser_replace.add_argument('--dest_dir', required=True)
    parser_replace.add_argument('--replacements', nargs='+')
    parser_replace.add_argument('--report', required=True)
    parser_replace.add_argument('--list_file', required=True)

    # copy_directory
    parser_copy = subparsers.add_parser('dataset_copy', help='Copy directory')
    parser_copy.add_argument('--src_dir', required=True)
    parser_copy.add_argument('--dest_dir', required=True)

    # add_prefix
    parser_prefix = subparsers.add_parser('dataset_prefix', help='Add prefix to files')
    parser_prefix.add_argument('--directory', required=True)
    parser_prefix.add_argument('--prefix', required=True)

    # copy_files_flat
    parser_flat = subparsers.add_parser('dataset_flat', help='Copy files to flat structure')
    parser_flat.add_argument('--src_dir', required=True)
    parser_flat.add_argument('--dest_dir', required=True)
    parser_flat.add_argument('--report', required=True)

    # copy_by_structure
    parser_struct = subparsers.add_parser('dataset_structure', help='Copy files based on structure')
    parser_struct.add_argument('--src_dir', required=True)
    parser_struct.add_argument('--dest_dir', required=True)
    parser_struct.add_argument('--structure_file', required=True)
    parser_struct.add_argument('--extensions', nargs='+', required=True)
    parser_struct.add_argument('--report', required=True)

    # copy_by_extension
    parser_ext = subparsers.add_parser('dataset_by_ext', help='Copy files by extension')
    parser_ext.add_argument('--src_dir', required=True)
    parser_ext.add_argument('--dest_base', required=True)

def setup_file_parsers(subparsers):
    """ファイル関連のパーサー設定"""
    # find_file
    parser_find = subparsers.add_parser('file_find', help='Find files with tokens/words')
    parser_find.add_argument('--directory', required=True)
    parser_find.add_argument('--tokens_file', required=True)
    parser_find.add_argument('--ext', required=True)

    # remove_duplicate
    parser_rm_dup = subparsers.add_parser('file_rm_dup', help='Remove duplicate files')
    parser_rm_dup.add_argument('--text_dir', required=True)
    parser_rm_dup.add_argument('--image_dir', required=True)

    # rename_file
    parser_rename = subparsers.add_parser('file_rename', help='Rename files')
    parser_rename.add_argument('--directory', required=True)
    parser_rename.add_argument('--append', type=bool, default=False)
    parser_rename.add_argument('--old_string', default='')
    parser_rename.add_argument('--new_string', default='')

    # report_duplicate
    parser_rep_dup = subparsers.add_parser('file_report_dup', help='Report duplicate files')
    parser_rep_dup.add_argument('--directory', required=True)
    parser_rep_dup.add_argument('--output_path', required=True)
    parser_rep_dup.add_argument('--output_file', required=True)

def setup_image_parsers(subparsers):
    """画像関連のパーサー設定"""
    # resize_images
    parser_resize = subparsers.add_parser('image_resize', help='Resize images')
    parser_resize.add_argument('--src_dir', required=True)
    parser_resize.add_argument('--dest_dir', required=True)
    parser_resize.add_argument('--size', type=int, default=1024)

    # flip_images
    parser_flip = subparsers.add_parser('image_flip', help='Flip images')
    parser_flip.add_argument('--src_dir', required=True)
    parser_flip.add_argument('--dest_dir', required=True)
    parser_flip.add_argument('--replacements', nargs='+')

    # jpg_metadata
    parser_meta = subparsers.add_parser('image_metadata', help='Edit JPEG metadata')
    parser_meta.add_argument('--directory', required=True)
    parser_meta.add_argument('--new_metadata', type=dict, default=None)

def setup_text_parsers(subparsers):
    """テキスト関連のパーサー設定"""
    # add_word
    parser_add = subparsers.add_parser('text_add', help='Add words to text files')
    parser_add.add_argument('--directory', required=True)
    parser_add.add_argument('--text_file', required=True)
    parser_add.add_argument('--ext', required=True)
    parser_add.add_argument('--append', type=bool, default=True)

    # remove_commas
    parser_rm_comma = subparsers.add_parser('text_rm_comma', help='Remove duplicate commas')
    parser_rm_comma.add_argument('--directory', required=True)
    parser_rm_comma.add_argument('--ext', required=True)

    # remove_spaces
    parser_rm_space = subparsers.add_parser('text_rm_space', help='Remove spaces around commas')
    parser_rm_space.add_argument('--directory', required=True)
    parser_rm_space.add_argument('--ext', required=True)

    # remove_word
    parser_rm_word = subparsers.add_parser('text_rm_word', help='Remove words from text')
    parser_rm_word.add_argument('--src_dir', required=True)
    parser_rm_word.add_argument('--dest_dir', required=True)
    parser_rm_word.add_argument('--words_file', required=True)
    parser_rm_word.add_argument('--ext', required=True)

    # rename_word
    parser_ren_word = subparsers.add_parser('text_rename_word', help='Rename words in text')
    parser_ren_word.add_argument('--src_dir', required=True)
    parser_ren_word.add_argument('--dest_dir', required=True)
    parser_ren_word.add_argument('--words_file', required=True)
    parser_ren_word.add_argument('--ext', required=True)

    # statistics
    parser_stats = subparsers.add_parser('text_stats', help='Generate text statistics')
    parser_stats.add_argument('--directory', required=True)
    parser_stats.add_argument('--ext', required=True)

def execute_command(args, logger):
    """コマンドの実行"""
    try:
        if args.command.startswith('dataset_'):
            execute_dataset_command(args, logger)
        elif args.command.startswith('file_'):
            execute_file_command(args, logger)
        elif args.command.startswith('image_'):
            execute_image_command(args, logger)
        elif args.command.startswith('text_'):
            execute_text_command(args, logger)
    except Exception as e:
        logger.error(f"Error executing {args.command}: {e}")
        raise

def execute_dataset_command(args, logger):
    """データセット関連コマンドの実行"""
    command = args.command.replace('dataset_', '')
    if command == 'replace':
        replacements = [tuple(r.split(',')) for r in args.replacements]
        replace_func.replace_in_files_and_directories(
            args.src_dir, args.dest_dir, replacements, args.report, args.list_file)
    elif command == 'copy':
        copy_dir.copy_directory(args.src_dir, args.dest_dir)
    elif command == 'prefix':
        add_prefix.add_prefix_to_files(args.directory, args.prefix)
    elif command == 'flat':
        copy_flat.copy_files_flat_with_report(args.src_dir, args.dest_dir, args.report)
    elif command == 'structure':
        copy_structure.copy_files_based_on_structure(
            args.src_dir, args.dest_dir, args.structure_file, args.extensions, args.report)
    elif command == 'by_ext':
        copy_by_ext.copy_files_by_detected_extensions(args.src_dir, args.dest_base)

def execute_file_command(args, logger):
    """ファイル関連コマンドの実行"""
    command = args.command.replace('file_', '')
    if command == 'find':
        find_file.find_files_with_tokens_or_words(args.directory, args.tokens_file, args.ext)
    elif command == 'rm_dup':
        rm_dup.synchronize_directories(args.text_dir, args.image_dir)
    elif command == 'rename':
        rename_file.rename_files_in_directory(
            args.directory, args.append, args.old_string, args.new_string)
    elif command == 'report_dup':
        report_dup.report_duplicate(args.directory, args.output_path, args.output_file)

def execute_image_command(args, logger):
    """画像関連コマンドの実行"""
    command = args.command.replace('image_', '')
    if command == 'resize':
        resize_imgs.resize_and_copy_images(args.src_dir, args.dest_dir, args.size)
    elif command == 'flip':
        replacements = [tuple(r.split(',')) for r in args.replacements]
        flip_imgs.flip_and_rename_images(args.src_dir, args.dest_dir, replacements)
    elif command == 'metadata':
        jpg_meta.remove_metadata_from_jpeg_files(args.directory, args.new_metadata)

def execute_text_command(args, logger):
    """テキスト関連コマンドの実行"""
    command = args.command.replace('text_', '')
    if command == 'add':
        add_word.append_text_to_files(args.directory, args.text_file, args.ext, args.append)
    elif command == 'rm_comma':
        rm_commas.clean_text_content(args.directory, args.ext)
    elif command == 'rm_space':
        rm_spaces.remove_spaces_around_commas(args.directory, args.ext)
    elif command == 'rm_word':
        rm_word.remove_words_from_directory_updated(
            args.src_dir, args.dest_dir, args.words_file, args.ext)
    elif command == 'rename_word':
        rename_word.rename_words_from_directory_updated(
            args.src_dir, args.dest_dir, args.words_file, args.ext)
    elif command == 'stats':
        tokens, words = text_stats.count_tokens_and_words(args.directory, args.ext)
        text_stats.print_top_counts(tokens)
        text_stats.print_top_counts(words)

def main():
    parser = argparse.ArgumentParser(description="Dataset Utilities")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # 各カテゴリのパーサーを設定
    setup_dataset_parsers(subparsers)
    setup_file_parsers(subparsers)
    setup_image_parsers(subparsers)
    setup_text_parsers(subparsers)

    args = parser.parse_args()
    logger = setup_logging()

    if args.command:
        execute_command(args, logger)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
