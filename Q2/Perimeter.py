import sys
from collections import deque
def BFS(G,s,k):
    n = 0
    visited = [False]*len(G)
    q = deque()
    q.append((s,0))
    visited[s]=True
    while len(q)>0:
        u,d = q.popleft()
        if d==k:n+=1
        if d>k: break
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                q.append((v,d+1))
    return n
kb = sys.stdin
n,e,k = [int(e) for e in kb.readline().split()]
G = [[] for k in range(n+1)]
for i in range(e):
    a,b = [int(e) for e in kb.readline().split()]
    G[a].append(b)
    G[b].append(a)
print(BFS(G,0,k))
