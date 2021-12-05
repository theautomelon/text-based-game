debug = True


class Monster:
    def __init__(self, name, species):
        self.name = name
        self.species = species

        if species == 'Badger':
            self.health = 50
            self.attack = 50
            self.crit = 0
        elif species == 'Bobcat':
            self.health = 100
            self.attack = 60
            self.crit = 5
        elif species == 'Coyote':
            self.health = 150
            self.attack = 70
            self.crit = 5
        elif species == 'Owl':
            self.health = 100
            self.attack = 100
            self.crit = 15
        elif species == 'Eagle':
            self.health = 125
            self.attack = 110
            self.crit = 25

        # print monster to when creating to validate
        # this is purely for debugging
        if debug:
            print('Creating ' + str(self.name) + ' the ' + str(self.species) + ' with ' + str(self.health) + ' health, ' + str(self.attack) + ' attack, and ' + str(self.crit) + '%' + ' crit-chance')

    def healthStatus(self):
            print(str(self.name) + ' the ' + str(self.species) + ' has ' + str(self.health) + ' health')
    
