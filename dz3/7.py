from collections import Counter

text = input().split()
def f(text):
    u = max(text, key=len)
    c = Counter(text).most_common(1)[0][0]   # подсчет элементов
    print('Самое длинное: ' + u + ',самое частое: ' + c)
f(text)