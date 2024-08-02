import random
class Armor:

    def __init__(self, name, max_block=200):

        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)
        
    
