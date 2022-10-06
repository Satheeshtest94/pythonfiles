"""
def add(a,b):
    return a+b

print(add(5,6))
"""
"""
h = [1,2,3,4]
i = [7,8,9,10]



print(list(map(lambda h,i:h+i, h,i)))



"""
"""
def even(x):

    if x %2 == 0:
        return x

print(even(3))

"""
"""
j = 10

m  =list(filter(lambda x:x%2 == 0,10))

print(m)
"""




import functools

num = [1,2,3,4,5]


j = functools.reduce(lambda x,y:x*y ,num)

print(j)
