# merge sort algorithm
# sort left
# sort right
# merge
# rounding trick: -(-(numerator) // denominator) rounds a number up
# this works b/c -(numerator) // denominator rounds a number to negative infinity, which is like rounding up in our case when we negate that result
def merge_sort(arr):
    if len(arr) > 1:
        left_subarray = arr[:len(arr) // 2]
        right_subarray = arr[len(arr) // 2:]

        # sort left
        merge_sort(left_subarray)
        merge_sort(right_subarray)

        # merge step
        ls_ptr, rs_ptr, idx = 0, 0, 0
        while ls_ptr < len(left_subarray) and rs_ptr < len(right_subarray):
            if left_subarray[ls_ptr] < right_subarray[rs_ptr]:
                arr[idx] = left_subarray[ls_ptr]
                ls_ptr += 1
                idx += 1
            else:
                arr[idx] = right_subarray[rs_ptr]
                rs_ptr += 1
                idx += 1
        
        while ls_ptr < len(left_subarray):
            arr[idx] = left_subarray[ls_ptr]
            ls_ptr += 1
            idx += 1

        while rs_ptr < len(right_subarray):
            arr[idx] = right_subarray[rs_ptr]
            rs_ptr += 1
            idx += 1

    return arr

print(merge_sort([2, 6, 5, 1, 7, 4, 3]))
# print(merge_sort([5, 2, 1, 3, 6, 4]))
# print(merge_sort([7, 8, 1, 0, 3, 2, 5, 8, 4, 9, 6]))
