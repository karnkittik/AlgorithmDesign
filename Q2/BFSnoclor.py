from collections import deque
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
n = 9
G=[[1, 2, 5], [3, 4], [5], [8], [], [6], [2, 7], [4], [4]]
BFS(G)
