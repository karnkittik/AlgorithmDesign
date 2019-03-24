nv,ne = [int(e) for e in input().split()]
G = [[] for k in range(nv)]
for k in range(ne):
    u,v,w = [int(e) for e in input().split()]
    G[u].append((v,w))
print(G)
