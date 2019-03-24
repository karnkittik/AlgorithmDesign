def is_cyclic(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            if is_cyclicR(G,s,color):
                return True
    return False
def is_cyclicR(G,u,color):
    color[u]=1
    for v in G[u]:
        if color[v]==1: return True
        if color[v]==0 and is_cyclicR(G,v,color):
            return True
    color[u]==2
    return False
def is_cyclicD(G):
    color = [0]*len(G)
    for s in range(len(G)):
        if color[s]==0:
            if is_cyclicDR(G,-1,s,color):
                return True
    return False
def is_cyclicDR(G,p,u,color):
    color[u]=1
    for v in G[u]:
        if v==p: continue
        if color[v]==1:return True
        if color[v]==0 and is_cyclicDR(G,u,v,color):
            return True
    color[u]==2
    return False

G=[[1,2], [0], [0], [], [], [], [], [], []]
K=[[1, 2], [0, 2], [3, 1, 0], [2]]
print(is_cyclic(G))
print(is_cyclicD(K))
