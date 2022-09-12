# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = input('Введите число: ')
startPoint = 1
summary = 1
result = []

while startPoint <= int(N):
    summary = summary * startPoint
    result.append(summary)
    startPoint = startPoint + 1

print(result)