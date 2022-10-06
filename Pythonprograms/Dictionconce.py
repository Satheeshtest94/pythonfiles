Subject = ["Poet","Liner"]
courses = {"science":"Botany","Maths":"Algebra","English":"Grammer","addition":Subject}

"""

print(courses)
print(type(courses))

print(len(courses))
print(Subject)

"""

#print(courses["addition"])
"""
for i in courses["addition"]:
        print(i)
"""
"""

for i in courses.keys():
    print(courses.get(i))


print(courses.values())


print(courses.items())


if "Addition" in courses:print("Yes it is!....")
else:print("not it is")

"""

"""

var1 =5
var2 =6


var1 =var2 if var1 < var2 else var1

print(var2)
"""
"""





#print(courses["addition1"])

#print(courses.get("addition"))

#print(courses.keys())


"""



"""

#j = int(input("Any:"))

if j := int(input("Any:")) == 1:print("fine")
else:
    print("No")

"""

"""
Subject = ["Poet","Liner"]
courses = {"science":"Botany","Maths":"Algebra","English":"Grammer","addition":Subject}

if "addition" in courses:print("Yes it is!....")
else:print("not it is")

courses["English"] ="Poem"
print(courses)

courses.update({"Maths3":"Derivatives"})
print(courses)

courses.pop("Maths")
courses.popitem()

#del courses


print(courses)


#courses.clear()
print(courses)

jk = courses.copy()
print(jk)
"""
"""
for x,y in courses.items():
    print(x,y)
"""


fooditems = ("Idly","Pongal","Poori")

price = 100

menu  = courses.setdefault("New1","hspps")


#menu = dict.fromkeys(fooditems,price)

print(courses)