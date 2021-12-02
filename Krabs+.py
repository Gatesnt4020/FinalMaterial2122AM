from Order import Order
menu=["Krabby Patty","Double Krabby Patty","Triple Krabby Patty","Seafoam Soda","Kelp Shake","Coral Bits","Kelp Rings","Krabby Meal", "Double Krabby Meal","Triple Krabby Meal","Salty Sea Dog","Footlong","Sailors Surprise","Golden Loaf"]
masterOrder=[]

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

ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ")
while ui != "y" and ui != "n":
     ui = input("Welcome to the Krusty Krab would you like something today?(y/n) ")
if ui == "y":
     while ui !="Quit":
          ui = input(greeting)
          if ui == "Menu":
               showMenu()
          elif ui == "Order":#use the menuChecker on this 
               addFood = input("What do you want to add")
               #look at static method to d othis
               food = Order(addFood)
               masterOrder.append(food)
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
