def topological_sort(G):
    n = len(G)
    visited = [False]*n

    sorted_graph = []

    def dfs_visit(v):
        nonlocal G, visited

        visited[v] = True
        for adj,_ in G[v]:
            if not visited[adj]:
                dfs_visit(adj)

        sorted_graph.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)

    sorted_graph.reverse()

    return sorted_graph

def shortest_path_DAG(G, s):
    n = len(G)
    order = topological_sort(G)

    distance = [float("inf")]*n
    distance[s] = 0

    ind = 0

    while order[ind] != s:
        ind += 1
    
    for i in range(ind, n):
        for adj, w in G[order[i]]:
            if distance[adj] > distance[order[i]] + w:
                distance[adj] = distance[order[i]] + w
    
    return distance