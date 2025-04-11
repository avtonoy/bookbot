def get_num_words(text: str):
    liste = text.split()
    return len(liste)


def get_count_letters(text: str):

    letters_dict = {}
    words = text.split()

    for word in words:
        for letter in word:
            if letter.lower() in letters_dict:
                letters_dict[letter.lower()] += 1
            else:
                letters_dict[letter.lower()] = 1

    return letters_dict
