from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: None
        team_two: None
    '''

    # TODO: create instance variables named team_one and team_two that
    # will hold our teams.
    self.team_one= None
    self.team_two = None

  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?  ")
    max_damage = input(
      "What is the max damage of the ability?  ")

    return Ability(name, max_damage)

  def create_weapon(self):
    '''Prompt user for Weapon information
        return Weapon with values from user input.
    '''
    # TODO: This method will allow a user to create a weapon.
    # Prompt the user for the necessary information to create a new weapon object.
    # return the new weapon object.
    name = input("What is the weapon name?  ")
    max_damage = int(input("What is the max damage of the weapon?  "))
    return Weapon(name, max_damage)
  

  def create_armor(self):
    '''Prompt user for Armor information
      return Armor with values from user input.
    '''
    # TODO:This method will allow a user to create a piece of armor.
    #  Prompt the user for the necessary information to create a new armor object.
    #  return the new armor object with values set by user.
    name = input("What is the weapon name?  ")
    max_block = int(input("What is the max damage of the weapon?  "))
    return Weapon(name, max_block)

  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        # TODO add an ability to the hero
        # HINT: First create the ability, then add it to the hero
        ability= self.create_ability()
        hero.add_ability(ability)
      elif add_item == "2":
        # TODO add a weapon to the hero
        # HINT: First create the weapon, then add it to the hero
        weapon= self.create_weapon()
        hero.add_weapon(weapon)

      elif add_item == "3":
        # TODO add an armor to the hero
        # HINT: First create the armor, then add it to the hero
        armor= self.create_armor()
        hero.add_armor(armor)
    return hero

  # build_team_one is provided to you
  def build_team_one(self):
    '''Prompt the user to build team_one '''
    # This method should allow a user to create team one.
    # Prompt the user for the number of Heroes on team one
    # call self.create_hero() for every hero that the user wants to add to team one.
    team_name = input("Enter name for Team One: ")
    self.team_one = Team(team_name)

    # Add the created hero to team one.
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  # Now implement build_team_two
  #HINT: If you get stuck, look at how build_team_one is implemented
  def build_team_two(self):
    '''Prompt the user to build team_two'''
    # TODO: This method should allow a user to create team two.
    # This method should allow a user to create team two.
    # Prompt the user for the number of Heroes on team two
    # call self.create_hero() for every hero that the user wants to add to team two.
    # Add the created hero to team two.
    team2_name= input("Enter name for Team TwO: ")
    self.team_two= Team(team2_name)
    numOfTeam2Members= int(input("How many members would you like on Team TwO?\n"))
    for i in range(numOfTeam2Members):
      hero = self.create_hero()
      self.team_two.add_hero(hero)


  def team_battle(self):
    '''Battle team_one and team_two together.'''
    # TODO: This method should battle the teams together.
    # Call the attack method that exists in your team objects
    # for that battle functionality.
    self.team_one.attack(self.team_two)

  def show_stats(self):
    '''Prints team statistics to terminal.'''
    for hero in self.heroes:
        if hero.deaths == 0:
             print ("survived from " + self.team_one.name + ": " + hero.name)
        # declare the winning team
        if self.kills > self.deaths:
            print (f' (self.name) team won the game!')
         
    # This is how to calculate the average K/D for Team One
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

# This is how to calculate the average K/D for Team Two
    team_kills = 0
    team_deaths = 0
    for hero in self.team_two.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team_kills / team_deaths))

   
# Here is a way to list the heroes from Team One that survived
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    #TODO: Now list the heroes from Team Two that survived
    for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

