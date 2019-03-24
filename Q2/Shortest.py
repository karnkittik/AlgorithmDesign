from collections import deque

def BFS(M,sr,sc,tr,tc):
    R = len(M);
    C = len(M[0])
    Q = deque()
    visited = { (sr,sc) }
    Q.append( (0,sr,sc) )
    while len(Q) > 0:
        d,r,c = Q.popleft()
        if (r,c) == (tr,tc):
            return d
        for dr,dc in ((1,0),(0,1),(0,-1),(-1,0)):
            r1 = r+dr
            c1 = c+dc
            if(0<=r1<R and 0<=c1<C) and\
                M[r1][c1] == '.' and\
                (r1,c1) not in visited:
                visited.add((r1,c1))
                Q.append((d+1,r1,c1))
                print((d+1,r1,c1))
    return -1
r,c = [int(e) for e in input().split()]
G = [[e for e in input().strip()] for k in range(r)]
print(BFS(G,0,0,r-1,c-1))
