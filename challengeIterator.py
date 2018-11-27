#Create a list of items (you may use either strings or numbers in the list),
#then create an iterator using the iter() function.

#Use a for loop "n" times, where n is the number of items in your list.
#Each time rount the loop, use next() on your list to print the next item.
#
#hint: use the len() function rather than counting the number of items in the list.

items = ["item1", "item2", "item3", "item4", "item5",]

itemIterate = iter(items)
#print(itemIterate)



for n in range(0, len(items)): # para makuha niya yung lenght or number of items from 0-4
     nextItems = next(itemIterate) # another variable para sa next function
     print(nextItems) 
