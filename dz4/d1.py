from dz3.d1 import f


def swap(pl, k):
    k %= len(pl)
    return pl[-k:] + pl[:-k]


if __name__ == "__main__":
    print(swap(f(input()), int(input())))