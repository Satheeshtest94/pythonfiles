Vegetable = ("Lemon","Tomato","Cabbage","Potato")
fruits = ("Apple","Orange","Mango")

print("Concatenate:",Vegetable+fruits)

new = list(fruits)
print("After type casting:",new)

# Looping

for i in Vegetable:
    print(i)

#add

len(Vegetable)

print("Length:",len(Vegetable))

print("Last value:",Vegetable[-1])

for i in range(1,len(Vegetable)):
    print(Vegetable[i])


print(Vegetable.count("Lemon"))
print(Vegetable.index("Lemon"))




fruits += Vegetable

print(fruits)
