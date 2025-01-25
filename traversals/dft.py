
from collections import deque
order = []
visited = set()

def dft_rec(adj_lst, s):
    # recursive
    order.append(s)
    visited.add(s)

    for v in adj_lst[s]:
        if v not in visited:
            dft_rec(adj_lst, v)
    return

def dft_it(adj_lst, s):
    # iterative
    stack = deque([s])
    order = []
    visited = set()

    while stack:
        top = stack.pop()
        
        if top not in visited:
            visited.add(top)
            order.append(top)
            for v in adj_lst[top]:
                if v not in visited:
                    stack.append(v)
    return order




print(dft_rec([[3, 2, 1], [4, 3, 0], [0], [1, 0], [1]], 0))
print(order)

print(dft_it([[1, 2, 3], [0, 3, 4], [0], [0, 1], [1]], 0))