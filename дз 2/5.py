n=input('Введите:')
k=0
n=int(n[::-1])
while n>0:
    k=n%10
    print(k)
    n=n//10
    k=0