from sys import stdin
from collections import defaultdict
input = stdin.readline 
 
for c in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    inds_by_num = defaultdict(list)
    for ind, num in enumerate(a):
        inds_by_num[num].append(ind)
 
    ans = 0
    for num in inds_by_num:
        if len(inds_by_num[num]) <= 1: continue
        orig = 0; prefix = []
        for i in range(1, len(inds_by_num[num])):
            prefix.append((n - 1 - inds_by_num[num][i] + 1))
            orig += (inds_by_num[num][0] + 1) * (n - 1 - inds_by_num[num][i] + 1)
 
 
        ans += orig
        psum = sum(prefix)
 
        for i in range(1, len(inds_by_num[num])):
            psum -= prefix[i - 1]
            ans += (inds_by_num[num][i] + 1) * (psum)
 
    print(ans)
            
 
 