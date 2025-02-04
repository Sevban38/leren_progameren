boodschappenlijst = {}

while True:
    artikel = input("Welk artikel wilt u toevoegen? ").strip().lower()
    try:
        aantal = int(input(f"Hoeveel {artikel} wilt u toevoegen? "))
    except ValueError:
        print("Ongeldige invoer. Voer een getal in voor het aantal.")
        continue

    if artikel in boodschappenlijst:
        boodschappenlijst[artikel] += aantal
        print(f"Het aantal {artikel} is bijgewerkt naar {boodschappenlijst[artikel]}.")
    else:
        boodschappenlijst[artikel] = aantal
        print(f"{artikel} is toegevoegd aan de lijst met {aantal} stuks.")

    keuze = input("Wilt u nog meer boodschappen toevoegen? (ja/nee) ").strip().lower()
    if keuze != "ja":
        break

print("\nUw boodschappenlijst:")
for artikel, aantal in boodschappenlijst.items():
    print(f"- {artikel}: {aantal} stuks")
