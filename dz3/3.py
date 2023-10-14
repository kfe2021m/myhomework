def f(n):
    fi = [0,1]
    for _ in range(2, n):
        fi.append(fi[-1] + fi[-2])
    print(' '.join(str(w) for w in fi[:n]))


n = int(input())
f(n)
