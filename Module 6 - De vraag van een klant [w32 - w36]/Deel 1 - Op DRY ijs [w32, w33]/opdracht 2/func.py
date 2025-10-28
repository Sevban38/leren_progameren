def bestel_ijsje(smaken, prijzen):
    """Vraagt de klant om een aantal bolletjes en smaken te kiezen."""
    gekozen_smaken = []

    while True:
        try:
            aantal_bolletjes = int(input("Hoeveel bolletjes ijs wilt u? "))
            if aantal_bolletjes < 1:
                print("Voer een positief aantal in.")
                continue
            break
        except ValueError:
            print("Voer een geldig getal in.")

    for i in range(aantal_bolletjes):
        print("\nBeschikbare smaken:")
        for idx, smaak in enumerate(smaken, 1):
            print(f"{idx}. {smaak} - €{prijzen[smaak]:.2f}")

        while True:
            try:
                keuze = int(input(f"Kies de smaak voor bolletje {i + 1}: "))
                if 1 <= keuze <= len(smaken):
                    gekozen_smaken.append(smaken[keuze - 1])
                    break
                else:
                    print("Kies een geldig nummer.")
            except ValueError:
                print("Voer een nummer in.")
    
    return gekozen_smaken


def print_bon(gekozen_smaken, prijzen):
    """Print een overzicht met alle gekozen smaken en de totaalprijs."""
    print("\n--- Bon ---")
    totaal = 0

    for i, smaak in enumerate(gekozen_smaken, 1):
        prijs = prijzen[smaak]
        totaal += prijs
        print(f"Bolletje {i}: {smaak} - €{prijs:.2f}")

    print(f"\nTotaal aantal bolletjes: {len(gekozen_smaken)}")
    print(f"Totaal te betalen: €{totaal:.2f}")
    print("Bedankt voor uw bestelling!\n")
