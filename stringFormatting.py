__author__ = 'dev'
age = 24
print("My age is " + str(age) + " years")

###replace field == {}, meaning its replacing the formatting for age variable
print("My age is {0} years".format(age))

###replacing the field on {0 - 7} with 31 as 0 and months from 1-7
print("The are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "january"
     , "March", "May", "July", "Aug", "Oct", "Dec"))

print("""jan: {2}
feb: {0} 
mar: {1}
apr: {2}
may: {1}
jun: {2}
jul: {1}
aug: {2}
sep: {0}
oct: {1}
nov: {2}
dec: {0}""".format(20,30,31))


print("##### ENTERING STRING FORMAT OPERATOR #######")

##old format
print("My age is %d years" % age)

print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

###adding 2 or 4 on %d is to have a neat formatting on the output
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i **2, i **3 ))

print("Pi is approximately is %12.50f" %(22 / 7))

###new format
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}" .format(i, i **2, i **3 ))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}" .format(i, i **2, i **3 ))

print("Pi is approxiamtely {0:12.50f}".format( 22 / 7))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}" .format(i, i **2, i **3 ))
