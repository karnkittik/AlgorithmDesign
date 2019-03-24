import copy
def Johnson(G):
    K = copy.deepcopy(G)
    K.append([(u,0) for u in range(nv)])
    h, p = Bellman_Ford(K, len(K)-1)
    if h == None: return None,None   # negative cycle
    for u in range(len(K)):
        for i in range(len(K[u])):
            v,w = K[u][i]
            K[u][i] = (v, w + (h[u]-h[v]))
    D = []; P = []
    for u in range(len(K)):
        d, p = Dijkstra(K, u)
        for v in range(len(K)):
            d[v] -= (h[u] - h[v])
        D.append(d[:-1]); P.append(p[:-1])
    return D, P
