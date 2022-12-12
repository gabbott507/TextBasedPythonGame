from menus import AttackMenu
from rich.console import Console 
from time import sleep
from termcolor import colored
import colorama
from random import randint
from random import randrange as RR

console = Console()

class Weapon:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage


class Helmets:
  def __init__(self, name, reduction):
    self.name = name 
    self.reduction = reduction


class BodyArmour:
  def __init__(self, name, reduction):
    self.name = name
    self.reduction = reduction


class LegArmour:
  def __init__(self, name, reduction):
    self.name = name
    self.reduction = reduction


class Boots:
  def __init__(self, name, reduction):
    self.name = name
    self.reduction = reduction


class Enemy:
  def __init__(self, name, hp, exp_held, damage, currency_held):
    self.name = name
    self.hp = hp
    self.exp_held = exp_held
    self.damage = damage
    self.currency_held = currency_held

  def attack(self, enemy, player):
    zombie = [1,2] # 0,1
    ghoul = [2,3] # 0,1
    goblin = [3,4,5] # 0,1,2
    ogre = [5, 6, 7]
    cyclopse = [7, 8, 9, 10]

    if(self.name == 'Zombie'): self.damage = zombie[RR(0,len(zombie))-1] # Range 0, len(zombie) = (1,2) so 2 - 1 = 1) Range 0-1 
    if(self.name == 'Ghoul'): self.damage = ghoul[RR(0,len(ghoul))-1]
    if(self.name == 'Goblin'): self.damage = goblin[RR(0,len(goblin))-1]
    if(self.name == 'Ogre'): self.damage = ogre[RR(0,len(ogre))-1]
    if(self.name == 'Cyclopse'): self.damage = cyclopse[RR(0,len(cyclopse))-1]

    print(colored(f'\n| BATTLE! | YOUR HP: {player.hp} | YOUR DEFENSE: {player.defense} |',attrs=['bold'], color='red'))
    print(colored('------------------------------------------\n',attrs=['bold'], color='red'))
    with console.status("[bold green]Attacking...."):
      if (enemy.damage - player.defense) <= 0:
        player.hp -= 1
        total_dmg = 1
      else:
        player.hp = (player.hp - enemy.damage) + player.defense
        total_dmg = enemy.damage - player.defense
      sleep(1)
      print(colored(f"\n{enemy.name} did {total_dmg} damage to you!",attrs=["bold"], color="cyan"))
    print('\n')
    sleep(1)


class Character:
  def __init__(self):
    self.level = 1
    self.exp = 0
    self.hp = 5
    self.damage = 0
    self.currency = 0
    self.defense = 0
    self.helmet = False
    self.bodyArmour = False
    self.legArmour = False
    self.boots = False

  def attack(self, enemy, weapon, player):
    print(colored(f'\n| BATTLE: {enemy.name.upper()} | HP: {enemy.hp} | DAMAGE: {enemy.damage} |',attrs=['bold'], color='red'))
    print(colored('--------------------------------------\n',attrs=['bold'], color='red'))
    selection = AttackMenu()
    if selection == '1':
      with console.status("[bold green]Attacking...."):
        enemy.hp -= weapon.damage + player.damage 
        sleep(1)
        print(colored(f"\nYou did {weapon.damage + player.damage} damage!",attrs=["bold"], color="cyan"))
      print('\n')
      sleep(1)

  def conclusion(self, player, enemy):
    if player.hp > 0:
      self.exp += enemy.exp_held
      self.currency += enemy.currency_held
      oldLevel = self.level
      if self.exp >= (self.level * 100):
        newLevel = self.level + 1
        self.level += 1
        if newLevel % 5 == 0:
          player.damage += 1
          player.defense += 1
          increases = "   BASE DAMAGE AND DEFENSE INCREASED BY 1!"
        else:
          increases = ""
        print(colored("       VICTORY!",attrs=["bold"], color="cyan"), 
          colored('\n+======================================+\n',attrs=["bold"], color="magenta"),
          colored(f"   YOU DEFEATED {enemy.name} \n",attrs=["bold"], color="yellow"),
          colored(f"   YOU ACQUIRED {enemy.exp_held} XP\n",attrs=["bold"], color="yellow"),  
          colored(f"   YOU ACQUIRED {enemy.currency_held} COINS\n",attrs=["bold"], color="yellow"), 
          colored(f"   YOU LEVELED UP TO LEVEL {newLevel}!\n",attrs=["bold"], color="yellow"), 
          colored(f'{increases}',attrs=["bold"], color="yellow"), 
          colored('\n+======================================+\n',attrs=["bold"], color="magenta"))
        self.exp = 0
      elif(self.level == oldLevel):
        print(colored("       VICTORY!",attrs=["bold"], color="cyan"), 
          colored('\n+====================+\n',attrs=["bold"], color="magenta"),
          colored(f"   YOU DEFEATED {enemy.name} \n",attrs=["bold"], color="yellow"),
          colored(f"   YOU ACQUIRED {enemy.exp_held} XP\n",attrs=["bold"], color="yellow"),  
          colored(f"   YOU ACQUIRED {enemy.currency_held} COINS",attrs=["bold"], color="yellow"),   
          colored('\n+====================+\n',attrs=["bold"], color="magenta"))
    else: 
       print(colored("       DEFEAT!",attrs=["bold"], color="cyan"), 
          colored('\n+==============================+\n',attrs=["bold"], color="magenta"),
          colored(f"   YOU WERE DEFEATED BY {enemy.name.upper()}!",attrs=["bold"], color="yellow"),   
          colored('\n+==============================+\n',attrs=["bold"], color="magenta"))

