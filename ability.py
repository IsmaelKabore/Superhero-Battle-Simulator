import random
class Ability:
     def __init__(self, name, max_damage=300):
          
        '''Instance properties:
        name: String
        max_damage: Integer
        '''
    

        # we know the name of our hero, so we assign it here
        self.name = name
        self.max_damage= max_damage
    
     def attack(self):
        damage= random.randint(0, self.max_damage)
        return damage


