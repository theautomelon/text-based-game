import random as r
from player import *

debug = True


class Monster:
    def __init__(self, name, species):
        self.name = name
        self.species = species

        if species == 'Badger':
            self.health = 50
            self.attackDamage = 50
            self.crit = 0
        elif species == 'Bobcat':
            self.health = 100
            self.attackDamage = 60
            self.crit = 5
        elif species == 'Coyote':
            self.health = 150
            self.attackDamage = 70
            self.crit = 5
        elif species == 'Owl':
            self.health = 100
            self.attackDamage = 100
            self.crit = 15
        elif species == 'Eagle':
            self.health = 125
            self.attackDamage = 110
            self.crit = 25

        # print monster to when creating to validate
        # this is purely for debugging
        if debug:
            print('Creating ' + str(self.name) + ' the ' + str(self.species) + ' with ' + str(self.health) + ' health, ' + str(self.attackDamage) + ' attack, and ' + str(self.crit) + '%' + ' crit-chance')

    def healthStatus(self):
        print(str(self.name) + ' the ' + str(self.species) + ' has ' + str(self.health) + ' health')
    
    def attack(self, player):
        damage = r.randint(self.attackDamage -10,self.attackDamage +10)
        
        
        if r.randint(0,100) < self.crit:
            damage = damage * 2
            print('It was a critical hit! ' + self.name + ' did ' + str(damage) + ' damage to you')
        else:
            print(self.name + ' did ' + str(damage) + ' damage to you')
        
        player.health = player.health - damage
        if player.health <= 0:
            print(str(self.name) + ' the ' + str(self.species) + ' killed you')