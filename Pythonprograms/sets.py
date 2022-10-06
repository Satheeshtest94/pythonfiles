"""
s1 = {"hai", "Hello", "How are you"}
print(s1)
# Access
for x in s1:
    print(x)
# add
s1.add("No")
print(s1)
# remove
s1.remove("No")
print(s1)
"""
""""
# join
#union
s1 = {"hai", "Hello", "How are you"}
s2 = {"No", "buddy", "How are you"}
s3 = s1 .union(s2)
print(s3)
#update
s3 = s1 .update(s2)

"""

""""
# intersection update - want only duplicate funtion
s1 = {"hai", "Hello", "How are you"}
s2 = {"No", "buddy", "How are you"}
# s1.intersection_update(s2)
#print(s1)
#Common thing
#s3 = s1.intersection(s2)
#print(s3)
#Not present in both sets
s4 = s1.symmetric_difference(s2)
print(s4)

"""

