import random,string
upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

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
        password+=upper[random.randint(0, len(upper)-1)]
    for i in range(low):
        password+=lower[random.randint(0, len(lower)-1)]
    for i in range(num):
        password+=numbers[random.randint(0, len(numbers)-1)]
    for i in range(sym):
        password+=symbols[random.randint(0, len(symbols)-1)]
    password = list(password)
    random.shuffle(password)
    return "".join(password)

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