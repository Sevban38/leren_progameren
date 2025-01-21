from fruitmand import fruitmand

beschikbare_kleuren = {fruit['color'] for fruit in fruitmand}

while True:
   
    gekozen_kleur = input(f"Kies een kleur uit {', '.join(beschikbare_kleuren)}: ").lower()
    
    
    if gekozen_kleur not in beschikbare_kleuren:
        print(f"De kleur {gekozen_kleur} zit er niet in de fruitmand")
        continue

    
    geselecteerd_fruit = [fruit for fruit in fruitmand if fruit['color'] == gekozen_kleur]

   
    ronde_vruchten = sum(1 for fruit in geselecteerd_fruit if fruit['round'])
    niet_ronde_vruchten = len(geselecteerd_fruit) - ronde_vruchten

    
    if ronde_vruchten > niet_ronde_vruchten:
        verschil = ronde_vruchten - niet_ronde_vruchten
        print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
    elif ronde_vruchten < niet_ronde_vruchten:
        verschil = niet_ronde_vruchten - ronde_vruchten
        print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
    else:
        print(f"Er zijn {ronde_vruchten} ronde vruchten en {niet_ronde_vruchten} niet ronde vruchten in de kleur {gekozen_kleur}")
    break
