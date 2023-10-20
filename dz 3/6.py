def f(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


n = int(input())
if f(n):
    print('Простое число')
else:
    print('Непростое число')