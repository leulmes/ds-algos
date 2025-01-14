
def insertion_sort(nums):
    N = len(nums)

    # assume first elt is sorted, so start @ index 1
    for i in range(1, N):
        tmp = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = tmp

    return nums

print(insertion_sort([4, 3, 1, 8, 3]))