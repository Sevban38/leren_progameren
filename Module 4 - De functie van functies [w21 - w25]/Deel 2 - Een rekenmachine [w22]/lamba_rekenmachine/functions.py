def addition(number1, number2):
  return number1 + number2

def subtraction(number1, number2):
  return number1 - number2

def multiplication(number1, number2):
  return number1 * number2

def division(number1, number2):
  return number1 / number2

def perform_operation(choice, n1, n2=None ):
  if choice == 'A':
    result = addition(n1, n2)
  elif choice == 'B':
    result = subtraction(n1, n2)
  elif choice == 'C':
    result = multiplication(n1, n2)
  elif choice == 'D':
    result = division(n1, n2)
  elif choice == 'E':
    n1 = float(input("Getal: "))
    result = addition(n1, 1)
  elif choice == 'F':
      n1 = float(input("Getal: "))
      result = subtraction(n1, 1)
  elif choice == 'G':
      n1 = float(input("Getal: "))
      result = multiplication(n1, 2)
  elif choice == 'H':
      n1 = float(input("Getal: "))
      result = division(n1, 2)
  
  return result

