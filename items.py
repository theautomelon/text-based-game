import random as r
from player import *
from monster import *

#list of item names
nameList= ['Health Potion','White Claw', 'Bomb']

class Item(object):
    def __init__(self,name,cost,monster,player):
        self.name= name
        self.cost= cost

class hPotion(Item):
    def __init__(self,name,cost,player):
        super.__init__(name,cost,player)
        self.name = "Health Potion"
        self.description = "Use this to heal between 40 and 60 HP."
        health = r.randint(40,60)
        player.heal(health)
        print(player.name+" has healed "+ str(health)+" HP.")

class claw(Item):
    def __init__(self,name,cost,player):
        super.__init__(name,cost,player)
        self.name = "White Claw"
        self.description = "Use this to get a guarenteed critical hit on the next hit you land."
        player.crit = 101
        print(player.name+ " has 100 percent crit chance on the next successful attack!")


class bomb(Item):
    def __init__(self,name,cost,monster):
        super.__init__(name,cost,monster)
        self.name = "Bomb"
        self.description = "Use this to deal 100 damage to an enemy monster."
        monster.currentHealth-= 100
        print(monster.name + " has lost 100 health!")
        

