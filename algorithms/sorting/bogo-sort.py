import random

def bogo_sort(arr):
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    while not is_sorted(arr):
        random.shuffle(arr)
    return arr
    
unordered_list = [7, 1, 3, 0, 5 ,2, 6, 4, 8, 9]
print(unordered_list)
ordered_list = bogo_sort(unordered_list)
print(ordered_list)