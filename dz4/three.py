def f(x):
    x = [(i, type(i)) for i in x]
    return len(x) == len(set(x))


if __name__ == "__main__":
    print(f([a for a in input().split()]))