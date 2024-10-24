import random


kleuren = ("oranje", "blauw", "groen", "bruin")


aantal_mms = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))


zak_mms = []


for _ in range(aantal_mms):
    zak_mms.append(random.choice(kleuren))


print("Inhoud van de zak met M&M's:", zak_mms)