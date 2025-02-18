from functions import get_all_primes, get_n_primes, get_primes_between, is_prime

def main():
    print("Kies een functie:")
    print("1: Controleer of een getal een priemgetal is")
    print("2: Alle priemgetallen tot een bepaald getal")
    print("3: De eerste N priemgetallen")
    print("4: Priemgetallen tussen twee getallen")
    
    choice = input("Voer het nummer van de gewenste functie in: ")
    
    if choice == "1":
        num = int(input("Voer een getal in: "))
        result = is_prime(num)
        print(f"{num} is een priemgetal." if result else f"{num} is geen priemgetal.")
    elif choice == "2":
        n = int(input("Voer het maximum getal in: "))
        primes = get_all_primes(n)
        print("Gevonden priemgetallen:", primes if primes else "Geen priemgetallen gevonden.")
    elif choice == "3":
        n = int(input("Voer het aantal priemgetallen in: "))
        primes = get_n_primes(n)
        print("De eerste", n, "priemgetallen zijn:", primes)
    elif choice == "4":
        start = int(input("Voer het begingetal in: "))
        end = int(input("Voer het eindgetal in: "))
        primes = get_primes_between(start, end)
        print(f"Priemgetallen tussen {start} en {end}:", primes if primes else "Geen priemgetallen gevonden.")
    else:
        print("Ongeldige keuze.")

if __name__ == "__main__":
    main()
