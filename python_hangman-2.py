import random
from words import words
from hangman_visual import lives_visual_dict
from hangman_visual import starting
from words import encourage 
from words import failed 
import string
import time

def getvalidword(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word or 'Zimmerman' in word or 'Rai' in word:
        word = random.choice(words) #will choose another word if word if classified as invalid (fits above criteria)
    return word.upper() #everything will be capitalized so it matches up (ie. a --> A)


def hangman():
    word = getvalidword(words)
    
    word_letters = set(word)  #letters in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #what the user has guessed

    lives = 7
    print(starting[0])
  
    while len(word_letters) > 0 and lives > 0:
        #letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('lives remaining:', lives, ' letters guessed: ', ' '.join(used_letters))
        time.sleep(1)

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('current word: ', ' '.join(word_list))
        time.sleep(1)
        user_letter = input('guess a letter: ').upper() #input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                #
                encourage_message = random.choice(encourage) #random message 
                print(encourage_message, 'that letter is in the word!!')
                time.sleep(1)

            else:
                lives = lives - 1  # takes away a life if wrong
                #
                failed_message = random.choice(failed) #random message 
                print('\nur letter:', user_letter, ' is not in the word :( ', failed_message)

        elif user_letter in used_letters: #already in 'guessed' list
            print('\nalready used ._. try again')

        else:
            print('\ninvalid letter ._. try again')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print("\033[1;32;41m u didnt guess the word: ", word) #red
    else:
        print("\033[1;32;42m congrats! u guessed the word!!: ", word) #green 
        #my unique change: adds colour to the game depending on if u win/lose

hangman()
#repeats the game 
while True:
    play_again = input("play again? (y/n): ")

    if play_again == "y":
        hangman()
    elif play_again == "n":
        print("game over ._.")
        break  #loop ends if they dont want to play    
    else:
        print("oops, pls try again")
        continue #re-asks




