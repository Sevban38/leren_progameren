# Vraag de gebruiker om de naam van de gastheer
gastheer = input("Wie is de gastheer? ")

# namen van student (ik) en slb'er
mijn_naam = "Sevban"
slb_naam = "Eugene"

# Controleer of er een gastheer is
is_gastheer = bool(gastheer)

# Vraag de gebruiker om het aantal gasten
try:
    gasten = int(input("Hoeveel gasten zijn er? "))
except ValueError:
    gasten = 0

print(gasten)
drank = True
chips = True

# Een feest moet minimaal gasten of een gastheer hebben
start_condition_1 = is_gastheer or gasten > 0

# Het feest kan alleen beginnen als de gastheer er is tenzij er gasten chips en drank zijn
start_condition_2 = is_gastheer or (gasten > 0 and chips and drank)

# Een feest met chips maar zonder drank kan niet beginnen
start_condition_3 = not (chips and not drank)

# Een feest met gasten kan niet beginnen als er geen chips en geen drank is
start_condition_4 = not (gasten > 0 and not (chips or drank))

# Een gastheer kan een feest geven zonder chips en gasten maar niet zonder drank
start_condition_5 = not (is_gastheer and not drank)

# Alleen chips is geen feest
start_condition_6 = not (chips and not (is_gastheer or gasten > 0 or drank))

# Nieuwe voorwaarden:
# Een feest met gasten kan pas beginnen als er minimaal 4 gasten zijn
start_condition_7 = gasten >= 4 or gasten == 0

# Een feest kan niet starten als er meer dan 20 aanwezigen zijn
start_condition_8 = gasten <= 20

# Controleer naam gastheer
special_condition_1 = gastheer == mijn_naam
special_condition_2 = gastheer == slb_naam

if (special_condition_1 or 
    (not special_condition_2 and gasten > 0 and start_condition_1 and start_condition_2 and 
     start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6 and
        start_condition_7 and start_condition_8)):
    print('Start the Party')
else:
    print('No Party')
