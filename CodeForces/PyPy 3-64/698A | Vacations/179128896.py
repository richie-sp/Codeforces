from sys import stdin
input = stdin.readline
 
n = int(input())
a = list(map(int, input().split()))
 
g, c, r = [float('inf') for i in range(n)], [float('inf') for i in range(n)], [float('inf') for i in range(n)]
 
 
r[-1] = 1
 
if a[-1] == 1:
    c[-1] = 0
 
if a[-1] == 2:
    g[-1] = 0
 
if a[-1] == 3:
    c[-1], g[-1] = 0, 0
 
 
for i in range(n - 2, -1, -1):
    r[i] = 1 + min(r[i + 1], g[i + 1], c[i + 1])
    
    if a[i] == 1:
        c[i] = min(g[i + 1], r[i + 1])
    elif a[i] == 2:
        g[i] = min(c[i + 1], r[i + 1])
    elif a[i] == 3:
        c[i] = min(g[i + 1], r[i + 1])
        g[i] = min(c[i + 1], r[i + 1])
 
 
print(min(g[0], c[0], r[0]))