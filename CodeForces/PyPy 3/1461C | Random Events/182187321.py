from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    sort_req = n
    for i in range(n - 1, -1, -1):
        if a[i] != i + 1:
            sort_req = i
            break
 
    ans = 1; comp = 1
    for e in range(m):
        r, p = map(float, input().split())
        r -= 1
        if r >= sort_req: comp *= (1 - p)
 
    if sort_req == n:
        print(1)
        continue
 
    print(1 - comp)
        