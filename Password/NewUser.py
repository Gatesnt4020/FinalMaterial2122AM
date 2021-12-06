from PasswordChecker import PasswordChecker
import os.path
class NewUser:
    @staticmethod
    def makeUser():
        uname = "users.txt"
        pasd = "passes.txt"
        filename = "tempPass.txt"
        print("Do NOT enter spaces because they will be removed")
        first = input("Enter your first name: ")
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
            username = input("Enter your first name: ")
        filed = f"{username}.txt"
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
                fileToWrite.write(username+"\n")
            password = input("Enter a password: ")
            password = password.replace(" ", "")
            PasswordChecker.checkPassword(password)
            with open(filename, 'r') as file:
                password = file.read().rstrip()
            filename = open("tempPass.txt")
            with open(filed,"a+") as fileToWrite:
                fileToWrite.write(password+"\n")
            with open(pasd,"a+") as fileToWrite:
                fileToWrite.write(password+"\n")
            filename.close()
'''Sources:
    https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string   #used for taking out the spaces at the beginning, middle, and end in a string
    https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines  #used for reading a text file and make it a string instead of a list 
    '''