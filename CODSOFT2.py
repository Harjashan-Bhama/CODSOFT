import string
import random

chars = [x for x in string.printable if x not in string.whitespace]

def password(l):
    if (l<3):
        print("Password too short")
        return
        
    pswd = ""
    for i in range(l-3):
        pswd+= random.choice(string.ascii_letters)

    pswd+=random.choice(string.ascii_uppercase)
    pswd+=random.choice(string.digits)
    pswd+=random.choice(string.punctuation)
    return pswd

a = int(input("Enter Length of password: "))
print(f'Your generated password is:\n{password(a)}')