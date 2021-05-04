from hangman.valid_input import is_valid_input, check_valid_input


def main():
    #letter_guessed = input("please enter an input")
    old_letters = ['a', 'b', 'c']
    check_valid_input('C', old_letters)
    check_valid_input('ep', old_letters)
    check_valid_input('$', old_letters)
    check_valid_input('s', old_letters)

if __name__ == "__main__":
    main()

