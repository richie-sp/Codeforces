"""
Accepted
"""
from sys import stdin
input = stdin.readline
 
n1, n2, k1, k2 = map(int, input().split())
 
dp = [[[[0 for st in range(max(k1, k2) + 1)] for fh in range(2)] for j in range(n2 + 1)] for i in range(n1 + 1)]; dp[0][0][0][0] = 1; dp[0][0][1][0] = 1; dp[1][0][0][1] = 1; dp[0][1][1][1] = 1
 
for i in range(n1 + 1):
    for j in range(n2 + 1):
        if i == 0 and j == 0: continue
        for fh in range(2):
            for st in range(max(k1, k2) + 1):
                if i + 1 <= n1 and fh == 1:
                    dp[i + 1][j][0][1] += dp[i][j][1][st]
                if j + 1 <= n2 and fh == 0:
                    dp[i][j + 1][1][1] += dp[i][j][0][st]
                if i + 1 <= n1 and fh == 0 and 2 <= st + 1 <= k1:
                    dp[i + 1][j][0][st + 1] = dp[i][j][0][st]
                if j + 1 <= n2 and fh == 1 and 2 <= st + 1 <= k2:
                    dp[i][j + 1][1][st + 1] = dp[i][j][1][st]
 
 
# for i in range(n1 + 1):
#     for j in range(n2 + 1):
#         for fh in range(2):
#             for st in range(max(k1, k2) + 1):
#                 if dp[i][j][fh][st] != 0:
#                     print(f"footmen {i}, horseman {j}, fh {fh}, streak {st}  --- value:  {dp[i][j][fh][st]}")
 
ans = 0
for i in range(len(dp[n1][n2])):
    for j in range(len(dp[n1][n2][0])):
        ans += dp[n1][n2][i][j]
 
print(ans % (10 ** 8))
 
 
 
 
 
 
        
 
        
 