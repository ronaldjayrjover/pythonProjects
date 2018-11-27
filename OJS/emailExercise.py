import re

emails = ['brandon@opswerks.com', 'alex@opswerks.com', 'bennette_bakke@apple.com',
          'ben@opswerks.com', 'alex_carter2@apple.com', 'bennette_bakke@apple.com',
          'brandon_mcintyre@apple.com', 'sk@opswerks.com', 'alex@opswerks.com', 'alex_carter2@apple.com']


#* return all the items in the original list that are in the _apple.com_ domain
appleList = re.compile(".*@apple.com")
newappleList = list(filter(appleList.match, emails))

#* make sure the list is sorted *alphabetically*
newappleList.sort(reverse=False)
print(newappleList)

#* make sure all the emails in the result list are *unique*
newappleListU = []

for i in newappleList:
    if i not in newappleListU:
        newappleListU.append(i)

print(newappleListU)


print("####################### Another Exercise ########################")

emails2 = ['brandon@opswerks.com', 'alex@opswerks.com', 'bennette_bakke@apple.com',
          'ben@opswerks.com', 'alex_carter2@apple.com', 'bennette_bakke@apple.com',
          'brandon_mcintyre@apple.com', 'sk@opswerks.com', 'alex@opswerks.com', "alex_carter2@apple.com.biz", "alex_carter2@apple.com.biz", 'alex_carter2@apple.com']

#* return all the items in the original list that are in the _apple.com_ domain
appleList2 = re.compile(".*@apple.com*")
newappleList2 = list(filter(appleList.match, emails2))

#* make sure the list is sorted *alphabetically*
newappleList2.sort(reverse=False)
print(newappleList2)

#* make sure all the emails in the result list are *unique*
newappleListU2 = []

for i in newappleList2:
    if i not in newappleListU2:
        newappleListU2.append(i)

print(newappleListU2)

