def f(n):
    a = []
    while n:
        a.append(n)
        n = input()
    lst = []
    print('Элемент | Частота')
    for x in a:
        if x not in lst:
            print(x, '|', a.count(x))
            lst.append(x)
n = input()
print(f(n))
