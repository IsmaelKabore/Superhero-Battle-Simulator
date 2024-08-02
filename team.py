import random
from hero import Hero
class Team :
    def __init__(self, name, heroes=[]):
        self.name= name
        self.heroes= heroes
        self.total_kills = 0
        self.total_deaths = 0


    def add_heroes(self, hero: Hero):
        self.heroes.append(hero)
    
    def remove_hero(self, hero: Hero):
        if hero in self.heroes:
            self.heroes.remove(hero)     
    
    def view_all_heroes(self,):
        for hero in self.heroes:
            print (hero.name)
  
    def add_death(self, death_value):
      self.deaths+=death_value

    def add_kills(self, kill_value):
        self.kills+= kill_value
    
    def team_attack(self, opponent_team: 'Team') :
        chosen_hero = random. choice (opponent_team.heroes)
        chosen_opponent = random. choice(self.heroes)
        chosen_hero.battle(chosen_opponent)
        if chosen_hero.current_health < 0:
            self.living_heroes.removel(chosen_hero) 
            self.deaths += 1
            opponent_team.kills+= 1 
        elif chosen_opponent. current_health <=0:
            opponent_team. living_opponents. remove ( chosen_opponent)
            self.kills=+ 1 
            opponent_team.deaths=+1

    def revive_heroes (self) :
        for hero in self. heroes:
            hero.current_health = hero.starting_health 
            self.living_heroes= self.heroes

            