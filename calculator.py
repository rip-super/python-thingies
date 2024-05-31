import math
from fractions import Fraction
import os

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def find_roots(a, b, c):
  cls()
  discriminant = (b**2) - (4 * a * c)
  sqrt_D = math.sqrt(abs(discriminant))

  if discriminant > 0:
    print("This equation has: 2 real roots")
    print("\n")
    print("Discriminant: " + str(discriminant))
    print("\n")
    print("Solution 1. -> " + str((-b + sqrt_D) / (2 * a)))
    print("Solution 2. -> " + str((-b - sqrt_D) / (2 * a)))
    print("\n")

  elif discriminant == 0:
    print("This equation has: 1 real root")
    print("\n")
    print("Discriminant: " + str(discriminant))
    print("\n")
    print("Solution 1. -> " +  str(-b / (2 * a)))
    print("\n")

  else:
    print("This equation has: 2 complex roots")
    print("\n")
    print("Discriminant: " + str(discriminant))
    print("\n")
    real_part = -b / (2 * a)
    imaginary_part = sqrt_D / (2 * a)
    print(f"Solution 1. ->  {real_part:.2f} + {imaginary_part:.4f} * i")
    print(f"Solution 2. ->  {real_part:.2f} - {imaginary_part:.4f} * i")
    print("\n")

def mean():
  string = input("What numbers would you like to find the mean of? (no commas)\n> ")
  num_list = [int(element) for element in string.split()]
  mean = str(sum(num_list)/len(num_list))
  print("The mean is " + mean)
  
