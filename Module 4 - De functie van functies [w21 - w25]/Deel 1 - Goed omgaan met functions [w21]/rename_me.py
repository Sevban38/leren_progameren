def is_even(getal:int) -> bool:
    return getal % 2 == 0

def woorden_omkeren(zin:str) -> str:
    woorden = zin.split()
    omgekeerde_woorden = woorden[::-1]
    omgekeerde_zin = ' '.join(omgekeerde_woorden)
    return omgekeerde_zin

def tel_unieke_karakters(tekst:str) -> int:
    unieke_karakters = set(tekst)
    aantal = len(unieke_karakters)
    return aantal

def gemiddelde_woordlengte(zin:str) -> float:
    woorden = zin.split()
    
    totale_lengte = 0
    for woord in woorden:
        totale_lengte += len(woord)

    gemiddelde_lengte = totale_lengte / len(woorden)
    return gemiddelde_lengte

def print_vermenigvuldigingstabel(getal:int, limiet:int=10) -> None:
    for i in range(1, limiet+1):
        resultaat = i * getal
        print(f'{i} x {getal} = {resultaat}')


