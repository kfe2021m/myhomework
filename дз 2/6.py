s = input('Введите строку:')
k = int(input('Введите число:'))
sch = 0
a = []
for x in s:
    if x in ('1234567890'):
        sch += 1
        a.append(x)
if sch < k:
    print('Нет такой')
else:
    print(a[k - 1])
        