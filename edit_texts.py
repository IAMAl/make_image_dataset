import utils.texts.append_text_to_files as add
import utils.texts.remove_spaces_around_commas as rm_space
import utils.texts.clean_text_content as rm_commas
import utils.texts.remove_words_from_directory_updated as rm_word
import utils.texts.rename_words_from_directory_updated as rename_word
import argparse

open('utils/__init__.py', 'a').close()

parser = argparse.ArgumentParser(description="args")

parser.add_argument('--cap_dir',    help='target caption file path',                        required=True)
parser.add_argument('--command',    help='[add_words/rm_spaces/rm_commas/rm_word/replace]', required=True)
parser.add_argument('--ext',        help='file extension name',                             default='caption')
parser.add_argument('--func',       help='functions',                                       default=True)
parser.add_argument('--list',       help='list file name',                                  default='list.txt')
parser.add_argument('--o_path',     help='output path',                                     default='.')

args = parser.parse_args()

cap_dir = args.cap_dir
command = args.command
ext = args.ext
func = args.func
list = args.list
o_path = args.o_path


if 'add_words' == command:
    directory = cap_dir
    text_file_path = list
    add.append_text_to_files(directory, text_file_path, ext, func)

elif 'rm_spaces' == command:
    directory = cap_dir
    rm_space.remove_spaces_around_commas(directory, ext)

elif 'rm_commas' == command:
    directory = cap_dir
    rm_commas.clean_text_content(directory, ext)

elif 'rm_word' == command:
    input_directory = cap_dir
    output_directory = o_path
    remove_words_file_name = list
    rm_word.remove_words_from_directory_updated(input_directory, output_directory, remove_words_file_name, ext)
    
elif 'rm_word' == command:
    input_directory = cap_dir
    output_directory = o_path
    rename_words_file_name = list
    rename_word.rename_words_from_directory_updated(input_directory, output_directory, rename_words_file_name, ext)