def f(n):
#n = input()
    s = []
    while n:
        s.append(n)
        n = input()
    return s


if __name__ == '__main__':
    print(f(input('Введите:')))