import numpy as np
a = np.array([[1],[2],[3]],float)
b = np.ones((2,3),float)
c = np.identity(4,int)
d = np.diagonal(c)
e = np.ndarray((1,2),int)
print(a,b,c,d,e)
f = np.array([[2,4,6],[1,3,5]])
print(f)
g = np.cumsum(f,axis=1)
print(g)
h = np.ndarray(3, dtype=int)
print(h)
i = h.reshape(3,1)
print(i)