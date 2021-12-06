from NEWUSER import NewUser
import io
ui = ""

def makeChecker(filename):
    for i in usered:
        listOfList.append([])
    with open(filename,"r") as file:
        #readlines returns a list
        listOflines= file.readlines()
    for row in listOflines:
        for i in range(len(usered)):
            if usered[i] in row:
                listOfList[i].append(row)
            

print("Need help remembering all of the passwords in the world? This program will save all of the passwords you need for your computer.")
while ui != "Quit":
    ui = input(f'''are you a (new) user or are you (login) in: ''').lower()
    if ui == "new":
        NewUser.makeUser()
    elif ui == "login":
        trys = 3
        while trys != 0:
            usered = []
            listOfList = []
            username = input("Enter a username: ")
            usered.append(username)
            password = input("Enter a password: ")
            usered.append(password)
            filename = "checker.txt"
            makeChecker(filename)
            print(listOfList)
            if listOfList ==[]:
                print("The username or password is incorrect")
                trys+=1
            else:
                print("You have succesfully login in :)")
#            listOfList = str(listOfList)
#            print(listOfList)
#            usered = str(usered)
#            listOfList = listOfList.replace("[","")
#            listOfList = listOfList.replace("]","")
#            listOfList = listOfList.replace("\\n","")
#            print(listOfList)
#            with io.StringIO(listOfList) as uname:
#                num = 0
#                wordIndex=[]
#                for row in uname:
#                    word = row.strip()
#                    if word not in wordIndex:
#                        wordIndex[word]
#                    num+=1
#            with io.StringIO(usered) as pasd:
#                for row in pasd:
#                    word = row.strip()
#                    if word not in wordIndex:
#                        print("This is the wronge username or password")
#                        trys-=1
#                    else:
#                        print("You have succesfully login in :)")
#        if trys == 0:
#            exit()
file = open(f"{username}.txt","r+")
file.truncate(0)
file.close()
#make an account.txt to store the users names then use a password.txt and for checking look to see 
#if (with a for loop) the username and password match
#check and see if the username and password is there if not automatically subtract 1
#maybe check and see first if their there and if they are then running the for loop
'''Sources:
    https://stackoverflow.com/questions/43147534/iterate-over-file-and-get-word-index-from-other-file
    '''