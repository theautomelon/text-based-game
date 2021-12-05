import random as r
import textwrap
from player import *


#VARIABLES
gameOver = False
introText= "Welcome, you little weasel. You are a ferret, specifically Fabio the Illustrious Ferret. You, in your infinite wisdom, have decided to escape from your human enslavers and embark on a journey to finally make a name for yourself. The road to stardom is arduous but luckily your former masters taught you everything there is to know about the ancient combat ritual 剪刀石頭布, or as the filthy Americans call it- Rock, Paper, Scissors. Stay on your guard, as there is not telling what dangers may lie ahead."

#FUNCTIONS

#print out story and create player character
def setup():

    #create object of player class
    Fabio = Player("Fabio")
    #story introduction dedentedText makes text look nicer
    dedentedText = textwrap.dedent(introText).strip()
    print(dedentedText)

    

#function which generates one of 3 values and compares it against player choice
#simulates rock paper scissors
def rps(player):

    #three outcomes- tie, win (player wins), loss, (monster wins)
    outcome=""
    #values: 1 = rock, 2 = paper, 3 = scissors
    monster = r.randint(1,3)

    #monster and player tie
    if(monster== player):
        outcome = "tie"
    #monster chooses rock
    elif(monster == 1):
        #player chooses paper
        if(player == 2):
            outcome= "win"
        #player chooses scissors
        elif(player == 3):
            outcome= "loss"
    #monster chooses paper
    elif(monster == 2):
        #player chooses rock
        if(player == 1):
            outcome= "loss"
        #player chooses scissors
        elif(player == 3):
            outcome= "win"
    #monster chooses scissors
    elif(monster == 3):
        #player chooses rock
        if(player == 1):
            outcome= "win"
        #player chooses paper
        elif(player == 2):
            outcome= "loss"

    return outcome




#GAME LOOP

#prints introduction and create player object
setup()

while(not gameOver):

    


    pass
