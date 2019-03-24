from sys import stdin as kb
def Buffet(F,w,n):
    out = 0
    i = 1
    while i<=n:
        if i in F:
            out+=1
            i = i+2*w+1
        else:
            i+=1
    return out
f,w,n = [int(e) for e in input().split()]
F = sorted([int(e) for e in kb.readline().split()])
print(Buffet(F,w,n))
