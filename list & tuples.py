"""
list = ["one", "two", "three"]
tinylist = ["Done"]
list.remove("three")
list.append(1)
k = len(list)
print(list)
i = list.index("two")
print(i)
print(k)
print(list+tinylist)
"one" in list

"""
#List

range = [1, 2, 3, 4, 5, 10, 20, 30]

#print(range)
range.append(40)
print(range[0])

for x in range:

    if x > 5:
        range.remove(10)
        print(range)
        break


    else:

        print("Print", x)



"""
"""
# Creating tuple
tuple1 = (1, 2, 3)

#Converting tuple to list
y = list(tuple1)

print(y)
print(y[0])
print(y[1])
print(y[2])


# Tuple unpacking
a, b, *c = (1, 2, 3, 4)
print(a)
print(c)

"""
"""
#Listcomprehend

a1 = [1, 2, 23]
b1 = []

for x in a1:
    b1.append(x)
    #print("Comprehend ", b1[0])

print(b1)

"""
"""
# sort list
# Ascending default
numbers = [5, 1, 2, 3, 4]
numbers.sort()
# Descending default
print("This is ascending order ", numbers)
numbers.sort(reverse=True)
print(numbers)

"""
# copy

l2 = ["S", "b", "c"]
l3 = []

l3 = l2.copy()
print(l3)

"""














