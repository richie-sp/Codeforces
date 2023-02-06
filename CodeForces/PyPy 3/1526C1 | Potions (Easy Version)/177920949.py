n = int(input())
 
a = [int(x) for x in input().split()]
 
 
 
dp = [[float('-inf') for j in range(n + 1)] for i in range(n)]
 
for i in range(n):
    dp[i][0] = 0
 
if a[0] >= 0: dp[0][1] = a[0]
 
for i in range(1, n):
    for k in range(n + 1):
        if dp[i - 1][k] + a[i] >= 0:
            dp[i][k + 1] = max(dp[i][k + 1], dp[i - 1][k] + a[i])
        
        dp[i][k] = max(dp[i][k], dp[i - 1][k])
 
 
 
ans = 0
 
for ind, elem in enumerate(dp[-1]):
    if elem >= 0: ans = ind
 
print(ans)
 