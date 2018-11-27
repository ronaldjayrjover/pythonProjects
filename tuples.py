#order set of data, inmuttable(cannot be changed) but list can be change

# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda may", 2011
metallica = "Ride the Lightning", "Metallica", 1984
print('=' * 50)
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
print('=' * 50)
#metallica[0] = "Master of Puppets" ## error kasi immutable nga tuples so hindi mo pwedeng palitan ang value

###sneaky way is mag lagay ka panibagong declaration ng variable using yung slicing through sa tuple
###see below
imelda = imelda[0], "Imelda day", imelda[2] #pinalitan yung Emilda may to Imelda May by using pa rin yung value ng index 0 at index 2
print(imelda)
print('=' * 50)
###List ang metallica2
metallica2 = ["Ride the lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)
