from termcolor import colored, cprint, COLORS

croissantjes = 17
croissant_price = 0.39


stokbroden = 2
stokbrood_price = 2.78


kortingsbonnen = 3
kortingsbon_value = 0.50


total_cost = (croissantjes * croissant_price) + (stokbroden * stokbrood_price) - (kortingsbonnen * kortingsbon_value)


print(f"de totale prijs is: {colored(total_cost, "red")} euro")  
