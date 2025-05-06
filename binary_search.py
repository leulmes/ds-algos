#  Binary Search algorithm
#  This function returns the target and returns -1, if the target is not found.
#  Divide & Conquer algo
def binary_search(lst, target):
    l, r = 0, len(lst) - 1
    lst.sort()

    while l <= r:
        mid = (r + l) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
            
    return -1



print(binary_search([0, 0, 4, 4, 6, 7, 8, 9, 9, 10, 12, 13, 13, 14, 14, 17, 18, 19, 19, 19], 17))
print(binary_search([1], 1)) # 1 element list example
    