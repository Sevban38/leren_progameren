PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

# Start van het programma
leeftijd = int(input("Hoe oud ben je? "))

if leeftijd < 18:
    print("Sorry, je mag niet naar binnen.")
else:
    naam = input("Wat is je naam? ").strip().lower()
    vip = naam in VIP_LIST
    
    if leeftijd >= 21:
        print("Je krijgt van mij een stempel.")
    else:
        print("Je krijgt van mij een blauw bandje.")
    
    while True:
        drankje = input("Wat wil je drinken? (cola, bier, champagne) ").strip().lower()
        
        if drankje not in DRANKJES:
            print("Sorry, geen idee wat je bedoelt. Probeer opnieuw.")
        elif drankje == "champagne" and not vip:
            print("Sorry, alleen VIP's mogen champagne bestellen. Kies iets anders.")
        elif drankje == "bier" and leeftijd < 21:
            print("Sorry, je mag geen alcohol bestellen onder de 21. Kies iets anders.")
        else:
            if drankje == "cola":
                prijs = PRIJS_COLA
            elif drankje == "bier":
                prijs = PRIJS_BIER
            elif drankje == "champagne":
                prijs = PRIJS_CHAMPAGNE
            
            print(f"Alstublieft, je {drankje}. Dat is €{prijs:.2f}.")
            break
