import random as r

#list of item names
nameList= ['Health Potion','White Claw', 'Bomb']

class Item(object):
    def __init__(self,name,cost):
        self.name= name
        self.cost= cost

class hPotion(Item):
    def __init__(self,name,cost):
        super.__init__(name,cost)
        self.name = "Health Potion"
        self.description = "Use this to heal between 40 and 60 HP."

    def use(player):
        health = r.randint(40,60)
        player.heal(health)
        print(player.name+" has healed "+ str(health)+" HP.")

class claw(Item):
    def __init__(self,name,cost):
        super.__init__(name,cost)
        self.name = "White Claw"
        self.description = "Use this to get a guarenteed critical hit on the next hit you land."
    
    def use(player):
        player.crit = 101
        print(player.name+ " has 100 percent crit chance on the next successful attack!")

class bomb(Item):
    def __init__(self,name,cost):
        super.__init__(name,cost)
        self.name = "Bomb"
        self.description = "Use this to deal 100 damage to an enemy monster."
    
    def use(monster):
        monster.currentHealth-= 100
        print(monster.name + " has lost 100 health!")
        

