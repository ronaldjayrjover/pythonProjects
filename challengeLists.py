#add to the program below so that if it finds a meal without spam
#it prints out each of the ingredients of the meal
#You will need to setup the menu as we did in lines-13

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

#menuIng = list(menu)
#menuIng.sort(reverse=True)

#print(menu)

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredient in meal: # itong for loop para iprint niya yung meal nana nasa if not condition
            print(ingredient)
                #['egg', 'sausage', 'bacon']
                # egg
                # sausage
                # bacon
