import math



x = (float(input("enter number :")))


def hesab(number):
    if number >= 0:
        return number
    else:
        return -number

print("your number :", hesab(x))

# ------------------------------------------------------
from math import exp

def hesab2(x):
    if 0 < x <= 1:
        return x
    else:
        return math.exp(-x)

y = float(input("enter number:"))
result = hesab2(y)
print("نتیجه:", result)