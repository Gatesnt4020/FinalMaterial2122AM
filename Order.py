class Order:
    
    #use order numbers for deleting and editing so its easier
        
    def __init__(self,addFood):
        self.add = addFood
        
    def __str__(self):
        return str(self.add)+" was added to your order"


    @staticmethod
    def menuChecker():
        menu = ["krabby patty","double krabby patty","triple krabby patty","seafoam soda","kelp shake","coral bits","kelp rings","krabby meal", "double krabby meal","triple krabby meal","salty sea dog","footlong","sailors surprise","golden loaf"]
        while not (add in menu):
            add = input("What do you want to add ")