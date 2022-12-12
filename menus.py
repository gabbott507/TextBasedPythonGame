from termcolor import colored
import colorama

def StartMenu(level):
    if(level < 2):
        print(colored("       GAME MENU",attrs=["bold"], color="cyan"), 
              colored('\n+====================+\n',attrs=["bold"], color="magenta"), 
              colored("   [1] START GAME\n",attrs=["bold"], color="green"),  
              colored("   [3] QUIT GAME",attrs=["bold"], color="red"), 
              colored('\n+====================+\n',attrs=["bold"], color="magenta"))
        selection = input("> ")
    if(level >= 2):
        print(colored("       GAME MENU",attrs=["bold"], color="cyan"), 
              colored('\n+====================+\n',attrs=["bold"], color="magenta"),
              colored("   [1] START GAME\n",attrs=["bold"], color="green"),
              colored("   [2] SHOP\n",attrs=["bold"], color="yellow"),  
              colored("   [3] QUIT GAME",attrs=["bold"], color="red"), 
              colored('\n+====================+\n',attrs=["bold"], color="magenta"))
        selection = input("> ")
    return selection


def ShopMenu():
    print(colored("       SHOP",attrs=["bold"], color="cyan"), 
          colored('\n+====================+\n',attrs=["bold"], color="magenta"),
          colored("   [1] WEAPONS\n",attrs=["bold"], color="yellow"),
          colored("   [2] HELMETS\n",attrs=["bold"], color="yellow"),  
          colored("   [3] BODY ARMOR\n",attrs=["bold"], color="yellow"), 
          colored("   [4] PANTS\n",attrs=["bold"], color="yellow"),  
          colored("   [5] BOOTS",attrs=["bold"], color="yellow"), 
          colored('\n+====================+\n',attrs=["bold"], color="magenta"))
    shop = input("> ")
    return shop


def AttackMenu():
    print(colored("       ATTACK",attrs=["bold"], color="cyan"), 
          colored('\n+====================+\n',attrs=["bold"], color="magenta"),
          colored("   [1] ATTACK",attrs=["bold"], color="yellow"),
          colored('\n+====================+\n',attrs=["bold"], color="magenta"))
    selection = input("> ")
    return selection

    
def WeaponsList(currency, Weapons, ownedWeapons):
    print(colored("          WEAPON LIST",attrs=["bold"], color="cyan"), 
          colored('\n+===================================+\n',attrs=["bold"], color="magenta"),
          colored('        NAME',attrs=["bold"], color="magenta"), "       ",colored('DAMAGE',attrs=["bold"], color="magenta"), "   ",colored('PRICE\n',attrs=["bold"], color="magenta")
          )
    x = 1
    
    for key,value in Weapons.items():
        print(colored("[",attrs=["bold"],color="magenta"),colored(x,attrs=["bold"],color="yellow"),colored("]",attrs=["bold"], color="magenta"),
            (colored(key + "  ",attrs=["bold"], color="green")),"  ", colored(value[0],attrs=["bold"], color="red"),"       ", colored(value[1],attrs=["bold"], color="red"))
        x += 1
    print(colored('\n+===================================+\n',attrs=["bold"], color="magenta"))
    selection = input("Select Weapon> ")
    weaponsList = list(Weapons)
    weapons = weaponsList[(int(selection) - 1)]
    owned = ownedWeapons[int(selection)-1]
    if owned == False:
        while Weapons[weapons][1] >= currency:
            if(Weapons[weapons][1] <= currency):
                currency -= Weapons[weapons][1]
                owned = True
                return weapons, (int(selection)-1), owned, currency
            if(owned == True):
                return weapons, (int(selection)-1), owned, currency
            print(colored(f"\nYou don't have enough coins! You need: {Weapons[weapons][1]} You have: {currency}\n", attrs=["bold"], color="red"))
            selection = input("Select Weapon> ")
            weapons = weaponsList[(int(selection) - 1)]
            owned = ownedWeapons[int(selection)-1]
    if owned == False:
        currency -= Weapons[weapons][1]
    owned = True 
    return weapons, (int(selection)-1), owned, currency
    
    
