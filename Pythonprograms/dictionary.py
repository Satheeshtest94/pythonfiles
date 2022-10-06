""""
# Declare & access dictionary
k_dict = {'name': 'Jack', 'age': 26}

print(k_dict['name'])
print(k_dict['age'])

#Add & update

k_dict['address'] = 'downtown'
print(k_dict)
#print(k_dict['name'])
#print(k_dict['age'])
# remove unwanted item
print(k_dict.pop('age'))
print(k_dict)
# remove unwanted item at last
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.popitem())
print(squares)
# clear the dictionary
squares.clear()
print(squares)
# Delete the dictionary
#del squares
#print(squares)
# copy dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares2 = squares.copy()
print("Copied one", squares2)

"""
# nested dictionary


family = {"child1": {"name": 'Sat', "age": 2}, "child2": {"name": 'pat', "age": 3}, "child3": {"name": 'cat', "age": 4}}

print(family)

#copy

new = family.copy()
print(new)

# Dictionary loop with items to displaykey , value

for x, y in family.items():
    print(x, y)

#Value
#Key
for x in family.keys():
    print(x)

# Value
for x in family.values():
    print(x)
# pop remove last item
family.popitem()
print(family)
"""""
# del
del family["name"]
print(family)

"""

"""
# clear

family.clear()
print(family)

"""
"""
# add

family["name"] = 'satheesh'
family["age"] = 2

print(family)

"""

# update

family.update({"name": 'hai'})
print(family)











