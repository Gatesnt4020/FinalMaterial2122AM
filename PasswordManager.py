import random,string
upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

inProgram=True
print("Welcome to the program to help remember all of the passwords in the world")
ui = input("Are you a new user (y/n) ")
while ui != "y" and "n" : ui = input("Are you a new user (y/n) ")
while inProgram == True:
    if ui == "y":
        First=input("Enter your first name. ").upper()
        while (not First.isalpha()) : First=input("Enter your first name ").upper()
        Last=input("Enter your last name ").upper
        while (not Last.isalpha()) : Last=input("Enter your last name ").upper
        User=input("Enter your username ").upper
        while (User != chr(33,126)) : User=input("Enter your username without spaces ").upper
        '''while (not User.isalpha() or not User.isdigit()) : User=input("Enter your username ").upper'''
        password=input("Enter a password requirements: 8 characters, 1 upper, 1 lower, and includes a special character")
        while (8<=len(password)) : print("")

def generate(cap, low, num, sym):
    password = ""
    for i in range(cap):
        password+=random.choice(upper)
    for i in range(low):
        password+=random.choice(lower)
    for i in range(num):
        password+=random.choice(numbers)
    for i in range(sym):
        password+=random.choice(symbols)
    return "".join(random.sample(password,len(password)))

ui = input("Do you want to generate a password: ")
print("Enter quit to stop the program")
while ui != "quit":
    cap = input("How many upper: ")
    while(not cap.isdigit()):
        cap = input("How many upper: ")
    cap = int(cap)
    low = input("How many lower: ")
    while(not low.isdigit()):
        low = input("How many lower: ")
    low = int(low)
    num = input("How many numbers: ")
    while(not num.isdigit()):
        num = input("How many numbers: ")
    num = int(num)
    sym = input("How many symbols: ")
    while(not sym.isdigit()):
        sym = input("How many symbols: ")
    sym = int(sym)
    print(generate(cap, low, num, sym))
    ui = input("Do you want to generate a password: ")