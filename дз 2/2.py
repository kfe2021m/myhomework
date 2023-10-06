list = []
a = input('Введите:')
while a != '':
    list.append(a)
    a = input('Введите:')
list = sorted(list)[::-1]
l = ''.join(list)
print(l)