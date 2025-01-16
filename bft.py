

# 0 is False, 1 is True
def bf_traverse(adj_lst):
    N = len(adj_lst)
    visited = [0] * N
    visited[0] = 1 # assuming graph vertices start with 0
    order = [0]
    queue = [0]

    while queue:
        vertex = queue.pop(0)
        vertices = adj_lst[vertex] 

        for v in vertices:
            # if vertex is not visited, mark it as visited, add it to order
            if visited[v] == 0:
                visited[v] = 1
                order.append(v)
                queue.append(v)
            
    
    return order




print(bf_traverse([[1, 2], [0, 2], [0, 1, 3], [2]]))

