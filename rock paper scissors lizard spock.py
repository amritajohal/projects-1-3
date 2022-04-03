import random
Quit = False
Win = 0
Loss = 0 #setting the starting values of wins-losses to 0

#asks user for their choice, gives x a value of 1 no matter what
def Play():
    global Win
    Player = input("rock(r), paper(p), scissors(s), lizard(l), spock(k) or (q) to quit: ")
    me = random.choice(["r", "p", "s", "l", "k"])
    
    if Player == "r" or Player == "p" or Player == "s" or Player == "l" or Player == "k" or Player == "q":
        x = 1
        
    else:    
        return ("invalid ._. pls put r,p,s,l,k,q") 
        
    if Player == "q":
        global Quit 
        Quit = True 
    
    print (f"u chose {Player}, i chose {me}") #repeats our choices 
    
    if Player == me:
        return ("tie ._. ")

    elif won(Player, me):
        global Win
        Win = Win + 1 #the value of x gets added to wins if the user wins 
        return ("u win  :`(")

    global Loss 
    Loss = Loss + 1 #the value of x gets added to losses if the user loses
    return("i win :-)")

def won(Competitor, Opponent):
    
    if (Competitor == "k" and (Opponent == "s" or Opponent == "r") or (Competitor == "s" and (Opponent == "p" or Opponent == "l")) or (Competitor == "p" and (Opponent == "r" or Opponent == "k")) or (Competitor == "r" and (Opponent == "l" or Opponent == "s")) or (Competitor == "l" and (Opponent == "k" or Opponent == "p"))):
        return True 

#need to ask the user if they want to play or not
while True:
    Start = input("play, rock, paper, scissors, lizard, spock (play)? or (q) to quit: ")
    
    if Start == "play":
        Game = True #if game is true, it will continue to run
        break
    elif Start == "q": 
        Game = False #if game is false, it will stop 
        break
    else:
        print("invalid ._. choose (play) or (q). ")
        continue #if response is invalid, the loop will repeat until it gets a valid response
    
while Game == True: #the game continues 
    
    print(Play())
    
    if Quit == True: #the game has ended
        
        print(f"scoreboard- u: {Win} me: {Loss}")
        
        if Win > Loss:
            print("u won the game :-[")
            break
        elif Loss > Win:
            print("i win the game :-]")
            break
        else:
            print("tie game ._.")
            break #breaks end game 
        
    print(f"total- u: {Win} me: {Loss}") #final result from round  