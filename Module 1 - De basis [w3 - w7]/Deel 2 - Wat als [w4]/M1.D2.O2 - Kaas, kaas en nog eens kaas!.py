def main():
    print("Welkom bij het kaas spel!")
    antwoord = input("Is de kaas geel? (ja/nee): ").strip().lower()

    if antwoord == "ja":
        antwoord = input("Zitten er gaten in? (ja/nee): ").strip().lower()
        if antwoord == "ja":
            antwoord = input("Is de kaas belachelijk duur? (ja/nee): ").strip().lower()
            if antwoord == "ja":
                print("De kaas die je in gedachten hebt is Emmenthaler.")
            else:
                print("De kaas die je in gedachten hebt is Leerdammer.")
        else:
            antwoord = input("Is de kaas hard als steen? (ja/nee): ").strip().lower()
            if antwoord == "ja":
                print("De kaas die je in gedachten hebt is Parmigiano Reggiano.")
            else:
                print("De kaas die je in gedachten hebt is Goudse kaas.")
    else:
        antwoord = input("Heeft de kaas een blauwe schimmel? (ja/nee): ").strip().lower()
        if antwoord == "ja":
            antwoord = input("Heeft de kaas een korst? (ja/nee): ").strip().lower()
            if antwoord == "ja":
                print("De kaas die je in gedachten hebt is Bleu de Rochbaron.")
            else:
                print("De kaas die je in gedachten hebt is Foume d'Ambert.")
        else:
            antwoord = input("Heeft de kaas een korst? (ja/nee): ").strip().lower()
            if antwoord == "ja":
                print("De kaas die je in gedachten hebt is Camembert.")
            else:
                print("De kaas die je in gedachten hebt is Mozzarella.")

#niet belangerijk!!
if __name__ == "__main__":
    main()