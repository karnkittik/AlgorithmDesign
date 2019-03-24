n,m = map(int,input().split())
L = [int(x) for x in input().split()]
l = max(L[0],max([L[i]-L[i-1] for i in range(1,n)]))
r = L[-1]

def day(k):
	cur,d = 0,0
	for i in range(n):
		if L[i] > cur+k : cur = L[i-1]; d += 1
	if cur < L[-1]: d += 1
	return d

while l < r:
	k = (l+r)//2
	t = day(k)
	if t > m : l = k+1
	else : r = k

print(r,day(r))
