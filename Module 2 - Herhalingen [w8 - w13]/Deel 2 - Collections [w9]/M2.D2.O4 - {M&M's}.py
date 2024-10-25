import random

kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']

aantal_mnms = int(input("Hoeveel M&M's moeten er in de zak toegevoegd worden? "))

zak_met_mnms = {}


for _ in range(aantal_mnms):
    kleur = random.choice(kleuren)
    if kleur in zak_met_mnms:
        zak_met_mnms[kleur] += 1
    else:
        zak_met_mnms[kleur] = 1


print("Inhoud van de zak met M&M's:", zak_met_mnms)
