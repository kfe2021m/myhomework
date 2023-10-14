from collections import Counter
from ty import f

def ff(n):
    print('Элемент | Частота')
    return Counter(n)


n = f()
v = ff(n)
print(*[f'{i} | {v[i]}' for i in v], sep='\n')