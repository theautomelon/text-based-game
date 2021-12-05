import random as r
from monster import *

debug = False

class Player:
    def __init__(self, name):
        self.name = name
        self.species = 'Ferret'
        self.maxHealth = 100
        self.currentHealth = self.maxHealth
        self.attackDamage = 50
        self.crit = 10

        # print player to when creating to validate
        # this is purely for debugging
        if debug:
            print('Creating ' + str(self.name) + ' the ' + str(self.species) + ' with ' + str(self.maxHealth) + ' health, ' + str(self.attackDamage) + ' attack, and ' + str(self.crit) + '%' + ' crit-chance')


    def healthStatus(self):
            print('You have ' + str(self.currentHealth) + '/' + str(self.maxHealth) + ' health')
            
    def attack(self, monster):
        damage = r.randint(self.attackDamage -10,self.attackDamage +10)
        
        
        
        if r.randint(0,100) < self.crit:
            damage = damage * 2
            print('It was a critical hit! You did ' + str(damage) + ' damage to ' + monster.name + ' the ' + monster.species)
        else:
            print('You did ' + str(damage) + ' damage to ' + monster.name + ' the ' + monster.species)
        
        monster.currentHealth = monster.currentHealth - damage
    
        
    def checkDead(self):
        if self.currentHealth <= 0:
            print(str(self.name) + ' the ' + str(self.species) + ' has died')
            return True
        else:
            return False
        
    def heal(self, healAmount):
        self.currentHealth = self.currentHealth + healAmount
        
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth
            
        print('You have been partially healed!')
        self.healthStatus()
        
    def healFull(self):
        self.currentHealth = self.maxHealth

        print('You have been fully healed!')
        self.healthStatus()