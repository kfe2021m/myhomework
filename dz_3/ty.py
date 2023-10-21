def f(n):
    s = []
    while n:
        s.append(n)
        n = input()
    return s


if __name__ == '__main__':
    n = input()
    print(f(input('Введите:')))