debug = True

class Player:
    def __init__(self, name):
        self.name = name
        self.species = 'Ferret'
        self.health = 100
        self.attack = 50
        self.crit = 10

        # print player to when creating to validate
        # this is purely for debugging
        if debug:
            print('Creating ' + str(self.name) + ' the ' + str(self.species) + ' with ' + str(self.health) + ' health, ' + str(self.attack) + ' attack, and ' + str(self.crit) + '%' + ' crit-chance')

Fabio = Player("Fabio")