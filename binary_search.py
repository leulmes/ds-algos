
#  Binary Search algorithm
#  This function returns the target and returns -1, if the target is not found.
#  Divide & Conquer algo
def binary_search(lst, target):
    if len(lst) == 0:
        return -1
    
    N = len(lst)
    l, r = 0, N - 1
    lst.sort() # Binary Search works only on a sorted list

    print('the left: ', l)
    print('the right: ', r)
    print('mid: ', (r - l) // 2)
    
    # we use <= instead of < to handle the casee of a 1 elt list. See example below...
    while l <= r:
        mid = (l + r) // 2
        print('mid: ', mid)
        
        if lst[mid] > target:
            # target could be in left subarray
            r = mid - 1
        elif lst[mid] < target:
            # target could be in right subarray
            l = mid + 1
        else:
            return lst[mid]

    return -1 # target not found

print(binary_search([0, 0, 4, 4, 6, 7, 8, 9, 9, 10, 12, 13, 13, 14, 14, 17, 18, 19, 19, 19], 17))
print(binary_search([1], 1)) # 1 element list example
    