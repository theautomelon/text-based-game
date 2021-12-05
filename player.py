import random as r
from monster import *
from format import *

debug = False

class Player:
    def __init__(self, name):
        
        # initialize the player's stats
        self.name = name
        self.species = 'Ferret'
        self.maxHealth = 100
        self.currentHealth = self.maxHealth
        self.attackDamage = 50
        self.maxCrit = 10
        self.crit = self.maxCrit
        
        self.clawActive = False
        
        self.inventory = []

        if debug:   # only prints if debug is set to True
            print('DEBUG:   Creating ' + str(self.name) + ' the ' + str(self.species) + ' with ' + str(self.maxHealth) + ' health, ' + str(self.attackDamage) + ' attack, and ' + str(self.crit) + '%' + ' crit-chance')

    # checks the player's current health
    def healthStatus(self):
            print('You have ' + str(self.currentHealth) + '/' + str(self.maxHealth) + ' health')
            
    # player attacks the monster
    def attack(self, monster):
        
        # calculates the initial damage using attack stat
        damage = r.randint(self.attackDamage -10,self.attackDamage +10)
        
        if debug:   #only prints if debug is set to True
            print('DEBUG:   Precrit Damage:' + str(damage))
        
        # calculates if it is a crit attack
        if r.randint(0,100) < self.crit:    #if it is a crit hit
            damage = damage * 2
            print('It was a critical hit! You did ' + str(damage) + ' damage to ' + monster.name + ' the ' + monster.species)
            print()

        else:   #if it is not a crit hit
            print('You did ' + str(damage) + ' damage to ' + monster.name + ' the ' + monster.species)
            print()
        
        # subtracts the damage from the monster's current health
        monster.currentHealth = monster.currentHealth - damage
        
        return
    
    # checks if the player is dead
    # returns a boolean (True if dead, False if not dead)    
    def checkDead(self):
        if self.currentHealth <= 0:
            if debug: #only prints if debug is set to True 
                print('DEBUG:   ' + str(self.name) + ' the ' + str(self.species) + ' has died')
            return True
        else:
            return False
        
    # heals the player a set amount   
    def heal(self, healAmount):
        self.currentHealth = self.currentHealth + healAmount
        
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth
        
        if debug:   #only prints if debug is set to True 
            print('DEBUG:   You have been partially healed!')
            self.healthStatus()
    
    #heals the player fully    
    def healFull(self):
        self.currentHealth = self.maxHealth

        print('You have been fully healed!')
        
        if debug:   #only prints if debug is set to True 
            print('DEBUG:   You have been fully healed!')
            self.healthStatus()

    def upgradeStats(self):
        # increase health by 10-30
        self.maxHealth += r.randint(10,30)
        # increase health by 10-20
        self.attackDamage += r.randint(10,20)
        # increase crit by 1-5
        self.maxCrit += r.randint(1,5)
        self.crit = self.maxCrit
    
    def displayHealth(self, length):
        Format.displayHealth(self.currentHealth, self.maxHealth, length)