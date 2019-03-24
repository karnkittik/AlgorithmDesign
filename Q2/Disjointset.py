#Kruskal
import heapq
def findset(P,e):
    while P[e]!=e:
        e=P[e]
    return e
def unionset(P,H,e1,e2):
    s1 = findset(P,e1)
    s2 = findset(P,e2)
    if H[s1]<H[s2]:
        P[s1]=s2
    else:
        P[s2]=s1
        if H[s1]==H[s2]:
            H[s1]+=1
def Kruskal(G):
    nv = len(G)
    P = list(range(nv))
    H = [0]*nv
    E = [(w,u,v) for u in range(nv) for v,w in G[u] if u<v]
    heapq.heapify(E)
    mst = []
    while len(mst)< nv-1:
        w,u,v = heapq.heappop(E)
        if findset(P,u) != findset(P,v):
            unionset(P,H,u,v)
            mst.append((u,v))
    return mst
G = [[(1,2),(2,3),(3,3)],[(0,2),(2,5),(3,7)],[(0,3),(1,5),(3,4)],[(0,3),(1,7),(2,4)]]
print(Kruskal(G))
