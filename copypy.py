from Order import Order
orderInfo = "\nOrder1:\n"
total=0
orderTotal=0
menu=["Krabby Patty","Double Krabby Patty","Triple Krabby Patty","Seafoam Soda","Kelp Shake","Coral Bits","Kelp Rings","Krabby Meal", "Double Krabby Meal","Triple Krabby Meal","Salty Sea Dog","Footlong","Sailors Surprise","Golden Loaf"]
def menuFries(question,choice,size,price):
     global orderInfo
     global orderTotal
     option = input(question)
     if option == "y":
          for i in choice:
               print(i)
          option = input("Which choice? ")
          while option != choice[0] and option != choice[1]:
               for i in choice:
                    print(i)
               option = input("Which choice? ")
          orderInfo+=(f"\t{option} ")
          if option == choice[0]:
               for i in size:
                    print(i)
               option = input("Which size? ")
               while option != [0] and option != [1] and option != [3]:
                    for i in size:
                         print(i)
                    option = input("Which size? ")
               if option == size[0]:
                    orderTotal+=price[0]
               elif option == size[1]:
                    orderTotal+=price[1]
               elif option == size[2]:
                    orderTotal+=price[2]
               elif option ==size[3]:
                    orderTotal+=price[3]
               orderInfo+=(f"{option}\n")
          elif option ==  choice[1]:
               option = input("Do you want salty sauce with that? (y/n) ")
               while option != "y" and option != "n":
                    option = input("Do you want salty sauce with that? (y/n) ")
               if option == "y":
                    orderTotal+=price+.5
                    orderInfo+=(f"w/ salty sauce\n")
               elif option == "n":
                    orderTotal+=price
                    orderInfo+=(f"w/o salty sauce\n")
                    
def menuDrink(question,choice,size,price):
     global orderInfo
     global orderTotal
     option = input(question)
     if option == "y":
          for i in choice:
               print(i)
          option = input(f"Which choice? {choice} ")
          while option != choice[0] and option != choice[1]:
               option = input(f"Which choice? {choice} ")
          orderInfo+=(f"\t{option} ")
          if option == choice[0]:
               for i in size:
                    print(i)
               option = input("Which size? ")
               while option != size[0] and option != size[1] and option != size[2]:
                    option = input("Which size? ")
                    for i in size:
                         print(i)
               if option == size[0]:
                    orderTotal+=price[0]
               elif option == size[1]:
                    orderTotal+=price[1]
               elif option == size[2]:
                    orderTotal+=price[2]
               elif option ==size[3]:
                    orderTotal+=price[3]
               orderInfo+=(f"{option}\n")
          elif option ==  choice[1]:
               orderTotal+=price[4]
               
def menuBurger(question,choice,price):
     global orderTotal
     global orderInfo
     option = input(question)
     if option == "y":
          for i in choice:
               print(i)
          option = input("Which choice? ")
          while option != choice[0] and option != choice[1] and option != choice[2]:
               for i in choice:
                    print(i)
               option = input(f"Which choice? ")
          orderInfo+=(f"\t{option} ")
          if option == choice[0]:
               orderTotal+=price[0]
               option = input("Would you like sea cheese with that? (y/n) ")
               while option != "y" and option != "n":
                    option = input("Would you like sea cheese with that? (y/n) ")
               if option =="y":
                    orderTotal+=price[3]
                    orderInfo+=(f"w/ sea cheese\n")
               else:
                    orderInfo+=(f"w/o sea cheese\n")
          elif option == choice[1]:
               orderTotal+=price[1]
               option = input("Would you like sea cheese with that? (y/n) ")
               while option != "y" and option != "n":
                    option = input("Would you like sea cheese with that? (y/n) ")
               if option =="y":
                    orderTotal+=price[3]
                    orderInfo+=(f"w/ sea cheese\n")
               else:
                    orderInfo+=(f"w/o sea cheese\n")
          elif option == choice[2]:
               orderTotal+=price[2]
               option = input("Would you like sea cheese with that? (y/n) ")
               while option != "y" and option != "n":
                    option = input("Would you like sea cheese with that? (y/n) ")
               if option =="y":
                    orderTotal+=price[3]
                    orderInfo+=(f"w/ sea cheese\n")
               else:
                    orderInfo+=(f"w/o sea cheese\n")
               
def menuFoods(question,choice,price):
     global orderInfo
     global orderTotal
     option = input(question)
     if option == "y":
          for i in choice:
               print(i)
          option = input("Which choice? ")
          while option != choice[0] and option != choice[1] and option != choice[3] and option != choice[4] and option != choice[5] and option != choice[6]:
               option = input(f"Which choice? {choice} ")
          orderInfo+=(f"\t{option}")
          if option == choice[0]:
               orderTotal+=price[0]
          elif option == choice[1]:
               orderTotal+=price[1]
          elif option == choice[2]:
               orderTotal+=price[2]
          elif option == choice[3]:
               orderTotal+=price[3]
          elif option == choice[4]:
               orderTotal+=price[4]
          elif option == choice[5]:
               orderTotal+=price[5]
          elif option == choice[6]:
               orderTotal+=price[6]
               option = input("Do you want sauce with that? (y/n) ")
               while option != "y" and option != "n":
                    option = input("Do you want sauce with that? (y/n) ")
               if option == "y":
                    orderTotal+=price+.5
                    orderInfo+=(f" w/ sauce\n")
               else:
                    orderTotal+=price
                    orderInfo+=(f" w/o sauce\n")

ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ")
while ui != "y" and ui != "n":
     ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ")
if ui == "y":
     while ui != "n":
          q="Would you like a Patty? (y/n) "
          c=["Krabby Patty","Double Krabby Patty","Triple Krabby Patty"]
          p=[1.25,2,3,.25]
          menuBurger(q,c,p)
          q="Would you like a drink? (y/n) "
          c=["Seafoam Soda","Kelp Shake"]
          s=["Small","Medium","Large"]
          p=[1,1.25,1.50,2]
          menuDrink(q,c,s,p)
          q="Would you like fries? (y/n) "
          c=["Coral Bits","Kelp Rings"]
          s=["Small","Medium","Large"]
          p=[1,1.25,1.5,1.5]
          menuFries(q,c,s,p)
          q="Would you like some of the other stuff? (y/n) "
          c=["Krabby Meal", "Double Krabby Meal","Triple Krabby Meal","Salty Sea Dog","Footlong","Sailors Surprise","Golden Loaf"]
          p=[3.50,3.75,4,1.25,2,3,2]
          menuFoods(q,c,p)
          orderInfo+=(f"\tSubTotal: $\t{round(orderTotal,2)}\n")
          total+=orderTotal 
          ui = input("Would you like to add a order (y/n) ")
          orderTotal=0
     if ui == "n":
          print(orderInfo)
          finalTotal = (total*1.07)
          orderInfo+=(f"\tfinal Total: $\t{round(finalTotal,2)}\n")
elif ui == "n":
     print("Thank you for coming have a nice day")