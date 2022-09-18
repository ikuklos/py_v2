#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
#  Пример:
#  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import sample as sample

testList = sample(range(30), 10)
print(testList)
sumElements = 0

for oddNumber in range(0, len(testList), 2):
    sumElements += testList[oddNumber]

print(sumElements)