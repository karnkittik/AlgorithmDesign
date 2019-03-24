import sys
import heapq
kb = sys.stdin


def find(e):
    while P[e] != e:
        e = P[e]
    return e


def union(e1, e2):
    s1 = find(e1)
    s2 = find(e2)
    if R[s1] > R[s2]:
        P[s2] = s1
    else:
        P[s1] = s2
        if R[s1] == R[s2]:
            R[s2] += 1


n, m, k = [int(i) for i in kb.readline().split()]
P = [int(i) for i in range(n)]
R = [0 for i in range(n)]
graph = {}

for i in range(n):
    graph[i] = []
for i in range(m):
    a, b, c = [int(i) for i in kb.readline().split()]
    graph[a].append((b, c))
    graph[b].append((a, c))

D = []
for i in range(k):
    d = int(kb.readline())
    D.append([d, i, 0])

D.sort(reverse=True)

E = [(w, u, v) for u in range(n) for v, w in graph[u] if u < v]
heapq.heapify(E)
nClusters = n
K = 0
i = 0
while nClusters > 1:
    if(nClusters <= D[i][0]):
        D[i][2] = K
        i += 1
        if(i >= len(D)):
            break
    K, u, v = heapq.heappop(E)
    if find(u) != find(v):
        nClusters -= 1
        union(u, v)
else:
    D[i][2] = K


D = sorted([[i, K, d] for d, i, K in D])
print(*[K for i, K, d in D], sep='\n')
