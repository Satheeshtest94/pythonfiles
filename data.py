"""
def math():
    a =5
    def add():
        b =6
        c = a+b
        return c
    return add

obj  = math()
print(obj())



def math():
    print("No1")

def add(v):
    print("No2")
    v()
add(math)

"""
"""

def func2(func):
    def inner():
     s = func()
     return s.upper()
    return inner


@func2
def func1():
    return "Hi hello buddy"


obj = func2(func1)

print(func1())


"""
def handle(func):
    def inner(a,b):
        if b == 0:
            return "Denominator should not be zero"
        return a/b
    return inner
@handle
def div(a,b):
    return a/b

print(div(5,8))