def HelmetMenu(currency, Helmets, ownedHelmets):
    
    print(colored("          HELMETS",attrs=["bold"], color="cyan"), 
          colored('\n+=========================================+\n',attrs=["bold"], color="magenta"),
          colored('        NAME',attrs=["bold"], color="magenta"), "     ",colored('REDUCTION',attrs=["bold"], color="magenta"),"    ",colored('PRICE\n',attrs=["bold"], color="magenta")
          )
    x = 1
    
    for key,value in Helmets.items():
        print(colored("[",attrs=["bold"],color="magenta"),colored(x,attrs=["bold"],color="yellow"),colored("]",attrs=["bold"], color="magenta"),
            (colored(key + "  ",attrs=["bold"], color="green")),"  ", colored(value[0],attrs=["bold"], color="red"),"       ", colored(value[1],attrs=["bold"], color="red"))
        x += 1
    print(colored('\n+=========================================+\n',attrs=["bold"], color="magenta"))
    selection = input("Select Helmet> ")
    helmetList = list(Helmets)
    helmet = helmetList[(int(selection) - 1)]
    owned = ownedHelmets[int(selection)-1]
    if owned == False:
        while Helmets[helmet][1] >= currency:
            if(Helmets[helmet][1] <= currency):
                currency -= Helmets[helmet][1]
                owned = True
                return helmet, (int(selection)-1), owned, currency
            if(owned == True):
                return helmet, (int(selection)-1), True, currency
            print(colored(f"\nYou don't have enough coins! You need: {Helmets[helmet][1]} You have: {currency}\n", attrs=["bold"], color="red"))
            selection = input("Select Weapon> ")
            helmet = helmetList[(int(selection) - 1)]
            owned = ownedHelmets[int(selection)-1]
    if owned == False:
        currency -= Helmets[helmet][1]
    owned = True 
    return helmet, (int(selection)-1), owned, currency


def bodyMenu(currency, BodyArmour, ownedBody):
    print(colored("          BODY ARMOUR",attrs=["bold"], color="cyan"), 
          colored('\n+=========================================+\n',attrs=["bold"], color="magenta"),
          colored('        NAME',attrs=["bold"], color="magenta"), "     ",colored('REDUCTION',attrs=["bold"], color="magenta"),"    ",colored('PRICE\n',attrs=["bold"], color="magenta")
          )
    x = 1
    for key,value in BodyArmour.items():
        print(colored("[",attrs=["bold"],color="magenta"),colored(x,attrs=["bold"],color="yellow"),colored("]",attrs=["bold"], color="magenta"),
            (colored(key + "  ",attrs=["bold"], color="green")),"  ", colored(value[0],attrs=["bold"], color="red"),"       ", colored(value[1],attrs=["bold"], color="red"))
        x += 1
    print(colored('\n+============================+\n',attrs=["bold"], color="magenta"))
    selection = input("Select Body Armour> ")
    bodyList = list(BodyArmour)
    body = bodyList[(int(selection) - 1)]
    owned = ownedBody[int(selection)-1]
    if owned == False:
        while BodyArmour[body][1] >= currency:
            if(BodyArmour[body][1] <= currency):
                currency -= BodyArmour[body][1]
                owned = True
                return body, (int(selection)-1), owned, currency
            if(owned == True):
                return body, (int(selection)-1), True, currency
            print(colored(f"\nYou don't have enough coins! You need: {BodyArmour[body][1]} You have: {currency}\n", attrs=["bold"], color="red"))
            selection = input("Select Weapon> ")
            body = bodyList[(int(selection) - 1)]
            owned = ownedBody[int(selection)-1]
    if owned == False:
        currency -= BodyArmour[body][1]
    owned = True 
    return body, (int(selection)-1), owned, currency


