# Python's range() Parameters
# The range() function has two sets of parameters, as follows:
#
# range(stop)
#
# stop: Number of integers (whole numbers) to generate, starting from zero. eg. range(3) == [0, 1, 2].
# range([start], stop[, step])
#
# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.



# myList = list(range(10))
# print(myList)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)

# myString = "abcdefghijklmnopqrstuvwxz"
# ### below prints will give you what is the index number of e and what is the string on the 4th number, 0=a,1=b,2=c,3=d,4=e
# print(myString.index('e'))
# print(myString[4])
#
# smallDecimals = range(0, 10)
# print(smallDecimals)
# print(smallDecimals.index(3))
#
#
# odd = range(1, 10000, 2)
# print(odd)
# print(odd[985])
#
# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisble by seven".format(x))
# else:
#     print("{} is not divisible by seven".format(x))
#
# myRange = smallDecimals[::2]
# print(myRange)
# print(myRange.index(4))

decimals = range(0, 100)
print(decimals)
#
myRange = decimals[6:80:3]  ###on range when you specify range(0,100) ibig sabihin 0-100 range mo now
#pag nag splice ka and you have used about variable(myRange) 6-is your base, 80-range to splice and 3 is yung number ng splice
print(myRange)
#
for i in myRange:
     print(i)
#
# print('x' * 40) #seperator only
#
# for i in range(3, 40, 3):
#     print(i)
#
# print(myRange == range(3, 40, 3))

# decimals = range(0, 100)
# myRange = decimals[3:40:3]
# #testing for equality
# print(myRange == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
# print('x' * 50)
#
# for i in range(99, 0, -2):
#     print(i)
#
# print('x' * 50)
#
# #testng for equality
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# backString = "egaugnal lufrewop yrev a si nohtyP"
# print(backString[::-1])
#
# r = range(0,10)
# for i in r[::-1]:
#     print(i)