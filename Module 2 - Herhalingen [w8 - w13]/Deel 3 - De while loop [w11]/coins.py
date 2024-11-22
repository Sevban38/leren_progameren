# naam van de student: Sevban  
# studentnummer: 99081630
# doel van het programma: Het berekenen en teruggeven van het juiste bedrag aan wisselgeld met het minste aantal munten.
# structuur van het programma: Het programma berekent het terug te geven wisselgeld en bepaalt iteratief het aantal munten van elke muntsoort dat moet worden teruggegeven.

muntWaardes = [500, 200, 100, 50, 20, 10, 5, 2, 1] # Lijst van muntwaardes in centen, inclusief 1, 2 en 5-euromunten.

teBetalen = int(float(input('Te betalen bedrag: ')) * 100) # Converteer het te betalen bedrag van euro naar centen.
betaald = int(float(input('Betaald bedrag: ')) * 100) # Converteer het betaalde bedrag van euro naar centen.
wisselgeld = betaald - teBetalen # Bereken het totale wisselgeld dat moet worden teruggegeven.

teruggegevenMunten = {} # Woordenboek om het aantal teruggegeven munten bij te houden.

while wisselgeld > 0 and len(muntWaardes) > 0: # Blijf doorgaan totdat al het wisselgeld is teruggegeven of er geen muntsoorten meer over zijn.
  muntWaarde = muntWaardes.pop(0) # Krijg de hoogste beschikbare muntwaarde.
  aantalMunten = wisselgeld // muntWaarde # Bereken het maximale aantal munten van dit type dat kan worden teruggegeven.

  if aantalMunten > 0: # Als er munten van dit type moeten worden teruggegeven.
    print('Geef maximaal', aantalMunten, 'munten van', muntWaarde, 'cent terug!') # Informeer de gebruiker over het maximale aantal munten dat moet worden teruggegeven.
    aantalTeruggegevenMunten = int(input('Hoeveel munten van ' + str(muntWaarde) + ' cent heb je teruggegeven? ')) # Vraag de gebruiker hoeveel munten van dit type daadwerkelijk zijn teruggegeven.
    if aantalTeruggegevenMunten > aantalMunten:
        print(f"Je kunt niet meer dan {aantalMunten} munten van {muntWaarde} cent teruggeven.")
        aantalTeruggegevenMunten = aantalMunten
    wisselgeld -= aantalTeruggegevenMunten * muntWaarde # Trek de waarde van de teruggegeven munten af van het wisselgeld.
    teruggegevenMunten[muntWaarde] = aantalTeruggegevenMunten # Registreer het aantal teruggegeven munten voor dit munttype.

if wisselgeld > 0: # Als er nog wisselgeld over is om terug te geven.
  print('Niet teruggegeven wisselgeld:', str(wisselgeld) + ' cent') # Informeer de gebruiker dat niet al het wisselgeld is teruggegeven.
else:
  print('Klaar') # Informeer de gebruiker dat al het wisselgeld is teruggegeven.

# Print een samenvatting van alle teruggegeven munten.
print('Samenvatting van teruggegeven munten:')
for munt in sorted(teruggegevenMunten.keys(), reverse=True):
  print(f'{teruggegevenMunten[munt]} munten van {munt} cent')