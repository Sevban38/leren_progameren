operations = {
    'A': lambda x, y: x + y,
    'B': lambda x, y: x - y,
    'C': lambda x, y: x * y,
    'D': lambda x, y: x / y,
    'E': lambda x: x + 1,
    'F': lambda x: x - 1,
    'G': lambda x: x * 2,
    'H': lambda x: x / 2
}

def perform_operation(choice, n1, n2=None):
    if choice in ['A', 'B', 'C', 'D']:
        return operations[choice](n1, n2)
    elif choice in ['E', 'F', 'G', 'H']:
        return operations[choice](n1)

def main():
    while True:
        print("Wat wilt u doen? ")
        print("A) Getallen optellen")
        print("B) Getallen aftrekken")
        print("C) Getallen vermenigvuldigen")
        print("D) Getallen delen")
        print("E) Getal ophogen")
        print("F) Getal verlagen")
        print("G) Getal verdubbelen")
        print("H) Getal halveren")
        print("I) Stoppen")
        choice = input().upper()
        
        if choice == 'I':
            break
        
        if choice in ['A', 'B', 'C', 'D']:
            n1 = float(input("Voer het eerste getal in: "))
            n2 = float(input("Voer het tweede getal in: "))
        elif choice in ['E', 'F', 'G', 'H']:
            n1 = float(input("Voer het getal in: "))
            n2 = None
        else:
            print("Ongeldige keuze, probeer opnieuw.")
            continue
        
        result = perform_operation(choice, n1, n2)
        print(f"De uitkomst is: {result}")
        
        while True:
            print(f"Wil je wat met de uitkomst ({result}) doen? A) Optellen, B) Aftrekken, C) Vermenigvuldigen, D) Delen, E) Ophogen, F) Verlagen, G) Verdubbelen, H) Halveren of I) Niets?")
            choice = input().upper()
            if choice == 'I':
                break
            
            if choice in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                if choice in ['A', 'B', 'C', 'D']:
                    n2 = float(input("Voer het getal in: "))
                else:
                    n2 = None
                
                result = perform_operation(choice, result, n2)
                print(f"De uitkomst is: {result}")
            else:
                print("Ongeldige keuze, probeer opnieuw.")

main()

