from Order import Order
menu=["Krabby Patty","Double Krabby Patty","Triple Krabby Patty","Seafoam Soda","Kelp Shake","Coral Bits","Kelp Rings","Krabby Meal", "Double Krabby Meal","Triple Krabby Meal","Salty Sea Dog","Footlong","Sailors Surprise","Golden Loaf"]
menuPrice=[1.25,2.00,3.00,1.00,1.50,3.50,3.75,4.00,1.25,2.00,3.00,2.00,2.00,1.00]
masterOrder=[]
masterPrice=[]
i=1

def addOns():
     if ui == "Small" or ui == "Medium" or ui == "Large":
          masterPrice.append(0.25)
     elif ui == "With sauce":
          masterPrice.append(0.50)
     elif ui == "With chesse":
          masterPrice.append(0.25)

def showMenu():
     for i in menu:
          print(i)

greeting = (f"""What would you like to do?
"Menu" - See what the menu is
"Order" - Order something from the menu
"New order" - Make a new order
"Edit order" - Edit an order that has already been made
"Remove order" - Remove an order that has already been made
"Quit" - Finalize your order(s) and leave
""")

#use ui for sizes because of how the menu is made 
ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ")
while ui != "y" and ui != "n":
     ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ")
if ui == "y":
     while ui !="Quit":
          ui = input(greeting)
          if ui == "Menu":
               showMenu()
          elif ui == "Order":#use the menuChecker on this 
               if masterOrder == []:
                    masterOrder.append([])
               #need to access list inside list to be able to add to different list
               addFood = input("What do you want to add")
               #look at static method to do this
               food = Order(addFood)#post=Post(username,message)
               Order.menuChecker
               masterOrder.append(food)
               for i in range(len(menu)):
                    if menu[i] == food:
                         masterPrice.append(menuPrice[i]) 
                    else:     
                         i+=1
          elif ui == "New order":
               if masterOrder==[]:
                    print("Please order something before adding another order")
               else:
                    masterOrder.append([])
                    print("Add to your next order")
          elif ui == "Edit order":#look order comment
               if masterOrder==[]:
                    print("Please order something before editing an order")
               else:
                     ui = input("Which order would you like to edit")
                     while(not ui.isdigit()):
                         ("Which order would you like to edit")
                     for i in range(len(masterOrder)):
                         if masterOrder[i]==ui:
                              print(masterOrder[ui])
                              #do the rest of editing prb like adding
          elif ui == "Remove order":
               if masterOrder==[]:
                    print("Please order something before removing an order")
               else:
                     ui = input("Which order would you like to remove")
                     while(not ui.isdigit()):
                         ui = input("Which order would you like to remove")
                     ui = int(ui)
                     for i in range(len(masterOrder)):
                         if masterOrder[i]==ui:
                              del masterOrder[i]
                              break
          ui = input(greeting)
     #print receipt  here
elif ui == "n":
     print("Thank you for coming have a nice day")

#use id()
#  for encryption or something
