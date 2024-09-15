import os

def remove_words_from_directory_updated(input_directory, output_directory, words_file_name, ext):
    count = 0
    words_file_path = os.path.join(os.path.dirname(__file__), words_file_name)  # remove_list.txt ファイルのパスを取得

    # Reading the words to remove from the words file
    with open(words_file_path, 'r', encoding='utf-8') as file:
        words_to_remove = {line.strip() for line in file}

    for root, dirs, files in os.walk(input_directory):
        # Processing each file in the directory
        for filename in files:
            if filename.endswith("." + ext):
                input_file_path = os.path.join(root, filename)
                output_file_path = os.path.join(output_directory, os.path.relpath(input_file_path, input_directory))

                # Reading the input file
                with open(input_file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # Processing each line
                updated_lines = []
                for line in lines:
                    tokens = line.strip().split(',')
                    filtered_tokens = [token for token in tokens if not any(word in token for word in words_to_remove)]
                    updated_lines.append(','.join(filtered_tokens))

                # Writing the updated content to the output file
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.write('\n'.join(updated_lines))
                count += 1

    print(f"{count} files are explored.")
