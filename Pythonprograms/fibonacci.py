print("Enter the first number")
a = int(input())
print("Enter the second number")
b = int(input())
c = 0
print("Enter the length of series")
d = input()

for x in d:
    if x > d:
        c = c + 1
        a = b
        b = c
    print(a, b, c)
