def swap(lst, x, y):
    tmp = lst[x]
    lst[x] = lst[y]
    lst[y] = tmp

def bubble_sort(nums):
    N = len(nums)
    for i in range(N):
        for j in range(0, N - 1):
            if nums[j] > nums[j + 1]:
                print(f'{nums[j]} is > than {nums[j + 1]}')
                print(f'swapping {nums[j]} and {nums[j + 1]}')
                print('list BEFORE swap: ', nums)
                swap(nums, j, j + 1)
                print('list AFTER swap: ', nums)
    return nums
    
# print(bubble_sort([2, 4, 1, 5, 3, 7]))
print(bubble_sort([8, 4, 3, 4, 1]))

# Time: O(n^2) -> n iterations for outer loop in worst case, n - 1 iterations for inner loop in worst case

# Space: O(1) b/c no new DS or memory was used. We modified the input list in-place

# Stability: Stable sort. Order of identical entries is PRESERVED

# In-Place? List is sorted by moving elements within the list
