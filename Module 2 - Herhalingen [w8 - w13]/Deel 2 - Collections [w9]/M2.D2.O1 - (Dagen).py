weekdagen = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')

print("Alle dagen van de week zijn:")
for dag in (weekdagen):
    print(f"- {dag}")

print("\nDe werkdagen zijn: maandag, dinsdag, woensdag, donderdag & vrijdag.")

print("\nDe weekenddagen zijn: zaterdag & zondag.")

print("\nAlle dagen in omgekeerde volgorde zijn:")
print(" -> ".join(weekdagen[::-1]))

werkdagen = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag')

print("\nDe werkdagen in omgekeerde volgorde zijn:")
for dag in reversed(werkdagen):
    print(f"- {dag}")


print("\nDe weekenddagen in omgekeerde volgorde zijn: zondag + zaterdag.")