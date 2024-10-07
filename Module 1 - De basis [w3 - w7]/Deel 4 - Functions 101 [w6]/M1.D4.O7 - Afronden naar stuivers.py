def afronding_naar_stuivers(price):
    rounded_price = round(price * 20) / 20  
    return rounded_price

# Test the function with example prices
prices = [2.24, 13.01, 5.99, 10.50, 7.75]
rounded_prices = [afronding_naar_stuivers(price) for price in prices]
print(rounded_prices) 