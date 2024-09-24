import random

# selecteer 2 nummers
num1 = str(random.randint(1, 10))
num2 = str(random.randint(5, 15))

# vraag om een antwoord
number = input('Weet jij wat ' + num1 + '+' + num2 + ' is? ')

# geef reactie op het antwoord
try:
    if int(number) == int(num1) + int(num2):
        print('Dat is juist')
    else:
        print('Nee dat klopt niet')
except ValueError:
    print('Dat is geen nummer!')
