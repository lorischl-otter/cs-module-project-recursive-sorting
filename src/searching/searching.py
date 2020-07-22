# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # if empty array, return -1
    if start > end:
        return -1
    # once start and end pointing at same number, must return something
    if start == end:
        # if that number is the target, return that index
        if arr[start] == target:
            return start
        # otherwise, target not in list
        else:
            return -1

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


# Solution implemented in class
def descending_binary_search(arr, target, start, end):
    # coded in class
    if start > end:
        return -1
    # if empty array, return -1
    else:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return descending_binary_search(arr, target, start, mid-1)
        else:
            return descending_binary_search(arr, target, mid+1, end)


arr = [101, 99, 87, 76, 66, 65]
print(descending_binary_search(arr, 67, 0, len(arr)-1))


def agnostic_binary_search(arr, target):
    # figure out whether input array is ascending or descending
    # keep boolean to indicate order
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True

    # if ascending, call 'binary_search'
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    # otherwise, call 'descending_binary_search'
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)


print(agnostic_binary_search(arr, 67))
