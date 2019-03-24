from collections import deque
def BFS(G,s,t):
    Q = deque()
    visited = [False]*len(G)
    visited[s] = True
    Q.append((s,0))
    while len(Q) > 0:
        u, d = Q.popleft()
        if u == t: return d
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.append((v, d+1))
nv, ne = [int(e) for e in input().split()]
G = [[] for k in range(nv)]
for k in range(ne):
    u,v = [int(e) for e in input().split()]
    G[u].append(v); G[v].append(u)
s, t = [int(e) for e in input().split()]
print(BFS(G, s, t))

