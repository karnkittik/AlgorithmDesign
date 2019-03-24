import sys
sys.setrecursionlimit(5000)
def DFS(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            DFSR(G,s,color)
def DFSR(G,u,color):
    color[u] = 1
    print(u)
    for v in G[u]:
        if color[v]==0:
            DFSR(G,v,color)
    color[u] = 2
G=[[1, 2, 5], [3, 4], [5], [8], [], [6], [2, 7], [4], [4]]
DFS(G)
