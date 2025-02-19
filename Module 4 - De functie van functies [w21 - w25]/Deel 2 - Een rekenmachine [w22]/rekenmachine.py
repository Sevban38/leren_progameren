from functions import *

def main():
  while True:
    print("Wat wilt u doen? ")
    print("A getallen optellen")
    print("B getallen aftrekken")
    print("C getallen vermenigvuldigen")
    print("D getallen delen")
    print("E getal ophogen")
    print("F getal verlagen")
    print("G getal verdubbelen")
    print("H getal halveren")
    print("I stoppen")
    choice = input().upper()

    if choice in ['A', 'B', 'C', 'D']:
      print("Voer het eerste getal in:")
      n1 = float(input())
      print("Voer het tweede getal in:")
      n2 = float(input())
    else:
      print("Voer het getal in:")
      n1 = float 
      n2 = None

    result = perform_operation(choice, n1,n2)
    print(f"De uitkomst is: {result}")

    if choice == 'I':
      break

    n1 = result

main()