class Order:

    @staticmethod
    def menuChecker(addFood):
        menu=["Krabby Patty","Double Krabby Patty","Triple Krabby Patty","Coral Bits","Kelp Rings","Krabby Meal", "Double Krabby Meal","Triple Krabby Meal","Salty Sea Dog","Footlong","Sailors Surprise","Golden Loaf","Kelp Shake","Seafoam Soda"]
        while not (addFood in menu):
            addFood = input("Please ask for something from the menu ")
        print(addFood+" has been added to your order\n")