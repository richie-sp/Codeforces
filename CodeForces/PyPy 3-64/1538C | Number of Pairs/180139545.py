from typing import List
from sys import stdin
input = stdin.readline
 
def compute_pairs(arr: List[int], targ: int) -> int:
    if targ < a[0] + a[1]: 
        return 0
    lo = 0; hi = 1
    while hi + 1 < len(arr) and arr[lo] + arr[hi + 1] <= targ:
        hi += 1
 
    ans = hi - lo
 
    for lo in range(1, len(arr) - 1):
        while arr[lo] + arr[hi] > targ and hi - 1 > lo:
            hi -= 1
 
        if arr[lo] + arr[hi] > targ:
            break
        ans += hi - lo
 
    return ans
 
 
for case in range(int(input())):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
 
    a.sort()
    if n == 1:
        print(0)
        continue
    r_ans = compute_pairs(a, r)
    l_ans = compute_pairs(a, l - 1)
    print(r_ans - l_ans)
    
 