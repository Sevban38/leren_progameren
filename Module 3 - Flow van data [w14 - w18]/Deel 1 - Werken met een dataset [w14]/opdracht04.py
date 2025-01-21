import random
from fruitmand import fruitmand
aantal = int(input("Hoeveel fruitnamen wil je zien? "))
for _ in range(aantal):
    print(random.choice(fruitmand)['name'])
