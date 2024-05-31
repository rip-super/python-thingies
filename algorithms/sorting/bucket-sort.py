def bucket_sort(arr):
    min_value = min(arr)
    max_value = max(arr)
    range_of_elements = max_value - min_value + 1
    buckets = [[] for _ in range(range_of_elements)]

    for num in arr:
        buckets[num - min_value].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

unordered_list = [3, 8, 1, 6, 2, 7, 4, 9, 5, 0]
print(unordered_list)
ordered_list = bucket_sort(unordered_list)
print(ordered_list)