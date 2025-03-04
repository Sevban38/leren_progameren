import random

rondes = 0
geradengetalen = []
kansen = 0
geheimgetal = random.randint(1, 100)
while True:
    try:
        geradengetal = int(input("Geef een getal: "))
    except ValueError:
        print("Ongeldige invoer. Voer een getal in.")
        continue
    if geradengetal == geheimgetal:
        print("Gefeliciteerd, je hebt het getal geraden!")
        print(f"Het geheime getal was {geheimgetal}.")
        break
        rondes += 1
    else: 
        geradengetalen.append(geradengetal)
    kansen += 1
    if kansen == 20:
        print("De getallen die je geraden hebt zijn: " + ', '.join(map(str, geradengetalen)))
        print(f"Je hebt het getal niet geraden. Het geheime getal was {geheimgetal}.")
        break
        rondes += 1

