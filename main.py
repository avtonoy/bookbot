from stats import *

file_path = './books/frankenstein.txt'


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


content = get_book_text(file_path=file_path)
count = get_num_words(content)
letter_dict = get_count_letters(content)

print(f'{count} words found in the document')
print(letter_dict)
