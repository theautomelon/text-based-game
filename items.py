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
        for i in range(len(inventory)):
            if inventory[i] == '':
                inventory[i]= self
                break

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
        claw.description= 'Use this to get guarenteed critical strikes during the encounter.'
        return claw

    elif(name.lower() == 'bomb'):
        bomb = Weapon("Bomb", 150, 1, 100)
        bomb.description='Use this to deal 100 damage to an enemy monster.'
        bomb.damage=100
        return bomb


#defines items uses
def useItem(name, creature,inventory):
    if(name.lower() == "hp" or name.lower() == "health potion"):
        if(creature.name == "Fabio"):
            healAmount = r.randint(40,60)
            creature.heal(healAmount)
            print(creature.name+" has healed \033[1;32;40m"+ str(healAmount)+"\033[0;37;40m HP.")
            for x in inventory:
                if x.name.lower() == 'hp' or x.name.lower() == 'health potion':
                    x.quantity-= 1
                    break
        else:
            print("You cannot use a health potion on an enemy!")

    elif(name.lower() == 'claw' or name.lower() == 'white claw'):
        if(creature.name == "Fabio"):
            creature.crit=101
            print(creature.name+ "'s crit chance has been increased to 100%% for this encounter")
            for x in inventory:
                if x.name.lower() == 'claw' or x.name.lower() == 'white claw':
                    x.quantity-= 1
                    break
        else:
            print("You cannot use a white claw on an enemy!")

    elif(name.lower() == 'bomb'):
        if(creature.name is not "Fabio"):
            creature.currentHealth-= 100
            print(creature.name+" has been dealt 100 damage!")
            for x in inventory:
                if x.name.lower() == 'bomb':
                    x.quantity-= 1
                    break
        else:
            print("You cannot use a bomb on yourself!")
    
    

#undos the white claw item
def undoItem(name, creature):
    if(name.lower == 'claw' or name.lower == 'white claw'):
        if(creature.name == "Fabio"):
            creature.crit=creature.maxCrit
        else:
            print("Something has gone wrong with the white claw undo function")

        

