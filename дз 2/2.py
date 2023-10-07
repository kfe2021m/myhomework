lst = []
a = input('Введите:')
while a != '':
    lst.append(a)
    a = input('Введите:')
lst = reversed(sorted(lst))
l = ''.join(lst)
print(l)