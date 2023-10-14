

def f(n):
    fi = [0,1]
    for x in range(2,n):
        fi.append(fi[x-1]+fi[x-2])
    print(' '.join(str(w) for w in fi[:n]))

n=int(input())
f(n)
