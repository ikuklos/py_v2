x = int(input("введите координату X: "))
y = int(input("введите координату Y: "))
E = 0
if x > 0:
    if y > 0:
        E = 1
    else:
        E = 4
else:
    if y < 0:
        E = 3
    else:
        E = 2


print('x = ',x,";","y = ",y, " --> ", E)