def median():
  string = input("What numbers would you like to find the median of? (no commas)\n> ")
  num_list = [int(element) for element in string.split()]
  num_list.sort()

  if len(num_list) % 2 == 0:
      m1 = num_list[len(num_list)//2]
      m2 = num_list[len(num_list)//2 - 1]
      median = str((m1 + m2)/2)
  else:
      median = num_list[len(num_list)//2]
  print("The median is " + median)

def mode():  
  string = input("What numbers would you like to find the mode of? (no commas)\n> ")
  num_list = [int(element) for element in string.split()]
  frequency = {}
  for i in num_list:
      frequency.setdefault(i, 0)
      frequency[i]+=1

  frequent = max(frequency.values())
  for i, j in frequency.items():
      if j == frequent:
          mode = str(i)
  print("The mode is " + mode)

def convert_C_to_F():
    c = int(input("Enter a temperature to convert from Celsius to Fahrenheit.\n> "))
    print(str(c) + "°C is " + str(((9/5) * c) + 32) + "°F")
    
def convert_F_to_C():
    f = int(input("Enter a temperature to convert from Fahrenheit to Celsius.\n> "))
    print(str(f) + "°F is " + str((f - 32) * (5/9)) + "°C")

def find_factorial():
    num = int(input("What number would you like to find the factorial of?\n> "))
    cls()
    factorial = 1
    if num < 0:
       print(f"{num}! is undefined")
    elif num == 0:
       print(f"{num}! = 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print(f"{num}! = {factorial}")

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def exponentiate(x, y):
  return x ** y
  
def sqrt(x):
  return math.sqrt(x)
  
def cbrt(x):
  return x ** (1/3)
  
def nthrt(x, y):
  return y ** (1/x)
  
def log(x, base):
  return math.log(x, base)

def sin(x):
  return math.sin(x)
  
def cos(x):
  return math.cos(x)
  
def tan(x):
  return math.tan(x)
  
def asin(x):
  return math.asin(x)
  
def acos(x):
  return math.acos(x)
  
def atan(x):
  return math.atan(x)
  
def csc(x):
  return 1 / math.sin(x)
    
def sec(x):
  return 1 / math.cos(x)
    
def cot(x):
  return 1 / math.tan(x)
  
cls()

print("Python Calculator \n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
print("5. Exponentiation")
print("6. Square Root")
print("7. Cube Root")
print("8. Nth Root")
print("9. Logarithms")
print("10. Trigonomentric Functions")
print("11. Conversions")
print("12. Mean, Median and Mode")
print("13. Quadratic Equation Solver")
print("14. Factorial")

choice = input("What would you like to do today? (Number) \n> ")
if choice == "1":
  cls()
  num1 = float(input("What is the first number? "))
  num2 = float(input("What is the second number? "))
  print(num1, "+", num2, "=", add(num1, num2))
  
elif choice == "2":
  cls()
  num1 = float(input("What is the first number? "))
  num2 = float(input("What is the second number? "))
  print(num1, "-", num2, "=", subtract(num1, num2))
  
elif choice == "3":
  cls()
  num1 = float(input("What is the first number? "))
  num2 = float(input("What is the second number? "))
  print(num1, "*", num2, "=", multiply(num1, num2))
  
elif choice == "4":
  cls()
  num1 = float(input("What is the first number? "))
  num2 = float(input("What is the second number? "))
  print(num1, "/", num2, "=", divide(num1, num2))

elif choice == "5":
  cls()
  num1 = float(input("What is the first number? "))
  num2 = float(input("What is the second number? "))
  print(num1, "^", num2, "=", exponentiate(num1, num2))
  
elif choice == "6":
  cls()
  num1 = float(input("What number would you like to find the square root of? "))
  print("√", num1, "=", math.sqrt(num1))
  
elif choice == "7":
  cls()
  num1 = float(input("What number would you like to find the cube root of? "))
  print("∛", num1, "=", cbrt(num1))
  
elif choice == "8":
  cls()
  num1 = float(input("What is the index of the radicand? "))
  num2 = float(input("What is the radicand? "))
  print(num1, "√", num2, "=", nthrt(num1, num2))

elif choice == "9":
  cls()
  num1 = float(input("What is the argument of the logarithm? "))
  base = float(input("What is the base of the logarithm? "))
  print("Log to the base", base, "of", num1, "=", math.log(num1, base))
  
elif choice == "10":
  cls()
  print("1. Sine")
  print("2. Cosine")
  print("3. Tangent")
  print("4. Arc Sine")
  print("5. Arc Cosine")
  print("6. Arc Tangent")
  print("7. Cosectant")
  print("8. Secant")
  print("9. Cotangent")
  choice2 = input("Which Trig function would you like to use? (Number) \n> ")
  if choice2 == "1":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("sin of", num1, "=", sin(num1), "(Answer in radians)")
    
  elif choice2 == "2":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("cos of", num1, "=",cos(num1), "(Answer in radians)")
    
  elif choice2 == "3":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("tan of", num1, "=",tan(num1), "(Answer in radians)")
  
  elif choice2 == "4":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("asin of", num1, "=",asin(num1), "(Answer in radians)")
  
  elif choice2 == "5":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("acos of", num1, "=",acos(num1), "(Answer in radians)")
  
  elif choice2 == "6":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("atan of", num1, "=",atan(num1), "(Answer in radians)")
    
  elif choice2 == "7":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("csc of", num1, "=",csc(num1), "(Answer in radians)")
    
  elif choice2 == "8":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("sec of", num1, "=",sec(num1), "(Answer in radians)")
  
  elif choice2 == "9":
    cls()
    num1 = float(input("What is the first number (no fractions)? "))
    print("cot of", num1, "=",cot(num1), "(Answer in radians)")
    
elif choice == "11":
  cls()
  print("1. Decmial to Percentage")
  print("2. Decmial to Fraction")
  print("3. Fraction to Percentage")
  print("4. Fraction to Decimal")
  print("5. Percentage to Decimal")
  print("6. Percentage to Fraction")
  print("7. Fahrenheit to Celsius")
  print("8. Celsius to Fahrenheit")
  choice3 = input("What conversion would you like to do? (Number) \n> ")
  if choice3 == "1":
    cls()
    num1 = float(input("What number would you like to convert to a percentage? "))
    print(num1, "as a percentage is", (num1 * 100), "%")
    
  elif choice3 == "2":
    cls()
    num1 = float(input("What number would you like to convert to a fraction? "))
    print(num1, "as a fraction is", Fraction(num1).limit_denominator())
    
  elif choice3 == "3":
    cls()
    frac1 = input("What fraction would you like to convert to a percentage? ")
    num1 = float(Fraction(frac1))
    print(frac1, "as a percentage is", (num1 * 100), "%")
    
  elif choice3 == "4":
    cls()
    frac1 = input("What fraction would you like to convert to a decimal? ")
    num1 = float(Fraction(frac1))
    print(frac1, "as a decimal is", num1)
    
  elif choice3 == "5":
    cls()
    num1 = float(input("What percentage would you like to convert to a decimal? (No percent sign) "))
    print(num1, "as a decimal is", (num1 / 100))
    
  elif choice3 == "6":
    cls()
    num1 = float(input("What percentage would you like to convert to a fraction? (No percent sign) "))
    num2 = num1 / 100
    print(num1, "%" +  " as a fraction is", Fraction(num2).limit_denominator())

  elif choice3 == "7":
    cls()
    convert_F_to_C()

  elif choice3 == "8":
    cls()
    convert_C_to_F()

  else:
    print("Invalid Input")

elif choice == "12":
  cls()
  print("1. Mean")
  print("2. Median")
  print("3. Mode")
  choice4 = input("What would you like to do today? (number)\n> ")
  if choice4 == "1":
    cls()
    mean()

  elif choice4 == "2":
    cls()
    median()

  elif choice4 == "3":
    cls()
    mode()

elif choice == "13":
  cls()
  print("Quadratic equation, Standard Form:\n\nax^2 + bx + c = 0\n\n")
  a = float(input('What is "a"?\n> '))
  b = float(input('What is "b"?\n> '))
  c = float(input('What is "c"?\n> '))

  if a == 0: 
    print('Invalid Input. "a" cannot be equal to 0. Please try again.')

  else:
    find_roots(a, b, c)

elif choice == "14":
  cls()
  find_factorial()

else:
  print("Invalid input, try again")

os.system("pause")
cls()