fruit = {"orange": "a sweert, orange, citrus fruit",
         "apple": "good for making cider" ,
         "lemon": "a citrus fruit" }

print(fruit)
# print(fruit["lemon"])
#
# ###to add to an exisiting dictionary
# fruit["pear"] = "an ood shaped apple"
# print(fruit)
# fruit["lime"] = "good for tequilla"
# print(fruit)
# ### to delete an entry from dict
# del fruit["lime"]
# print(fruit)

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we dont have a " + dict_key)




print("========")

bike = {"make": "Honda" , "engine": "250cc" , "color": "red", "engine_size": 250}
print(bike)
print(bike["engine_size"])