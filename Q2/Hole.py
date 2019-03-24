import heapq
import sys
INF = float('inf')
kb = sys.stdin

def BFS(M,hr,hc,Out):
    R = len(M); C = len(M[0])
    Q = [(0,hr,hc)]
    while len(Q) > 0:
        d,r,c  = Q[0]
        heapq.heappop(Q)
        if r == R-1 or c == C-1 or r == 0 or c ==0: return d
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            r1 = r+dr; c1 = c+dc
            if d+M[r1][c1] < Out[r1][c1]:
                Out[r1][c1] = d+M[r1][c1]
                heapq.heappush(Q,(d+M[r1][c1],r1,c1))
    return -1

N,hc,hr = [int(x) for x in kb.readline().strip().split()]
G = [[0]*1000 for i in range(1000)]
dis = [[1000]*1000 for i in range(1000)]
dis[hr-1][hc-1] = 0
for i in range(N):
    c,r  = [int(x) for x in kb.readline().strip().split()]
    G[r-1][c-1] = 1
print(int(BFS(G,hr-1,hc-1,dis)))
