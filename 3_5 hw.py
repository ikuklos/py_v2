# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# еще одно ужасное решение которое затыкается на -10000, но тз в виде k = -8 - отрабатывает

f = -8
itsNegafibonaci = False
if f < 0:
    itsNegafibonaci = True

fibonaciNumbers = []
if f >= 2:
    fibonaciNumbers.append(0)
    fibonaciNumbers.append(1)
elif f <= -2:
    fibonaciNumbers.append(0)
    fibonaciNumbers.append(1)
    f = -f


count = 0
while f >= 0:
    fibonaciNumbers.append(fibonaciNumbers[count] + fibonaciNumbers[count + 1])
    count += 1
    f -= 1

countList = len(fibonaciNumbers) - 1


if itsNegafibonaci is True:
    while countList > 0:
        fibonaciNumbers.append(-fibonaciNumbers[countList])
        countList -= 1

print(sorted(fibonaciNumbers))
