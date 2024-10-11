import time, math
import random

player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(3)

# === [kamer 2] === #
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
    print('Het standbeeld laat de sleutel vallen en je pakt het op')
    items = ['sleutel']
else:
    print('Er gebeurt niets....')
    print('Je probeert het nog een keer.')
    antwoord = int(input('Wat toets je in?'))
    if antwoord == eval(f'{num1} {operator} {num2}'):
        print('Het standbeeld laat de sleutel vallen en je pakt het op')
        items = ['sleutel']
    else:
        print('Er gebeurt niets....')
        print('Je probeert het nog een keer.')
        antwoord = int(input('Wat toets je in?'))
        if antwoord == eval(f'{num1} {operator} {num2}'):
            print('Het standbeeld laat de sleutel vallen en je pakt het op')
            items = ['sleutel']
        else:
            print('Er gebeurt niets....')
            print('dit was je laatste kans.')
            items = []

print('Je ziet een deur achter het standbeeld.')
print('')
time.sleep(3)

# === [kamer 3] === #
item = random.choice(items) if items else None
schild = "schild"
if item == 'schild':
    player_defense += 1
else:
    player_attack += 2

print('Je duwt hem open en stapt een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {schild}.')
if item:
    print(f'Je pakt het {schild} op en houdt het bij je.')
    items.append(schild)
print('Op naar de volgende deur.')
print('')
time.sleep(3)

# === [kamer 4] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.') 

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        player_health -= player_attack_amount * zombie_hit_damage
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(2)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

time.sleep(2)

if item == 'sleutel':
    print('Je hebt de sleutel en opent de schatkist.')
    print('Gefeliciteerd, je hebt het spel gewonnen!')
else:
    print('Je hebt geen sleutel om de schatkist te openen.')
    print('Helaas, je verliest het spel.')