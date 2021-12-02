class Order:
    
    #use order numbers for deleting and editing so its easier
        
    def addOrder(self,addFood):
        global orderNumber
        self.add = addFood
        

        
    def newOrder(self,newFood):
        global orderNumber
        self.new = newFood


        
#    def editOrder(self,editFood):
#        self.edit = editFood
#        
#    def removeOrder(self,removeFood):
#        self.remove = removeFood
#put in the actual program because it  easier to edit and remove orders  


    @staticmethod
    def menuChecker():
        menu = ["Krabby Patty","Double Krabby Patty","Triple Krabby Patty","Seafoam Soda","Kelp Shake","Coral Bits","Kelp Rings","Krabby Meal", "Double Krabby Meal","Triple Krabby Meal","Salty Sea Dog","Footlong","Sailors Surprise","Golden Loaf"]
        while not (add in menu):
            add = input("Please ask for something from the menu")
"""
    elif user_input=="remove":
        id=int(input("Which post do you want to delete? "))
        #loop through the list using index numbers(0,1,2,3,etc)
        for i in range(len(allPostArchive)):
            #if postwe are on's postId is equal the one we are looking for
            if allPostArchive[i]==id:
        #delete an item in the list
                del allPostArchive[i]
                break
"""