def print_upper_words1(words):

    for word in words:
        if word.index("e") == 0:
            word = word.upper()
        else:
            word = word.lower()
        print(word)


# print_upper_words(['hello', 'goodbye', 'everyone'])

# print([word.upper() for word in words])


def print_upper_words2(words, must_start_wtih):
    for word in words:
        for letter in must_start_wtih:
            if word.startswith(letter):
                print(word.toupper())
