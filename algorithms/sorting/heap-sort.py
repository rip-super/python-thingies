def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i  
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  
            heapify(arr, n, largest)
            
    def build_max_heap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
    
    build_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
    return arr

unordered_list = [5, 3, 8, 2, 0, 9, 1, 4, 7, 6]
print(unordered_list)
ordered_list = heap_sort(unordered_list)
print(ordered_list)
