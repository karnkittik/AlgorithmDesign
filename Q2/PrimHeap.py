#PrimHeap
import heapq
def Prim(G):
    INF = float('inf')
    nv = len(G)
    d = [INF]*nv
    p = [None]*nv
    inMST = [False]*nv
    s = 0
    d[s]=0
    H = [(d[s],s)]
    while len(H)>0:
        du,u = heapq.heappop(H)
        inMST[u]=True
        for v,w in G[u]:
            if not inMST[v] and w<d[v]:
                d[v]=w
                p[v]=u
                heapq.heappush(H,(d[v],v))
    return p
G = [[(1,2),(2,3),(3,3)],[(0,2),(2,5),(3,7)],[(0,3),(1,5),(3,4)],[(0,3),(1,7),(2,4)]]
print(Prim(G))
