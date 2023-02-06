from sys import stdin
input=stdin.readline
 
from collections import defaultdict
 
for case in range(int(input())):
    n = int(input())
 
    a = list(map(int, input().split()))
    sorted_a = list(sorted(a))
 
    inds_by_val = defaultdict(list)
    sorted_inds_by_val = defaultdict(list)
 
    for ind, v in enumerate(a):
        inds_by_val[v].append(ind)
 
    for ind, v in enumerate(sorted_a):
        sorted_inds_by_val[v].append(ind)
 
    
    ans = True
    for v in inds_by_val:
        reg_ctr, sorted_ctr = [0, 0], [0, 0]
 
        for x in inds_by_val[v]:
            reg_ctr[x % 2] += 1
 
        for x in sorted_inds_by_val[v]:
            sorted_ctr[x % 2] += 1
 
 
        if reg_ctr != sorted_ctr:
            ans = False
            break
        
 
            
 
    print('YES') if ans else print('NO')
    