lst = []
a = input('Введите:')
while a:
    lst.append(a)
    a = input('Введите:')
lst = sorted(lst, reverse=True)

print(''.join(lst)))