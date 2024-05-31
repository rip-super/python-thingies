def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Note that for binary search to work, the list must be in order
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = binary_search(arr, target)
if index != -1:
    print(f"Target ({target}) found at index [{index}] of the array.")
else:
    print(f"Target ({target}) not found in the array.")
