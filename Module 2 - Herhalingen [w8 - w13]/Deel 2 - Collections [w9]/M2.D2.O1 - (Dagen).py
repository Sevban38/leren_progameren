
dagen_van_de_week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("De dagen van de week zijn:")
for dag in dagen_van_de_week:
    print('-', dag)

print("\nDe werkdagen zijn:", end=" ")
werkdagen = dagen_van_de_week[:5]
for dag in werkdagen:
    print(dag, end=" ")
print ('\n')
print("\nDe weekenddagen zijn:", end=" ")
weekend = dagen_van_de_week[5:]
for dag in weekend:
    print(dag, end=" ")
print ('\n')
print("\nDe dagen van de week omgekeerd:", end=" ")
for dag in reversed(dagen_van_de_week):
    print(dag, end=" ")
print ('\n')

print("\nDe werkdagen van vrijdag tot maandag zijn:")
werkdagen_omgekeerd = dagen_van_de_week[4::-1]
for dag in werkdagen_omgekeerd:
    print(dag)

print("\nDe weekenddagen omgekeerd zijn:", end=" ")
weekend_omgekeerd = dagen_van_de_week[6:4:-1]
for dag in weekend_omgekeerd:
    print(dag, end=" ")
print('\n')