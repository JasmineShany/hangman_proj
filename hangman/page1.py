import random
HANGMAN_ASCII_ART = ("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
                     """)
MAX_TRIES = 6
print(HANGMAN_ASCII_ART, "\n",
      MAX_TRIES)


#Expose the user the wording
game_wording = input("Please enter a word:").lower().replace(" ", "")
print(game_wording, len(game_wording))
user_len = len(game_wording)
hidden_game_wording = game_wording.replace(game_wording, user_len * "_")
print(hidden_game_wording)

#Guess a letter
user_guess = input("Guess a letter:").lower()
player_letter_len = len(user_guess)
if (player_letter_len > 1) and not (user_guess.isalpha()):
      print ("E3")
elif player_letter_len > 1:
      print ("E1")
elif not user_guess.isalpha():
      print ("E2")
else:
      print (user_guess)




