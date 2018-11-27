#augmented assignemnet is more on a shorthand version of a longhand, sample below

number = "9,223,372,036,854,775,807"
cleanNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanNumber = cleanNumber + number[i]
        # cleanNumber += number[i]  ## its the shorthand way of the top

newNumber = int(cleanNumber)
print("The number is {}".format(newNumber))


x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

greeting = "good"
greeting += " morning "
print(greeting)

greeting *= 5
print(greeting)

## other is <<= >>= &= ^= |= 