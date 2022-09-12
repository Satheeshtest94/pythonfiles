"""
# creating the new file using write mode
f = open("new1.txt","w")
# adding data to that file

f.write("Hello")
f.write("Closed\n")

# to confirm which mode
m = f.writable() #this will return true
#print(m)
m = f.readable() #this will return false
print(m)
"""

#To find which mode
f = open("new1.txt","w")
j = f.mode
#j = f.readlines()
print(j)

"""
f = open("new1.txt","w")
# adding list of items to the file
list = ['Hai','Hello','New']
f = open("new1.txt","w")
list = ['Hai1','Hello','New']
for i in range(3):

    f.writelines(list[i] + "\n")

f.close()

"""