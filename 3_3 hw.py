# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#   Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#нижепредставленный код колхозный, некрасивый работает только в рамках генерируемого списка, но работает.

from random import sample as sample

testListFloat = []

for i in sample(range(10000), 10):
    testListFloat.append(i/100)

maxFractions = 0
minFractions = 0
difference = maxFractions - minFractions

onlyFractions = []
for decim in testListFloat:
    onlyFractions.append(int((round(decim-int(decim/1), 2))*100))
onlyFractions.sort()

print(testListFloat, '=>', (onlyFractions[len(onlyFractions)-1] - onlyFractions[0])/100)

