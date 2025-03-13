
def quicksort_algo(arr):
    return quick_sort(arr, 0, len(arr) - 1)
    

def quick_sort(array, s, e):
    if s < e:
        mid = (s + e) // 2
        pivot = array[mid]
        index = partition(array, s, e, pivot)
        quick_sort(array, s, index - 1)
        quick_sort(array, index, e)

def partition(arr, l, r, pivot):
    while l <= r:
        while arr[l] < pivot:
            l += 1
        while arr[r] > pivot:
            r -= 1
            
        if l <= r:
            # swap
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return l

nums = [5, 2, 4, 1, 3]
nums2 = [2, 1, 6, 1, 8, 4, 5]
print("Before sort: ", nums)
quicksort_algo(nums)
print("After sort: ", nums)

print("============================")
print("Before sort: ", nums2)
quicksort_algo(nums2)
print("After sort: ", nums2)
