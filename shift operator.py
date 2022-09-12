

x = 5

print("before shift", bin(x))
xy = x >> 2
print("After right shift ",  xy, "Binary", bin(xy), "Converting binary to int ", int(xy))
xy = x << 2
print("After left shift ",  xy, "Binary", bin(xy), "Converting binary to int ", int(xy))


# invert operator
a = 20
print(~a)

#& - And both shoudld be 1 & return 0
#| - OR either any 1 return1 else 0
#~ - Not = 1 as 0 & 0 as 1
#^ - XOR 1& 0  = 1 & 0
