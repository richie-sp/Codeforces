"""
Seems like DP
"""
from sys import stdin
input = stdin.readline 
 
for c in range(int(input())):
    n, p = map(int, input().split())
    a = list(map(int, input().split())); a.sort()
    """
    f[i][g][b] = max power @ index i *before* eating human given that there are g greens and b blues remaining
    """
    f = [[[0 for b in range(1 + 1)] for g in range(2 + 1)] for i in range(n)]; f[0][2][1] = p; f[0][1][1] = p * 2; f[0][0][1] = p * 4; f[0][2][0] = p * 3; f[0][1][0] = p * 6; f[0][0][0] = p * 12
  
    for i in range(n - 1):
        # valid = False
        for g in range(3):
            for b in range(2):
                initial = f[i][g][b]; large_enough = initial > a[i];
                if large_enough: initial += a[i] // 2
                for gp in range(g + 1):
                    for bp in range(b + 1):
                        mult = 2 ** gp * 3 ** bp
                        new = initial * mult
                       
                        if new > a[i]:
                            if large_enough:
                                f[i + 1][g - gp][b - bp] = max(f[i + 1][g - gp][b - bp], new)
                            else:
                                f[i + 1][g - gp][b - bp] = max(f[i + 1][g - gp][b - bp], new + a[i] // 2)
                            # if i == 1 and g == 1 and b == 0:
                            #     print('hi', new, f[i + 1][g - gp][b - bp])
 
    ans = 0
    for i in range(n):
        maxim = 0
        for g in range(3):
            for b in range(2):
                maxim = max(maxim, f[i][g][b])
 
        if maxim > a[i]:
            ans = i + 1
 
    print(ans)