def f(n):
    s = []
    while n:
        s.append(n)
        n = input()
    return s
n = input()
print(f(input('Введите:')))