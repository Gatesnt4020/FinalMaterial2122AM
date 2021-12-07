import random,string
class Generator:
    @staticmethod
    def generatePass():
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        numbers = string.digits
        symbols = "!@#$%^&*()"
        filename = "tempPass.txt" 
        numbers = 0

        def generate(cap, low, num, sym):
            global password
            password = ""
            for i in range(cap):
                password+=random.choice(upper)
            for i in range(low):
                password+=random.choice(lower)
            for i in range(num):
                password+=random.choice(numbers)
            for i in range(sym):
                password+=random.choice(symbols)
            password =  "".join(random.sample(password,len(password)))

        ui = input("How long do you want the password: ")
        while(not ui.isdigit()):
            ui = input("How long do you want the password: ")
        while numbers != ui:
            cap = random.randint(1,ui)
            low = random.randint(1,ui)
            num = random.randint(1,ui)
            sym = random.randint(1,ui)
        generate(cap, low, num, sym)
        with open(filename,"w") as fileToWrite:
            fileToWrite.write(password)