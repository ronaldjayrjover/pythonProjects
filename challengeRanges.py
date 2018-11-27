#Experiment with different ranges and slice to get a feel for how they work.
#Remember that you can print the range as well as iterating through it to print
#its values, to check that your ranges are what you expected
#You may also want to include things like.
#


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


o = range(0, 100, 4)
print(o)

p = o[::2]
print(p)

for i in p:
    print(i)

#and see if you can work out what will be printed before running the program. If you are unsure, use a
#for loop to print our the values of o to see why p returns what it does

