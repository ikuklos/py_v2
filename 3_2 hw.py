#    Напишите программу, которая найдёт произведение пар чисел списка.
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#    Пример:
#  - [2, 3, 4, 5, 6] => [12, 15, 16];
#  - [2, 3, 5, 6] => [12, 15]

from random import sample as sample

testList = sample(range(10), 5)
multipul = []
count = 0
lastNum = len(testList)-1
while count <= lastNum:
    multipul.append(testList[count]*testList[lastNum])
    count += 1
    lastNum -= 1

print(testList, '=>', multipul)