def legMenu(currency, LegArmour, ownedLegs):
    print(colored("          LEG ARMOUR",attrs=["bold"], color="cyan"), 
          colored('\n+=========================================+\n',attrs=["bold"], color="magenta"),
          colored('        NAME',attrs=["bold"], color="magenta"), "     ",colored('REDUCTION',attrs=["bold"], color="magenta"),"    ",colored('PRICE\n',attrs=["bold"], color="magenta")
          )
    x = 1
    for key,value in LegArmour.items():
        print(colored("[",attrs=["bold"],color="magenta"),colored(x,attrs=["bold"],color="yellow"),colored("]",attrs=["bold"], color="magenta"),
            (colored(key + "  ",attrs=["bold"], color="green")),"  ", colored(value[0],attrs=["bold"], color="red"),"       ", colored(value[1],attrs=["bold"], color="red"))
        x += 1
    print(colored('\n+============================+\n',attrs=["bold"], color="magenta"))
    selection = input("Select Leg Armour> ")
    legList = list(LegArmour)
    leg = legList[(int(selection) - 1)]
    owned = ownedLegs[int(selection)-1]
    if owned == False:
        while LegArmour[leg][1] >= currency:
            if(LegArmour[leg][1] <= currency):
                currency -= LegArmour[leg][1]
                owned = True
                return leg, (int(selection)-1), owned, currency
            if(owned == True):
                return leg, (int(selection)-1), True, currency
            print(colored(f"\nYou don't have enough coins! You need: {LegArmour[leg][1]} You have: {currency}\n", attrs=["bold"], color="red"))
            selection = input("Select Weapon> ")
            leg = legList[(int(selection) - 1)]
            owned = ownedLegs[int(selection)-1]
    if owned == False:
        currency -= LegArmour[leg][1]
    owned = True 
    return leg, (int(selection)-1), owned, currency


def bootMenu(currency, BootArmour, ownedBoots):
    print(colored("          BODY ARMOUR",attrs=["bold"], color="cyan"), 
          colored('\n+=========================================+\n',attrs=["bold"], color="magenta"),
          colored('        NAME',attrs=["bold"], color="magenta"), "     ",colored('REDUCTION',attrs=["bold"], color="magenta"),"    ",colored('PRICE\n',attrs=["bold"], color="magenta")
          )
    x = 1
    for key,value in BootArmour.items():
        print(colored("[",attrs=["bold"],color="magenta"),colored(x,attrs=["bold"],color="yellow"),colored("]",attrs=["bold"], color="magenta"),
            (colored(key + "  ",attrs=["bold"], color="green")),"  ", colored(value[0],attrs=["bold"], color="red"),"       ", colored(value[1],attrs=["bold"], color="red"))
        x += 1
    print(colored('\n+============================+\n',attrs=["bold"], color="magenta"))
    selection = input("Select Boots> ")
    bootList = list(BootArmour)
    boot = bootList[(int(selection) - 1)]
    owned = ownedBoots[int(selection)-1]
    if owned == False:
        while BootArmour[boot][1] >= currency:
            if(BootArmour[boot][1] <= currency):
                currency -= BootArmour[boot][1]
                owned = True
                return boot, (int(selection)-1), owned, currency
            if(owned == True):
                return boot, (int(selection)-1), True, currency
            print(colored(f"\nYou don't have enough coins! You need: {BootArmour[boot][1]} You have: {currency}\n", attrs=["bold"], color="red"))
            selection = input("Select Weapon> ")
            boot = bootList[(int(selection) - 1)]
            owned = ownedBoots[int(selection)-1]
    if owned == False:
        currency -= BootArmour[boot][1]
    owned = True 
    return boot, (int(selection)-1), owned, currency


def EnemyList():
  print(colored("       ENEMIES",attrs=["bold"], color="cyan"), 
          colored('\n+====================+\n',attrs=["bold"], color="magenta"),
          colored("   [1] ZOMBIE\n",attrs=["bold"], color="yellow"),
          colored("   [2] GHOUL\n",attrs=["bold"], color="yellow"),  
          colored("   [3] GOBLIN\n",attrs=["bold"], color="yellow"), 
          colored("   [4] OGRE\n",attrs=["bold"], color="yellow"),  
          colored("   [5] CYCLOPSE",attrs=["bold"], color="yellow"), 
          colored('\n+====================+\n',attrs=["bold"], color="magenta"))
  enemy = input("> ")
  return enemy