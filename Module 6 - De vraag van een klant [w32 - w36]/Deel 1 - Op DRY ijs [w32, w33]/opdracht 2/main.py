from data import smaken, prijzen
from func import bestel_ijsje, print_bon

def main():
    print("Welkom bij de IJssalon!")
    bestelling = bestel_ijsje(smaken, prijzen)
    print_bon(bestelling, prijzen)

if __name__ == "__main__":
    main()
