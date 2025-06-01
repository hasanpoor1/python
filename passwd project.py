import random
import string
from idlelib.colorizer import color_config
lower = (string.ascii_lowercase)
upper = (string.ascii_uppercase)
symbols ="!@#45)(*&^/<>+{}[]"
numbers ="0123456789"
all = lower + upper + symbols + numbers

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
#project 1    این کد رمز قوی برامون مسیازه

#--------------------------------------------------------------------------
#project 2    این کد متن هارو به صورت رمزنگاری تبدیل میکند و متن های رمز نگاری به صورت اولیه برات میشکنه
while True:
    print("Choose Your Option:\n\t1) Encrypt\n\t2) Decrypt\n\t3) Exit")
    choice = input("Your Choice: ")

    if choice == "1":
        plain_text = input("text: ")
        encrypted_text = ""
        for c in plain_text:
            x = ord(c) * 2 + 5
            encrypted_text += chr(x)
        print("encrypted text:", encrypted_text)
        print("*" * 40 + "\n")

    elif choice == "2":
        encrypted_text = input("encrypted text: ")
        plain_text = ""
        for c in encrypted_text:
            x = (ord(c) - 5) // 2
            plain_text += chr(x)
        print("decrypted text:", plain_text)
        print("*" * 40 + "\n")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.\n")


