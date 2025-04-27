
def insertion_sort(lst):
    N = len(lst)
    currElt = 0

    for i in range(1, N):
        j = i
        currElt = lst[i]
        while j >= 1 and lst[j - 1] >= currElt:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = currElt
    return lst
        
print(insertion_sort([7, 2, 4, 1, 5, 3]))
