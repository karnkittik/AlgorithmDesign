import sys
import heapq
kb = sys.stdin

r,c = [int(e) for e in kb.readline().split()]
w = [[] for i in range(r)]
for i in range(r):
    w[i]=[int(e) for e in kb.readline().split()]
d = [[float('inf')]*c for i in range(r)]
def D(u,v):
    d[u][v] = 0
    H = [(d[u][v],u,v)]
    while len(H)>0:
        x,i,j = heapq.heappop(H)
        i1 = i + 1
        j1 = j + 1
        i2 = i - 1
        j2 = j - 1
        if i1 < r and d[i][j] + w[i1][j] < d[i1][j]:
            d[i1][j] = d[i][j] + w[i1][j]
            heapq.heappush(H,(d[i1][j],i1,j))
        if j1 < c and d[i][j] + w[i][j1] < d[i][j1]:
            d[i][j1] = d[i][j] + w[i][j1]
            heapq.heappush(H,(d[i][j1],i,j1))
        if i2 >= 0 and d[i][j] + w[i2][j] < d[i2][j]:
            d[i2][j] = d[i][j] + w[i2][j]
            heapq.heappush(H,(d[i2][j],i2,j))
        if j2 >= 0 and d[i][j] + w[i][j2] < d[i][j2]:
            d[i][j2] = d[i][j] + w[i][j2]
            heapq.heappush(H,(d[i][j2],i,j2))
D(0,0)         
for i in d: print(*i)
