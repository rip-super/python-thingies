def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1
    count = [0] * range_of_elements

    for num in arr:
        count[num - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    output = [0] * len(arr)

    for num in reversed(arr):
        output[count[num - min_value] - 1] = num
        count[num - min_value] -= 1

    return output


unordered_list = [2, 7, 4, 1, 8, 5, 3, 9, 0, 6]
print(unordered_list)
ordered_list = counting_sort(unordered_list)
print(ordered_list)
