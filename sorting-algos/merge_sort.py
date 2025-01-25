
# merge sort algorithm
def merge_sort(nums):
    # base case: 1 elt list is sorted
    if len(nums) == 1:
        return nums
    
    # recursive case: keep halving list (split into left and right subarray)
    N = len(nums)
    # left subarray
    left = merge_sort(nums[0 : (N // 2) - 1])
    # right subarray
    right = merge_sort(nums[(N // 2) :])

    # merging step



print(merge_sort([5, 2, 1, 3, 6, 4]))
