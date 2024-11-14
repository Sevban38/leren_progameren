start = 50

totaal = 0

teller = 1


getallen = []


while totaal <= 1000:
    getallen.append(start)
    totaal += start
    print(f"{teller}. {' + '.join(map(str, getallen))} = {totaal}")
    start += 1
    teller += 1