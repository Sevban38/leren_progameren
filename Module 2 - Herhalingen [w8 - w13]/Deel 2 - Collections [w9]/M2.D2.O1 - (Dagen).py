
dagen_van_de_week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")


print("De dagen van de week zijn:")
for dag in dagen_van_de_week:
    print(dag, end=", " if dag != "zondag" else ".\n")


werkdagen = dagen_van_de_week[:5]
print("\nDe werkdagen zijn:")
for dag in werkdagen:
    print(dag, end=", " if dag != "vrijdag" else ".\n")


weekend = dagen_van_de_week[5:]
print("\nDe weekenddagen zijn:")
for dag in weekend:
    print(dag, end=", " if dag != "zondag" else ".\n")
