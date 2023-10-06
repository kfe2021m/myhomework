from random import randint
r = randint(0, 100)
a = int(input('Введите число:'))
if a == r:
        print('Вы угадали!')
while a != r:
    if a < r:
        print('Загаданное число больше!')
    else:
        print('Загаданное число меньше')
    a = int(input('Введите число:'))
print('Вы угадали')