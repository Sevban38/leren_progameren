def bestel_ijsje(smaken, prijzen):
    """Vraagt de klant om een aantal bolletjes en smaken te kiezen."""  # Functie om ijs te bestellen
    gekozen_smaken = []  # Lijst om gekozen smaken op te slaan

    while True:  # Blijft herhalen tot geldig aantal is ingevoerd
        try:
            aantal_bolletjes = int(input("Hoeveel bolletjes ijs wilt u? "))  # Vraagt hoeveel bolletjes
            if aantal_bolletjes < 1:  # Controle of het positief is
                print("Voer een positief aantal in.")
                continue  # Terug naar begin als het fout is
            break  # Stopt de while-loop als invoer goed is
        except ValueError:  # Als er geen getal is ingevoerd
            print("Voer een geldig getal in.")

    for i in range(aantal_bolletjes):  # Herhaal voor elk bolletje
        print("\nBeschikbare smaken:")  # Laat de smakenlijst zien
        for idx, smaak in enumerate(smaken, 1):  # Geeft elke smaak een nummer
            print(f"{idx}. {smaak} - €{prijzen[smaak]:.2f}")  # Print nummer, naam en prijs

        while True:  # Blijft herhalen tot een geldige keuze is gemaakt
            try:
                keuze = int(input(f"Kies de smaak voor bolletje {i + 1}: "))  # Vraagt om smaaknummer
                if 1 <= keuze <= len(smaken):  # Check of nummer in de lijst zit
                    gekozen_smaken.append(smaken[keuze - 1])  # Voeg gekozen smaak toe
                    break  # Verlaat de while-loop als keuze goed is
                else:
                    print("Kies een geldig nummer.")  # Foutmelding bij ongeldig nummer
            except ValueError:  # Als er geen nummer is ingevoerd
                print("Voer een nummer in.")
    
    return gekozen_smaken  # Geeft de lijst met gekozen smaken terug


def print_bon(gekozen_smaken, prijzen):
    """Print een overzicht met alle gekozen smaken en de totaalprijs."""  # Functie om bon te tonen
    print("\n--- Bon ---")  # Print bonkop
    totaal = 0  # Start totaalbedrag op 0

    for i, smaak in enumerate(gekozen_smaken, 1):  # Gaat door alle gekozen smaken
        prijs = prijzen[smaak]  # Haalt prijs van die smaak op
        totaal += prijs  # Telt prijs op bij totaal
        print(f"Bolletje {i}: {smaak} - €{prijs:.2f}")  # Print bolletje met smaak en prijs

    print(f"\nTotaal aantal bolletjes: {len(gekozen_smaken)}")  # Print aantal bolletjes
    print(f"Totaal te betalen: €{totaal:.2f}")  # Print totaalprijs
    print("Bedankt voor uw bestelling!\n")  # Afsluitende boodschap
