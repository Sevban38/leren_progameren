naam = input("Wat is je naam? ")
age = int(input("Hoe oud ben je? "))
gender = input("Ben je een A) een jongen of B) een meisje? ").lower()
color = input("Wat is je favoriete kleur? ")
favorite_number = int(input("Wat is je favoriete getal? "))
age_difference = abs(age - favorite_number)
pronoun = 'haar' if gender == 'b' else 'zijn'


print("")
print(f"Mag ik je voorstellen aan", {naam})
print(f"{naam()} leeftijd is:", age)
print(f"{naam}'s favoriete kleur is:", color)
print(f"Het verschil tussen {naam} leeftijd en {favorite_number} is:", age_difference)
