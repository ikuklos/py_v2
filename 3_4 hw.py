#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

number = 45

def decimalTobinary(x):
    bitNumber = ''
    xForEnd = x
    while x > 0:
        bitNumber = f'{x % 2}' + bitNumber
        x = x//2
    print(xForEnd, ' -> ', bitNumber)

decimalTobinary(45)
decimalTobinary(3)
decimalTobinary(2)