def menuFries(question,choice,size,price):
     total=0
     option = input(question)
     if option == "y":
          option = input(f"Which choice? {choice} ")
          while option != choice[0] and option != choice[1]:
               option = input(f"Which choice? {choice} ")
          if option == choice[0]:
               option = input(f"Which size? {size} ")
               while option != [0] and option != [1] and option != [3]:
                    option = input(f"Which size? {size} ")
               if option == size[0]:
                    total+=price[0]
               elif option == size[1]:
                    total+=price[1]
               elif option == size[2]:
                    total+=price[2]
               elif option ==size[3]:
                    total+=price[3]
          elif option ==  choice[1]:
               option = input("Do you want salty sauce with that? (y/n) ")
               while option != "y" and option != "n":
                    option = input("Do you want salty sauce with that? (y/n) ")
               if option == "y":
                    total+=price
               elif option == "n":
                    total+=price
                    
def menuDrink(question,choice,size,price):
     total=0
     option = input(question)
     if option == "y":
          option = input(f"Which choice? {choice} ")
          while option != choice[0] and option != choice[1]:
               option = input(f"Which choice? {choice} ")
          if option == choice[0]:
               option = input(f"Which size? {size} ")
               while option != "Small" and option != "Medium" and option != "Large":
                    option = input(f"Which size? {size} ")
               if option == size[0]:
                    total+=price[0]
               elif option == size[1]:
                    total+=price[1]
               elif option == size[2]:
                    total+=price[2]
               elif option ==size[3]:
                    total+=price[3]
          elif option ==  choice[1]:
               total+=price
               
def menuBurger(question,choice,price):
     total=0
     option = input(question)
     if option == "y":
          option = input(f"Which choice? {choice} ")
          while option != "Krabby Patty" and option != "Double Krabby Patty" and option != "Triple Krabby Patty":
               option = input(f"Which choice? {choice} ")
          
     
               
          
     
     

ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ")
while ui != "y" and ui != "n":
     ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ")
if ui == "y":
     while ui != "quit":
          menuDrink()
elif ui == "n":
     print("Thank you for coming have a nice day")