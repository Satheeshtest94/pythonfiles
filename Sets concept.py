fruits = {"Orange","Apple","Mango","Plum"}
fruits1 = [1,2,3,4]
"""
#add
fruits.add("Lemon")

print(fruits)
#remvove
fruits.remove("Lemon")

print(fruits)

#clear
#fruits.clear()

print(fruits)

#Copy





new = fruits.copy()

print("Copy:",new)

# Discard

fruits.discard("Plum")
print("Discard:",fruits)

#Pop

#fruits.pop()

#print(fruits)

#Remove

fruits.remove("Apple")

print(fruits)

#update

#fruits.update("Lemon1")

#print("Update:",fruits)

fruits.update(fruits1)

print(fruits)

"""
"""
#Difference

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print("Difference:",z)

# difference_update

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print("Difference_update:",x)

# intersection

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print("Intersection:",z)

#intersection_update

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print("Intersection_update:",x)

"""

"""

#is disjoint

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)

print("Is disjoint:",z)

# sub set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana","cherry"}

z = x.issubset(y)

print("Is Subset:",z)

#Super set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana","cherry"}

z = y.issuperset(x)

print("Is Subset:",z)

#union

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana","cherry"}

z = y.union(x)

print("Union:",z)

# Syemmetric


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana","cherry"}

z = y.symmetric_difference(x)

print("symmetric:",z)

#symmetric_update

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","banana","cherry"}

y.symmetric_difference_update(x)
print("symmetric_difference_update:",y)

"""

#Set discard
