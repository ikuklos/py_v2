# Задайте список из n чисел последовательности Sn = (Sn-1 + 3) и выведите на экран их сумму.
# Пример
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

someDict = {1: 4}
n = int(input("Задайте длинну последовательности: "))
for key in range(2, n + 1):
    someDict[key] = someDict[key - 1] + 3
print(list(range(2, n+1)))
print(someDict)
