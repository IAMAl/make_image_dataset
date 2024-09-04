import os
from collections import Counter

def count_tokens_and_words(directory, ext):
    token_counts = Counter()
    word_counts = Counter()

    for filename in os.listdir(directory):
        if filename.endswith("."+ext):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                for line in file:
                    tokens = line.strip().split(',')
                    token_counts.update(tokens)
                    for token in tokens:
                        words = token.split()
                        word_counts.update(words)

    return token_counts, word_counts

directory_path = 'path'
ext='caption'
tokens, words = count_tokens_and_words(directory_path, ext)

from collections import Counter

def print_top_counts(counter, top_n=250):
    """ Prints the top N counts from a Counter object in a more readable format. """
    for item, count in counter.most_common(top_n):
        print(f"{item}: {count}")

print("Top Token Counts:")
print_top_counts(tokens)
print("Total Tokens:", sum(tokens.values()))

print("\nTop Word Counts:")
print_top_counts(words)
print("Total Words:", sum(words.values()))