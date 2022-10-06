def this_is_dec(a):
    def new():
        print("I am new")
        a()
    return new
#actual  function
@this_is_dec
def display():
    print("actual behaviour")

def new1():
    print("Hello")

#display = this_is_dec(new1)
#new1()
display()
