from menus import *
from classes import *
from rich.console import Console 
from time import sleep
import random
console = Console()


player = Character()
weapon = Weapon('Broken Sword', 1)
launch = True
player.defense = 0
ownedWeapons = [True, False, False, False]
ownedHelmets = [False, False, False, False, False, True]
ownedBody = [False, False, False, False, False, True]
ownedLegs = [False, False, False, False, False, True]
ownedBoots = [False, False, False, False, False, True]

while launch == True:
    selection = StartMenu(player.level)
    player.hp = 5
    
    if selection == '1':
        enemy = EnemyList()
        if enemy == '1':
            enemy = Enemy('Zombie', 3, 50, random.randint(1, 2), 100)
        elif enemy == '2':
            enemy = Enemy('Ghoul', 5, 70, random.randint(2, 3), 200)
        elif enemy == '3':   
            enemy = Enemy('Goblin', 7, 100, random.randint(3, 5), 250)
        elif enemy == '4':
            enemy = Enemy('Ogre', 10, 125, random.randint(5, 7), 300)
        elif enemy == '5':
            enemy = Enemy('Cyclopse', 15, 150, random.randint(7, 10), 350)
        while True:
            player.attack(enemy, weapon, player)
            if enemy.hp <= 0:
                break
            enemy.attack(enemy, player)
            if player.hp <= 0:
               break
        player.conclusion(player, enemy)


    elif selection == '2' and player.level >= 2:
        shop = ShopMenu()
        if shop == '1':
            weaponSwitcher = {
                'Broken Sword  ': [1, 0],
                'Short Sword   ': [2, 1000],
                'Long Sword    ': [3, 2000],
                'Straight Sword': [4, 3000]
                }

            sword, num, owned, player.currency = WeaponsList(player.currency, weaponSwitcher, ownedWeapons)
            weapon = Weapon(list(weaponSwitcher.keys())[list(weaponSwitcher.values()).index(weaponSwitcher.get(sword))], weaponSwitcher[sword][0])
            ownedWeapons[num] = owned
            
            

        if shop == '2':
            helmetSwitcher = {
                'Leather  ' : [1, 500],
                'Wood     ' : [2, 1000],
                'Aluminium' : [3, 2000],
                'Bronze   ' : [4, 3000],
                'Titanium ' : [8, 4000],
                'None     ' : [0, 0]
            }
            if (player.helmet): # Checks if player has helmet is True
                player.helmet = False
                player.defense -= helmet.reduction
        
            helmet, num, owned, player.currency = HelmetMenu(player.currency, helmetSwitcher, ownedHelmets)
            helmet = Helmets(list(helmetSwitcher.keys())[list(helmetSwitcher.values()).index(helmetSwitcher.get(helmet))], helmetSwitcher[helmet][0])
            ownedHelmets[num] = owned
            if (helmet): # Checks if player has helmet is True
                player.helmet = True
                player.defense += helmet.reduction
                
        if shop == '3':
            bodySwitcher = {
                'Leather  ' : [1, 500],
                'Wood     ' : [2, 1000],
                'Aluminium' : [3, 2000],
                'Bronze   ' : [4, 3000],
                'Titanium ' : [8, 4000],
                'None     ' : [0, 0]
            }
            if (player.bodyArmour): # Checks if player has body armour is True
                player.bodyArmour = False
                player.defense -= body_armour.reduction

            body_armour, num, owned, player.currency = bodyMenu(player.currency, bodySwitcher, ownedBody)
            body_armour = BodyArmour(list(bodySwitcher.keys())[list(bodySwitcher.values()).index(bodySwitcher.get(body_armour))], bodySwitcher[body_armour][0])
            ownedBody[num] = owned

            if (body_armour): # Checks if player has body armour is True
                player.bodyArmour = True
                player.defense += body_armour.reduction

        if shop == '4':
            legSwitcher = {
                'Leather  ' : [1, 500],
                'Wood     ' : [2, 1000],
                'Aluminium' : [3, 2000],
                'Bronze   ' : [4, 3000],
                'Titanium ' : [8, 4000],
                'None     ' : [0, 0]
            }
            if (player.legArmour): # Checks if player has body armour is True
                player.legArmour = False
                player.defense -= leg_armour.reduction

            leg_armour, num, owned, player.currency = legMenu(player.currency, legSwitcher, ownedLegs)
            leg_armour = LegArmour(list(legSwitcher.keys())[list(legSwitcher.values()).index(legSwitcher.get(leg_armour))], legSwitcher[leg_armour][0])
            ownedLegs[num] = owned

            if (leg_armour): # Checks if player has body armour is True
                player.legArmour = True
                player.defense += leg_armour.reduction

        if shop == '5':
            bootSwitcher = {
                'Leather  ' : [1, 500],
                'Wood     ' : [2, 1000],
                'Aluminium' : [3, 2000],
                'Bronze   ' : [4, 3000],
                'Titanium ' : [8, 4000],
                'None     ' : [0, 0]
            }
            if (player.boots): # Checks if player has body armour is True
                player.boots = False
                player.defense -= boots.reduction 
            boots, num, owned, player.currency = bootMenu(player.currency, bootSwitcher, ownedBoots)
            boots = Boots(list(bootSwitcher.keys())[list(bootSwitcher.values()).index(bootSwitcher.get(boots))], bootSwitcher[boots][0])
            ownedBoots[num] = owned


            if (boots): # Checks if player has body armour is True
                player.boots = True
                player.defense += boots.reduction





    elif selection == '3':
        launch = False
