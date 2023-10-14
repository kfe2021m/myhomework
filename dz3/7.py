from collections import Counter

def f(text):
    u = max(text, key=len)
    c = Counter(text).most_common(1)[0][0]   # подсчет элементов
    print('Самое длинное: ' + u + ',самое частое: ' + c)


text = input().split()
f(text)