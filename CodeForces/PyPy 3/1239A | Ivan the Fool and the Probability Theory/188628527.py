from sys import stdin
input = stdin.readline 
 
mod = 10 ** 9 + 7
def compute_max_two_configs(n: int) -> int:
    dp = [[0, 0, 0] for i in range(n + 1)]; dp[1][1] = 1
    for i in range(2, n + 1):
        dp[i][1] = (dp[i - 1][1] + dp[i - 1][2]) % mod; dp[i][2] = dp[i - 1][1]
    return (2 * sum(dp[-1])) % mod
 
n, m = map(int, input().split()); 
row_configs = compute_max_two_configs(n); col_configs = compute_max_two_configs(m)
if n > 1: 
    forced_configs = row_configs - 2
    print((forced_configs + col_configs) % mod)
else:
    print(col_configs)