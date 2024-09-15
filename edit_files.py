import utils.files.find_file as ffile
import utils.files.remove_duplicate as rm_dup
import utils.files.rename_file as rn
import utils.files.report_duplicate as rep_dup
import argparse

open('utils/__init__.py', 'a').close()

parser = argparse.ArgumentParser(description="args")

parser.add_argument('--cap_dir',    help='target caption file path',    required=True)
parser.add_argument('--img_dir',    help='target image file path',      default='.')
parser.add_argument('--repo_dir',   help='report output path',          default='.')
parser.add_argument('--repo_name',  help='report file name',            default='report_text')
parser.add_argument('--command',    help='[find/rm_dup/rename/rep_dup]',required=True)
parser.add_argument('--ext',        help='file extension name',         default='caption')
parser.add_argument('--func',       help='function',                    default=False)

args = parser.parse_args()

cap_dir = args.cap_dir
img_dir = args.img_dir
repo_dir = args.repo_dir
repo_name = args.repo_name
command = args.command
ext = args.ext
func = args.func

if 'find' == command:
    input_directory = cap_dir
    find_list_directry = repo_dir
    ffile.find_files_with_tokens_or_words(input_directory, find_list_directry, ext)

elif 'rm_dup' == command:
    text_directory_path = cap_dir
    image_directory_path = img_dir
    rm_dup.synchronize_directories(text_directory_path, image_directory_path)

elif 'rename' == command:
    directory_path = cap_dir
    append = func
    old_string = ''
    new_string = ''
    rn.rename_files_in_directory(directory_path, append, old_string, new_string)

elif 'rep_dup' == command:
    directory_r = cap_dir
    path = repo_dir
    output_file = repo_name
    rep_dup.report_duplicate(directory_r, path, output_file)