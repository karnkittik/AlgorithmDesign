n,a,b,c = [int(e) for e in input().split()]
L = [0]*10000

L[a] = L[b] = L[c] = 1

for i in range(n+1):
  if L[i]!=0:
    L[i+a] = max(L[i+a],L[i]+1)
    L[i+b] = max(L[i+b],L[i]+1)
    L[i+c] = max(L[i+c],L[i]+1)

print(L[n])
