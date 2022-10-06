"""
a  = "satheesh is a student hello hai"

print(len(a))

x = "satheesh" in a

print(x)

#a = "\Satheesh"

#print(a)

#a = r"C:\new"

#print(a)

for each in range(0,len(a)):
    print(a[each])






#len(a)


"""

# To check no of t in a

a  = "   satheesh is a student hello hai    "
count =0
for x in range(0,21):
    if (a[x]) == "t":
      count = count +1
print(count)

j = "t" not in a

print(j)
a  = "satheesh is a student hello hai"
print(a.upper())
print(a.lower())

k  =len(a)
# Slicing
print(a[2:5])
# Left strip
print(a.lstrip())
# right strip
print(a.rstrip())

print(a.replace("t","T"))
print(a.split("a"))

a = "Satheesh \"kumar\""
b = "Here"
print(a+b)

print(a)

print(a.startswith("sat"))
print(a.endswith("km"))
print(a.count(a))

print(a[0:5])
