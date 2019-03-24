def Bellman_Ford(G, s):
    INF = float('inf'); nv = len(G)
    d = [INF] * nv
    p = [None] * nv
    d[s] = 0
    for i in range(n+1):
        relax = False
        for u in range(n):
            for v,w in G[u]:
                if d[u]+w < d[v]:
                    d[v] = d[u]+w
                    p[v] = u
                    relax = True
    if relax: return None,None  # negative cycle
    return d, p
