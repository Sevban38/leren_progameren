import random

Passwords = ["wachtwoord123", "wachtwoord456", "wachtwoord789", "wachtwoord012", "wachtwoord345", "appel", "banaan", "citroen", "druif", "kiwi"]

correct_password = random.choice(Passwords).lower()

attempts = 0
max_attempts = 5
max_attempts_display = 5 

while attempts < max_attempts:
    
    entered_password = input("Voer het wachtwoord in: ")
    
    
    if entered_password == correct_password:
        print(f"Correct! Je hebt het wachtwoord geraden in {attempts + 1} pogingen.")
        break
    else:
        print(f"Onjuist wachtwoord. Probeer het opnieuw. je hebt nog {max_attempts_display - attempts - 1} pogingen over.")
        attempts += 1


if attempts == max_attempts:
    print(f"Je hebt het maximale aantal pogingen bereikt. Je mag niet meer inloggen. het wachtwoord was: {correct_password}")