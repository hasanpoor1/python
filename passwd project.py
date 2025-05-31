import random
import string
from idlelib.colorizer import color_config

lower = (string.ascii_lowercase)
upper = (string.ascii_uppercase)
symbols ="!@#45)(*&^/<>+{}[]"
numbers ="0123456789"
all =lower + upper + symbols +numbers

while True:
    print("Option\n\t1)Crate a password:\n\t2)Exit:")
    choice = input("your choice:")
    if choice == "1":
        meqdar = int (input("تعداد حروف خود را انتخاب کنید:"))
        password = "".join(random.sample(all,meqdar))
        print(password)
    elif choice == "2":
        break
    else:
        print("!***!WRONG!***!\n")


