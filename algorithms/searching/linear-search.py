def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [2, 8, 5, 0, 3, 9, 7, 1, 6, 4]
target = 7
index = linear_search(arr, target)
if index != -1:
    print(f"Target ({target}) found at index [{index}] of the array.")
else:
    print(f"Target ({target}) not found in the array.")
