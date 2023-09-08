from collections import deque

def topological_sort_DFS(G):
    n = len(G)
    visited = [False]*n

    sorted_graph = []

    def dfs_visit(v):
        nonlocal G, visited

        visited[v] = True
        for adj in G[v]:
            if not visited[adj]:
                dfs_visit(adj)

        sorted_graph.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)

    sorted_graph.reverse()

    return sorted_graph


def topological_sort_kahns(G):
        n = len(G)
        in_degree = [0]*n
        
        for v in range(n):
            for adj in G[v]:
                in_degree[adj] += 1
 
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
 
        cnt_of_visited = 0
        top_order = []
 
        while queue:
            u = queue.popleft()
            top_order.append(u)

            for i in G[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
 
            cnt_of_visited += 1
 
        if cnt_of_visited != n:
            return "Cycle in graph"
        else:
            return top_order


G = [[3, 2],
     [0,2, 3],
     [3],
     []]

print(topological_sort_DFS(G))
print(topological_sort_kahns(G))