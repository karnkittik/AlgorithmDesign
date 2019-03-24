def BFS(G,s,k):
    Q = []
    visited = [0]*len(G)
    visited[s]=1
    Q.append((s,0))
    while len(Q)>0:
        u,d = Q.pop(0)
        if d==k:
            return sum(visited)
        for v in G[u]:
            if visited[v]==0:
                visited[v]=1
                Q.append((v,d+1))
    return sum(visited)
n,e,k = [int(e) for e in input().split()]
G = [[] for k in range(n)]
for i in range(e):
    a,b = [int(e) for e in input().split()]
    G[a].append(b)
    G[b].append(a)
max_c = max([BFS(G,s,k) for s in range(n)])
print(max_c)
