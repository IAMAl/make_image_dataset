import os

def rename_words_from_directory_updated(input_directory, output_directory, words_file_name, ext):
    count = 0
    words_file_path = os.path.join(os.path.dirname(__file__), words_file_name)

    # Reading the words to remove from the words file
    words_from_rename = []
    words_to_rename = []
    with open(words_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words_from_rename.append(line.split(',')[0])
            words_to_rename.append(','.join(line.split(',')[1:]))

    for root, dirs, files in os.walk(input_directory):
        # Processing each file in the directory
        for filename in files:
            if filename.endswith("." + ext):
                input_file_path = os.path.join(root, filename)
                output_file_path = os.path.join(output_directory, os.path.relpath(input_file_path, input_directory))

                try:
                    # Reading the input file
                    with open(input_file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                except FileNotFoundError:
                    print(f"File '{input_file_path}' not found.")
                    continue
                except IOError as e:
                    print(f"Error reading file '{input_file_path}': {e}")
                    continue

                if not lines:
                    print(f"File '{input_file_path}' is empty.")
                    continue

                # Processing each line
                updated_lines = []
                for line in lines:
                    filtered_tokens = []
                    tokens = line.strip().split(',')
                    for token in tokens:
                        if ( len(token) > 1 and not token in filtered_tokens ) or ('v' in token and len(token)==1):
                            for index, word in enumerate(words_from_rename):
                                if word in token and len(token) > 1 and len(word) > 1:
                                    if len(words_to_rename[index].split(',')) == 2:
                                        if len(words_to_rename[index].split(',')[0]) == 1:
                                            words_to_rename[index] = words_to_rename[index].split(',')[1]
                                        elif len(words_to_rename[index].split(',')[1]) == 1:
                                            words_to_rename[index] = words_to_rename[index].split(',')[0]

                                    token = token.replace(word, words_to_rename[index]).replace('\n','')
                                    print(f"{word} → {words_to_rename[index]}")
                            filtered_tokens.append(token)
                    updated_lines = ','.join(updated_lines) + ','.join(filtered_tokens)

                # Writing the updated content to the output file
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    #file.write('\n'.join(updated_lines))
                    file.write(updated_lines)
                count += 1

    print(f"{count} files are explored.")