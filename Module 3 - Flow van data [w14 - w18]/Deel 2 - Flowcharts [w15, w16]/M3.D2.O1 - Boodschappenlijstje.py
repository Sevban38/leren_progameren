boodschappenlijst = {}

def boodschappenlijstje():
    print("Welkom bij de boodschappenlijst generator!")
    print("Typ 'stop' om te stoppen")
    while True:
        boodschap = input("Voer een boodschap in: ")
        if boodschap == 'stop':
            break
        if boodschap in boodschappenlijst:
            boodschappenlijst[boodschap] += 1
        else:
            boodschappenlijst[boodschap] = 1
    print("Dit is je boodschappenlijstje:")
    for boodschap, aantal in boodschappenlijst.items():
        if aantal > 1:
            print(f"{boodschap} {aantal}x")
        else:
            print(boodschap)
boodschappenlijstje()