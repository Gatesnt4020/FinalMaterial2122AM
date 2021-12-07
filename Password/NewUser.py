from os import stat
import os.path
import random,string
class NewUser:
    @staticmethod
    def makeUser():
        xs = False
        while xs == False:
            filename = "tempPass.txt"
            print("Do NOT enter spaces because they will be removed")
            first = input("Enter your first name: ")
            #https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines  #used for reading a text file and make it a string instead of a list 
            first = first.replace(" ", "")
            while first == "":
                first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            last = last.replace(" ", "")
            while last == "":
                last = input("Enter your first name: ")
            username = input("Enter a username: ")
            username = username.replace(" ", "")
            while username == "":
                username = input("Enter your username name: ")
            filed = f"{username}.txt"
            uname = username + "user.txt"
            upass = username +"pass.txt"
            if os.path.exists(f"{username}.txt"):
                print("This username has already been taken")
            else:
                with open(filed,"a+") as fileToWrite:
                    fileToWrite.write(username+"\n")
                with open(filed,"a+") as fileToWrite:
                    fileToWrite.write(last+"\n")
                with open(filed,"a+") as fileToWrite:
                    fileToWrite.write(first+"\n")
                with open(uname,"a+") as fileToWrite:
                    fileToWrite.write(username)
                password = input("Enter a password: ")
                password = password.replace(" ", "")
                NewUser.checkPassword(password)
                with open(filename, 'r') as file:
                    password = file.read().rstrip()
                filename = open("tempPass.txt")
                with open(filed,"a+") as fileToWrite:
                    fileToWrite.write(password+"\n")
                with open(upass,"a+") as fileToWrite:
                    fileToWrite.write(password)
                filename.close()
                xs =True

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
            numbers = cap+low+num+sym
        generate(cap, low, num, sym)
        with open(filename,"w") as fileToWrite:
            fileToWrite.write(password)

    @staticmethod
    def checkPassword(password):
        #       1 #, 1 Cap, lower, 1 special, length
        checkList = [False,False,False,False,False]
        specialCharacters="!@#$%^&*()"
        filename = "tempPass.txt"

        #its harder to iterate
        #check first, is it long enough?
        while False in checkList:
            password = password.replace(" ", "")
            if len(password) >= 8:
                checkList[4] = True

                #loop through our password
                for c in password:  #c stands for character
                    
                    if ord(c) in range(48,58): #if there is a number
                        checkList[0] = True
                    elif ord(c) in range(65,91):#if there is a Cap
                        checkList[1] = True
                    elif ord(c) in range(97,123):   #if there is a lower
                        checkList[2] = True
                    elif c in specialCharacters: #if there is a special
                        checkList[3] = True
                    else:                           #Oh crap, this is a bad character
                        break
            if False in checkList:
                password = input("Please enter a stronger password: ")
        with open(filename,"w") as fileToWrite:
            fileToWrite.write(password)

    @staticmethod
    def bruteForcer():

        def brute(password):
            upper = string.ascii_uppercase
            lower = string.ascii_lowercase
            numbers = string.digits
            symbols = "!@#$%^&*()"
            maxnum = 0
            passwordguesser = ""
            listy=[]
            while passwordguesser != password:
                passwordguesser = ""
                for i in range(maxnum):
                    passwordguesser+=random.choice(upper)
                for i in range(maxnum):
                    passwordguesser+=random.choice(lower)
                for i in range(maxnum):
                    passwordguesser+=random.choice(numbers)
                for i in range(maxnum):
                    passwordguesser+=random.choice(symbols)
                passwordguesser =  "".join(random.sample(passwordguesser,len(password)))
            
            
        
        ui = input("Enter a password or generate one: ")
        if ui == "generate":
            NewUser.generatePass
            brute(password)
        else:
            brute(ui)
