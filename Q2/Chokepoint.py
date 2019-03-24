from itertools import combinations
from sys import stdin as kb
def cc(G,visited,u,v,nc):
    visited[v] = True
    d =1
    for e in G[v]:
        if not visited[e]:
           d+= cc(G,visited,v,e,nc)
    nc[u].append(d)
    nc[v].append(len(G)-d)
    return d
n = int(kb.readline())
G = [[] for i in range(n)]
for i in range(n-1):
    a,b = [int(e) for e in kb.readline().split()]
    G[a].append(b)
    G[b].append(a)
nc = [[] for k in range(n+1)]
cc(G,[False]*n,-1,0,nc)
print(nc)
for k in range(n):
    s = n-1 + sum(c1*c2 for c1,c2 in combinations(nc[k],2))
    print(s)
