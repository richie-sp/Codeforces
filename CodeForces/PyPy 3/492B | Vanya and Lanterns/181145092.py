from sys import stdin
input = stdin.readline
 
n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = max(a[0] - 0, l - a[-1])
for i in range(1, len(a)):
    ans = max(ans, (a[i] - a[i - 1]) / 2)
 
print(ans)