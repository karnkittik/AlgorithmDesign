n = int(input())
G = [[0]*n for j in range(n)]
for u in range(n-1):
    w = [int(e) for e in input().split()]
    for v in range(u+1,n):
        G[u][v] = G[v][u] = w[v-u-1]
print(G)
