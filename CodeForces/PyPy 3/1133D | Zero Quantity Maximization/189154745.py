from sys import stdin
from collections import defaultdict
from fractions import Fraction
input = stdin.readline 
 
count_by_val = defaultdict(int)
 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
adjustment = 0
for bi, ai in zip(b, a):
    if ai == 0:
        if bi == 0:
            adjustment += 1
        continue
    count_by_val[Fraction(-bi, ai)] += 1
 
if len(count_by_val) == 0:
    print(0 + adjustment)
else:
    print(max(count_by_val.values()) + adjustment)
 