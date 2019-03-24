import heapq
def findset(P,e):
    while P[e]!=e:
        e = P[e]
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
    mst = []
    E = [(w,u,v) for u in range(nv) for v,w in G[u] if u<v]
    heapq.heapify(E)
    while len(mst)<nv-1:
        w,u,v = heapq.heappop(E)
        if findset(P,u)!=findset(P,v):
            unionset(P,H,u,v)
            mst.append((u,v))
    return mst
def Prim(G):
    INF = float('inf')
    nv = len(G)
    d = [INF]*nv
    p = [None]*nv
    inMST = [False]*nv
    d[0] = 0
    for i in range(nv):
        u = d.index(min(d))
        d[u] = INF
        inMST[u] = True
        for v in range(nv):
            if not inMST[v] and G[u][v] < d[v]:
                d[v] = G[u][v]
                p[v] = u
    return p


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
                d[v]=G[u][v]
                p[v]=u
    return p
def Kruskal(G):
    nv = len(G)
    H = [0]*nv
    P = list(range(nv))
    E = [(w,u,v) for u in range(nv) for v,w in G[u] if u<v]
    mst = [ ]
    heapq.heapify(E)
    while len(mst)<nv-1:
        w,u,v = heapq.heappop(E)
        if findset(P,u)!= findset(P,v):
            unionset(P,H,u,v)
            p[v] = u
            mst.append((u,v,w))
    return mst
def Prim(G):
    nv = len(G)
    INF = float('inf')
    d = [INF]*nv
    p = [None]*nv
    inMST = [False]*nv
    d[0] = 0
    for i in range(nv):
        u = d.index(min(d))
        d[u] = INF
        inMST[u] = True
        for v in range(nv):
            if not inMST[v] and G[u][v]<d[v]:
                d[v]=G[u][v]
                p[v]=u
    return p
def Dijkstra(G,s):
    nv = len(G)
    INF = float('inf')
    d = [INF]*nv
    p = [None]*nv
    d[s] = 0
    H = [(d[s],s)]
    while len(H)>0:
        du,u = heapq.heappop(H)
        for v,w in G[u]:
            if d[u]+w<d[v]:
                d[v] = d[u]+w
                d[v] = u
                heapq.heappush((d[v],v))
    return d,p
def Dijkstra(G,s):
    nv = len(G)
    INF = float('inf')
    d = [INF]*nv
    p = [None]*nv
    d[s] = 0
    H = [(d[s],s)]
    heapq.heapify(H)
    while len(H)>0:
        du,u = heapq.heappop(H)
        for v,w in G[u]:
            if d[u]+w < d[v]:
                d[v] = d[u]+w
                p[v] = u
                heapq.heappush(H,(d[v],v))
    return d




    
def Prim(G):
    nv = len(G)
    INF = float('inf')
    d = [INF]*nv
    p = [None]*nv
    inMST = [False]*nv
    d[0] = 0
    for i in range(nv):
        u = d.index(min(d))
        d[u] = INF
        inMST[u]=True
        for v in range(nv):
            if not inMST[v] and G[u][v]<d[v]:
                d[v] = G[u][v]
                p[v] = u
    return p
def Kruskal(G):
    nv = len(G)
    P = list(range(nv))
    H = [0]*nv
    E = [(w,u,v) for u in range(nv) for v,w in G[u] if u<v]
    mst = []
    heapq.heapify(E)
    while len(E)<nv-1:
        w,u,v = heapq.heappop(E)
        if findset(P,u)!=findset(P,v):
            unionset(u,v)
            mst.append((u,v))
    return mst


def BellmanFord(G,s):
    nv = len(G)
    inf = float('inf')
    d = [inf]*nv
    p = [None]*nv
    d[s]=0
    for i in range(nv+1):
        relax = False
        for u in range(nv):
            for v,w in G[u]:
                if d[u]+w < d[v]:
                    d[v] = d[u]+w
                    p[v] = u
                    relax = True
    if relax: return None
    return p






        









        


























