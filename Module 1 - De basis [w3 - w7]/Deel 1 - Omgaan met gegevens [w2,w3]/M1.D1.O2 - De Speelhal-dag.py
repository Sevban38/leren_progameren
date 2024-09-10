from termcolor import colored, cprint, COLORS


vrienden = 4

ticket_kosten = 7.45

spelduur = 45

spel_kosten_per_minuut = 0.37 / 5

totale_kosten = (vrienden * ticket_kosten) + (vrienden * (spelduur / 5) * spel_kosten_per_minuut)

print(f"De totale kosten voor dit geweldige uitje naar de speelhal is: {colored(totale_kosten, "red")} euro.")