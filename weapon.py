import random
from ability import Ability
class Weapon(Ability):
  def attack(self):
    """  This method returns a random value
    between one half to the full attack power of the weapon.
    """
    # TODO: Use integer division to find half of the max_damage value
    # then return a random integer between half of max_damage and max_damage
    half_max_damage= self.max_damage//2
    return random.randint(half_max_damage, self.max_damage)
  

  

