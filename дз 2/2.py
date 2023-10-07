lst = []
a = input('Введите:')
while a != '':
    lst.append(a)
    a = input('Введите:')
lst = sorted(lst)[::-1]
l = ''.join(lst)
print(l)