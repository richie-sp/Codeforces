from sys import stdin
from math import ceil
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
 
    health_ct = [0 for i in range(101)]
    for hi in h:
        health_ct[hi] += 1
 
    ans = 0
    for ind, ct in enumerate(health_ct):
        if ind == 0: continue
        ans += min(ct, ind * int(ceil(ct / 2)))
 
    print(ans)
 