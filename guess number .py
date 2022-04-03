import random #so we can use random numbers. 
#will be faster than subtracting by x after each guess in computerguesses()
def userguesses():
    randomnumber = random.randint(1, 100) # comp generated random number
    userguess = 0 #user guess set to 0
    while userguess != randomnumber:
        userguess = int(input(f'guess a number, 1-{100}:')) 
        #user keeps guessing until their guess matches the random generated number 
        if userguess < randomnumber:
            print('too low ._. guess again')
        elif userguess > randomnumber:
            print('too high ._. guess again') 
    #the while loop breaks when the guessed number and random number are equal 
    print(f'congrats, u have guessed the number {randomnumber} !! :-]')

def computerguesses():
    low_possible = 1 #lowest possible starting guess
    high_possible = 100 #highest possible starting guess
    userfeedback = ''
    while userfeedback != 'c': #while comp guess is incorrect ... 
        if low_possible != high_possible: 
            compguess = random.randint(low_possible, high_possible) 
        else:
            compguess = low_possible 
        userfeedback = input(f'is {compguess} too high (h), low (l), or correct (c)?')
        if userfeedback == 'h':
            high_possible = compguess - 1 #lowers possible guess by 1
        elif userfeedback == 'l':
            low_possible = compguess + 1 #increases possible guess by 1 
    print(f'the computer guessed ur number {compguess} correctly !! :-]')

#ask the user to call the game they choose to play 
while True:
    game = input('would u like the computer to guess ur number(m), guess the computers number(c), or quit(q) *number must be 1-100*?')
    if game == 'm':
        computerguesses()
        break
    elif game == 'c':
        userguesses()
        break 
    elif game == 'q':
        print('u have quit :-]')
        break 
    #anything else will be invalid 
    else:
        print('invalid response ._. try again ')
        continue 