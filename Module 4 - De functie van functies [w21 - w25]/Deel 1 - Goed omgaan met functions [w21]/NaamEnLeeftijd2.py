from termcolor import colored
from NaamEnLeeftijdfunc import data

for person in data:
    name = person['name']
    age = int(person['age'])  # Zorg dat age een integer is
    city = person['city']

    if age >= 18:
        age_text = colored(f"al {age} jaar volwassen", "red")
    else:
        age_text = colored("nog niet volwassen", "green")

    city_text = colored(city, "yellow")
    name_text = colored(name, "cyan")

    print(f"In {city_text} woont {name_text}, die {age_text} is.")
