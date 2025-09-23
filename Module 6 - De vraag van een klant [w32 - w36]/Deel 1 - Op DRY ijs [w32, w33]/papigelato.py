def stap1():
    while True:
        try:
            aantal = int(input("Hoeveel bolletjes wilt u? ")) 
            if 1 <= aantal <= 3:
                return aantal, None  # naar stap2
            elif 4 <= aantal <= 8:
                print(f"Dank, krijgt u van mij een bakje met {aantal} bolletjes.") 
                return aantal, "bakje"  # direct naar stap3
            elif aantal > 8:
                print("Sorry, zulke grote bakken hebben we niet.") #als het boven 8 is
            else:
                print("Sorry dat snap ik niet...") #ongeldige antwoorden
        except ValueError:
            print("Sorry dat snap ik niet...")


def stap2(aantal):
    while True:
        keuze = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ").lower()
        if keuze in ["hoorntje", "hoorn", "bak", "bakje"]: #de geldige keuzes
            return keuze
        else:
            print("Sorry, dat snap ik niet...") #voor ongeldige antwoorden


def stap3(aantal, verpakking): #de laatste stap
    print(f"Hier is uw {verpakking} met {aantal} bolletje(s).")
    while True:
        meer = input("Wilt u nog meer bestellen? ").lower()
        if meer == "ja":
            return True
        elif meer == "nee":
            print("Bedankt en tot ziens!")
            return False
        else:
            print("Sorry, dat snap ik niet...")


def main(): #main functie met alles erin
    print("Welkom bij Papi Gelato je mag alles maken kiezen zolang het maar vanille ijs is.")
    while True:
        aantal, verpakking = stap1()
        if not verpakking:  
            verpakking = stap2(aantal)
        doorgaan = stap3(aantal, verpakking)
        if not doorgaan:
            break


main()