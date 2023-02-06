from sys import stdin
from collections import defaultdict
import bisect
input = stdin.readline
 
 
def is_valid(k: int, p):
    shops_by_person = defaultdict(set)
    for i in range(len(p[0])):
        for j in range(len(p)):
            if p[j][i] >= k:
                shops_by_person[i].add(j)
 
    #if we can only choose 1 per each shop, then not valid, otherwise, it's valid b/c we can choose up to n - 1 shops
    m = len(p); n = len(p[0])
    prev_seen = set(); overlap = False
    for i in range(n):
        if len(shops_by_person[i]) == 0: 
            return False
        for shop in shops_by_person[i]:
            if shop in prev_seen:
                overlap = True; break
            prev_seen.add(shop)
 
    return overlap
 
 
 
 
for _ in range(int(input())):
    l = input()
    m, n = map(int, input().split())
    p = []
    for line in range(m):
        p.append(list(map(int, input().split())))
 
 
    lo = 1; hi = 10 ** 9; possible = False
    while lo < hi:
        if lo == hi - 1:
            break
        mid = (lo + hi) // 2
        if is_valid(mid, p):
            lo = mid
        else:
            hi = mid - 1
 
    ans = 1
    if is_valid(lo, p):
        ans = max(ans, lo)
    if is_valid(lo + 1, p):
        ans = max(ans, lo + 1)
    if is_valid(hi, p):
        ans = max(ans, hi)
    if is_valid(hi + 1, p):
        ans = max(ans, hi + 1)
 
    print(ans)
 
 
 