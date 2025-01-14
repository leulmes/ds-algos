
def selection_sort(nums):
    N = len(nums)

    for i in range(N):
        min = nums[i]
        idx = i
        for j in range(i, N):
            if nums[j] < min:
                min = nums[j]
                idx = j
        
        tmp = nums[i]
        print('min: ', min)
        nums[i] = min
        nums[idx] = tmp
    return nums

print(selection_sort([4, 3, 2, 4, 1]))
