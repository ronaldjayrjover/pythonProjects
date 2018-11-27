# shopping_list = ["milk", "pasta", "eggs", "bread" ]
# for item in shopping_list:
#     if item == "eggs":
#         print("I did not include " + item)
#         # continue ## it will continue to process if it hit the argument = egg
#         break # it will exit once it hit the argument
#
#     print("Buy " + item)



# meal = ["egg", "bacon", "spam", "saudages"]
#
# nasty_food_item = '' #this will initialize nasty food variable so even if it has no defined
#                      # it will still continue the loop as its defined before the condition
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         print("this is the" + item)
#         break
#
# if nasty_food_item:
#     print("Can i have anything withour spam in it? ")

meal = ["egg", "bacon", "spam", "saudages"]

nasty_food_item = '' #this will initialize nasty food variable so even if it has no defined
# it will still continue the loop as its defined before the condition
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        print("this is the" + item)
        break
else:
    print("ill have a plate of the, then, please") #if the loop has continue it will still run but will
                                                  # to else
if nasty_food_item:
    print("Can i have anything withour spam in it? ")