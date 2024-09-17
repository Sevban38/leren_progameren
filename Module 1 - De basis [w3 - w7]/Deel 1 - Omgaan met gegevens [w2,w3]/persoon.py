# persoon.py

def main():
    # Vraag de gebruiker om zijn gegevens
    naam = input("Voer uw naam in: ")
    adres = input("Voer uw adres in: ")
    postcode = input("Voer uw postcode in: ")
    woonplaats = input("Voer uw woonplaats in: ")

    # de adreskaart
    print(" ----------------------------------------------------")
    print(f"|  Naam      : {naam:<35}|")
    print(f"|  Adres     : {adres:<35}|")
    print(f"|  Postcode  : {postcode:<35}|")
    print(f"|  Woonplaats: {woonplaats:<35}|")
    print(" ----------------------------------------------------")

if __name__ == "__main__":
    main()