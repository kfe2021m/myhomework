from prosh import f


def s_list(a, n):
    n %= len(a)
    return a[-n:] + a[:-n]


if __name__ == "__main__":
    print(s_list(f(), int(input("Введите число сдвига: "))))