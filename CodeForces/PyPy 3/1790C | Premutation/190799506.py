from sys import stdin
import math
input = stdin.readline
 
for case in range(int(input())):
    n = int(input()); perms = []
    for line in range(n):
        perms.append(list(map(int, input().split())))
 
    nums_after = [0 for i in range(n + 1)]
 
    for p in perms:
        for ind, elem in enumerate(p):
            nums_after[elem] += n - ind
 
    cts = []
    for ind, ct in enumerate(nums_after):
        if ind == 0: continue
 
        cts.append((ct, ind))
 
    cts.sort(reverse=True)
 
    ans = []
    for a, b in cts:
        ans.append(str(b))
 
    print(' '.join(ans))
 
 
    