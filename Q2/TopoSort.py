from collections import deque
Q = deque()
def tsort(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            tsortR(G,s,color)
    return Q
def tsortR(G,u,color):
    global Q
    color[u]=1
    print(u)
    for v in G[u]:
        if color[v]==0:
            tsortR(G,v,color)
    color[u] = 2
    Q.append(u)
G=[[1, 2], [3, 4], [4], [8], [], [0,6], [7], [2], [4]]
print(tsort(G)) #use by pop as stack
