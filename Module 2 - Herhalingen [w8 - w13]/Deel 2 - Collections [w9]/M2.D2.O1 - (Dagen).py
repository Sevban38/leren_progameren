
dagen_van_de_week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("De dagen van de week zijn:")
for dag in dagen_van_de_week:
    print('-', dag)

print("\nDe werkdagen zijn:")
werkdagen = dagen_van_de_week[:5]
for dag in werkdagen:
    print(dag)

print("\nDe weekenddagen zijn:")
weekend = dagen_van_de_week[5:]
for dag in weekend:
    print(dag)

print("\nDe dagen van de week omgekeerd:")
for dag in reversed(dagen_van_de_week):
    print(dag)

print("\nDe werkdagen van vrijdag tot maandag zijn:")
werkdagen_omgekeerd = dagen_van_de_week[4::-1]
for dag in werkdagen_omgekeerd:
    print(dag)

print("\nDe weekenddagen omgekeerd zijn:")
weekend_omgekeerd = dagen_van_de_week[6:4:-1]
for dag in weekend_omgekeerd:
    print(dag)
