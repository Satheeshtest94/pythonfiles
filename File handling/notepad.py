# Creating the new file

for i in range(90):
 a = open("notepad.txt", "w")
 b = input("Enter the text to enter:")
 a.write(b)
 a2 = open("notepad.txt", "r")
 a2 = open("notepad.txt", "a")
 c= input("Enter the text to enter:")
 a2.write(c)
