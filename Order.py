class Order:
    
    masterOrder=[]
    menu = ["Krabby Patty","Double Krabby Patty","Triple Krabby Patty","Seafoam Soda","Kelp Shake","Coral Bits","Kelp Rings","Krabby Meal", "Double Krabby Meal","Triple Krabby Meal","Salty Sea Dog","Footlong","Sailors Surprise","Golden Loaf"]
        
    def addOrder(self,addFood):
        self.add = addFood
        
    def newOrder(self,newFood):
        self.new = newFood
        
    def editOrder(self,editFood):
        self.edit = editFood
        
    def removeOrder(self,removeFood):
        self.remove = removeFood

    @staticmethod
    def menuChecker:
        while not (self.add in menu):
            add = input("Please ask for something from the menu")
        while not (self.edit in )