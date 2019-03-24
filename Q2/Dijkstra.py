#Dijkstra
import heapq

def Dijkstra1(G, s):   # G – Adjacency List (no -cycle)
    print(1)
    INF = float('inf'); nv = len(G)
    d = [INF]*nv
    p = [None]*nv
    d[s] = 0; H = [(d[s],s)]
    while len(H) > 0:
        du,u = heapq.heappop(H)
        for v,w in G[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                p[v] = u
                heapq.heappush(H, (d[v],v))
    return d, p
def Dijkstra2(G, s):   # G – Adjacency List (no -weight)
    print(2)
    INF = float('inf'); nv = len(G)
    d = [INF]*nv
    p = [None]*nv
    d[s] = 0; H = [(d[s],s)]
    in_spt = [False]*nv
    while len(H) > 0:
        du,u = heapq.heappop(H)
        in_spt[u] = True
        for v,w in G[u]:
            if not in_spt[v] and d[u] + w < d[v]:
                d[v] = d[u] + w
                p[v] = u
                heapq.heappush(H, (d[v],v))
    return d, p
G = [[(1,2),(2,8),(3,3)],[(0,2),(2,5),(3,7)],[(0,8),(1,5),(3,4)],[(0,3),(1,7),(2,4)]]
a,b =Dijkstra1(G,0)
c,d =Dijkstra1(G,0)
print(a,b)
print(c,d)

