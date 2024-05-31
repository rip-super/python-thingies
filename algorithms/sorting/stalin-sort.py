def stalin_sort(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            del arr[i + 1]
        else:
            i += 1
    return arr

unordered_list = [3, 6, 8, 2, 4, 1, 7, 0, 9, 5]
print(unordered_list)
ordered_list = stalin_sort(unordered_list)
print(ordered_list)
