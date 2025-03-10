

def bubble_sort(lst):
    N = len(lst)

    for i in range(0, N):
        for j in range(0, N - i - 1):
            if lst[j] > lst[j + 1]:
                tmp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = tmp
        
    return lst
    



print(bubble_sort([10, 8, 6, 4, 3, 1]))