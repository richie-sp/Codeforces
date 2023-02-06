from sys import stdin
from itertools import accumulate
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    psum = list(accumulate(a)); special_values = set(); set_a = set(a)
 
    for l in range(n):
        for r in range(l + 2, n):
            curr_sum = psum[r] - psum[l]
            if curr_sum in set_a: special_values.add(curr_sum)
 
    for i in range(1, n):
        if psum[i] in set_a: special_values.add(psum[i])
 
    ct = 0
    for elem in a:
        if elem in special_values: ct += 1
 
    print(ct)