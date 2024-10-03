def vergelijk_getallen(nr1: int, nr2: int) -> str:
    if nr1 > nr2:
        return f"Maximum: {nr1} en minimum: {nr2}"
    elif nr1 < nr2:
        return f"Maximum: {nr2} en minimum: {nr1}"
    else:
        return "Beide getallen zijn even groot"

#Voorbeeld
resultaat = vergelijk_getallen(5, 3)
print(resultaat)

resultaat = vergelijk_getallen(5, 5)
print(resultaat)

resultaat = vergelijk_getallen(2, 3)
print(resultaat)
