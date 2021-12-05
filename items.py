import random as r
from player import *
from monster import *

#list of item names
nameList= ['Health Potion','White Claw', 'Bomb']

#defines the item class
class Item():
    def __init__(self,name, value, quantity):
        self.name = name
        self.value = value
        self.quantity = quantity
        self.description = ''
    def itemAdd(self,inventory):
        inventory.append(self)

#defines the subclass weapon for the item class
class Weapon(Item):
    def __init__(self, name, value, quantity, damage):
        super().__init__(name, value, quantity)
        self.damage = damage

#creates object of requested item
#options: health potion, white claw, or bomb
def createItem(name):
    if(name.lower() == "hp" or name.lower() == "health potion"):
        hP = Item("Health Potion", 100, 1)
        hP.description = 'Use this to heal between 40 and 60 HP.'
        return hP

    elif(name.lower() == 'claw' or name.lower() == 'white claw'):
        claw = Item("White Claw", 200, 1)
        claw.description= 'Use this to get a guarenteed critical hit on the next hit you land.'
        return claw

    elif(name.lower() == 'bomb'):
        bomb = Weapon("Bomb", 150, 1)
        bomb.description='Use this to deal 100 damage to an enemy monster.'
        bomb.damage=100
        return bomb


#defines items uses
def useItem(name, creature):
    if(name.lower() == "hp" or name.lower() == "health potion"):
        if(creature.name == "Fabio"):
            healAmount = r.randint(40,60)
            creature.heal(healAmount)
            print(creature.name+" has healed "+ str(healAmount)+" HP.")
        else:
            print("You cannot use a health potion on an enemy!")

    elif(name.lower() == 'claw' or name.lower() == 'white claw'):
        if(creature.name == "Fabio"):
            creature.crit==101
        else:
            print("You cannot use a white claw on an enemy!")

    elif(name.lower() == 'bomb'):
        if(creature.name is not "Fabio"):
            creature.currentHealth-= 100
        else:
            print("You cannot use a bomb on yourself!")

#undos the white claw item
def undoItem(name, creature):
    if(name.lower == 'claw' or name.lower == 'white claw'):
        if(creature.name == "Fabio"):
            creature.crit==creature.maxCrit
        else:
            print("Something has gone wrong with the white claw undo function")

        

