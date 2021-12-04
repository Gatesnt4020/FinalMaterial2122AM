from Order import Order
menu=["Krabby Patty","Double Krabby Patty","Triple Krabby Patty","Coral Bits","Kelp Rings","Krabby Meal", "Double Krabby Meal","Triple Krabby Meal","Salty Sea Dog","Footlong","Sailors Surprise","Golden Loaf","Kelp Shake","Seafoam Soda"]
order = []
total=0
menuPrice=[1.25,2.00,3.00,1.00,1.50,3.50,3.75,4.00,1.25,2.00,3.00,2.00,2.00,1.00]
masterOrder=[]
masterTotal=0
orderPrintOut=""
i=1

def showMenu():
     for i in menu:
          print(i)

def printOrder():
     for i in order:
          print(i)

greeting = (f"""What would you like to do?
"Menu" - See what the menu is
"Order" - Order something from the menu
"New order" - Make a new order
"Edit order" - Edit an order that has already been made
"Remove order" - Remove an order that has already been made
"Quit" - Finalize your order(s) and leave
""")


ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ").lower()
while ui != "y" and ui != "n":
     ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ").lower()
orderName = input("What is the name of the order ")
if ui == "y":
     while ui !="quit":
          ui = input(greeting).lower()
          if ui == "menu":
               showMenu()
          elif ui == "order":
               addFood = input("What do you want to add ")
               Order.menuChecker(addFood)
               if addFood == menu[0] or addFood == menu[1] or addFood == menu[2]:
                    ui = input("Would you like sea cheese with that(y/n) ").lower()
                    while ui != "y" and ui != "n":
                         ui = input("Would you like sea cheese with that(y/n) ").lower()
                    if ui == "y":
                         total+=0.25
                         addFood+=" w/ Sea Cheese"
                         order.append(addFood)
                    elif ui =="n":
                         order.append(addFood)
               elif addFood == menu[4] or addFood == menu[11]:
                    ui = input("Would you like salty sauce with that(y/n) ").lower()
                    while ui != "y" and ui != "n":
                         ui = input("Would you like salty sauce with that(y/n) ").lower()
                    if ui == "y":
                         addFood+=" w/ Salty Sauce"
                         order.append(addFood)
                         total+=0.50
                    elif ui =="n":
                         order.append(addFood)
               elif addFood == menu[3] or addFood == menu[13]:
                    ui = input("What size would you like (Small,Medium,Large) ").lower()
                    while ui != "small" and ui != "medium" and ui != "large":
                         ui = input("What size would you like (Small,Medium,Large) ").lower()
                    if ui == "small":
                         total+=0
                         order.append("Small Coral Bits")
                    elif ui == "medium":
                         total+=0.25
                         order.append("Medium Coral Bits")
                    elif ui == "large":
                         total+=0.50
                         order.append("Large Coral Bits")
               else:
                    order.append(addFood)
               for i in range(len(menu)):
                    if menu[i] == addFood:
                         total+=(menuPrice[i])
                    else:     
                         i+=1
          elif ui == "new order":
               if order==[]:
                    print("Please order something before adding another order\n")
               else:
                    orderName = input("What is the name of the order ")
                    masterOrder.append(orderPrintOut)
                    print("Add to your next order\n")
                    order = []
                    total=0
          elif ui == "edit order":
               if masterOrder==[]:
                    print("Please order something before editing an order\n")
               else:
                    for i in range(len(masterOrder)):
                         print(i)
                    ui = input("Which order would you like to edit ")
                    while(not ui.isdigit()):
                         ui = input("Which order would you like to edit ")
                    for i in range(len(masterOrder)):
                         if masterOrder[i]==int(ui):
                              print("hello")
          elif ui == "remove order":
               if masterOrder==[]:
                    print("Please order something before removing an order\n")
               else:
                    for i in range(len(masterOrder)):
                         print(i)
                    ui = input("Which order would you like to remove ")
                    while(not ui.isdigit()):
                         ui = input("Which order would you like to remove ")
                    ui = int(ui)
                    for i in range(len(masterOrder)):
                         if masterOrder[i]==ui:
                              del masterOrder[i]
                              break
          masterOrder.append(orderPrintOut)
          totalTotal = total*.07
          masterTotal+=totalTotal+total
          orderPrintOut = [f'''
{orderName}'s order:
     {printOrder()}
     Subtotal: ${total}
     ''']
     for i in masterOrder:
          print(i)
     print(masterOrder, end = '\n')
     print(f'''Final total: {round(masterTotal),2}''')
elif ui == "n":
     print("Thank you for coming have a nice day")