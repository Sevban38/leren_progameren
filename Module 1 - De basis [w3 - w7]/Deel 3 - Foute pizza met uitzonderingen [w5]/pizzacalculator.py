def get_pizza_count(size, price):
    while True:
        try:
            count = float(input(f'Hoeveel {size} pizzas wilt u? ({price}$) '))
            if count.is_integer() and count >= 0:
                return int(count)
            else:
                print("Voer een positief geheel getal in.")
        except ValueError:
            print("U heeft iets verkeerd ingevuld, probeer nogmaals.")

def calculate_total(small_count, medium_count, large_count):
    small_price = 7
    medium_price = 9.50
    large_price = 12

    total_small = small_count * small_price
    total_medium = medium_count * medium_price
    total_large = large_count * large_price

    total = total_small + total_medium + total_large

    print('-------------------------')
    if small_count > 0:
        print(f'   {total_small} voor small')
    if medium_count > 0:
        print(f'   {total_medium} voor medium')
    if large_count > 0:
        print(f'   {total_large} voor large')
    print(f'   {total} euro totaal')
    print('-------------------------')

small_pizza = get_pizza_count('small', 7)
medium_pizza = get_pizza_count('medium', 9.50)
large_pizza = get_pizza_count('large', 12)

calculate_total(small_pizza, medium_pizza, large_pizza)