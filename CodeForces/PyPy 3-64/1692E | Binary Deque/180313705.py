"""
Sliding Window Help Bookmark follow template!!!!
"""
from sys import stdin
from typing import List
input = stdin.readline
 
 
for case in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
 
    min_ops = n
    
    l = 0; curr_sum = 0; ans = float('inf')
    for r in range(n):
        curr_sum += a[r]
        while curr_sum > s:
            curr_sum -= a[l]
            l += 1
        if curr_sum == s:
            ans = min(ans, n - (r - l + 1))
 
    print(ans) if ans < float('inf') else print(-1)
 
        