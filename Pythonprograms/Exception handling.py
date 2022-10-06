"""
global x
x = -1
try:
    y = type(x)
    if y is not int:
     print("This is not int", x)
     raise ("Only int allowed")
    else:
        print("This is int")
except:
    print("This is unknown")
else:
    print("Unpredictable")
finally:
    print("we are overided the else")
"""

x = -1

if x < 1:
    raise Exception("Enter right no")

