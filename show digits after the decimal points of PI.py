import math

def calcPi(number):
    sol = round(math.pi, number)
    return sol

num = input("Enter a number which you want to see the digit after the decimal point of PI: ")
try:
    value = int(num)
    print(calcPi(value))
except:
    print("You do not enter any number.")
