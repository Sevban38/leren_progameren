croissantjes = int(input("Hoeveel croissantjes wil je kopen? "))
croissant_price = float(input("Wat is de prijs van een croissantje? "))

stokbroden = int(input("Hoeveel stokbroden wil je kopen? "))
stokbrood_price = float(input("Wat is de prijs van een stokbrood? "))

kortingsbonnen = int(input("Hoeveel kortingsbonnen heb je? "))
kortingsbon_value = float(input("Wat is de waarde van een kortingsbon? "))

total_cost = (croissantjes * croissant_price) + (stokbroden * stokbrood_price) - (kortingsbonnen * kortingsbon_value)

print(f"De totale prijs is: {total_cost} euro")



vrienden = int(input("Hoeveel vrienden gaan er mee? "))

ticket_kosten = float(input("Wat is de prijs van een ticket? "))

spelduur = int(input("Hoeveel minuten duurt het spel? "))

spel_kosten_per_minuut = float(input("Wat zijn de kosten per minuut voor het spel? ")) / 5

totale_kosten = (vrienden * ticket_kosten) + (vrienden * (spelduur / 5) * spel_kosten_per_minuut)

print(f"De totale kosten voor dit geweldige uitje naar de speelhal is: {totale_kosten} euro.")