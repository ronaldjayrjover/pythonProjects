# __author__ = 'dev'
# for i in range(1, 12):
#     print("No {} squared is {} and cubed is {:4}".format(i, i**2, i**4))
#
# print("#### Start of If  #####")
#
# name = input("Pls enter ur name: ")
# age = int(input("How old are you, {0}?: ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old to vote")
# else:
#     print("pls comeback in {0}".format(18 - age))

# print("Pls guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < 5:
#     print("Pls guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("well done")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > 5:
#     print("Pls guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("well donee ")
#     else:
#         print("Sorry you guess wrong")
# else:
#    print("You got it first time")

# print("##Complex If Else####")

# age = int(input("How ols are you? "))
#
# if age >=16 and age <=54:
# #if 16 <= age <== 65:
# #if 15 < age < 66:
#     print("Have a good day at work")
#
# if (age < 16) or (age > 65):
#     print("Enjoy")
# else:
#     print("Have a good day at work")

##if (some_condition) or (some_weird_function_that_does_stuff()):
# do something


# x = input("Enter a text: ")
# if x:
#     print("you entered '{}'".format(x))
# else:
#     print("no value")
#
# print(not True)
# print(not False)
#
#
# age = int(input("How ols are you? "))
#
# if not(age < 18):
#     print("Enjoy")
# else:
#     print("go back {0} years".format(18 - age))

# parrot = "Norwegian Blue"
#
# letter = input("Enter a character: ")
#
# if letter in parrot:
#     print("Give me an {} jay".format(letter))
# elif letter not in parrot:
#     print("No {} letter".format(letter))
# else:
#     print("I dont need that letter")

print("######START OF FOR LOOP#####")
# for i in range(1, 20):
#    print("i is now {}".format(i))

# number = "9,333,123,456,798,098"
# cleanedNumber = ''
# # for i in range(0, len(number)):
# #     print(number[i])
#
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print("THe numer is {}".format(newNumber))

number = "9,333,123,456,798,098"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)

for i in range(0, 100, 5):
    print("i is {} ".format(i))

for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j), end='\t')
        #print("######")