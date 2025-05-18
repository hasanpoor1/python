def revtxt(text):
    revstr1 =("")
    for harf in text:
       revstr1 = harf + revstr1
    return revstr1
stringORG = input(str("enter string:"))
endstr = revtxt(stringORG)
print("strig orginal: " , stringORG)
print("revers string:", endstr)