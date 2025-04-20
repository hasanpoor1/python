def  calnumber_1 (a,c,b):
    return a/c+b
a = float(input("enter number:"))
c = float(input("enter number:"))
b = float(input("enter number:"))
print(calnumber_1(a,c,b))

#******************************************

def calnumber2 (a,b,x):
    return (b*x)/(a/x)
b = float(input("enter number:"))
x = float(input("enter number:"))
a = float(input("enter number:"))
print(calnumber2(b,x,a))

#******************************************

r = float(input("شعاع دایره راوارد کنید:"))
pi = 3.14
en = pi * r * r
print(en,"مساحت دایره")
