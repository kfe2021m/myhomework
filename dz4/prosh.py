def f(n):
    s = []
    while n:
        s.append(n)
        n = input()
    return s



print(f(input('Введите:')))