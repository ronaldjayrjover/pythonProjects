string = "1234567890"
# for char in string:
#     print(string)

#myIterator = iter(string)
#print(myIterator)
#print(next(myIterator)) ### it iterates 2 times (because of below) on all the string
#print(next(myIterator))
#### next is also the same as for loop , its the "silent one or running in the background type of iterator"

for char in string:
    print(char)

for char in iter(string):
    print(char)
