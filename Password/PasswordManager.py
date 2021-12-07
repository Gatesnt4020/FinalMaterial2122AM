from NEWUSER import NewUser
import os
ui = ""



print("Need help remembering all of the passwords in the world? This program will save all of the passwords you need for your computer.")
while ui != "Quit":
    ui = input(f'''are you a (new) user or are you (login) in: ''').lower()
    if ui == "new":
        NewUser.makeUser()
    elif ui == "login":
        trys = 3
        notCorrect = True
        while trys > 0 and notCorrect:
            usered = []
            listOfList = []
            username = input("Enter a username: ")
            username = username.replace(" ", "")
            while username == "":
                username = input("Enter your username: ")
            if os.path.exists(f"{username}.txt"):
                usered.append(username)
                password = input("Enter a password: ")
                password = password.replace(" ", "")
                while password == "":
                    password = input("Enter your password: ")
                usered.append(password)
                #https://stackoverflow.com/questions/24021202/python-compare-a-string-with-a-text-file/24021243 used to grab the string from the text file
                if open(f"{username}user.txt").read():
                    x = open(f"{username}user.txt").read()
                    listOfList.append(x)
                else:
                    print("error in the files please try again")
                if open(f"{username}pass.txt").read():
                    y = open(f"{username}pass.txt").read()
                    listOfList.append(y)
                else:
                    print("error in the files please try again")
                if usered == listOfList:
                    print("congrats you got it right")
                    notCorrect = False
                else:
                    print("You have entered the worng password try again")
                    trys-=1
            else:
                print("You have entered the wrong username")
                trys-=1
        if trys <= 0:
            exit()
        inProgram = True
        while inProgram == True:
            ui = input(f'''what would you like to do
1) Generate a password
2) Make a category
3) View categories
4) Brute force checker(Unfinished)
5) Exit
''')
            if ui == "5":
                inProgram = False
            elif ui == "1":
                NewUser.generatePass()
            elif ui == "3":
                filess = f"{username}"+"Category"
                if os.path.exists(filess):
                    print()
                else:
                    print("You have no categories made")
            elif ui == "2":
                filess = f"{username}"+"Category"
                cat = input("What cateogry would you like to make (example... home, work, entertainment, bills, etc.): ")
                
                
            elif ui == "4":
                print("This addition of the program hasn't been made yet")
#print folder or print a text file called something like user+category

#make an account.txt to store the users names then use a password.txt and for checking look to see 
#if (with a for loop) the username and password match
#check and see if the username and password is there if not automatically subtract 1
#maybe check and see first if their there and if they are then running the for loop
'''Sources not used:
    https://stackoverflow.com/questions/43147534/iterate-over-file-and-get-word-index-from-other-file   #was going to be use for the login section but wasnt able to figrue it out
    '''