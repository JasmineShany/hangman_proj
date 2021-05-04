def check_valid_input(letter_guessed, old_letters_guessed):
    """This Function should get an input and return false if
    the letter is more than 2 letters or not alfa,
    otherwise its a true input"""

    #letter_guessed = input("Guess a letter:").lower()
    player_letter_guessed_len = len(letter_guessed)
    if (player_letter_guessed_len > 1) and not (letter_guessed.isalpha()) and (letter_guessed.lower() in old_letters_guessed):
        print(False)
    elif (player_letter_guessed_len > 1):
        print(False)
    elif not (letter_guessed.isalpha()):
        print(False)
    elif letter_guessed.lower() in old_letters_guessed:
        print(False)
    else:
        print(True)
# To Do append the letter guess to the list old_letters_guessed
