def Floyd_Warshall(G):  # Adjacency Matrix
    INF = float('inf'); nv = len(G)
    P = [[None]*nv for i in range(nv)]
    for u in range(nv):
        for v in range(nv):
            if u!=v and G[u][v] != INF:
                P[u][v] = u
    D = [list(G[u]) for u in range(nv)]
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                if D[i][k]+D[k][j] < D[i][j]:
                    D[i][j] = D[i][k]+D[k][j]
                    P[i][j] = P[k][j]
    return D, P
