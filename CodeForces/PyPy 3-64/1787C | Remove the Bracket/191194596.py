from sys import stdin
input = stdin.readline
 
#returns the value which makes x as close to s as possible
def closex(a, i, s) -> int:
    if a[i] >= s:
        return s
    return a[i]
 
 
def closey(a, i, s) -> int:
    return a[i] - closex(a, i, s)
 
 
for case in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
 
    dp = [[None, None] for i in range(n + 1)]
    dp[1][0] = a[0] * closex(a, 1, s); dp[1][1] = a[0] * closey(a, 1, s)
 
    for i in range(2, n - 1):
        dp[i][0] = min(dp[i - 1][0] + closey(a, i - 1, s) * closex(a, i, s), dp[i - 1][1] + closex(a, i - 1, s) * closex(a, i, s))
        dp[i][1] = min(dp[i - 1][0] + closey(a, i - 1, s) * closey(a, i, s), dp[i - 1][1] + closex(a, i - 1, s) * closey(a, i, s))
 
    ans = min(dp[n - 2][0] + closey(a, n - 2, s) * a[n - 1], dp[n - 2][1] + closex(a, n - 2, s) * a[n - 1])
 
    print(ans)