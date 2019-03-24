time = 0
d = [0]*10
f = [0]*10
def DFST(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            DFSTR(G,s,color)
    return (d,f)
def DFSTR(G,u,color):
    global time
    color[u]=1
    time+=1
    d[u]=time
    print(u,time)
    for v in G[u]:
        if color[v]==0:
            DFSTR(G,v,color)
    color[u] = 2
    time+=1
    f[u]=time
    print(u,time)
G=[[1, 2], [3, 4], [4], [8], [], [0,6], [7], [2], [4]]
print(DFST(G))
