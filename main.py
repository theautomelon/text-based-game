import random as r
import textwrap
from player import *
from monster import *


#VARIABLES
gameOver = False
introText= "Welcome, you little weasel. You are a ferret, specifically Fabio the Illustrious Ferret. You, in your infinite wisdom, have decided to escape from your human enslavers and embark on a journey to finally make a name for yourself. The road to stardom is arduous but luckily your former masters taught you everything there is to know about the ancient combat ritual 剪刀石頭布, or as the filthy Americans call it- Rock, Paper, Scissors. Stay on your guard, as there is not telling what dangers may lie ahead."
stage = 0
validAnswer = False
#FUNCTIONS

#print out story and create player character
def setup():
    
    #starting game
    #ASCII art taken from http://www.ascii-art.de/ascii/def/ferret.txt
    print(' ')
    print(",____          (\=-,")
    print("\ '=.`'-.______/ /^")
    print(" `-._.-'(=====' /")
    print("         \<'--\(")
    print("          ^^   ^^")
    print(' ')
    
    print(" ______     ______     ______     __  __        ______   ______     ______   ______     ______        ______   ______     ______     ______     ______     ______  ")
    print("/\  == \   /\  __ \   /\  ___\   /\ \/ /       /\  == \ /\  __ \   /\  == \ /\  ___\   /\  == \      /\  ___\ /\  ___\   /\  == \   /\  == \   /\  ___\   /\__  _\ ")
    print("\ \  __<   \ \ \/\ \  \ \ \____  \ \  _'-.     \ \  _-/ \ \  __ \  \ \  _-/ \ \  __\   \ \  __<      \ \  __\ \ \  __\   \ \  __<   \ \  __<   \ \  __\   \/_/\ \/ ")
    print(" \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\     \ \_\    \ \_\ \_\  \ \_\    \ \_____\  \ \_\ \_\     \ \_\    \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\    \ \_\ ")
    print("  \/_/ /_/   \/_____/   \/_____/   \/_/\/_/      \/_/     \/_/\/_/   \/_/     \/_____/   \/_/ /_/      \/_/     \/_____/   \/_/ /_/   \/_/ /_/   \/_____/     \/_/ ")
    print("                                                                                                                                                                   ")

    
    #story introduction dedentedText makes text look nicer
    dedentedText = textwrap.dedent(introText).strip()
    print(dedentedText)
    input("Press enter to continue.")


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
fabio = Player("Fabio")

while(not gameOver):

    #checks stage number to assign monster type
    if (stage == 0):
        enemy = Monster("Billy", "Badger")
    elif (stage == 1):
        enemy = Monster("Gargamel", "Bobcat")
    elif (stage == 2):
        enemy = Monster("Wily", "Coyote")
    elif (stage == 3):
        enemy = Monster("Gahool", "Owl")
    elif (stage == 4):
        enemy = Monster("Eddy", "Eagle")
    
    #prints name of enemy
    print('-----------------------------------------------')
    print()
    print("You have come across "+ enemy.name + " the "+ enemy.species)
    print("")

    combatOver = False
    while(not combatOver):
        outcome = ""
        validAnswer = False
        #Rock paper scissors loop
        while(not validAnswer):
            #displays health of enemy and player
            print(enemy.name+": "+str(enemy.currentHealth)+"/"+str(enemy.maxHealth)+" HP")
            print(fabio.name+": "+str(fabio.currentHealth)+"/"+str(fabio.maxHealth)+" HP")
            print()
            #asks player for move input
            print("What attack would you like to select?")
            player = input("Rock, Paper, or Scissors? ")
            if(player.lower() == "rock" or player.lower() == "r"):
                player = 1
                validAnswer=True
            elif(player.lower() == "paper" or player.lower() == "p"):
                player = 2
                validAnswer=True
            elif(player.lower() == "scissors" or player.lower() == "s"):
                player = 2
                validAnswer=True
            else:
                print("Please choose a valid answer")

        outcome = rps(player)
        #chooses attack and message based on outcome of rps function
        if(outcome == "win"):
            print()
            print("You have outwitted "+ enemy.name)
            print()
            fabio.attack(enemy)
            combatOver = enemy.checkDead()
        elif(outcome == "loss"):
            print()
            print("Alas! " + enemy.name +" landed a blow!")
            print()
            enemy.attack(fabio)
            combatOver = fabio.checkDead()
        else:
            print()
            print("Twinning! " + enemy.name + " chose the same move! Try again.")
            print()
    
    #checks if either player or monster is dead
    if (enemy.checkDead()):
        print()
        print(enemy.name+ " is dead! May he rest in hell! As a reward for your efforts your stats are now: ")
        print("Max Health: "+ str(fabio.maxHealth))
        print("Attack: " + str(fabio.attackDamage))
        print("Crit-Chance: "+ str(fabio.crit))
        print()

        

    if (fabio.checkDead()):
        print()
        print("Aye, ya blasted Ferret! You succumbed to your wounds. I knew you could never make it!")
        gameOver= True
        break


    #increases stage after loop, ends game once past 4
    stage+=1
    #heals player character after combat ends
    fabio.healFull()
    validAnswer = False
    if (stage == 5):
        print()
        print("I always knew ya had it in ya!")
        gameOver = True
        break
    
