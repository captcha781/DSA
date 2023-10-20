def selection_sort (arr: list, n: int) -> list:
    for i in range(0, n-1):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

arr = [64, 25, 12, 22, 11]
print(selection_sort(arr, len(arr)))
    