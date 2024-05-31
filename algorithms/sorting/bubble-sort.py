def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
                
unordered_list = [4, 6, 9, 3, 0, 8, 1, 2, 7 ,5]
print(unordered_list)
ordered_list = bubble_sort(unordered_list)
print(ordered_list)
