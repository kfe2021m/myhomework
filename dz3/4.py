from collections import Counter
def f(n):
    a = []
    while n:
        a.append(n)
        n = input()
    lst = []
    print('Элемент | Частота')
    c = Counter(a)
    return c
    #for x in a:
     #   if x not in lst:
      #      print(x, '|', a.count(x))
       #     lst.append(x)


n = input()
v=f(n)
print(*[f'{i} | {v[i]}' for i in v], sep='\n')
