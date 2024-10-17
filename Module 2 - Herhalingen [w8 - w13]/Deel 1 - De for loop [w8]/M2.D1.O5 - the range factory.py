def generate_lists(list_lengths):
    lists = []
    for i, length in enumerate(list_lengths, start=1):
        lists.append(list(range(i, i * length + 1, i)))
    return lists

def main():
    num_lists = int(input("Hoeveel lijstjes wil je genereren? "))
    list_lengths = []
    
    for i in range(1, num_lists + 1):
        length = int(input(f"Wat moet de lengte van lijst {i} zijn? "))
        list_lengths.append(length)
    
    generated_lists = generate_lists(list_lengths)
    
    for idx, lst in enumerate(generated_lists, start=1):
        print(f"Lijst {idx}: {lst}")

if __name__ == "__main__":
    main()
