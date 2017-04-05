def add_underscores(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = new_word + word[i] + "_"
    return new_word

phrase = "Hello"
print(add_underscores(phrase))
