def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Recursion
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    # Merging
    i = 0 # left_arr idx
    j = 0 # right_arr idx
    k = 0 # merged_arr idx
    merged_arr = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            j += 1
        k += 1

    while i < len(left_arr):
        merged_arr.append(left_arr[i])
        i += 1
        k += 1

    while j < len(right_arr):
        merged_arr.append(right_arr[j])
        j += 1
        k += 1
    
    return merged_arr

unordered_list = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
print(unordered_list)
ordered_list = merge_sort(unordered_list)
print(ordered_list)
