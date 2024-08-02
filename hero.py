# hero.py
import random
from ability import Ability
from armor import Armor
from weapon import Weapon
class Hero:
  
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer

      current_health: Integer
    '''

    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health
    self.abilities= []
    self.armors= []
    self.deaths=0
    self.kills=0

  def battle(self, opponent):
    if not self.abilities and not opponent.abilities:
        print("Draw")

    while self.current_health > 0 and opponent.current_health>0:
        damage_to_opponent = self.attack()
        damage_to_self = opponent.attack()
        
        self.take_damage(damage_to_self)
        opponent.take_damage(damage_to_opponent)
    
    # Determine and print the winner
    if self.current_health > 0:
        print(f"{self.name} won!")
    else :
        print(f"{opponent.name} won!")


  def add_ability(self, ability: Ability):
        self.abilities.append(ability)
    

  def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
        
  def add_armor(self, armor):
      self.armors.append(armor)

  def defend(self):
      total_block=0
      for armor in self.armors:
          total_block = total_block+ armor.block()
      return total_block
      
  def take_damage(self,damage):
      eff_damage=damage-self.defend()
      if eff_damage>0:
          self.current_health-= eff_damage

  def add_weapon(self, weapon: Weapon):
    self.abilities.append(weapon)
      
  def add_death(self, death_value):
      self.deaths+=death_value

  def add_kills(self, kill_value):
      self.kills+= kill_value