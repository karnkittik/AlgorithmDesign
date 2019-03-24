from collections import deque
import sys
sys.setrecursionlimit(5000)
def BFS(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            Q=deque()
            Q.append(s)
            color[s]=1
            while len(Q)>0:
                u = Q.popleft()
                print(u)
                color[u]=2
                for v in G[u]:
                    if color[v]==0:
                        Q.append(v)
                        color[v]=1
def DFS(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            DFSR(G,s,color)
def DFSR(G,u,color):
    color[u]=1
    print(u)
    for v in G[u]:
        if color[v]==0:
            DFSR(G,v,color)
G=[[1, 2, 5], [3, 4], [5], [8], [], [6], [2, 7], [4], [4]]
BFS(G)
DFS(G)
    
