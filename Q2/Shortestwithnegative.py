import sys
kb = sys.stdin
def BellmanFord(G,s):
    nv = len(G)
    inf = float('inf')
    d = [inf]*nv
    p = [None]*nv
    d[s] = 0
    for i in range(nv+1):
        relax = False
        for u in range(nv):
            for v,w in G[u]:
                if d[u]+w<d[v]:
                    d[v] = d[u]+w
                    p[v] = u
                    relax = True
    if relax: return [-1]
    return d
N,E,s = [int(e) for e in kb.readline().split()]
G = [[] for i in range(N)]
for i in range(E):
    u,v,w = [int(e) for e in kb.readline().split()]
    G[u].append((v,w))
f = BellmanFord(G,s)
print(*f,sep=" ")

