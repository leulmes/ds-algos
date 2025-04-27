
def swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

def bubble_sort(lst):
    N = len(lst)
    flag = False 

    for i in range(N): # num of sorted elts
        for j in range(N - i - 1):
            if lst[j] > lst[j + 1]:
                swap(lst, j, j + 1)
                flag = True
        if not flag: # optimization for best case
            break


        

lst = [10, 9, 8, 7]
bubble_sort(lst)
print(lst)