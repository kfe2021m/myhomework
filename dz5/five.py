from dz3.d1 import f


def binp(place, num):
    if place == []:
        return
    mid = len(place) // 2
    small = 0
    big = len(place) -1
    while place[mid] != num and small <= big:
        if num > place[mid]:
            small = mid + 1
        else:
            big = mid - 1
        mid = (small + big) // 2
    if small <= big:
        return mid


if __name__ == "__main__":
    print(binp(list(map(float, f(input()))), int(input())))