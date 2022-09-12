#List
fruits = ["Apple","Orange","Mango"]
summerfruit = ["Mangostan","Blueberry"]


print(fruits)

#Loop through list

for i in fruits:
    print(i)

#Append

fruits.append("Kiwi")

print("Adding:",fruits)

#remove

fruits.remove("Kiwi")

print("Removing:",fruits)


# extend

fruits.extend(summerfruit)

print("Extended:",fruits)

#clear

#fruits.clear()

#print("Clear:",fruits)

# POP

print("POP:",fruits.pop(0))

#sort

summerfruit.sort()

#Before sort
print("Before sort:",summerfruit)
summerfruit.sort(reverse=True)
#After sort

print("After sort:",summerfruit)

print(fruits[-1])

fruits.insert(1,"Rambootan")

print("After insert:",fruits)

print("length of fruits:",len(fruits))




