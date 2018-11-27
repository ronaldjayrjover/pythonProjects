#for i in range(10):
#    print("i is now {}".format(i))
#
# i = 0
# while i < 10 :
#     print("i is now {}".format(i))
#     i += 1 ## if there is no increment the condition will just loop

# availableExits = ["north", "east", "south", "west"]
#
# chosenExit = ''
# while chosenExit not in availableExits:
#     chosenExit = input("Enter a direction: ")
#     ## add to break the loop not on the list
#     if chosenExit == "quit":
#         print("Game over")
#         break
#
# #print("Nice")
# ##the same as print("Nice") below
# else:
#     print("nice version 2")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")