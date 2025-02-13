import random

def vraag_namen():
    namen = set()  # Set om unieke namen te garanderen
    while len(namen) < 3:
        naam = input(f"Voer een unieke naam in ({len(namen) + 1}): ").strip()
        if naam in namen:
            print("Deze naam is al ingevoerd. Probeer opnieuw.")
        else:
            namen.add(naam)
    
    while True:
        extra_naam = input("Wil je nog een extra naam toevoegen? (ja/nee): ").strip().lower()
        if extra_naam == 'ja':
            naam = input("Voer een extra unieke naam in: ").strip()
            if naam in namen:
                print("Deze naam is al ingevoerd. Probeer opnieuw.")
            else:
                namen.add(naam)
        elif extra_naam == 'nee':
            break
        else:
            print("Ongeldige invoer. Typ 'ja' of 'nee'.")
    
    return list(namen)

def trek_lootjes(namen):
    lootjes = namen[:]
    random.shuffle(lootjes)
    
    while any(namen[i] == lootjes[i] for i in range(len(namen))):
        random.shuffle(lootjes)
    
    return dict(zip(namen, lootjes))

def main():
    print("Welkom bij het lootjes-trek-programma!")
    namen = vraag_namen()
    lootjes_resultaat = trek_lootjes(namen)
    
    print("\nDe lootjes zijn getrokken!")
    
    while True:
        zoek_naam = input("\nVoer een naam in om het bijbehorende lootje te zien (of typ 'stop' om te stoppen): ").strip()
        if zoek_naam == 'stop':
            break
        elif zoek_naam in lootjes_resultaat:
            lootje = lootjes_resultaat[zoek_naam]
            print(f"{zoek_naam} heeft {lootje} getrokken.")
        else:
            print("Deze naam is niet gevonden. Probeer opnieuw.")

main()
