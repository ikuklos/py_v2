# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
import random

N = int(input('Введите число: '))
testList = list(range(-N, N + 1))

testFile = open('file.txt', 'w+')
testFile.writelines(f'{random.randint(-N, N + 1)},{random.randint(-N, N + 1)}')
testFile.close()

testFile = open('file.txt', 'r')
listFile = list(testFile.readlines())
testFile.close()

print('Произведение элементов из заданного списка: ',testList[int(listFile[0].split(',')[0])]*testList[int(listFile[0].split(',')[1])])

# Есть простор для улучшения всего, но все работает согласно ТЗ :)