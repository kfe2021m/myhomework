s = input('Введите строку:')
k = int(input('Введите число:'))
sch = 0
for x in s:
    if x.isdigit():
        sch += 1
        if sch == k:
            print(x, 'ваше число')


        