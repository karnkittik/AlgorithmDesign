ab =0
ba =0
n = int(input())
a = [int(i) for i in input().split()]
b = sorted(list(a))
for i in range(n):
    if a[i]<b[i]:
        ab+=1
    if a[i]>b[i]:
        ba+=1
print(max(ab,ba))
