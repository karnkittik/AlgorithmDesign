from collections import deque
Q = deque()
def tsort(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s] == 0:
            tsortR(G,s,color)
    return Q
def tsortR(G,u,color):
    global Q
    color[u]=1
    for v in G[u]:
        if color[v]==0:
            tsortR(G,v,color)
    color[u]=2
    Q.append(u)
n = int(input())
G = [[] for i in range(n)]
for v in range(n):
    a = [int(e) for e in input().split()]
    for u in a[1:]:
        G[u].append(v)
#print(G)
f = list(reversed(tsort(G)))
print(*f,sep=" ")
