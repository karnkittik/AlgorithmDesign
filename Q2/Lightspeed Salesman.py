import numpy as np
import sys
kb = sys.stdin

N,M = [int(e) for e in kb.readline().split()]
P = [int(e) for e in kb.readline().split()]
P.append(P[0])
P = np.array(P)
L = np.array([int(e) for e in kb.readline().split()])
C = np.ndarray(M+1, dtype=int)
C[0] = 0
C[1:] = np.cumsum(L)
#print(C)
#print(C.reshape(M+1,1))
C1 = np.abs(C - C.reshape((M+1,1)))
#print(C1)
C2 = (C[-1] - C1) % C[-1]
#print(C2)
D = np.minimum(C1, C2)
#print(D)
U = P[:-1]; V = P[1:]
#print(U,V)
DUV = D[U,V]
#print(DUV)
for k in range(N):
    a, b = [int(e) for e in kb.readline().split()]
    M1 = np.minimum(D[U,a]+D[b,V], D[U,b]+D[a,V])
    #print(M1)
    s = np.sum(np.minimum(DUV, M1))
    print(s)
