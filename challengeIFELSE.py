name = input("Pls enter ur name: ")
age = int(input("Pls enter ur age: "))


###the person should be in the age of more than 18 and under 31, if true then welcome
### if not then sorry

if name:
    print("hi {} how are you".format(name))
else:
    print("pls enter ur name")

if (age > 17) and (age < 31):
    print("Hi {0}, enjoy ur vacation".format(name))
else:
    print("sorry")