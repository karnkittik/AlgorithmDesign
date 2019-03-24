from collections import deque
def BFS(G,s):
    color = ['W']*len(G)
    for s in range(len(G)):
        if color[s]=='W':
            BFSI(G,s,color)
def BFSI(G,s,color):
    Q = deque()
    color[s] = 'G'
    Q.append(s)
    while len(Q) >0:
        u = Q.popleft()
        print(u)
        color[u] = 'B'
        for v in G[u]:
            if color[v] =='W':
                color[v]='G'
                Q.append(v)
n = 9
##G = [[]*n for i in range(n)]
##for i in range(n):
##    v = [int(e) for e in input().split()]
##    G[i]=v
##print(G)
G=[[1, 2, 5], [3, 4], [5], [8], [], [6], [2, 7], [4], [4]]
BFS(G,0)
