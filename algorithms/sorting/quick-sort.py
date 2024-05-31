def quick_sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        if left < right:
            pivot = arr[right]
            i = left - 1
            for j in range(left, right):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[right] = arr[right], arr[i + 1]
            pivot_index = i + 1
            stack.append((left, pivot_index - 1))
            stack.append((pivot_index + 1, right))
    return arr

unordered_list = [22, 11, 88, 66, 55, 77, 33, 44]
print(unordered_list)
ordered_list = quick_sort(unordered_list)
print(ordered_list)