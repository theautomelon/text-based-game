import random as r
from player import *
from format import *

debug = False

class Monster:
    def __init__(self, name, species):
        
        # initialize the monster's name and species
        self.name = name
        self.species = species

        # determines the monster's stats depending on its species
        if species == 'Badger':
            self.maxHealth = 50
            self.attackDamage = 50
            self.crit = 0
        elif species == 'Bobcat':
            self.maxHealth = 100
            self.attackDamage = 60
            self.crit = 5
        elif species == 'Coyote':
            self.maxHealth = 150
            self.attackDamage = 70
            self.crit = 5
        elif species == 'Owl':
            self.maxHealth = 100
            self.attackDamage = 100
            self.crit = 15
        elif species == 'Eagle':
            self.maxHealth = 125
            self.attackDamage = 110
            self.crit = 25
            
        #set the current health to the max health    
        self.currentHealth = self.maxHealth

        if debug:   #only prints if debug is set to True
            print('Creating ' + str(self.name) + ' the ' + str(self.species) + ' with ' + str(self.maxHealth) + ' health, ' + str(self.attackDamage) + ' attack, and ' + str(self.crit) + '%' + ' crit-chance')

    # checks the monster's current health
    def healthStatus(self):
        print(str(self.name) + ' the ' + str(self.species) + ' has ' + str(self.currentHealth) + '/' + str(self.maxHealth) + ' health')
    
    # monster attacks the player
    def attack(self, player):
        
        # calculates the initial damage using attack stat
        damage = r.randint(self.attackDamage -10,self.attackDamage +10)
        
        if debug:   #only prints if debug is set to True
            print('DEBUG:   Precrit Damage:' + str(damage))
        
        if r.randint(0,100) < self.crit: #if it is a crit hit
            damage = damage * 2
            print('It was a critical hit! \033[1;31;40m' + self.name + ' did ' + str(damage) + ' damage \033[0;37;40mto you')
            print()
        else:   #if it is not a crit hit
            print(self.name + ' did \033[1;31;40m' + str(damage) + ' damage \033[0;37;40mto you')
            print()
        
        # subtracts the damage from the player's current health
        player.currentHealth = player.currentHealth - damage
        
        return
        
    # checks if the monster is dead
    # returns a boolean (True if dead, False if not dead)
    def checkDead(self):
        if self.currentHealth <= 0:
            if debug:   #only prints if debug is set to True
                print('DEBUG:   ' + str(self.name) + ' the ' + str(self.species) + ' has died')
            return True
        else:
            return False
    
    # heals the monster a set amount 
    def heal(self, healAmount):
        self.currentHealth = self.currentHealth + healAmount
        
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth
        
        if debug:   #only prints if debug is set to True
            print('DEBUG:   The enemy has been partially healed!')
            self.healthStatus()
    
    #heals the monster fully    
    def healFull(self):
        self.currentHealth = self.maxHealth

        if debug:   #only prints if debug is set to True
            print('DEBUG:   The enemy has been fully healed!')
            self.healthStatus()
            
    def displayHealth(self, length):
        Format.displayHealth(self.currentHealth, self.maxHealth, length)
