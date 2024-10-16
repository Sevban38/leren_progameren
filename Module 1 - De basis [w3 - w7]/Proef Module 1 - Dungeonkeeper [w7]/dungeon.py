import time, math
import random
import sys
import math

# Functie om gevechten te simuleren
def fight(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health):
    enemy_hit_damage = (enemy_attack - player_defense)
    if enemy_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de vijand, hij kan je geen schade doen.')
        return player_health
    else:
        enemy_attack_amount = math.ceil(player_health / enemy_hit_damage)
        
        player_hit_damage = (player_attack - enemy_defense)
        player_attack_amount = math.ceil(enemy_health / player_hit_damage)

        if player_attack_amount < enemy_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de vijand.')
            player_health -= player_attack_amount * enemy_hit_damage
            print(f'Je health is nu {player_health}.')
            return player_health
        else:
            print('Helaas is de vijand te sterk voor je.')
            print('Game over.')
            sys.exit()

item = []
player_attack = 1
player_defense = 0
player_health = 3


# === [kamer 1] === #
def kamer1(): 
    print('Door de twee grote deuren loop je een gang binnen.')
    print('Het ruikt hier muf en vochtig.')
    print('Je ziet een deur voor je.')
    print('')
    time.sleep(3)
    kamer7()

# === [kamer 7] === #
def kamer7():

    print('Je opent de deur en ziet een grote kamer voor je.')
    print('In het midden van de kamer zie je een grote tafel staan.')
    chance = random.randint(1, 10)

    if chance == 1:
        print('Helaas, er ligt geen rupee op de tafel.')
    else:
        print('Op de tafel ligt een rupee.')
        print('Je pakt de rupee op en stopt hem in je zak.')
        item.append('rupee')

    time.sleep(3)

    print('Wil je naar kamer 2 of kamer 8?')
    keuze = input('Typ "2" voor kamer 2 of "8" voor kamer 8: ')
    if keuze == '2':
        kamer2()
    elif keuze == '8':
        kamer8()


def kamer2():
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    print('Daarboven zie je een som staan.')

    # Generate random numbers and operator for the math problem
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    operator = random.choice(['+', '-', '*'])

    print(f'Wat is de uitkomst van {num1} {operator} {num2}?')
    antwoord = int(input('Wat toets je in?'))

    if antwoord == eval(f'{num1} {operator} {num2}'):
        print('Het standbeeld laat de rupee vallen en je pakt het op')
        item.append('rupee')
    print('Wil je naar kamer 6 of kamer 8?')
    keuze = input('Typ "6" voor kamer 6, "8" voor kamer 8: ')
    if keuze == '6':
        kamer6()
    elif keuze == '8':
        kamer8()

def kamer6():
    global player_attack, player_defense, player_health
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    print(f'je loopt kamer in en ziet een zombie voor je.')
    print('Hij valt je opnieuw aan.')

    player_health = fight(player_attack, player_defense, player_health, zombie_attack, zombie_defense, zombie_health)
    
    
    print('')
    time.sleep(2)
    keuze = input('wilt uw naar kamer 3 of kamer 8?')
    if keuze == '3':
        kamer3()
    elif keuze == '8':
        kamer8()


def kamer8():
    global player_health
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print (f'Je hebt {dice1} en {dice2} gegooid. Het totaal is {total}.')
    if total > 7:
        print('Je hebt gewonnen! Het aantal rupees dat je hebt is verdubbeld.')
        rupee_count=item.count('rupee')
                
        for i in range (rupee_count):
            item.append('rupee')
        player_health += 4
    elif total < 7:
        print('Je hebt verloren! Je verliest 1 health.')
        player_health -= 1
    else:
        print('Je hebt gelijk gespeeld! Je krijgt 1 rupee en 4 health.')
        item.append('rupee')
        player_health += 4

    if player_health <= 0:
        print('Je hebt het spel verloren.')
        sys.exit()

    print('')
    time.sleep(2)
    keuze = input ('Wil je naar kamer 9 of kamer 3?')
    if keuze == '9':
        kamer9()
    elif keuze == '3':
        kamer3()



