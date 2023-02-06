from sys import stdin
input = stdin.readline
 
 
info = []
for l in range(int(input())):
    info.append(list(map(int, input().split())))
 
info.sort()
ans = float('-inf')
 
for a,b in info:
    if b >= ans:
        ans = b
    else:
        ans = a
 
print(ans)
    