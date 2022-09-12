# return one function from another function
"""
def add(x):
    def sum(y):

        return x+y
    return sum


a = add(5)
b = a(30)
print(b)

"""





def func1(x):
    def b(y):

        x+y
        return x+y

    return b


z = func1(5)
m = z(30)
print(m)