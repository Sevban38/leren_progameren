from NaamEnLeeftijdfunc import data

for person in data:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
    print(f"{person['name']} is {person['age']} jaar en woont in {person['city']}.")


