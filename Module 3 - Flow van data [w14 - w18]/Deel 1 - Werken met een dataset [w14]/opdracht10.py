from fruitmand import fruitmand

gesorteerd_fruit = sorted(fruitmand, key=lambda fruit: fruit['weight'], reverse=True)

for fruit in gesorteerd_fruit:
    print(f"{fruit['name']}: {fruit['weight'] / 1000} kg")
