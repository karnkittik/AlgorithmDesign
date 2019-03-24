import heapq
def Dijkstra(G,s):
    nv = len(G)
    inf = float('inf')
    d = [inf]*nv
    p = [None]*nv
    d[s] = 0
    H = [(d[s],s)]
    while len(H)>0:
        du,u = heapq.heappop(H)
        for v,w in G[u]:
            if d[u]+w<d[v]:
                d[v] = d[u]+w
                p[v] = u
                heapq.heappush(H,(d[v],v))
    return d
G = [[(1,2),(2,8),(3,3)],[(0,2),(2,5),(3,7)],[(0,8),(1,5),(3,4)],[(0,3),(1,7),(2,4)]]
print(Dijkstra(G,0))
