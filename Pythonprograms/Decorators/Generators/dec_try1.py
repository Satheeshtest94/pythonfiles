# this is decorator



def this_is_dec(a):
    print("First write this")
    a()


def new1():
    print("I am going to write")


this_is_dec = this_is_dec(new1)

