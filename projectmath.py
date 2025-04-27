import math

def hesab (x,y):
    return (x /y) * math.log(x / y)
x = float (input("inter x:"))
y = float (input("inter y:"))
print('محاسبه',hesab(x , y))

#---------------------------***************
def hesabexp (a):
    return math.exp(a)
a = float(input("inter a:"))
print("exp(a):" , hesabexp(a))
print("exp(a/2):", hesabexp(1 / a))

#---------------------*************************

from math import exp

def hesab2(b):
    return 1 + exp(-b)
b = float(input("inter b:"))
print(hesab2(b))

#-----------------------------------------***********

from math import sqrt,log
def hesab3 (d,m):
    return sqrt(d)*(log(d))**m
d = float(input("inter d:"))
m = float(input("inter m:"))
kol = hesab3(d,m)
print(kol, "جواب")

#----------------------------------------******************
def hesab5 (n,s,s1):
    return (1/n)*(s - s1)
n = float(input("inter n:"))
s = float(input("inter s:"))
s1 = float(input("inter s1:"))
kolsh =hesab5(n,s,s1)
print(kolsh, "جواب")