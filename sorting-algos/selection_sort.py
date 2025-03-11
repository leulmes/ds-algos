
def find_min_idx(start, arr):
    min_idx = start
    N = len(arr)

    for i in range(start, N):
        if arr[i] < arr[min_idx]:
            min_idx= i
    
    return min_idx

def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        min_idx = find_min_idx(i, arr)
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #swap
    return arr


print(selection_sort([4, 3, 2, 4, 1]))
