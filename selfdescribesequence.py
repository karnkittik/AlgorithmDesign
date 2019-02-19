def binary(S,left,right,k,m):
    mid = (left+right)//2
    if left>= right: return mid
    if S[mid]==k:
        return mid
    if S[mid]<k:
        return binary(S,mid+1,right,k,mid)
    else:
        return binary(S,left,mid,k,mid)

A = [0,1,2,2]
S = [0,1,3,5]
i = 1
while S[-1]<2000000000:
    a = A[-1]+1
    A += [a]*A[a]
    for j in range(A[a]):
        S.append(S[-1]+A[-1])
n = int(input())
K = []
for i in range(n):
    r = int(input())
    K.append(r)
p = len(S)
m = p-1
for i in range(len(K)):
    print(binary(S,0,p,K[i],m))