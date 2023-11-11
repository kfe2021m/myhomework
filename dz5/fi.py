def binary_search(sequence, target):
    low, high = 0, len(sequence) - 1
    result = None
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] == target:
            result = mid
            high = mid - 1
        elif sequence[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

https://github.com/lec0baby/hardhw/blob/main/hardhw/dz5/ex5_1.py
