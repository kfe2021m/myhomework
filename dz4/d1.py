from prosh import f


def swap(pl: list, k: int) -> list:
    k %= len(pl)
    return pl[-k:] + pl[:-k]


if __name__ == "__main__":
    print(swap(f(input()), int(input())))