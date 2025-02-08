
def binary_search(lst, target):
    if len(lst) == 0:
        return -1
    
    N = len(lst)
    l, r = 0, N - 1
    lst.sort() # sort a list

    print('the left: ', l)
    print('the right: ', r)
    print('mid: ', (r - l) // 2)
    
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
    