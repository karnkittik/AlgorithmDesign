def SCC(G):
    GT = G_T(G)
    max_to_min_F = dfs_scc1(GT)
    return dfs_scc2(G, max_to_min_F)
    
def G_T(G):
    n = len(G)
    GT = [[] for k in range(n)]
    for u in range(n):
        for v in G[u]:
            GT[v].append(u)
    print(GT)
    return GT

def dfs_scc1(G):
    visited = [False]*len(G)
    F = []
    for s in range(len(G)):
        if not visited[s] :
            dfs_scc1R(G, s, visited, F)
    return F[::-1]  # max. to min. finish times

def dfs_scc1R(G, u, visited, F):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            dfs_scc1R(G, v, visited, F)
    F.append(u)  # finish
def dfs_scc2(G, v_order):
    visited = [False]*len(G) 
    scc = []
    for u in v_order:
        if not visited[u] :
            scc.append( [u] )
            dfs_scc2R(G, u, visited, scc[-1])
    return scc

def dfs_scc2R(G, u, visited, component):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            component.append(v) 
            dfs_scc2R(G, v, visited, component)
G=[[], [0,2,4], [4], [],[]]
print(SCC(G))
