# creating a new file to use append mode
import os
a = open("new2.txt", "w")
m = a.mode
print(m)
a.write("Hello world")

os.remove("new1.txt")


