class PasswordChecker:

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