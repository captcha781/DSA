def insertion_sort(arr: list, n:int) -> list:
    key = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    return arr

array = [12, 11, 13, 5, 6]
print(insertion_sort(array, len(array)))