k=0
n=int(input())
def f(n):
    k=0
    for x in range(1,n+1):
        k=k+x
        print(x, end='')
f(n)
