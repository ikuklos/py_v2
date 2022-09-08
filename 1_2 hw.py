#   Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def nums(x):
    xyz = ["X", "Y", "Z"]
    a = []
    i = 0
    while i < len(xyz):
        a.append(input(F"Введите значение {xyz[i]}: "))
        i=i+1
    return a


def predicate(x):
    disucsion = not (x[0] or x[1] or x[2])
    print(disucsion)
    conuction = not x[0] and not x[1] and not x[2]
    print(conuction)
    result = disucsion == conuction
    return result


state = nums(3)

if predicate(state) == True:
    print("Предикт True")
else:
    print(f"Предикт False")