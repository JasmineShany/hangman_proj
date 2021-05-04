def show_hidden_word(secret_word, old_letters_guessed):
    shown_word = ""
    for letter in secret_word:
        if letter not in old_letters_guessed:
            shown_word +="_"
        else:
            shown_word += letter
    return shown_word


def check_win(secret_word, old_letters_guessed):
    while letter in secret_word:



secret_word = "friends"
old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
print(check_win(secret_word, old_letters_guessed))