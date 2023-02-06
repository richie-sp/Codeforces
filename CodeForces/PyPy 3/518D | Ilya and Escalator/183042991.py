n, p, t = [float(x) for x in input().split()]; n = int(n); t = int(t)
 
if t <= n:
    print(p * t)
else:
    dp = [[0 for j in range(t + 1)] for i in range(n + 1)]; 
    dp[0][0] = 1
 
 
    for j in range(1, t + 1):
        for i in range(min(j + 1, n + 1)):
            prev1 = 0; prev2 = 0
            if i - 1 >= 0 and j - 1 >= 0: prev1 = dp[i - 1][j - 1]
            if j - 1 >= 0: prev2 = dp[i][j - 1]
 
            if i == n:
                coeff_2 = 1
            else:
                coeff_2 = (1 - p)
 
            dp[i][j] = p * prev1 + coeff_2 * prev2
 
    ev = 0
    for i in range(n + 1):
        ev += (i * dp[i][t])
 
    print(ev)
 
 
    