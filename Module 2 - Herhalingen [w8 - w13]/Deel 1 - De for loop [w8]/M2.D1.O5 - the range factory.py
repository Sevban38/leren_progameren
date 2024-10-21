
 
num_lists = int(input("Hoeveel lijstjes wil je genereren? "))


length = int(input("Hoe lang moeten de lijstjes zijn? "))


all_lists = []


for i in range(1, num_lists + 1):
    lijst = list(range(i, i * length + 1, i))
    all_lists.append(lijst)


print(all_lists)
