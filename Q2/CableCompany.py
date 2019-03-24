import sys
import heapq
kb = sys.stdin
def Prim(G):
    nv = len(G)
    INF = float('inf')
    d = [INF]*nv
    p = [None]*nv
    inMST = [False]*nv
    d[0]=0
    for i in range(nv):
        u = d.index(min(d))
        d[u] = INF
        inMST[u] = True
        for v in range(nv):
            if not inMST[v] and G[u][v] < d[v]:
                d[v] = G[u][v]
                #print(d)
                p[v] = u
    return p
nv = int(kb.readline())
G =[[0]*nv for k in range(nv)]
for u in range(nv-1):
    w = [int(e) for e in input().split()]
    for v in range(u+1,nv):
        G[u][v] = G[v][u] = w[v-u-1]
s = Prim(G)
out = 0
for i in range(1,nv):
    out+=G[i][s[i]]
print(out)
    
    
