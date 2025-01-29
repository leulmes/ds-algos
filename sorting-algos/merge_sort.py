

# merge sort algorithm
def merge_sort(lst):
    # base case: if len(lst) == 1, we return lst
    if len(lst) > 1:
        # recursive case: keep halving list (split into left and right subarray)
        N = len(lst)
        left_arr = lst[:(N // 2)]
        right_arr = lst[(N // 2):]

        merge_sort(left_arr) # left subarray
        merge_sort(right_arr) # right subarray

        # merge step
        l, r, i = 0, 0, 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] > right_arr[r]:
                lst[i] = right_arr[r]
                r += 1
            else:
                lst[i] = left_arr[l]
                l += 1
            i += 1
        
        # left list is exhausted before right list, add all elts of right list
        while r < len(right_arr):
            lst[i] = right_arr[r]
            r += 1
            i += 1
    
        # right list is exhausted before left list, add all elts of left list
        while l < len(left_arr):
            lst[i] = left_arr[l]
            l += 1
            i += 1
        
    return lst 


print(merge_sort([5, 2, 1, 3, 6, 4]))
print(merge_sort([7, 8, 1, 0, 3, 2, 5, 8, 4, 9, 6]))
