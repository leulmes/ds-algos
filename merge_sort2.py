
def merge_sort(lst):
    N = len(lst)
    i = 0

    if N > 1:
        left_sub = lst[0:(N // 2)]
        right_sub = lst[(N // 2):]

        ls = merge_sort(left_sub)
        rs = merge_sort(right_sub)

        # merging step
        L, R, i = 0, 0, 0
        lsLen, rsLen = len(ls), len(rs)
        new_lst = [0] * (lsLen + rsLen) # initialize an array of 0's of len (lsLen + rsLen)

        while L < lsLen and R < rsLen:
            if ls[L] <= rs[R]: # use <= to preserve stability
                new_lst[i] = ls[L]
                L += 1
            else:
                new_lst[i] = rs[R]
                R += 1
            i += 1

        # this is for when the subarrays are not the same length
        if L >= lsLen:
            while R < rsLen:
                new_lst[i] = rs[R]
                R += 1
                i += 1
        if R >= rsLen:
            while L < lsLen:
                new_lst[i] = ls[L]
                L += 1
                i += 1

        return new_lst
                
    return lst

    
arr = [7, 8, 1, 0, 3, 2, 5, 8, 4, 9, 6]
print("before sort: ", arr)
arr2 = merge_sort([7, 8, 1, 0, 3, 2, 5, 8, 4, 9, 6])
print("after sort: ", arr2)


    