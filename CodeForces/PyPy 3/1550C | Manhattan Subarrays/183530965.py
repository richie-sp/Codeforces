from sys import stdin
from typing import List
import itertools
 
input = stdin.readline
 
def fast_compute(a: List[int]) -> int:
    ans = 0
    for i in range(n - 1, -1, -1):
        if i >= n - 2:
            ans += ((n - 1) - i + 1)
            continue
        #length 2 and 1 automatically good
        ans += 2
        #length 3 check
        if not ((a[i] <= a[i + 1] <= a[i + 2]) or (a[i] >= a[i + 1] >= a[i + 2])): 
            ans += 1
        #length 4 check
        if i + 3 <= n - 1:
            four_good = True; subarr = a[i:i+4]
            for x in range(len(subarr)):
                for y in range(x  + 1, len(subarr)):
                    for z in range(y + 1, len(subarr)):
                        if (subarr[x] <= subarr[y] <= subarr[z]) or (subarr[x] >= subarr[y] >= subarr[z]):
                            four_good = False
            if four_good: 
                ans += 1
    return ans
 
def slow_compute(a: List[int]) -> int:
    ans = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            subarr = a[i:j + 1]
            if len(subarr) <= 2:
                ans += 1
 
            else:
                good = True
                for x in range(len(subarr)):
                    for y in range(x + 1, len(subarr)):
                        for z in range(y + 1, len(subarr)):
                            if (subarr[x] <= subarr[y] <= subarr[z]) or (subarr[x] >= subarr[y] >= subarr[z]):
                                good = False
                if good: 
                    ans += 1
    return ans
 
 
 
for c in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    print(fast_compute(a))
 
        
 
        