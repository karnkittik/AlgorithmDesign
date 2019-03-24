def is_cyclic(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            if is_cyclicR(G,-1,s,color):
                return True
    return False
def is_cyclicR(G,p,u,color):
    color[u]=1
    for v in G[u]:
        if v==p: continue
        if color[v]==1:return True
        if color[v]==0 and is_cyclicR(G,u,v,color):
            return True
    color[u]==2
    return False
n = int(input())
for i in range(n):
    nv,ne = [int(e) for e in input().split()]
    G = [[] for k in range(nv)]
    for j in range(ne):
        u,v = [int(e) for e in input().split()]
        G[u].append(v)
        G[v].append(u)
    if is_cyclic(G):print('YES')
    else: print('NO')
