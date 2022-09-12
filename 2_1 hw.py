# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

inputNumber = input('Введите ваше число: ')
summary = 0

for x in inputNumber:
    if x.isnumeric():
        summary = summary + int(x)
print(summary)