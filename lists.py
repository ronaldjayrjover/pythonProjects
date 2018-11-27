# # # # ipAddress = input("Please enter an UP address: ")
# # # # print(ipAddress.count("."))
# # #
# # # parrot_list = ["non pin", "no more", "a stiff", "berret"]
# # # parrot_list.append("Norweigran")
# # # for state in parrot_list:
# # #     print("This parror is " + state)
# # #
# # #
# # # even = [2, 4, 6, 8]
# # # odd = [1, 3, 5, 7, 9]
# # #
# # # numbers = even + odd
# # # #numbers.sort() is equal to [1, 2, 3, 4, 5, 6, 7, 8, 9] when you call the print
# # # ## you can also use below method
# # # numbersInOrder = sorted(numbers)
# # #
# # # print(numbersInOrder)
# # #
# # # if numbers == numbersInOrder:
# # #     print("The list is equal")
# # # else:
# # #     print("The list are not equal")
# # #
# # # if numbersInOrder == sorted(numbers):
# # #     print("The list is equal")
# # # else:
# # #     print("The list are not equal")
# #
# # # list1 = []
# # # list2 = list()
# # #
# # # print("List 1: {}".format(list1))
# # # print("List 2: {}".format(list2))
# # #
# # # if list1 == list2:
# # #     print("The lists are equal")  ### parameters is the "inside" and print is the function
# # #
# # # print(list("The lists are equal")) ## list here is a function(builtin)
# # #
# #
# # # even = [2, 4, 6, 8]
# # # anotherEven = even
# # # anotherEven1 = list(even)
# # # print(anotherEven1 == even) # You are comparing , if anotherEven1 has the same value (not sorted) with even variable
# # # print(anotherEven1 is even) # THe difference from the == , is you are refering that anotherEven1 is contrstrcuted with the exact string value
# # # anotherEven.sort(reverse=True)
# # # print(even)
# #
# # even = [2, 4, 6, 8]
# # odd = [1, 3, 5, 7, 9]
# #
# # numbers = [even, odd]
# # #print(numbers) #[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
# # for numberSet in numbers:
# #     print(numberSet)
# #
# #     for value in numberSet:
# #         print(value)
# #
#
# menu = []
# menu.append(["egg", "spam", "bacon"])
# menu.append(["egg", "sausage", "bacon"])
# menu.append(["egg", "spam"])
# menu.append(["egg", "bacon", "spam"])
# menu.append(["egg", "bacon", "sausage", "spam"])
# menu.append(["spam", "bacon", "sausage", "spam"])
# menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
# menu.append(["spam", "egg", "sausage", "spam"])
#
# #print(menu)
#
# for meal in menu:
#     if not "spam" in meal:
#         print(meal)