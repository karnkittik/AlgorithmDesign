#Prim
def Prim(G):
    INF = float('inf')
    nv = len(G)
    d = [INF]*nv
    p = [None]*nv
    inMST = [False]*nv
    d[0] = 0
    for i in range(nv):
        u = d.index(min(d))
        d[u]= INF
        inMST[u] = True
        for v in range(nv):
            if not inMST[v] and G[u][v] < d[v]:
                d[v] = G[u][v]
                p[v] = u
    return p
G = [[0,2,3,5],[2,0,6,7],[3,6,0,4],[5,7,4,0]]
print(Prim(G))
