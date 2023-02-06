from sys import stdin
from itertools import accumulate 
 
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [abs(1 - e) for e in a]
 
    #onect[i] = # 1s till index i and zeroct[i] = #0s till index i (inclusive)
    onect = list(accumulate(a))
    zeroct = list(accumulate(b))
 
    invs_by_ind = [0 for i in range(n)]
    ans = 0
    for i in range(n):
        if i == n - 1: break
        
        
        if a[i] == 1: 
            invs = zeroct[-1] - zeroct[i]
            ans += invs
            invs_by_ind[i] = invs
 
 
    max_diff = 0
    for i in range(n):
        curr_diff = 0
        if i == 0:
            if a[i] == 0:
                #update by zeroct after
                curr_diff += zeroct[-1] - zeroct[i]
            elif a[i] == 1:
                #decrease by zeroct after
                curr_diff -= (zeroct[-1] - zeroct[i])
        elif i == n - 1:
            if a[i] == 0:
                #decrease by 1ct before
                curr_diff -= onect[i - 1]
            elif a[i] == 1:
                #update by 1ct before
                curr_diff += onect[i - 1]
        else:
            if a[i] == 0:
                #update by zero_count after and decrease by 1 count before
                curr_diff += zeroct[-1] - zeroct[i] - (onect[i - 1])
            elif a[i] == 1:
                #update by 1 count before and decrease by 0 count after
                curr_diff += onect[i - 1] - (zeroct[-1] - zeroct[i])
 
        max_diff = max(max_diff, curr_diff)
 
    print(ans + max_diff)