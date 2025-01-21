from fruitmand import fruitmand

totaal_gewicht = sum(fruit['weight'] for fruit in fruitmand)
print(f"Totaal gewicht van de fruitmand: {totaal_gewicht} gram")

fruitmand.append({
    'name': 'watermeloen',
    'weight': 4000,
    'color': 'green',
    'round': True
})

totaal_gewicht = sum(fruit['weight'] for fruit in fruitmand)
print(f"Totaal gewicht na toevoegen van watermeloen: {totaal_gewicht} gram")
