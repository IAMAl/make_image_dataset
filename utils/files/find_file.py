import os

def find_files_with_tokens_or_words(directory, tokens_words_file_path, ext):
    # Reading the tokens or words to find from the specified file
    with open(tokens_words_file_path, 'r', encoding='utf-8') as file:
        tokens_words_to_find = {line.strip() for line in file}

    # Iterating through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith("."+ext):  # assuming text files
            file_path = os.path.join(directory, filename)

            # Reading the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Checking for tokens and words
            tokens = content.split(',')  # Splitting by token delimiter
            words = content.split()      # Splitting by word delimiter

            # If any of the tokens or words are found, print the file name
            for token in tokens:
                if token in tokens_words_to_find: 
                    print(f"token:{token} {filename}")
            for word in words:
                if word in tokens_words_to_find: 
                    print(f"word:{word} {filename}")
