def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
        arr[i],arr[cur_min_idx] = arr[cur_min_idx], arr[i]
    return arr

unordered_list = [2, 6, 5, 1, 3, 4]
print(unordered_list)
ordered_list = selection_sort(unordered_list)
print(ordered_list)