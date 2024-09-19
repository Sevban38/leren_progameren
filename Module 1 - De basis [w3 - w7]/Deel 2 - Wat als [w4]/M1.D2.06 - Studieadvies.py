# stellingen 
STELLINGEN = [
    "Ik werk altijd hard",
    "Ik ben vaak op tijd",
    "Ik doe regelmatig mijn huiswerk",
    "Ik ben soms afgeleid",
    "Ik maak nooit fouten"
]

COMPETENTIE_ADVIES_ZORGELIJK = "Zorgelijk"
COMPETENTIE_ADVIES_TWIJFELACHTIG = "Twijfelachtig"
COMPETENTIE_ADVIES_GERUSTSTELLEND = "Geruststellend"

def get_user_input(statement):
    while True:
        try:
            answer = int(input(f"{statement}\n0: altijd\n1: vaak\n2: regelmatig\n3: soms\n4: nooit\n"))
            if answer in [0, 1, 2, 3, 4]:
                return answer
            else:
                print("Ongeldige invoer. Probeer het opnieuw.")
        except ValueError:
            print("Ongeldige invoer. Probeer het opnieuw.")

def main():
    total_score = 0
    for statement in STELLINGEN:
        total_score += get_user_input(statement)
    
    average_score = total_score / len(STELLINGEN)
    
    if average_score <= 2:
        advies = COMPETENTIE_ADVIES_ZORGELIJK
    elif average_score <= 3:
        advies = COMPETENTIE_ADVIES_TWIJFELACHTIG
    else:
        advies = COMPETENTIE_ADVIES_GERUSTSTELLEND
    
    print(f"Je gemiddelde score is: {average_score:.2f}")
    print(f"Advies: {advies}")

if __name__ == "__main__":
    main()