from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    # q, r = map(int, input().split())
    a = list(map(int, input().split()))
 
    s = sum(a); ans = float('-inf')
 
    for i in range(1, len(a)):
        prev, nex = a[i - 1], a[i]
        prevp, nexp = -prev, -nex
 
        ans = max(ans, s + (prevp - prev + nexp - nex))
 
    print(ans)
 