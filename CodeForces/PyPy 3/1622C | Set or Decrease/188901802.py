from sys import stdin
from itertools import accumulate
from math import ceil
input = stdin.readline
 
for _ in range(int(input())):
    n, k  = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(); psum = list(accumulate(a))
 
 
    """
    Idea is that you decrease the smallest element by k1.... a1 -> a1 - k1
    and you pick k2 other elements (largest elements) to set to a1 - k1....
 
    Note this assumes that k2 <= n - 1
 
    Precompute prefixsum(i) = sum_{j = 1 to i} aj .... 
 
    we want to minimize k2....for any value of k2, we can find the smallest value of k1 
 
 
    Need (k2 + 1)(a1 - k1) + psum(n - k2) - psum(1) <= k .... solve for k1 for k2 in (0, 1, ...., n)
 
    """
 
    ans = float('inf')
    for k2 in range(n):
        k1 = max(int(ceil(a[0] - (k - psum[n - k2 - 1] + psum[0])/(k2 + 1))), 0)
        ans = min(ans, k1 + k2)
 
    if psum[-1] > k:
        print(max(ans, 1))
    else:
        print(max(ans, 0))
 