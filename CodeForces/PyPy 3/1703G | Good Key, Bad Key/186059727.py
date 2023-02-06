from sys import stdin
input = stdin.readline 
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    """
    Let dp[i][b] = The maximum score achievable given that we are at index and i and that *after* operation on index i, we have used b halving operations
 
    State requirements: i >= b (for 1 indexed) which means i + 1 >= b (0 indexed) => i >= b - 1
 
    Transition: dp[i][b] = max(dp[i - 1][b] + a[i] * (1/2) ** b - k, dp[i - 1][b - 1] + a[i] * (1/2) ** b)
 
    Base cases: dp[0][0] = a[0] - k, dp[0][1] = a[0] // 2, all the other states initialized to float('-inf')
 
    Order of computation: Compute in order of i first, then in order of b
 
    Precomputation: precompute a[i] * powers of 1/2 
 
    Answer: max(dp[n - 1])
    """
 
    a_halfed = [a] #a_halfed[h][i] = a[i] after h halfings
    while a_halfed[-1] != [0] * n:
        b = [e // 2 for e in a_halfed[-1]]
        a_halfed.append(b)
 
    dp = [[float('-inf') for b in range(40)] for i in range(n)]; dp[0][0] = a[0] - k; dp[0][1] = a[0] // 2
    for i in range(1, n):
        for b in range(len(dp[0])):
            if b < len(a_halfed):
                if b > 0:
                    dp[i][b] = max(dp[i - 1][b] + a_halfed[b][i] - k, dp[i - 1][b - 1] + a_halfed[b][i], dp[i][b])
                else:
                    dp[i][b] = max(dp[i - 1][b] + a_halfed[b][i] - k, dp[i][b])
            else:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - 1], dp[i - 1][b])
 
    print(max(dp[-1]))