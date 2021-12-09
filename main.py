import random as r
from player import *
from monster import *
from items import *
from format import *
from sound import playMusic

#VARIABLES
gameOver = False
stage = 0
validAnswer = False
itemNames = ['Health Potion','White Claw', 'Bomb']

#FUNCTIONS

#prints out names in an inventory list
def printInv(inventory):
    for i in range(len(inventory)):
        if inventory[i]== '':
            pass
        else:
            print("Item "+ str(i+1) + ": " + inventory[i].name+" --Quantity: "+str(inventory[i].quantity)+" -- "+inventory[i].description)

def randItem():
    num = r.randint(0,2)
    item = itemNames[num]
    return item


#print out story and create player character
def setup():

    #starts music
    playMusic()
    
    #starting game
    print(' ')
    Format.printFerret()
    print(' ')
    Format.printDivider(42)
    
    print(' ')
    Format.printGameTitle()
    print(' ')

    #story introduction dedentedText makes text look nicer
    Format.printScroll()
    print(' ')
    input("        PRESS ENTER TO CONTINUE")



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
    Format.printDivider(42)
    print()
    print("You have come across "+ enemy.name + " the "+ enemy.species)
    print("")

    combatOver = False
    while(not combatOver):
        outcome = ""

        #booleans for item and attack loop
        validAnswer1 = False
        validAnswerA = False
        validAnswerB = False

       
        #gives player the choice of attacking or using an item
        while (not validAnswer1):
            #displays health of enemy and player
            enemy.displayHealth(6)
            print(' ' + enemy.name+": "+str(enemy.currentHealth)+"/"+str(enemy.maxHealth)+" HP ")
            print()
            fabio.displayHealth(6)
            print(' ' + fabio.name+": "+str(fabio.currentHealth)+"/"+str(fabio.maxHealth)+" HP ", end='')
            print()
            #asks player if they want to attack or use an item
            print()
            print("Would you like to attack or use an item?")
            print("Attacks-----------------------------------------------Items")
            choice1= input()
            #sets item choice back to false to allow for multiple item uses in encounter
            validAnswerB = False
            if(choice1.lower()== "attack" or choice1.lower()== "a"):
                #Rock paper scissors loop
                while(not validAnswerA):
                    #asks player for move input
                    print()
                    print("What attack would you like to select? Enter 'return' to go back")
                    player = input("Rock, Paper, or Scissors? ")
                    if(player.lower() == "rock" or player.lower() == "r"):
                        player = 1
                        validAnswerA=True
                        validAnswer1 = True
                    elif(player.lower() == "paper" or player.lower() == "p"):
                        player = 2
                        validAnswerA=True
                        validAnswer1 = True
                    elif(player.lower() == "scissors" or player.lower() == "s"):
                        player = 2
                        validAnswerA=True
                        validAnswer1 = True
                    elif(player.lower() == 'return'):
                        validAnswerA=True
                    else:
                        print("Please choose a valid answer")
            elif(choice1.lower()== "items" or choice1.lower()== "i"):
                #item loop
                while(not validAnswerB):
                    printInv(fabio.inventory)
                    print()
                    item = input("Enter the number of the item you would like to choose or enter 'return' to go back.")
                    print()
                    
                    if (item.lower() == 'return'):
                        validAnswerB=True
                    elif(item not in '123456789'):
                        print("Please choose a valid item number.")
                    elif(not fabio.inventory[int(item)-1]):
                        print("You do not have an item in that slot!")
                    else:
                        if fabio.inventory[int(item)-1].quantity > 0:
                            chosenItemName = fabio.inventory[int(item)-1].name
                            if (chosenItemName.lower() == 'bomb'):
                                useItem(chosenItemName, enemy,fabio.inventory)
                                if (enemy.checkDead()):
                                    validAnswer1 = True
                                    combatOver = False
                                    break
                                    
                            else:
                                useItem(chosenItemName, fabio,fabio.inventory)
                        else:
                            print("You have run out of that item!")
                        validAnswerB=True
                    print()
            else:
                print("Please choose a valid option.")


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
        fabio.upgradeStats()
        itemName = randItem()
        print(enemy.name+ " is dead! May he rest in hell! As a reward for your efforts your stats are now: ")
        print("Max Health: "+ str(fabio.maxHealth))
        print("Attack: " + str(fabio.attackDamage))
        print("Crit-Chance: "+ str(fabio.crit))
        print()
        print("Also, the beast dropped a \033[1;37;40m"+itemName+"\033[0;37;40m which has been added to your inventory!")
        item = createItem(itemName)
        for i in range(len(fabio.inventory)):
            if fabio.inventory[i]== '':
                item.itemAdd(fabio.inventory)
                break
            elif itemName == fabio.inventory[i].name:
                fabio.inventory[i].quantity+=1
                break
            
                    

    if (fabio.checkDead()):
        print()
        print("\033[1;31;40m Aye, ya blasted Ferret! You succumbed to your wounds. I knew you could never make it! \033[0;37;40m ")
        gameOver= True
        break

    printInv(fabio.inventory)
    #increases stage after loop, ends game once past 4
    stage+=1
    #heals player character after combat ends
    validAnswer = False
    if (stage == 5):
        print()
        print("\033[1;32;40m I always knew ya had it in ya! \033[0;37;40m ")
        gameOver = True
        break
    

