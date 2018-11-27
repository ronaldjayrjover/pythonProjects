#Challenge part1

# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

ipAddress = input("Pls enter ur IP Address: " )
segment = 1
segmentLength = 0
char = ''  ## as I have observed (jay) if theres a variable inside a loop and it did not break you should have to initialize first

for char in ipAddress:
    if  char == '.':
        print("segment {} contains {} characters".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1

#because the last character on the input string is not a . , so it did not print the last segment

if char != '.':
    print("segment {} contains {} characters".format(segment, segmentLength))

#### if we enter a no value on the input, it will spit our an error because the loop did not run and the char did not initialize
### so there is no char value on the 2nd if condition
### need to initialize char before the loop with an empty value

#### part 2 of the video - explaining the sneaky method above , 2nd if condition

ipAddress = input("Pls enter ur IP Address: " )
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segmentLength = 0
#char = ''  ## as I have observed (jay) if theres a variable inside a loop and it did not break you should have to initialize first

for char in ipAddress:
    if  char == '.':
        print("segment {} contains {} characters".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1

#because the last character on the input string is not a . , so it did not print the last segment

#if char != '.':
#   print("segment {} contains {} characters".format(segment, segmentLength))