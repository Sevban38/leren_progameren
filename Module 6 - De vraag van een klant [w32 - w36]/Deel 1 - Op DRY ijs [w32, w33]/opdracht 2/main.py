from data import smaken, prijzen
from func import bestel_ijsje, print_bon

def main():
    print("Welkom bij de IJssalon!")
    bestelling = bestel_ijsje(smaken, prijzen) #besteling
    print_bon(bestelling, prijzen) #bon

if __name__ == "__main__":
    main()

