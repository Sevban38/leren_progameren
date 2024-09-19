# Vraag 2 gehele getallen op aan de gebruiker
a = int(input("Voer het eerste gehele getal in (a): "))
b = int(input("Voer het tweede gehele getal in (b): "))

# Bepaaling van groten 
if a > b:
    Max = a
    Min = b
    print(f"a is het grootste getal: {Max}")
elif a < b:
    Min = a
    Max = b
    print(f"a is het kleinste getal: {Min}")
else:
    Min = Max = a
    print("a en b zijn even groot")

# print min en max
print(f"Het minimum is: {Min}")
print(f"Het maximum is: {Max}")