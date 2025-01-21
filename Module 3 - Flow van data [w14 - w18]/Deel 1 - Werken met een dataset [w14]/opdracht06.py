from fruitmand import fruitmand

print(next(fruit['weight'] for fruit in fruitmand if fruit['name'] == 'appel'))
