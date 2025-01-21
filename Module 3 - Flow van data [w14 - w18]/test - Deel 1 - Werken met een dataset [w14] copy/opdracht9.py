from fruitmand import fruitmand

fruitmand = [fruit for fruit in fruitmand if fruit['name'] != 'druif']

kleuren = {fruit['color'] for fruit in fruitmand}

print("\n".join(kleuren))
