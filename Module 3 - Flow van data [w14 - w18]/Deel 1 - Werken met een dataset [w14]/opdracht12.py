from fruitmand import fruitmand

kleur_vertaling = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin',
}

langste_naam_fruit = max(fruitmand, key=lambda fruit: len(fruit['name']))

naam = langste_naam_fruit['name']
kleur = kleur_vertaling[langste_naam_fruit['color']]
gewicht = langste_naam_fruit['weight'] / 1000  

print(f"De {naam} heeft een {kleur} kleur en een gewicht van {gewicht} kg.")
