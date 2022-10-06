# inner function,passing function as argument
def display(msg):
    print("This will be second executed line")
    print(msg)


def mid(newfunc):
    print("This will be first executed line")
    #newfunc("This will be third executed line")


print("This will be 0th position")
# Calling one function from another func
#mid(display)
print("This will be terminated")
# storing function to the variable
# Single function but done dual action
a = display
a("Hello I am new")
display("Hello i am new1")
