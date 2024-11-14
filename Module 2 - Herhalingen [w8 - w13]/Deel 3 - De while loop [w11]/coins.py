# name of student: 
# number of student:
# purpose of program: To calculate and return the correct amount of change using the least number of coins.
# structure of program: The program calculates the change to be returned and iteratively determines the number of each coin type to return.

coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1] # List of coin values in cents, including 1, 2, and 5-euro coins.

toPay = int(float(input('Amount to pay: ')) * 100) # Convert the amount to pay from euros to cents.
paid = int(float(input('Paid amount: ')) * 100) # Convert the paid amount from euros to cents.
change = paid - toPay # Calculate the total change to be returned.

returnedCoins = {} # Dictionary to keep track of the number of each coin returned.

while change > 0 and len(coinValues) > 0: # Loop until all change is returned or there are no more coin types left.
  coinValue = coinValues.pop(0) # Get the highest coin value available.
  nrCoins = change // coinValue # Calculate the maximum number of coins of this type that can be returned.

  if nrCoins > 0: # If there are coins of this type to return.
    print('Return maximal ', nrCoins, ' coins of ', coinValue, ' cents!') # Inform the user of the maximum number of coins to return.
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? ')) # Ask the user how many coins of this type were actually returned.
    if nrCoinsReturned > nrCoins:
        print(f"You can't return more than {nrCoins} coins of {coinValue} cents.")
        nrCoinsReturned = nrCoins
    change -= nrCoinsReturned * coinValue # Subtract the value of the returned coins from the change.
    returnedCoins[coinValue] = nrCoinsReturned # Record the number of coins returned for this coin type.

if change > 0: # If there is still change left to return.
  print('Change not returned: ', str(change) + ' cents') # Inform the user that not all change was returned.
else:
  print('Done') # Inform the user that all change was returned.

# Print a summary of all returned coins.
print('Summary of returned coins:')
for coin in sorted(returnedCoins.keys(), reverse=True):
  print(f'{returnedCoins[coin]} coins of {coin} cents')