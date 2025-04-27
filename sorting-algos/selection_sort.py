
def find_min_idx(start, lst):
    N = len(lst)
    min_idx = start

    for i in range(start, N):
        if lst[min_idx] > lst[i]:
            min_idx = i
    return min_idx

# stability can be broken if duplicates are present b/c we don't check for it
def selection_sort(lst):
    N = len(lst)
    for i in range(N):
        idx = find_min_idx(i, lst)
        lst[i], lst[idx] = lst[idx], lst[i]
    return lst




print(selection_sort([4, 3, 2, 4, 1]))
