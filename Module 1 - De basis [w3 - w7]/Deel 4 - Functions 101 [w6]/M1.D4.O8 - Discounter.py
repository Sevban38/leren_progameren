def calc_discount(price: float, brand: str, month_discount_brands: str, discount_percentage: float) -> float:
    # Maak een lijst van de merken die in de maandaanbieding zitten
    discount_brands_list = month_discount_brands.split(',')
    
    # Controleer het merk 
    if brand in discount_brands_list:
        discount = round((price * discount_percentage) / 100, 2)
    else:
        discount = 0.0  # merk niet in lijst geen korting
    
    return discount


# Test 1: Merk komt voor
print(calc_discount(1000, 'Vespa', 'Vespa,Kymco,Yamama', 10))  #VW: 100.0

# Test 2: Merk komt niet voor 
print(calc_discount(1000, 'Honda', 'Vespa,Kymco,Yamama', 10))  #VW: 0.0

# Test 3: Prijs is een float getal en merk komt voor
print(calc_discount(750.50, 'Kymco', 'Vespa,Kymco,Yamama', 10))  #VW: 75.05

# Test 4: Lege lijst met maandaanbiedingen
print(calc_discount(500, 'Yamama', '', 10))  # VW:  0.0

# Test 5: Merk komt voor, maar prijs is 0
print(calc_discount(0, 'Yamama', 'Vespa,Kymco,Yamama', 10))  # VW: 0.0
