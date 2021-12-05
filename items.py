import random as r
from player import *
from monster import *

#list of item names
nameList= ['Health Potion','White Claw', 'Bomb']

class hPotion:
    def __init__(self):
        self.amount = 0
        self.name = "Health Potion"
        self.description = "Use this to heal between 40 and 60 HP."
    def use(player):
        health = r.randint(40,60)
        player.heal(health)
        print(player.name+" has healed "+ str(health)+" HP.")

class claw:
    def __init__(self,name,cost):
        
        self.amount = 0
        self.name = "White Claw"
        self.description = "Use this to get a guarenteed critical hit on the next hit you land."
    def use(player):
        player.crit = 101
        print(player.name+ " has 100 percent crit chance on the next successful attack!")


class bomb:
    def __init__(self,name,cost):
        self.amount = 0
        self.name = "Bomb"
        self.description = "Use this to deal 100 damage to an enemy monster."
    def use(monster):
        monster.currentHealth-= 100
        print(monster.name + " has lost 100 health!")
        

