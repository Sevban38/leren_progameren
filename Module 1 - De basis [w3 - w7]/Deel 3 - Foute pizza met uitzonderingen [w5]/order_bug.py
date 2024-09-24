def vraag_getal(aantal):
    antwoord = input("Voer het " + aantal + " getal in: ")
    getal = int(antwoord)
    return getal

def deel_getallen(a, b):
    return a / b

getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")

if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    resultaat = deel_getallen(getal_1, getal_2)
    print(f"{getal_1} gedeeld door {getal_2} is gelijk aan {resultaat}")