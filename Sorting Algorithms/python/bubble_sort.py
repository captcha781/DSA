def bubble_sort(arr: list, n: int) -> list:
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def recursive_bubble_sort(arr: list, n: int) -> list or function:
    if n == 1:
        return arr
    else:
        for i in range(0, n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return recursive_bubble_sort(arr, n - 1)


array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)
result = recursive_bubble_sort(array, n)
print(result)
