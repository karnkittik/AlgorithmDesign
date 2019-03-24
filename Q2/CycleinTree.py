import sys
kb = sys.stdin
def DFS(G):
    d=[0]
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            d.append(DFSR(G,-1,s,color))
    return max(d)-1
def DFSR(G,p,u,color):
    color[u]=1
    s = 0
    for v in G[u]:
        if v==p: continue
        if color[v]==1: break
        if color[v]==0:
            s =s+1+DFSR(G,u,v,color)
    return s
n = int(kb.readline())
G = [[] for i in range(n)]
for i in range(n):
    a,b = [int(e) for e in kb.readline().split()]
    G[a].append(b)
    G[b].append(a)
print(DFS(G))
