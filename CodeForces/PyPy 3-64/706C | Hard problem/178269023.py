n = int(input())
c = list(map(int,input().split()))
 
a = []
for line in range(n):
    a.append(input())
 
dp = [[float('inf'), float('inf')] for i in range(n)]
dp[n - 1][0], dp[n - 1][1] = 0, c[n - 1]
 
for i in range(n - 2, -1, -1):
    ans_0 = float('inf')
    if a[i] <= a[i + 1]:
        ans_0 = min(ans_0, dp[i + 1][0])
    if a[i] <= a[i + 1][::-1]:
        ans_0 = min(ans_0, dp[i + 1][1])
 
    ans_1 = float('inf')
    if a[i][::-1] <= a[i + 1]:
        ans_1 = min(ans_1, c[i] + dp[i + 1][0])
    if a[i][::-1] <= a[i + 1][::-1]:
        ans_1 = min(ans_1, c[i] + dp[i + 1][1])
 
    if ans_0 == ans_1 == float('inf'):
        break
 
    dp[i][0], dp[i][1] = ans_0, ans_1
 
res = min(dp[0][0], dp[0][1])
print(res) if res < float('inf') else print(-1)
 
 
 
 
 