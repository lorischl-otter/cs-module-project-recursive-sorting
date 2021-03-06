# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    # create pointers
    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    if a < len(arrA):
        merged_arr.extend(arrA[a:])

    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr
    # Incomplete attempt before class

    # num_elements = len(arrA) + len(arrB)
    # merged_arr = []
    # while num_elements > 0:
    #     if arrA[0] < arrB[0]:
    #         merged_arr.append(arrA[0])
    #         arrA.pop(0)
    #         num_elements -= 1
    #     else:
    #         merged_arr.append(arrB[0])
    #         arrB.pop(0)
    #         num_elements -= 1
    # return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr

    # Incomplete attempt before class
    # # if array is empty or only contains one item, return array
    # if len(arr) <= 1:
    #     return arr
    # # if array is 2 elements, utilize merge function
    # elif len(arr) == 2:
    #     return merge(, arr[1])
    # # if array is over 2 elements, continue recursive splitting
    # else:
    #     start = 0
    #     end = len(arr) - 1
    #     mid = len(arr) // 2
    #     return merge_sort(arr[start:mid]) + merge_sort(arr[mid:end])
    #     # call merge_sort on both halves

    # return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, left, right):
    # Your code here
    pass