# === [kamer 9] === #
def kamer9():
    global player_defense, player_health
    enchantment = random.choice(['defense', 'health'])
    if enchantment == 'defense':
        player_defense += 1
        print('Je voelt een betovering en je verdediging wordt versterkt.')
    elif enchantment == 'health':
        player_health += 2
        print('Je voelt een betovering en je gezondheid wordt versterkt.')
   
    print('')
    time.sleep(2)
    kamer3()

# === [kamer 3] === #
def kamer3():
    global player_attack, player_defense, player_health, item, rupee_count
    item_choice = ''
    print('Je komt vanuit kamer 2 en ziet een deur naar kamer 6.')
    print('Je ziet ook een deur naar kamer 4.')
    print('')
    print('Welkom bij het verkooppunt!')
    print('Je hebt', len(item), 'rupee(s) en kunt een item kopen.')
    print('Beschikbare items:')
    wantstobuy = True
    rupee_count = item.count('rupee')

    while wantstobuy == True: 
        if rupee_count >= 1:
            print('0. nee ik wil niks kopen')
            print('--------------------------------')
            if 'zwaard' not in item:
                print('1. Zwaard (+2 player damage)')
            print ('--------------------------------')
            if 'bijl' not in item:
                print('2. Bijl (+3 player damage)')
            print ('--------------------------------')
            if 'schild' not in item:
                print('3. Schild (+2 player defense)')
            print ('--------------------------------')
            if 'sleutel' not in item:
                print('4. Sleutel voor de schatkist')
            
            item_choice = input('Typ het nummer van het item dat je wilt kopen: ')

            if item_choice == '1' and 'zwaard' not in item:
                print('Je hebt een zwaard gekocht!')
                player_attack += 2
                item.append('zwaard')
                item.remove ('rupee')
                rupee_count -= 1
            elif item_choice == '2' and 'bijl' not in item:
                print('Je hebt bijl gekozen')
                player_attack += 3
                item.append('bijl')
                item.remove ('rupee')
                rupee_count -= 1
            elif item_choice == '3' and 'schild' not in item:
                print('Je hebt schild gekozen')
                player_defense += 2 
                item.append('schild')
                item.remove ('rupee')
                rupee_count -= 1
            elif item_choice == '4' and 'sleutel' not in item:
                print('Je hebt de sleutel voor de schatkist gekocht!')
                item.append('sleutel')
                item.remove ('rupee')
                rupee_count -= 1
            elif item_choice == '0':
                print ("je wilt niks kopen u gaat door.")
                wantstobuy = False
            else:
                print('Ongeldige keuze. Het spel eindigt hier.')
                sys.exit()
        else: 
            print('Je hebt geen rupees meer om items te kopen.')
            wantstobuy = False

    print('Op naar de volgende deur.')
    print('')
    time.sleep(3)
    kamer4()

# === [kamer 4] === #
def kamer4():
    global player_health, player_attack, player_defense 
    new_enemy_attack = 2
    new_enemy_defense = 0
    new_enemy_health = 3
    print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
    print('Je loopt tegen een nieuwe vijand aan.') 

    player_health = fight(player_attack, player_defense, player_health, new_enemy_attack, new_enemy_defense, new_enemy_health)

    print('')
    time.sleep(2)
    kamer5()

# === [kamer 5] === #
def kamer5():
    global item 
    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')

    time.sleep(2)

    if 'sleutel' in item:
        print('Je hebt de sleutel en opent de schatkist.')
        print('Gefeliciteerd, je hebt het spel gewonnen!')
    else:
        print('Je hebt geen sleutel om de schatkist te openen.')
        print('Helaas, je verliest het spel.')
kamer1()