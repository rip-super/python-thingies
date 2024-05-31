def radix_sort(arr):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1

        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    max_value = max(arr)

    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    return arr

unordered_list = [3, 8, 1, 6, 2, 7, 4, 9, 5, 0]
print(unordered_list)
ordered_list = radix_sort(unordered_list)
print(ordered_list)