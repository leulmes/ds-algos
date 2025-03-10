
def insertion_sort(arr):
    N = len(arr)
    for i in range(1, N):
       j = i
       while arr[j - 1] > arr[j] and j > 0:
           arr[j - 1], arr[j] = arr[j], arr[j - 1]
           j -= 1
    return arr
        
print(insertion_sort([7, 2, 4, 1, 5, 3]))